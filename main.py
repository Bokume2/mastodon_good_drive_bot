from .fuctions.streamings import login, listen

def main():
    client = login()
    listen(client)


if __name__ == "__main__":
    main()
