import numpy as np
from gensim.models import Word2Vec
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import re
import pickle
import torch
import torch.nn as nn
import torch.optim as optim
import torch

#ignore warnings
import warnings
warnings.filterwarnings('ignore')


# Preprocess texts
def preprocess(text):
    text = text.lower()
    text = re.sub(r'\W+', ' ', text)
    return text


class MLP(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(MLP, self).__init__()
        self.norm = nn.BatchNorm1d(input_size)
        self.layer1 = nn.Linear(input_size, hidden_size)
        self.relu1 = nn.ReLU()
        # self.dropout = nn.Dropout(0.2)
        self.layer2 = nn.Linear(hidden_size, num_classes)  # Ensure num_classes matches the number of categories

    def forward(self, x):
        out = self.norm(x)
        out = self.layer1(x)
        out = self.relu1(out)
        # out = self.dropout(out)
        out = self.layer2(out)
        return out



# model = Word2Vec.load("path_to_pretrained_model")  # If using a pre-trained model
# Vectorize sentences
def sentence_vector(sentence, model):
    words = sentence.split()
    word_vectors = [model.wv[word] for word in words if word in model.wv]
    if len(word_vectors) == 0:
        return np.zeros(model.vector_size)
    return np.mean(word_vectors, axis=0)



def main(new_sentence):
    vector_size = 200
    input_size = vector_size
    hidden_size = 32
    num_classes = 15
    # load word2vec model
    model_word2vec =model_word2vec = Word2Vec.load("model/word2vec.model")
    # load label encoder
    with open('model/label_encoder.pkl', 'rb') as f:
        label_encoder = pickle.load(f)

    # load model
    model = MLP(input_size, hidden_size, num_classes)

    model.load_state_dict(torch.load('model/MLP.pt'))

    new_sentence = preprocess(new_sentence)
    new_sentence = sentence_vector(new_sentence, model_word2vec)
    new_sentence = torch.Tensor(new_sentence).unsqueeze(0)
    model.eval()
    output = model(new_sentence)
    result = label_encoder.inverse_transform([output.argmax(dim=1)])[0]
    print(result)
    return result

if __name__ == '__main__':
    main(new_sentence="The president of the United States is Donald Trump")
