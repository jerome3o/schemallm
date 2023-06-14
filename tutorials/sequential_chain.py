from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import SimpleSequentialChain

from homegpt.llm import get_llm

llm = get_llm()


# This is an LLMChain to write a synopsis given a title of a play.
template = """You are a playwright. Given the title of play, it is your job to write a \
synopsis for that title.

Title: {title}
Playwright: This is a synopsis for the above play:"""

prompt_template = PromptTemplate(input_variables=["title"], template=template)
synopsis_chain = LLMChain(llm=llm, prompt=prompt_template)


# This is an LLMChain to write a review of a play given a synopsis.
template = """You are a play critic from the New York Times. Given the synopsis of play\
, it is your job to write a review for that play.

Play Synopsis:
{synopsis}
Review from a New York Times play critic of the above play:"""
prompt_template = PromptTemplate(input_variables=["synopsis"], template=template)
review_chain = LLMChain(llm=llm, prompt=prompt_template)

# This is the overall chain where we run these two chains in sequence.

overall_chain = SimpleSequentialChain(
    chains=[synopsis_chain, review_chain],
    verbose=True,
)

review = overall_chain.run("Tragedy at sunset on the beach")
