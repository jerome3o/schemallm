# Import things that are needed generically
import random
from langchain.agents import AgentType, initialize_agent
from langchain.tools import tool


@tool
def generate_random_numbers(n: int, lower: int, upper: int) -> list[int]:
    """Generates n random numbers given n, lower, and upper bounds."""
    return [random.randint(lower, upper) for _ in range(n)]


def main():
    from homegpt.llm import get_llm_chat

    tools = [generate_random_numbers]
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
