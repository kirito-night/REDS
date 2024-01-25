# ARG PYTHON_VERSION=3.12
# FROM python:${PYTHON_VERSION} AS build
# COPY ./requirements.txt .
# RUN --mount=type=cache,target=/var/cache/buildkit/pip \
#     pip wheel --wheel-dir /wheels -r requirements.txt

# FROM python:${PYTHON_VERSION}-slim
# COPY requirements.txt ./
# COPY --from=build /wheels /wheels
# RUN --mount=type=cache,target=/var/cache/buildkit/pip \
#     pip install --find-links /wheels --no-index -r requirements.txt
# # Set the working directory in the container
# WORKDIR /src
# # Copy the current directory contents into the container at /src
# COPY Bow_RandomForest.ipynb /src
# COPY word2vecMLP.ipynb /src
# COPY BERT.ipynb /src
# # Run the Python script when the container launches
# ENTRYPOINT ["jupyter", "notebook","--ip","0.0.0.0", "--no-browser","--allow-root"]
# # expose jupyter port
# EXPOSE 8888


ARG PYTHON_VERSION=3.9
FROM python:${PYTHON_VERSION} AS build
COPY ./requirements.txt .

FROM python:${PYTHON_VERSION}
COPY requirements.txt ./

# RUN things needed for python packages in requirements.txt
RUN pip install --upgrade pip  && pip install --no-cache-dir -r requirements.txt

# Set the working directory in the container
WORKDIR /src
# Copy the current directory contents into the container at /src
COPY inference_mlp.py /src
COPY model/MLP.pt /src/model/
COPY model/word2vec.model /src/model/
COPY model/label_encoder.pkl /src/model/

# Run the Python script when the container launches
ENTRYPOINT ["python", "inference_mlp.py"]
# expose port 
EXPOSE 7860


