import pytest

from schemallm.server.server import complete_with_cfg
from schemallm.tests.fixtures import model, tokenizer

from schemallm.models.api import CfgCompletionRequest


def test_cfg_completion_with_agent_prompt(model, tokenizer):
    prompt = """
Answer the following questions as best you can. You have access to the following tools:

send_email: Useful for sending emails, a subject, body, and recipient are required.

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [send_email]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: Send an email to jeromeswannack@gmail.com about frogs.

"""

    cfg = r"""
    start: (thought_action | final_thought_answer)

    ?thought_action: THOUGHT ": " TEXT NL ACTION ": " TEXT NL
    ?final_thought_answer: THOUGHT ": " TEXT NL FINALANSWER ": " TEXT NL

    TEXT: /[^:\r\n\u200b]+/
    TOOL: "send_email"
    NL: /\n/

    THOUGHT: "Thought"
    ACTION: "Action"
    FINALANSWER: "Final Answer"
    """
    result = complete_with_cfg(
        model=model,
        tokenizer=tokenizer,
        completion_request=CfgCompletionRequest(
            prompt=prompt,
            cfg=cfg,
            max_tokens=300,
        ),
    )
    print(result)
