import streamlit as st
from dotenv import load_dotenv
import pickle
from PyPDF2 import PdfReader
import pandas as pd
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
import os
from PIL import Image

st.set_page_config(
    page_title="Chat with PDF",
    page_icon="loco.png",  # Replace "path_to_your_logo.png" with the actual path to your logo image file.
    layout="wide",
    initial_sidebar_state="collapsed"
)


# Add custom CSS styles for chat layout 
st.markdown("""
    <style>
    
        div.block-container.css-z5fcl4.egzxvld4 {
        padding-top: 55px;
        }

        .user-chat {
            background-color: #F0F0F0;
            padding: 10px;
            margin-bottom: 10px;
        }
        
        .bot-chat {
            background-color: #E6F7FF;
            padding: 10px;
            margin-bottom: 10px;
        }
        
        footer.css-164nlkn.egzxvld1 {
        display: none;
        }
        
        
        body {
            background-image: url('back.png'); /* Replace 'path_to_your_background_image.jpg' with the actual path or URL to your background image */
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-size: cover;
        }
        
        div.css-1kyxreq.etr89bj2 {
        display: flex;
        flex-direction: row;
        justify-content: center;
        }

        
     

    </style>
""", unsafe_allow_html=True)

        

#load_dotenv()

def main():
    # Load and display the logo image
    #logo = Image.open('logo.png')  # Replace 'path_to_your_logo.png' with the actual path to your logo image file
    #st.image(logo)
        
    state = st.session_state.get('state', {'chat_history': []})
    st.header("Arya 🤖")
    st.write("I’m your friendly assistant ready to answer questions about your uploaded PDF files. Ask away!")
    openai_api_key = st.text_input("Enter your OpenAI API Key:")
    if not openai_api_key:
        st.warning("Please enter your OpenAI API Key.")
        return

    # Create a list to store all previous chats 
    all_chats = []

    # Upload PDF files 
    pdf_files = st.file_uploader("Upload your PDF files", type='pdf', accept_multiple_files=True)

    if pdf_files:
        all_text = ""
        for pdf in pdf_files:
            pdf_reader = PdfReader(pdf)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            
            all_text += text + " "

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
        )
        chunks = text_splitter.split_text(text=all_text)

        store_name = "combined_files"

        if os.path.exists(f"{store_name}.pkl"):
            with open(f"{store_name}.pkl", "rb") as f:
                VectorStore = pickle.load(f)
        else:
            embeddings = OpenAIEmbeddings()
            VectorStore = FAISS.from_texts(chunks, embedding=embeddings)
            with open(f"{store_name}.pkl", "wb") as f:
                pickle.dump(VectorStore, f)

        query = st.text_input("Ask questions about your PDF files:")

        if query:
            # Show a spinner/loader while generating the response 
            with st.spinner("Generating response..."):
                docs = VectorStore.similarity_search(query=query, k=3)

                llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.2, api_key=openai_api_key)
                chain = load_qa_chain(llm=llm, chain_type="stuff")
                with get_openai_callback() as cb:
                    prompt = "I want you to act a friendly support chatbot. Your name is 'Arya'. Please provide helpful answers based on the information in the documents uploaded.\nIf you don't know the answer, just say 'Hmm, I'm not sure of this question. Stay in the character all the time."
                    query_with_prompt = prompt + query
                    response = chain.run(input_documents=docs, question=query_with_prompt)
                    
                    state['chat_history'].append(("user", query))
                    state['chat_history'].append(("bot", response))
                    
                    reversed_chat_history = state['chat_history'][::-1]

                    for i, (role, message) in enumerate(reversed(state['chat_history'])):
                        if role == 'user':
                            # Apply CSS styling to display user on the right side
                            st.markdown(
                                f'<div style="display: flex; justify-content: flex-end;"><div style="max-width: 70%; background-color: #DCF8C6; padding: 10px;">{message}</div></div>',
                                unsafe_allow_html=True
                            )
                        else:
                            # Apply CSS styling to display bot on the left side
                            st.markdown(
                                f'<div style="display: flex; justify-content: flex-start;"><div style="max-width: 70%; background-color: #F2F3F5; padding: 10px;">{message}</div></div>',
                                unsafe_allow_html=True
                            )

                        if i % 2 == 1 and i != len(state['chat_history'])-1:
                            st.markdown("---")

                        st.session_state['state'] = state
    
if __name__ == '__main__':
    main()