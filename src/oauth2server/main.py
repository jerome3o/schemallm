from pathlib import Path

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


_script_dir = Path(__file__).parent.resolve()

# Set the path to your downloaded JSON file
credentials_file = _script_dir / "secret" / "credentials.json"

# Set the required scopes for the Calendar and Gmail APIs
scopes = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/gmail.modify",
]


def initialize_services(credentials_file, scopes):
    creds = None
    try:
        flow = InstalledAppFlow.from_client_secrets_file(credentials_file, scopes)
        creds = flow.run_local_server(port=0)
    except Exception as e:
        print(e)

    # Create the service objects
    calendar_service = build("calendar", "v3", credentials=creds)
    gmail_service = build("gmail", "v1", credentials=creds)

    return calendar_service, gmail_service


def main():
    try:
        calendar_service, gmail_service = initialize_services(credentials_file, scopes)

        # Use the services to interact with the Calendar and Gmail APIs
        # For example, list calendars
        calendar_list = calendar_service.calendarList().list().execute()
        for calendar in calendar_list["items"]:
            print(calendar["summary"])

        # For example, list the labels in Gmail
        labels = gmail_service.users().labels().list(userId="me").execute()
        for label in labels["labels"]:
            print(label["name"])

    except HttpError as error:
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    main()
