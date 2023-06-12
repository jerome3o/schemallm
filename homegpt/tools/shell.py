# Import things that are needed generically
import random
from typing import Type, Optional
from langchain import LLMMathChain
from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.tools import BaseTool, StructuredTool, Tool, tool
from pydantic import BaseModel, Field
from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)


def generate_random_numbers(n: int, lower: int, upper: int) -> list[int]:
    """Generates n random numbers given n, lower, and upper bounds."""
    return [random.randint(lower, upper) for _ in range(n)]


tool = StructuredTool.from_function(generate_random_numbers)


def main():
    from homegpt.llm import get_llm_chat

    tools = [tool]
    llm = get_llm_chat()
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        max_iterations=4,
    )

    agent.run("Generate 10 random numbers between 7 and 100")


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    main()
