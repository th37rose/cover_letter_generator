# Importing necessary libraries and modules
from common.best_prompt import get_template_cover_letter
from common.general_prompt import GENERAL_TMP_COVER_LETTER
from common.blockchain_prompt import BLOCKCHAIN_TMP_COVER_LETTER
from common.simple_prompt import TECH_TMP_COVER_LETTER
from common.useful_prompt import QUESTION_TMP_COVER_LETTER
from common.utils import (
    SELECT_COVER_LETTER_TEMPLATE,
    QUERIES,
    QUESTIONS_TEMPLATE,
    SELECT_GPT_MODEL,
)
from llms.code_gens import gen_codes
from llms.gpt_llm import GptLLM
from langchain.docstore.document import Document
import gradio as gr

# Define templates along with their respective prompts
TEMPLATES = {
    "Best Template - Normal": get_template_cover_letter(code_sample=False),
    "Simplest Template - Technical Solution": TECH_TMP_COVER_LETTER,
    "General Template - Skill set & Code": GENERAL_TMP_COVER_LETTER,
    "Useful Template - A Few Question": QUESTION_TMP_COVER_LETTER,
    "Blockchain Template": BLOCKCHAIN_TMP_COVER_LETTER,
}


def run(
    openai_key="",
    gpt_model=SELECT_GPT_MODEL[0],
    cover_letter_template=SELECT_COVER_LETTER_TEMPLATE[0],
    job_description: str = "",
    your_company: str = "",
    your_github: str = "",
    additional_question1: str = "",
    additional_question2: str = "",
    additional_question3: str = "",
    additional_question4: str = "",
    additional_question5: str = "",
    code_sample: bool = False,
):
    """
    Preprocess job description, company, and GitHub profile.
    Generate the cover letter and optional sample code.
    """
    questions_array = [
        additional_question1,
        additional_question2,
        additional_question3,
        additional_question4,
        additional_question5,
    ]

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
        return "Please provide all necessary details"

    # Generate expected documents
    docs = [Document(page_content=template, metadata="")]

    # Initialize the GptLLM model &  generate chain data
    gpt_llm = GptLLM(openai_key=openai_key, model=gpt_model)
    chain = gpt_llm.get_chain()

    # Generate answers for additional questions
    answers_array = [
        chain.run(input_documents=docs, question=QUESTIONS_TEMPLATE + question)
        if question
        else ""
        for question in questions_array
    ]

    # Check if code samples are requested; if so, generate them
    if code_sample:
        return (
            chain.run(input_documents=docs, question=QUERIES[cover_letter_template]),
            gen_codes(chain, job_description),
            answers_array[0],
            answers_array[1],
            answers_array[2],
            answers_array[3],
            answers_array[4],
        )

    # cover letter
    return (
        chain.run(input_documents=docs, question=QUERIES[cover_letter_template]),
        "",
        answers_array[0],
        answers_array[1],
        answers_array[2],
        answers_array[3],
        answers_array[4],
    )


def launch_app():
    # Define input fields and labels for the Gradio Interface

    inputs = [
        gr.inputs.Textbox(lines=1, placeholder="Enter your open_ai_key here..."),
        gr.inputs.Dropdown(
            SELECT_GPT_MODEL,
            default=SELECT_GPT_MODEL[0],
            label="Choose your gpt model",
        ),
        gr.inputs.Dropdown(
            SELECT_COVER_LETTER_TEMPLATE,
            default=SELECT_COVER_LETTER_TEMPLATE[0],
            label="Choose your cover letter template...",
        ),
        gr.inputs.Textbox(lines=15, placeholder="Enter the job description here..."),
        gr.inputs.Textbox(
            lines=1,
            placeholder="Enter your company name, where you've worked recently...",
        ),
        gr.inputs.Textbox(lines=1, placeholder="Enter your github here..."),
        gr.inputs.Textbox(lines=1, placeholder="Additional question 1"),
        gr.inputs.Textbox(lines=1, placeholder="Additional question 2"),
        gr.inputs.Textbox(lines=1, placeholder="Additional question 3"),
        gr.inputs.Textbox(lines=1, placeholder="Additional question 4"),
        gr.inputs.Textbox(lines=1, placeholder="Additional question 5"),
        gr.inputs.Checkbox(label="Do you want Sample Code as well?"),
    ]

    outputs = [
        gr.outputs.Textbox(label="Cover Letter"),
        gr.outputs.Textbox(label="Sample Code"),
        gr.outputs.Textbox(label="Answer 1"),
        gr.outputs.Textbox(label="Answer 2"),
        gr.outputs.Textbox(label="Answer 3"),
        gr.outputs.Textbox(label="Answer 4"),
        gr.outputs.Textbox(label="Answer 5"),
    ]

    # Initialize and launch the Gradio Interface
    demo = gr.Interface(fn=run, inputs=inputs, outputs=outputs)
    demo.launch()


if __name__ == "__main__":
    launch_app()
