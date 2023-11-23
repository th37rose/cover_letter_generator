import os
from common.best_prompt import KEY_WORDS, EMOTIONS

# env variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# error message
ERROR_OPENAI_KEY = "Please input openai_api_key"
ERROR_JOB_DESC = "Please input job description"
ERROR_COMPANY = "Please input company name"
ERROR_GITHUB = "Please input github link"


# dropdown option list
SELECT_COVER_LETTER_TEMPLATE = [
    "Best Template - Normal",
    "Simplest Template - Technical Solution",
    "Useful Template - A Few Question",
    "General Template - Skill set & Code",
    "Blockchain Template",
]

# dropdown option list for gpt model
SELECT_GPT_MODEL = ["gpt-4-1106-preview", "gpt-3.5-turbo", "gpt-4"]


# Define the specific queries for each template
QUERIES = {
    "Best Template - Normal": f"""
        Please analysis the job description step by step and give me a well-written cover letter following the cover 
        letter template I shared with you.
        And also think of finding out a troubleshooting or one of best approach with those tech stack.
        If the job description would include some special technology stack or field, please focus on those technology 
        stack and generate my work experience with them. 
        The technology stack means {KEY_WORDS}.
        Then, I don't want it in written style English and you should update it into Speaking American English. It is 
        very important that I don't want written style english for the cover letter.
        It's better if you can explain the matched tech stack in professional with your experience.

        Please generate its greetings and farewells randomly in the cover letter every time. Please do that step by 
        step!
    """,
    "Simplest Template - Technical Solution": f"""
        Please analysis the job description step by step and give me a well-written, smart and very short cover letter 
        in 4~5 sentences following the cover letter template I shared with you.
        
        And include cool technical solution for this job requirement as a senior software engineer.

        In addition, describe similar project with this job as experience.
        
        Please generate its greetings and farewells randomly with {EMOTIONS} at the start and the end of greetings in 
        the cover letter every time. Please do that step by step!
    """,
    "General Template - Skill set & Code": f"""
        Please analysis ths job description step by step and give me real technical cover letter following the cover 
        letter template I shared with you, with work experience and skill set. 

        With this, the proposal must be smart and clear. And work experience must be shown reality - not general.

        Then, I don't want it in written style English and you should update it into Speaking American English. 
        It is very important that I don't want written style english for the cover letter.

        Please generate its greetings and farewells randomly in the cover letter every time. Please do that step by 
        step!
    """,
    "Useful Template - A Few Question": f"""
        Please analysis the job description step by step and give me a well-written cover letter following the cover 
        letter template I shared with you.
        And include specific technical experience that is real and not just general.

        Then, I don't want it in written style English and you should update it into Speaking American English. 
        It is very important that I don't want written style english for the cover letter.
        
        Please generate its greetings and farewells randomly in the cover letter every time.
    """,
    "Blockchain Template": f"""
        Please analysis ths job description step by step and give me real technical cover letter following the cover 
        letter template I shared with you, with work experience and skill set.

        With this, the proposal must be smart and clear. And blockchain work experience must be shown reality - not general.

        Then, I don't want it in written style English and you should update it into Speaking American English, but it has the system as follows.
        It is very important that I don't want written style english for the cover letter.

        Please generate its greetings and farewells randomly in the cover letter every time. Please do that step by 
        step!
    """,
}


QUESTIONS_TEMPLATE = """
Write a cool and well-written technical answer about 3-4 sentences as speaking English randomly.
"""
