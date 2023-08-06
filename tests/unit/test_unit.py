from common.best_prompt import get_template_cover_letter
from common.utils import OPENAI_API_KEY, SELECT_COVER_LETTER_TEMPLATE
from llms.code_gens import gen_codes
from llms.gpt_llm import GptLLM
from app import run


TEST_JOB_DESCRIPTION = """Our company has established a strong partnership with a renowned firm that specializes in 
developing Xamarin iOS apps. Currently, we are seeking a highly skilled Xamarin expert to join our team and take charge 
of maintaining and enhancing these exceptional applications. The role involves integrating essential features like 
Firebase Messaging and Push notifications, ensuring smooth functionality, and implementing secure authentication 
measures.

As a vital member of our development team, you will collaborate closely with a seasoned senior iOS developer. 
This collaborative environment will provide you with ample opportunities to grow your expertise and contribute to 
cutting-edge projects.

Key responsibilities include:
1. Ensuring the seamless maintenance and optimization of Xamarin iOS apps.
2. Implementing Firebase Messaging and Push notifications to enhance user engagement.
3. Incorporating robust security measures to safeguard user authentication.
4. Collaborating effectively with our experienced senior iOS developer to drive innovation and excellence.

Required Skills
• At least 4 years of experience with Xamarin mobile development
• Team communication skills
• Strong knowledge of the iOS development platform
• Strong knowledge of APNS
• Strong knowledge of Firebase Cloud Messaging
• Strong understanding of software engineering principles
• Strong understanding of the Apple Guidelines (Human Interface Guidelines and App Store Distribution)
• Familiar with using REST APIs and JSON
• Familiar with GIT code repositories
• Experience with Continuous Integration / Delivery / Deployment
• Documenting your work
"""


TEST_YOUR_COMPANY = "Fixel"

TEST_YOUR_GITHUB = "https://github.com/test123"


def test_run_best():
    """
    Tests that `run` function works well without error.
    In this function, there are 5 possible parameters.
    And cover letter template formate is the best template.
    Hence, if result isn't equal to "Please provide all necessary details", it means success.
    Otherwise, it means fail.
    """
    error = "Please provide all necessary details"

    result = run(
        openai_key=OPENAI_API_KEY,
        cover_letter_template=SELECT_COVER_LETTER_TEMPLATE[0],
        job_description=TEST_JOB_DESCRIPTION,
        your_company=TEST_YOUR_COMPANY,
        your_github=TEST_YOUR_GITHUB,
    )

    assert result != error


def test_run_simplest():
    """
    Tests that `run` function works well without error.
    In this function, there are 5 possible parameters.
    And cover letter template formate is the simplest template.
    Hence, if result isn't equal to "Please provide all necessary details", it means success.
    Otherwise, it means fail.
    """
    error = "Please provide all necessary details"

    result = run(
        openai_key=OPENAI_API_KEY,
        cover_letter_template=SELECT_COVER_LETTER_TEMPLATE[1],
        job_description=TEST_JOB_DESCRIPTION,
        your_company=TEST_YOUR_COMPANY,
        your_github=TEST_YOUR_GITHUB,
    )

    assert result != error


def test_run_useful():
    """
    Tests that `run` function works well without error.
    In this function, there are 5 possible parameters.
    And cover letter template formate is a useful template.
    Hence, if result isn't equal to "Please provide all necessary details", it means success.
    Otherwise, it means fail.
    """
    error = "Please provide all necessary details"

    result = run(
        openai_key=OPENAI_API_KEY,
        cover_letter_template=SELECT_COVER_LETTER_TEMPLATE[2],
        job_description=TEST_JOB_DESCRIPTION,
        your_company=TEST_YOUR_COMPANY,
        your_github=TEST_YOUR_GITHUB,
    )

    assert result != error


def test_run_general():
    """
    Tests that `run` function works well without error.
    In this function, there are 5 possible parameters.
    And cover letter template format is the general template.
    Hence, if result isn't equal to "Please provide all necessary details", it means success.
    Otherwise, it means fail.
    """
    error = "Please provide all necessary details"

    result = run(
        openai_key=OPENAI_API_KEY,
        cover_letter_template=SELECT_COVER_LETTER_TEMPLATE[3],
        job_description=TEST_JOB_DESCRIPTION,
        your_company=TEST_YOUR_COMPANY,
        your_github=TEST_YOUR_GITHUB,
    )

    assert result != error


def test_gen_codes():
    """
    Tests that code is generated based on job description correctly.
    """
    gpt_llm = GptLLM(openai_key=OPENAI_API_KEY)
    # get chain
    chain = gpt_llm.get_chain()

    result = gen_codes(chain=chain, job_description=TEST_JOB_DESCRIPTION)

    print(result)

    assert result is not None


def test_get_template_cover_letter_without_code():
    """
    Tests that template_cover_letter is generated without sample code correctly.
    """
    result = get_template_cover_letter(code_sample=False)

    print(result)

    assert result is not None


def test_get_template_cover_letters_with_code():
    """
    Tests that template_cover_letter is generated with sample code correctly.
    """
    result = get_template_cover_letter(code_sample=True)

    print(result)

    assert result is not None
