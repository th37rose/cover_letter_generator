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
]


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
        I am going to make a bid with very short and smart 4~5 sentences based on this job requirement following the 
        cover letter template I shared with you.

        Include cool technical solution for this job requirement including {KEY_WORDS} as a software engineer.
        
        The technology stack means {KEY_WORDS}.

        And describe similar project with this job as experience.
        
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
}


QUESTIONS_TEMPLATE = """
Write a cool and well-written technical answer about 3 sentences.
I don't want written style english, write as speaking English.
"""
