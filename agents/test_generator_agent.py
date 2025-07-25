import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import warnings
warnings.filterwarnings('ignore')
load_dotenv()

llm = ChatOpenAI(temperature=0.1, model="gpt-4")


def generate_test_code(endpoint_description):
    prompt = PromptTemplate(
        input_variables=["description"],
        template="""
                    Write 5  pytest-based tests function in Python that:
                    - Tests this API: {description}
                    - Uses 'requests' library
                    - Pirnt the response
                    - Asserts status code 201, add failure text
                    - Parses JSON and verifies at least one key
                    - add x-api-key: reqres-free-v1 in header of request
                    - log test failures in /logs/test_failures.log
                    - if description says POST, then generate payload and proceed
                    - Use exception handling in all assertions in all tests, so failed assertions gets logged in the log file
                    ⚠️ DO NOT include any comments or explanations in the code.
                    ⚠️ DO NOT include extra text, return ONLY raw Python code.
                    """)

    chain = LLMChain(llm=llm, prompt=prompt)
    return chain.run(description=endpoint_description)


def save_test(test_code, filename="tests/test_generated_users.py"):
    with open(filename, "w") as f:
        f.write("import requests\nimport pytest\n\n")
        f.write(test_code)
