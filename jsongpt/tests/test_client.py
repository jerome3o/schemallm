from jsongpt.client import JsonGptClient


def main():
    client = JsonGptClient()
    print(client.completion_standard("Hello, world!", max_tokens=10))


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    main()
