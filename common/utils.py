import os

# env variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# error message
ERROR_OPENAI_KEY = "Please input openai_api_key"
ERROR_JOB_DESC = "Please input job description"
ERROR_COMPANY = "Please input company name"
ERROR_GITHUB = "Please input github link"

# dropdown option list
SELECT_COVER_LETTER_TEMPLATE = ["Best Template - Normal", "Simplest Template - Technical Solution", "Useful Template - A Few Question", "General Template - Skill set & Code"]

# template name
NORMAL_TEMPLATE = "Best Template - Normal"
TECHNICAL_TEMPLATE = "Simplest Template - Technical Solution"
QUESTION_TEMPLATE = "Useful Template - A Few Question"
GENERAL_TEMPLATE = "General Template - Skill set & Code"
