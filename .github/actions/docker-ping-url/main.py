if __name__ == "__main__":
    import requests, os

    url: str | None = os.getenv("INPUT_URL")
    r = requests.get(url)
    print("Status Code:", r.status_code)
