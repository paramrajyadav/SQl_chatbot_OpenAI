import os
from langchain.agents import *
from langchain.llms import OpenAI
from langchain.sql_database import  SQLDatabase
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import AgentExecutor
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

class ChatWithSql:
    """ ChatWithSql class is used for query user question with SQL Database using chat
    
    """
    def __init__(self,db_user,db_password,db_host,db_name):

        """This is a constructor method for the ChatWithSql class"""
        load_dotenv()
        os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

        self.db_user=db_user
        self.db_password=db_password
        self.db_host=db_host
        self.db_name=db_name


    def message(self,query):
        """message method will take the querry from the user and process the result and
        return the response
        
        Args:
            querry(String): this is the question of the user
        returns :
            response(String) : This is the reponse genrated by l
          """
        llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
        db=SQLDatabase.from_uri(f"mysql+pymysql://{self.db_user}:{self.db_password}@{self.db_host}/{self.db_name}")
        toolkit = SQLDatabaseToolkit(db=db,llm=llm)
        agent_executor = create_sql_agent(llm=llm,toolkit=toolkit,verbose=True)

        response=agent_executor.run(query)
        return response
    
obj = ChatWithSql("root","root","localhost","d1")
print(obj.message("How many rows do we have in salaries table ?"))
