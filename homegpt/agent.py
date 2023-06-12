from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.tools import ShellTool

from homegpt.llm import get_llm


def main():
    llm = get_llm()
    shell_tool = ShellTool()
    shell_tool.description = shell_tool.description + f"args {shell_tool.args}".replace(
        "{", "{{"
    ).replace("}", "}}")
    tools = load_tools(["llm-math"], llm=llm)
    agent = initialize_agent(
        tools + [shell_tool],
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        max_iterations=4,
    )

    output = agent.run("what is the square root of 15?")


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    main()
