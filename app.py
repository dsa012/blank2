from llama_index import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    ServiceContext,
    download_loader
)
from llama_index.llms import LlamaCPP
from llama_index.llms.llama_utils import (
    messages_to_prompt,
    completion_to_prompt,
)
from llama_index.embeddings import HuggingFaceEmbedding
import streamlit as st

model_url = "https://huggingface.co/TheBloke/Llama-2-13B-chat-GGUF/resolve/main/llama-2-13b-chat.Q5_K_M.gguf"
llm = LlamaCPP(
    model_url=model_url,
    model_path=None,
    temperature=0.1,
    max_new_tokens=256,
    context_window=3900,
    generate_kwargs={},
    model_kwargs={},
    messages_to_prompt=messages_to_prompt,
    completion_to_prompt=completion_to_prompt,
    verbose=True,
)

embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
service_context = ServiceContext.from_defaults(
    llm=llm,
    embed_model=embed_model,
)

ZendeskReader = download_loader("ZendeskReader")
loader = ZendeskReader(zendesk_subdomain="stackuphelpcentre", locale="en-us")
documents = loader.load_data()

index = VectorStoreIndex.from_documents(
    documents, service_context=service_context
)
query_engine = index.as_query_engine()
response = query_engine.query("What is Learn & Earn v2.0?")
st.write(response)
