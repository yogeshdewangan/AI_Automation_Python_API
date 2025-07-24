from langchain.document_loaders import TextLoader
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model="gpt-4")
import warnings
warnings.filterwarnings('ignore')

def analyze_logs(log_path="logs/test_failures.log"):
    loader = TextLoader(log_path)
    docs = loader.load()

    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(docs, embeddings)
    retriever = db.as_retriever()

    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    answer = qa.run("What are the main reasons for test failures and how can I fix them?")
    print("\n🧠 AI Log Summary:\n", answer)