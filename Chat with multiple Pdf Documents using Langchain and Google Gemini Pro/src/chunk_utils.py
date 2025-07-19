from langchain.text_splitter import RecursiveCharacterTextSplitter

def get_text_chunks(text, chunk_size=10000, chunk_overlap=1000):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_text(text)
