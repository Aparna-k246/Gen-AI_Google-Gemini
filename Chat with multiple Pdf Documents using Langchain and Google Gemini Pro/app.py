import streamlit as st
from src.config import *
from src.pdf_utils import extract_text_from_pdfs
from src.chunk_utils import get_text_chunks
from src.vectorstore_utils import save_vector_store, load_vector_store
from src.qa_chain import get_conversational_chain

def handle_user_input(user_question):
    db = load_vector_store()
    docs = db.similarity_search(user_question)
    chain = get_conversational_chain()
    response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)
    st.write("Reply:", response["output_text"])

def main():
    st.set_page_config("Chat PDF")
    st.header("Chat with PDF using Gemini💁")

    user_question = st.text_input("Ask a Question from the PDF Files")
    if user_question:
        handle_user_input(user_question)

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button",
                                     accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text = extract_text_from_pdfs(pdf_docs)
                chunks = get_text_chunks(raw_text)
                save_vector_store(chunks)
                st.success("Done ✅")

if __name__ == "__main__":
    main()
