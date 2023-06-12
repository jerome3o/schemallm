from typing import Optional, Type

from langchain.agents import AgentType, initialize_agent
from langchain.tools import BaseTool
from langchain.callbacks.manager import (
    CallbackManagerForToolRun,
    AsyncCallbackManagerForToolRun,
)
from pydantic import BaseModel, EmailStr
from googleapiclient.discovery import Resource

from homegpt.google_services import initialize_services, send_email


# You can provide a custom args schema to add descriptions or custom validation


class SendEmailSchema(BaseModel):
    subject: str
    body: str
    recipient: EmailStr


class SendEmailTool(BaseTool):
    name = "send_email"
    description = (
        "Useful for sending emails, a subject, body, and recipient are required."
    )
    args_schema: Type[SendEmailSchema] = SendEmailSchema
    gmail_service: Resource

    def _run(
        self,
        subject: str,
        body: str,
        recipient: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool."""
        send_email(
            body=body,
            subject=subject,
            recipient=recipient,
            gmail_service=self.gmail_service,
        )

    async def _arun(
        self,
        subject: str,
        body: str,
        recipient: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("custom_search does not support async")


def main():
    # Imports just for testing
    from homegpt.llm import get_llm_chat
    import os

    _, gmail_service = initialize_services()

    tools = [SendEmailTool(gmail_service=gmail_service)]
    llm = get_llm_chat()
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        max_iterations=4,
    )

    _recipient = os.environ.get("RECIPIENT_EMAIL")
    agent.run(
        f"Send an email to {_recipient} with subject 'hello'"
        " and the body is a poem about frogs"
    )


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    main()
