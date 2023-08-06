"""The General Prompt Template"""


HEAD_TMP_COVER_LETTER = """
Hi, I am a senior full Stack developer with over 8 years of experience who has rich experience in the several 
industries like LMS, Ecommerce, Survey, Travel, Medical and so on.

###
In addition, give me one sample code regarding this job description - not general - by your work experience. 

###
Write some skill sets regarding to this job description.
- Back-End:
- Front-End:
- DevOps:
- DataBase:
- Other:
...

"""

END_TMP_COVER_LETTER = """
###
Asking to have a meeting or call to discuss in more detail. 

###
Best regards,
"""

GENERAL_TMP_COVER_LETTER = f"""
{HEAD_TMP_COVER_LETTER}

{END_TMP_COVER_LETTER}
"""
