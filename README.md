
# Refrace
- This project is an applied project based on this course [mini-RAG | From notebooks to the PRODUCTION](https://www.youtube.com/playlist?list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj)
- You can find the course code and resources on the [GitHub repository](https://github.com/bakrianoo/mini-rag/tree/tut-009)
- Flollow Abu Bakr Soliman on [LinkedIn](https://www.linkedin.com/in/bakrianoo)

# RAG Application
The project aims to develop a Retrieval-Augmented Generation (RAG) application that combines the power of Large Language Models (LLMs) with robust data storage and retrieval mechanisms to deliver highly accurate, real-time responses. The objective is to create a scalable and efficient API that enables seamless integration with external systems.

![Application Diagram](./src/assets/Machine%20Learning.png)

## Requirements
- python 3.8 or later

#### Install Python using MiniConda

1) Download and install Miniconda from [here](https://docs.anaconda.com/free/miniconda/#quick-command-line-install)

2) Create a new environment using the following command:
```bash
$ conda create -n mini-rag python=3.8
```
3) Activate the environment:
```bash
$ conda activate mini-rag
```

### (Optional) Setup your command line interface for better readability
```bash
export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
```

## Installation

### install the required packages

```bash
$ pip install -r requirements.txt
```

### Setup the environment variables
```bash
$ cp .env.example .env
```
Set your environment variables in the `.env` file. Like `OPENAI_API_KEY` value.

## Run Docker Compose Services

```bash
$ cd docker
$ cp .env.example .env
```

- update `.env` with your credentials

```bash
$ cd docker
$ sudo docker compose up -d
```


## Run FastAPI Server
```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

## Postman Collection

Download the POSTMAN collection from [/src/assets/mini-rag.postman_collection.json](/src/assets/mini-rag.postman_collection.json)

