from jsongpt.client import JsonGptClient


def main():
    client = JsonGptClient()
    print(client.completion_standard("Hello, world!"))


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    main()
