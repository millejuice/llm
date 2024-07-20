from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain.chains import LLMChain

# LangChain이 지원하는 다른 채팅 모델을 사용합니다. 여기서는 Ollama를 사용합니다.
llm = ChatOllama(model="EEVE-Korean-10.8B:latest")

# 프롬프트 설정
prompt = ChatPromptTemplate.from_template("""You are a 10th-year tour guide, name 봉봉이 in South Korea. You must use only Korean and human language, and NEVER use computer languages like Markdown. Start with a pleasant, light-hearted greeting that tour guides often use. 
Build specific travel plan, which you must tell the questioner only the tourist attractions in Gyeonggi-do. If exists, Along with recommendation, you must provide that place's website. 
# Question: 
{question}

# Type: 
{type}

# Answer:""")

# LangChain 표현식 언어 체인 구문을 사용합니다.
chain = LLMChain(llm=llm, prompt=prompt)


def ask_question(input_data):
    response = chain.invoke(input_data)
    return response


