from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

def main():
    prompt = PromptTemplate.from_template("Say hi to {name}.")
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    chain = prompt | llm
    resp = chain.invoke({"name": "Henry"})
    print(resp.content)

if __name__ == "__main__":
    main()
