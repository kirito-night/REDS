from bs4 import BeautifulSoup
from mastodon import Mastodon
from networkx import all_shortest_paths
import re
from langdetect import detect



def extract_mastodon(mastodon, topic : str, max_results : int = 5): 

    # infos à colletcer
    list_dict = []
    # 收集每个话题的相关帖子
  
    # 使用Mastodon API搜索相关帖子
    results = mastodon.timeline_hashtag(hashtag=topic, limit =max_results)  # 每个话题最多获取100条帖子

    # 处理搜索结果
    for status in results:
        new_dict={}
        # 可以在这里提取有关帖子的信息，如作者、内容、时间等
        author = status["account"]["username"]
        content = status["content"]
        content,related_topics =treat_contents(content,topic)
        created_at = status["created_at"]
        #print(content)

        # 将信息存储到列表中
        new_dict["author"] = author
        new_dict["content"] = content
        new_dict["related_topics"] = related_topics
        new_dict["created_at"] = created_at
        # 在这里进行数据存储或其他分析操作
        list_dict.append(new_dict)
        


    
    # 完成后的数据处理代码放在这里
    return list_dict



def treat_contents(html_string:str ,present_hastag: str):

    #print('Start')
    # Parse the HTML
    soup = BeautifulSoup(html_string, 'html.parser')
    

    # Extract the text content
    text_content = soup.get_text(strip=True, separator=' ')


    # Extract hashtags
    hashtags = [a.text for a in soup.find_all('a', class_='mention hashtag')]
    
    cleaned_string = re.sub(r'#\w+', '', text_content)

    #print("#"+present_hastag, hashtags)
    if "#"+present_hastag in hashtags:
        hashtags.remove("#"+present_hastag)
    
    if len(hashtags) > 5:
        hashtags = hashtags[:5]
    else:
        hashtags = hashtags+[None]*(5-len(hashtags))
  
    #print(hashtags, len(hashtags),'   fini')

    return cleaned_string, hashtags



def is_english(text):
    try:
        return detect(text) == 'en'
    except:
        # 处理无法检测语言的情况
        return False