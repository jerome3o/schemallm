# Import things that are needed generically
from langchain import LLMMathChain
from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.tools import BaseTool, StructuredTool, Tool, tool


def tool_function(s: str) -> str:
    return s[::-1]


def main():
    from homegpt.llm import get_llm

    tools = [
        Tool.from_function(
            func=tool_function,
            name="reverse",
            description="Useful for when you want to reverse a string.",
        ),
    ]
    llm = get_llm()
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    agent.run("reverse this string: hello world")


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    main()
