from llama_index.core import VectorStoreIndex, Settings, SimpleDirectoryReader
from llama_index.core.chat_engine.types import ChatMode
from llama_index.llms.openai import OpenAI
import openai

# %% 

with open("key") as file:
    openai.api_key = file.readline().strip()

# %% 

docs = SimpleDirectoryReader("../data/").load_data()

index = VectorStoreIndex.from_documents(docs)

engine = index.as_query_engine()

response = engine.query("Write a Facebook ad for Penfolds Grange, targeted at the Indian market")

print(response)

# %% 



