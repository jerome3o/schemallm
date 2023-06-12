from homegpt.google_services import initialize_services

# base64 import
import base64


def main():
    calendar_service, gmail_service = initialize_services()

    # get all calendar events from the last 30 days
    events = (
        calendar_service.events()
        .list(
            calendarId="primary",
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    print("Events:")
    for event in events["items"]:
        print(event["summary"])
        print(event["start"]["dateTime"])
        print(event["end"]["dateTime"])

    # get all sent messages in the last 30 days
    messages = (
        gmail_service.users()
        .messages()
        .list(
            userId="me",
            q="in:sent",
        )
        .execute()
    )
    print("Messages:")
    for message in messages["messages"]:
        # print title
        print(message["id"])
        # get info about the message
        message_info = (
            gmail_service.users()
            .messages()
            .get(userId="me", id=message["id"])
            .execute()
        )
        print(message_info["snippet"])
        for header in message_info["payload"]["headers"]:
            print(header["name"], header["value"])

        # b64 decode message_info["payload"]["body"]["data"]
        body = (
            base64.decodebytes(message_info["payload"]["body"]["data"].encode("utf-8"))
            .decode("utf-8")
            .strip()
        )
        print(body)


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    main()
