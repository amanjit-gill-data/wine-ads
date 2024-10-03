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

    DATA_DIR = "./data"
    STORE_DIR = "./data/store"

    # %% obtain key 

    with open("key") as file:
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

# %% 

def main():

    prompt = "Write a Facebook ad for Penfolds Grange, " + \
                "targeted at Indians " + \
                "celebrating Diwali" 

    engine = data_to_engine()
    
    print(engine.query(prompt))

# %% 

if __name__ == '__main__':
    main()




