from langchain.chains.combine_documents.base import BaseCombineDocumentsChain
from langchain.docstore.document import Document

"""generate sample codes with solutions"""


def gen_codes(chain: BaseCombineDocumentsChain, job_description: str) -> str:
    # prompts
    template = f"""
    This is the Job Description or the requirement what they want.
    ###
    {job_description}
    """
    query = """
    Please analysis the job description or the requirement step by step to find out a troubleshooting or one of best 
    approach. 
    And then please give me some programming codes to reflect my professional with those technology stack in 
    development.
    You are a helpful code assistant that can teach a junior developer how to code. Your language of choice is the 
    programming language what they are specifically looking for . Don't explain the code, just generate the code block 
    itself.
    """
    docs = [Document(page_content=template, metadata="")]

    print("engine: started to generate sample codes")
    result = chain.run(input_documents=docs, question=query)
    print("engine: completed to generate the sample codes successfully")

    return result
