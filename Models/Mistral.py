from langchain_mistralai.chat_models import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from dotenv import load_dotenv
import os

memory_store = {}

class Mistral:
    def __init__(self):
        load_dotenv()
        mistral_api_key = os.getenv("MISTRAL_API_KEY")
        self.llm = ChatMistralAI(api_key=mistral_api_key, model="mistral-large-latest")

        prompt = ChatPromptTemplate.from_messages([
            ("system", "Jesteś pomocnym asystentem, testerem formularzy elektronicznych na stonach www."),
            ("human", "{input}")
        ])

        chain = prompt | self.llm

        self.conversation = RunnableWithMessageHistory(
            chain,
            get_session_history=self.get_history,
            input_messages_key="input"
        )

    def get_history(self, session_id):
        if session_id not in memory_store:
            memory_store[session_id] = ChatMessageHistory()
        return memory_store[session_id]

    def ask_simple_question(self, text, session_id="default"):
        return self.conversation.invoke(
            {"input": text},
            config={"configurable": {"session_id": session_id}}
        )
    
    def get_history_as_text(self, session_id="default"):
        history = self.get_history(session_id).messages
        return "\n".join(f"{msg.type}: {msg.content}" for msg in history)

    
    def ask_question(query):
        result = qa_chain({"query": query})
        print("Odpowiedź:", result["result"])
        print("\nŹródła:")
        for doc in result["source_documents"]:
            print("-", doc.page_content[:200] + "...")


# from langchain.document_loaders import TextLoader
# from langchain.text_splitter import CharacterTextSplitter
# from langchain.embeddings import HuggingFaceEmbeddings
# from langchain.vectorstores.pgvector import PGVector
# from langchain.chat_models import ChatMistralAI  # Nowe API Mistral Large
# from langchain.chains import RetrievalQA
# import os
# from dotenv import load_dotenv

# # Ładowanie zmiennych środowiskowych (API key i dane bazy)
# load_dotenv()

# # 1. Wczytanie dokumentu (np. plik TXT)
# loader = TextLoader("sciezka/do/pliku.txt", encoding="utf-8")
# documents = loader.load()

# # 2. Podział tekstu na fragmenty
# text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
# texts = text_splitter.split_documents(documents)

# # 3. Inicjalizacja embedderów (np. Hugging Face lub OpenAI)
# embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# # 4. Połączenie z PostgreSQL + PGVector
# CONNECTION_STRING = PGVector.connection_string_from_db_params(
#     driver="psycopg2",
#     host="localhost",
#     port=5432,
#     database="nazwa_bazy",
#     user="user",
#     password="haslo",
# )

# # 5. Zapis dokumentów do PGVector
# COLLECTION_NAME = "my_documents"
# db = PGVector.from_documents(
#     documents=texts,
#     embedding=embeddings,
#     collection_name=COLLECTION_NAME,
#     connection_string=CONNECTION_STRING,
# )

# # 6. Inicjalizacja Mistral Large (przez API)
# mistral_api_key = os.getenv("MISTRAL_API_KEY")  # Pobierz klucz z https://mistral.ai/
# llm = ChatMistralAI(api_key=mistral_api_key, model="mistral-large-latest")

# # 7. Stworzenie łańcucha QA
# qa_chain = RetrievalQA.from_chain_type(
#     llm=llm,
#     chain_type="stuff",
#     retriever=db.as_retriever(search_kwargs={"k": 3}),
#     return_source_documents=True
# )

# # 8. Funkcja do zadawania pytań
# def ask_question(query):
#     result = qa_chain({"query": query})
#     print("Odpowiedź:", result["result"])
#     print("\nŹródła:")
#     for doc in result["source_documents"]:
#         print("-", doc.page_content[:200] + "...")

# # Przykład użycia
# ask_question("Jakie są główne wnioski z dokumentu?")
