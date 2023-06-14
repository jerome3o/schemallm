from typing import Optional

from langchain.tools import BaseTool
from langchain.llms.base import BaseLLM
from langchain.callbacks.manager import (
    CallbackManagerForToolRun,
    AsyncCallbackManagerForToolRun,
)
from pydantic import BaseModel, EmailStr
from googleapiclient.discovery import Resource

from homegpt.google_services import send_email


class SendEmailParameters(BaseModel):
    subject: str
    body: str
    recipient: EmailStr


def get_email_parameters(input: str, llm: BaseLLM) -> SendEmailParameters:
    return SendEmailParameters(
        subject="This is the subject of the email",
        body="This is the body of the email",
        recipient="",
    )


class SendEmailTool(BaseTool):
    name = "send_email"
    description = (
        "Useful for sending emails, a subject, body, and recipient are required."
    )
    gmail_service: Resource
    llm: BaseLLM

    def _run(
        self,
        input: str,
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
