"""The Best Prompt Template"""

"""Please mention all keywords."""


KEY_WORDS = """
 java, python, node.js, GraphQL, vue, react, nest, next, ai, dl, gcp, aws, azure, kubernetes, docker, microservice, gpt, 
 chatbot, frontend, backend, video streamming, devops, CI/CD, mysql, mongodb, postgresql or etc
"""


"""Please add some emotions."""
EMOTIONS = """
✨, ❤, 🙋‍♀️, 😍, 🚀, 🎯, ✔, 🔺, 🧡, 💛, 💚, 💙, 💜, 🤎, 🖤, 💔, ❣, 💕, 💞, 💓, 💗, 💖, 💘, 💝
"""

BASIC_HEAD_TMP_COVER_LETTER = """
Hi, I am a seasoned software engineer with over eight years of professional experience.

###
My experiences with those tech stack which was mentioned in the job post. 

###
Trying to give the hot keywords they are looking for. 

"""

BASIC_END_TMP_COVER_LETTER = """
###
Asking to have a meeting or call to discuss in more detail. 

###
Attaching my git profile for their reference. 

Best regards,
"""

TMP_SAMPLE_CODE_CL = """
###
Trying to suggest one of the best approach to reflect my professional with those technology stack

"""
TEMPLATE_COVER_LETTER = f"""
{BASIC_HEAD_TMP_COVER_LETTER} 

{BASIC_END_TMP_COVER_LETTER}
"""


def get_template_cover_letter(code_sample: bool = False) -> str:
    print("----")
    print(code_sample)
    if code_sample:
        return f"""
            {BASIC_HEAD_TMP_COVER_LETTER}
            
            {TMP_SAMPLE_CODE_CL} 
            
            {BASIC_END_TMP_COVER_LETTER}
            """
    else:
        return f"""
            {BASIC_HEAD_TMP_COVER_LETTER}
    
            {BASIC_END_TMP_COVER_LETTER}
            """
