"""The Useful Prompt Template"""


HEAD_TMP_COVER_LETTER = """
Good day there, 

First, I'd want you to look at this URL, which is comparable to your project on which I worked: 
https://github.com/given github username

###
Provide rough timeline and cost as a senior software engineer.

While reviewing your requirements, I have a few quick questions regarding the job:
[write some technical questions about the job description]
-
-
...

I am a experienced full stack engineer with over 8 years of professional experience.

Recently, I’ve completed a project very similar to your requirements and received High Praise from my client.
[write relevant technical experience about the job description]

"""

END_TMP_COVER_LETTER = """
###
If you're interested, please contact me so we can set up a meeting and cooperate. I'm hoping to hear from you shortly.

Thank you very much.
"""

QUESTION_TMP_COVER_LETTER = f"""
{HEAD_TMP_COVER_LETTER}

{END_TMP_COVER_LETTER}
"""
