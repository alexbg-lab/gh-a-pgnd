if __name__ == "__main__":
    import requests, os

    url: str | None = os.getenv("INPUT_URL")

    print("Status Code:", requests.get(url).status_code)
