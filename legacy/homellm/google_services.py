from pathlib import Path
from typing import Optional, Tuple
import pickle
import os
from email.mime.text import MIMEText
from base64 import urlsafe_b64encode

from googleapiclient.discovery import Resource
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

_email = os.environ.get("GPT_EMAIL")

_project_dir = Path(__file__).parent.parent.resolve()

# Set the path to your downloaded JSON file
_client_credentials_file = _project_dir / "secret" / "credentials.json"
_user_credentials_file = _project_dir / "secret" / "token.pickle"

# Set the required scopes for the Calendar and Gmail APIs
_scopes = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/gmail.modify",
]


def initialize_services(
    credentials_file: Optional[str] = None,
    scopes: Optional[list] = None,
) -> Tuple[Resource, Resource]:
    credentials_file = credentials_file or _client_credentials_file
    scopes = scopes or _scopes

    creds: Optional[Credentials] = None

    # Check if the token.pickle file exists, and load the credentials from it.
    if os.path.exists(_user_credentials_file):
        with open(_user_credentials_file, "rb") as token:
            creds = pickle.load(token)

    # If there are no valid credentials available, run the OAuth2 flow.
    if not creds or not creds.valid:
        auth_failed = False
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except Exception:
                auth_failed = True

        if auth_failed:
            try:
                flow = InstalledAppFlow.from_client_secrets_file(
                    credentials_file, scopes
                )
                creds = flow.run_local_server(port=0)

                # Save the credentials for the next run
                with open(_user_credentials_file, "wb") as token:
                    pickle.dump(creds, token)

            except Exception as e:
                print(e)

    # Create the service objects
    calendar_service = build("calendar", "v3", credentials=creds)
    gmail_service = build("gmail", "v1", credentials=creds)

    return calendar_service, gmail_service


# TODO(j.swannack): inject "from" email address somehow, or couple it to the
# email address used to authenticate the API. For now, just use an env var.
# This is so multiple email addresses can be used.
def send_email(
    body: str,
    subject: str,
    recipient: str,
    gmail_service: str,
):
    message = MIMEText(body)
    message["to"] = recipient
    message["from"] = _email
    message["subject"] = subject

    message = {"raw": urlsafe_b64encode(message.as_bytes()).decode()}

    gmail_service.users().messages().send(userId="me", body=message).execute()


def main():
    calendar_service, gmail_service = initialize_services(
        _client_credentials_file, _scopes
    )

    # Use the services to interact with the Calendar and Gmail APIs
    # For example, list calendars
    calendar_list = calendar_service.calendarList().list().execute()
    for calendar in calendar_list["items"]:
        print(calendar["summary"])

    # For example, list the labels in Gmail
    labels = gmail_service.users().labels().list(userId="me").execute()
    for label in labels["labels"]:
        print(label["name"])

    # send an email to jeromeswannack@gmail.com
    subject = "hello world"
    body = "This is a test email"

    # Just using env vars for now
    destination = os.environ["RECIPIENT_EMAIL"]

    message = MIMEText(body)
    message["to"] = destination
    message["from"] = _email
    message["subject"] = subject

    message = {"raw": urlsafe_b64encode(message.as_bytes()).decode()}

    gmail_service.users().messages().send(userId="me", body=message).execute()
    print("Message sent successfully")


if __name__ == "__main__":
    main()
