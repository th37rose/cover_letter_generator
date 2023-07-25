from common.utils import OPENAI_API_KEY
from llms.gpt_llm import GptLLM
from langchain.docstore.document import Document
import gradio as gr

GITHUB_LINK = "https://github.com/stackdev37"

"""Prompt Template"""

"""Please describe your experience with your reent job."""
YOUR_EXPERIENCE = """
I've worked at BookBeam(bookbeam.io) as a software engineer for last 4 years from the scratch. 
It is a customer toolset to increase their booksales on Amazon. I can say it is a enterprise level application and the backend was built with microservice architecture. 
So the main functionality is to scrape the data from the exiting Amazon website. 
I've built the CI/CD for its infrastructure with github actions & jenkins and deployed in kubernetes cluster. 
It includes vast of tech stacks what you want. 
"""

TEMPLATE_COVER_LETTER = """
Hi, I am a Java software engineer with over eight years of professional experience.

###
My experiences with those tech stack which was mentioned in the job post. 

###
Trying to give the hot keywords they are looking for. 

###
Asking to have a meeting or call to discuss in more detail. 

###
Attaching my git profile for their reference. 

Best regards,
"""

"""main method to get the expected output"""
def run(job_desc: str) -> str:
    # generating prompts & query
    template = f"""
    This is the Job Description.
    ###
    {job_desc}
    
    This is my github profile.
    ###
    {GITHUB_LINK}
    
    This is my experience. 
    ###
    {YOUR_EXPERIENCE}
    
    This is the expected cover letter template. 
    {TEMPLATE_COVER_LETTER}
    """
    query = """
    Please analysis the job description step by step and give me a well-written cover letter following the cover letter template I shared with you.
    Then update it into Speaking American English. I don't want written style english for the cover letter.
    It's better if you can explain the matched tech stack in professional with your experience.
    """
    docs = []
    docs.append(Document(page_content=template, metadata=""))
    # get gpt llm
    gpt_llm = GptLLM(openai_key=OPENAI_API_KEY)
    # get chain
    chain = gpt_llm.get_chain()
    # get chain data / result
    print("engine: started")
    chain_data = chain.run(
        input_documents=docs, question=query
    )
    print("engine: completed successfully")
    return chain_data


"""run gradio demo"""
demo = gr.Interface(fn=run, inputs="text", outputs="text")

demo.launch()
