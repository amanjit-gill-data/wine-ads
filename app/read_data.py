from llama_index.core import (
    StorageContext,
    SimpleDirectoryReader,
    VectorStoreIndex,
    load_index_from_storage
)

import openai
import os

# read data, output engine 
# take query from user; output response 

def data_to_engine(): 

    """
    check if index exists; if not, read in data and create new index 
    create and return chat engine
    """

    APP_DIR = "app"

    DATA_DIR = APP_DIR + "/data"
    STORE_DIR = DATA_DIR + "/store"
    KEY_PATH = APP_DIR + "/key"

    # %% obtain key 

    with open(KEY_PATH) as file:
        openai.api_key = file.readline().strip()

    # %% read data 

    if not os.path.exists(STORE_DIR):
        docs = SimpleDirectoryReader(DATA_DIR).load_data()
        index = VectorStoreIndex.from_documents(docs)
        index.storage_context.persist(persist_dir=STORE_DIR)
    else:
        context = StorageContext.from_defaults(persist_dir=STORE_DIR)
        index = load_index_from_storage(context)

    return index.as_query_engine()

