# Importing necessary libraries and modules
from common.best_prompt import KEY_WORDS, get_template_cover_letter
from common.general_prompt import GENERAL_TMP_COVER_LETTER
from common.simple_prompt import TECH_TMP_COVER_LETTER
from common.useful_prompt import QUESTION_TMP_COVER_LETTER
from common.utils import SELECT_COVER_LETTER_TEMPLATE
from llms.code_gens import gen_codes
from llms.gpt_llm import GptLLM
from langchain.docstore.document import Document
import gradio as gr

# Define templates along with their respective prompts
TEMPLATES = {
    'Best Template - Normal': get_template_cover_letter(code_sample=False),
    'Simplest Template - Technical Solution': TECH_TMP_COVER_LETTER,
    'General Template - Skill set & Code': GENERAL_TMP_COVER_LETTER,
    'Useful Template - A Few Question': QUESTION_TMP_COVER_LETTER,
}

# Define the specific queries for each template
QUERIES = {
    'Best Template - Normal': f"""
        Please analysis the job description step by step and give me a well-written cover letter following the cover letter template I shared with you.
        And also think of finding out a troubleshooting or one of best approach with those tech stack.
        If the job description would include some special technology stack or field, please focus on those technology stack and generate my work experience with them. 
        The technology stack means {KEY_WORDS}.
        Then, I don't want it in written style English and you should update it into Speaking American English. It is very important that I don't want written style english for the cover letter.
        It's better if you can explain the matched tech stack in professional with your experience.

        Please generate its greetings and farewells randomly in the cover letter every time. Please do that step by step!
    """,
    'Simplest Template - Technical Solution': f"""
        I am going to make a bid with very short and smart 4~5 sentences based on this job requirement following the cover letter template I shared with you.
                
        Include cool technical solution for this job requirement including {KEY_WORDS} as a software engineer.
                
        And describe similar project with this job as experience, seperated by 🎈.
    """,
    'General Template - Skill set & Code': f"""
        Provide real technical proposal following the cover letter template I shared with you, with work experience and skill set. 
        
        With this, the proposal must be smart and clear. And work experience must be shown reality - not general.
        
        In addition, there must be sample code - not general - by your work experience. Skill sets must be shown like this:
        
        - Back-End:
        - Front-End:
        - DevOps:
        - DataBase:
        - Other:
                 
        Then, I don't want it in written style English and you should update it into Speaking American English. It is very important that I don't want written style english for the cover letter.
                 
        Please generate its greetings and farewells randomly in the cover letter every time. Please do that step by step!
    """,
    'Useful Template - A Few Question': f"""
        Please analysis the job description step by step and give me a well-written cover letter following the cover letter template I shared with you.
        And include specific technical experience that is real and not just general.
                
        Then, I don't want it in written style English and you should update it into Speaking American English. 
        It is very important that I don't want written style english for the cover letter.
    """
}


def run(openai_key="",
        cover_letter_template=SELECT_COVER_LETTER_TEMPLATE[0],
        job_description: str = "",
        your_company: str = "",
        your_github: str = "",
        code_sample: bool = False):
    """
        Preprocess job description, company, and Github profile.
        Generate the cover letter and optional sample code.
    """

    # Create the template with variable fields
    template = f"""
        ###
        This is the Job Description.
        {job_description}

        ###
        This is my github profile.
        {your_github}

        ###
        This is my recent company name I've worked for last 4 years. 
        {your_company}

        ###
        This is the expected cover letter template. 
        {TEMPLATES[cover_letter_template]}
    """

    # validate inputs
    if not all([openai_key, job_description, your_company, your_github]):
        return 'Please provide all necessary details'

    # Generate expected documents
    docs = [Document(page_content=template, metadata="")]

    # Initialize the GptLLM model &  generate chain data
    gpt_llm = GptLLM(openai_key=openai_key)
    chain = gpt_llm.get_chain()

    # Check if code samples are requested; if so, generate them
    if code_sample:
        return chain.run(input_documents=docs, question=QUERIES[cover_letter_template]), \
            gen_codes(chain, job_description)

    return chain.run(input_documents=docs, question=QUERIES[cover_letter_template]), ""


# Define input fields and labels for the Gradio Interface

inputs = [
    gr.inputs.Textbox(lines=1, placeholder="Enter your open_ai_key here..."),
    gr.inputs.Dropdown(SELECT_COVER_LETTER_TEMPLATE, default=SELECT_COVER_LETTER_TEMPLATE[0],
                       label="Choose your cover letter template..."),
    gr.inputs.Textbox(lines=15, placeholder="Enter the job description here..."),
    gr.inputs.Textbox(
        lines=1, placeholder="Enter your company name, where you've worked recently..."
    ),
    gr.inputs.Textbox(lines=1, placeholder="Enter your github here..."),
    gr.inputs.Checkbox(label="Do you want Sample Code as well?"),
]

outputs = [
    gr.outputs.Textbox(label="Cover Letter"),
    gr.outputs.Textbox(label="Sample Code"),
]

# Initialize and launch the Gradio Interface
demo = gr.Interface(fn=run, inputs=inputs, outputs=outputs)
demo.launch()
