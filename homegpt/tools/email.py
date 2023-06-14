from typing import Optional, Type

from langchain.tools import BaseTool
from langchain.llms.base import BaseLLM
from langchain.callbacks.manager import (
    CallbackManagerForToolRun,
    AsyncCallbackManagerForToolRun,
)
from pydantic import BaseModel, EmailStr
from googleapiclient.discovery import Resource

from homegpt.google_services import send_email


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
    llm: BaseLLM

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
