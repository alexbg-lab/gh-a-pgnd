import requests, os


def set_output(file_path, key, value):
    with open(file_path, "a") as f:
        print(f"{key}={value}", file=f)


def main():
    website_url: str | None = os.getenv("INPUT_URL")
    website_reachable = requests.get(website_url).status_code
    print("Website Status Code:", website_reachable)

    set_output(os.getenv("GITHUB_OUTPUT"), "url-reachable", website_reachable)
    if not website_url:
        raise Exception(f"Website URL: {website_url} is malformed/unreachable")


if __name__ == "__main__":
    main()
