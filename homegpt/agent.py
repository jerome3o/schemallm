import re
from typing import Any, List, Tuple, Union

from langchain import LLMChain, OpenAI, SerpAPIWrapper
from langchain.agents import (
    AgentExecutor,
    AgentOutputParser,
    BaseSingleActionAgent,
    LLMSingleActionAgent,
    Tool,
)
from langchain.callbacks.manager import CallbackManager
from langchain.prompts import StringPromptTemplate
from langchain.schema import AgentAction, AgentFinish

# following
# https://python.langchain.com/en/latest/modules/agents/agents/custom_llm_agent.html

# Prompt template
template = """Answer the following questions as best you can, but speaking as a pirate might speak. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin! Remember to speak as a pirate when giving your final answer. Use lots of "Arg"s

Question: {input}
{agent_scratchpad}"""


# Set up a prompt template
class CustomPromptTemplate(StringPromptTemplate):
    # The template to use
    template: str
    # The list of tools available
    tools: List[Tool]

    def format(self, **kwargs) -> str:
        # Get the intermediate steps (AgentAction, Observation tuples)
        # Format them in a particular way
        intermediate_steps = kwargs.pop("intermediate_steps")
        thoughts = ""
        for action, observation in intermediate_steps:
            thoughts += action.log
            thoughts += f"\nObservation: {observation}\nThought: "
        # Set the agent_scratchpad variable to that value
        kwargs["agent_scratchpad"] = thoughts
        # Create a tools variable from the list of tools provided
        kwargs["tools"] = "\n".join(
            [f"{tool.name}: {tool.description}" for tool in self.tools]
        )
        # Create a list of tool names for the tools provided
        kwargs["tool_names"] = ", ".join([tool.name for tool in self.tools])
        return self.template.format(**kwargs)


def main():
    from homegpt.llm import get_llm_chat

    reverse_tool = Tool(
        name="Reverse",
        description="Reverses a string.",
        func=lambda s: s[::-1],
    )
    tools = [reverse_tool]

    agent = FakeAgent()
    agent_executor = AgentExecutor.from_agent_and_tools(
        agent=agent,
        tools=[reverse_tool],
        verbose=True,
    )

    agent_executor.run("Reverse the string 'hey'")


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    main()
