import os

from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI


_openai_api_base = os.environ["OPENAI_API_BASE"]
_model = "vicuna-13b-v1.1-8bit"


def main():
    llm = OpenAI(
        temperature=0,
        openai_api_base=_openai_api_base,
        openai_api_key="no",
        model=_model,
    )
    tools = load_tools(["llm-math"], llm=llm)
    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    output = agent.run("what is the square root of 15?")


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    main()
