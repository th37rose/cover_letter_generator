from common.utils import OPENAI_API_KEY, ERROR_OPENAI_KEY, ERROR_JOB_DESC, ERROR_COMPANY, ERROR_GITHUB
from llms.gpt_llm import GptLLM
from langchain.docstore.document import Document
import gradio as gr

GITHUB_LINK = "https://github.com/stackdev37"

"""Prompt Template"""

"""Please mention all keywords."""
KEY_WORDS = """
 java, python, node.js, GraphQL, vue, react, nest, next, ai, dl, gcp, aws, azure, kubernetes, docker, microservice, gpt, chatbot, frontend, backend, video streamming, devops, CI/CD, mysql, mongodb, postgresql or etc
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


def run(
    openai_key="",
    job_description: str = "",
    your_company: str = "",
    your_github: str = GITHUB_LINK,
    code_sample: bool = False,
) -> str:
    # generating prompts & query
    template = f"""
    This is the Job Description.
    ###
    {job_description}
    
    This is my github profile.
    ###
    {your_github}
    
    This is my recent company name I've worked for last 4 years. 
    ###
    {your_company}
    
    This is the expected cover letter template. 
    {TEMPLATE_COVER_LETTER}
    """

    query = f"""
    Please analysis the job description step by step and give me a well-written cover letter following the cover letter template I shared with you.
    If the job description would include some special technology stack or field, please focus on those technology stack and generate my work experience with them. 
    The technology stack means {KEY_WORDS}.
    Then, I don't want it in written style English and you should update it into Speaking American English. It is very important that I don't want written style english for the cover letter.
    It's better if you can explain the matched tech stack in professional with your experience.
    
     
    Please generate its greetings and farewells randomly in the cover letter every time. Please do that step by step!
    """
    # validation
    if not openai_key:
        return ERROR_OPENAI_KEY
    if not job_description:
        return ERROR_JOB_DESC
    if not your_company:
        return ERROR_COMPANY
    if not your_github:
        return ERROR_GITHUB

    # generate the expected result
    docs = []
    docs.append(Document(page_content=template, metadata=""))
    # get gpt llm
    gpt_llm = GptLLM(openai_key=openai_key)
    # get chain
    chain = gpt_llm.get_chain()
    # get chain data / result
    print("engine: started")
    chain_data = chain.run(input_documents=docs, question=query)
    print("engine: completed successfully")
    return chain_data


"""run gradio demo"""
inputs = [
    gr.inputs.Textbox(lines=1, placeholder="Enter your open_ai_key here..."),
    gr.inputs.Textbox(lines=15, placeholder="Enter the job description here..."),
    gr.inputs.Textbox(
        lines=1, placeholder="Enter your company name, where you've worked recently..."
    ),
    gr.inputs.Textbox(lines=1, placeholder="Enter your github here..."),
    gr.inputs.Checkbox(label="Do you want Sample Code as well?"),
]

demo = gr.Interface(fn=run, inputs=inputs, outputs="text")

demo.launch()
