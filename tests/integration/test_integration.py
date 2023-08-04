from common.utils import (
	OPENAI_API_KEY,
	ERROR_OPENAI_KEY,
	ERROR_JOB_DESC,
	ERROR_COMPANY,
	ERROR_GITHUB,
)
from app import run

TEST_JOB_DESCRIPTION = """Our company has established a strong partnership with a renowned firm that specializes in developing Xamarin iOS apps. Currently, we are seeking a highly skilled Xamarin expert to join our team and take charge of maintaining and enhancing these exceptional applications. The role involves integrating essential features like Firebase Messaging and Push notifications, ensuring smooth functionality, and implementing secure authentication measures.

As a vital member of our development team, you will collaborate closely with a seasoned senior iOS developer. This collaborative environment will provide you with ample opportunities to grow your expertise and contribute to cutting-edge projects.

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
• Documenting your work"""
TEST_YOUR_COMPANY = "Fixel"
TEST_YOUR_GITHUB = "https://github.com/test123"


def test_run():
	"""
	Tests that `run` function works well without error.
	In this function, there are 4 possible errors.
	Hence, if result isn't equal to those 4 errors, it means success.
	Otherwise, it means fail.
	"""
	result = run(openai_key=OPENAI_API_KEY, job_description=TEST_JOB_DESCRIPTION, your_company=TEST_YOUR_COMPANY,
	                 your_github=TEST_YOUR_GITHUB)

	assert result != ERROR_OPENAI_KEY
	assert result != ERROR_JOB_DESC
	assert result != ERROR_COMPANY
	assert result != ERROR_GITHUB
