# Import things that are needed generically
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


class ReverseInput(BaseModel):
    """Input to the reverse tool."""

    text: str = Field(..., description="The text to reverse.")


class ReverseTool(BaseTool):
    name = "reverse"
    description = "Useful for reversing text."
    args_schema: Type[BaseModel] = ReverseInput

    def _run(
        self, query: str, run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        """Use the tool."""
        return query[::-1]

    async def _arun(
        self, query: str, run_manager: Optional[AsyncCallbackManagerForToolRun] = None
    ) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("Reverse does not support async")


def main():
    from homegpt.llm import get_llm

    tools = [ReverseTool()]
    llm = get_llm()
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        max_iterations=4,
    )

    agent.run("reverse this string: hello world")


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    main()
