from typing import List, Tuple, Any, Union
from langchain.schema import AgentAction, AgentFinish
from langchain.agents import Tool, AgentExecutor, BaseSingleActionAgent


class FakeAgent(BaseSingleActionAgent):
    """Fake Custom Agent."""

    @property
    def input_keys(self):
        return ["input"]

    def plan(
        self, intermediate_steps: List[Tuple[AgentAction, str]], **kwargs: Any
    ) -> Union[AgentAction, AgentFinish]:
        """Given input, decided what to do.

        Args:
            intermediate_steps: Steps the LLM has taken to date,
                along with observations
            **kwargs: User inputs.

        Returns:
            Action specifying what tool to use.
        """
        return AgentAction(tool="Reverse", tool_input=kwargs["input"], log="")

    async def aplan(
        self, intermediate_steps: List[Tuple[AgentAction, str]], **kwargs: Any
    ) -> Union[AgentAction, AgentFinish]:
        """Given input, decided what to do.

        Args:
            intermediate_steps: Steps the LLM has taken to date,
                along with observations
            **kwargs: User inputs.

        Returns:
            Action specifying what tool to use.
        """
        return AgentAction(tool="Search", tool_input=kwargs["input"], log="")


def main():
    from homegpt.llm import get_llm_chat

    reverse_tool = Tool(
        name="Reverse",
        description="Reverses a string.",
        func=lambda s: s[::-1],
    )
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
