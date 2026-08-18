import os

from dotenv import load_dotenv

load_dotenv()


def main() -> None:
    print("Hello from langchain-course!")
    print("OPENAI_API_Key:", os.getenv("OPENAI_API_Key"))


if __name__ == "__main__":
    main()
