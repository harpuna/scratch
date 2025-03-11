import requests


def get_post(post_id: str):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.get(url)

    if response.status_code >= 400:
        print(f"Request failed with status code {response.status_code}")
        return {}

    return response.json()


def get_post_comments(post_id: str):
    url = f"https://jsonplaceholder.typicode.com/comments?postId={post_id}"
    response = requests.get(url)

    if response.status_code >= 400:
        print(f"Request failed with status code {response.status_code}")
        return []

    return response.json()


def get_random_dog_href():
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    return response.json()["message"]


def get_word_of_the_day() -> str:
    url = "https://random-word-api.herokuapp.com/word"
    response = requests.get(url)
    return response.json()[0]


def get_open_credit_lines():
    url = "https://www.randomnumberapi.com/api/v1.0/random"
    response = requests.get(url)
    return response.json()[0]


def calculate_term_and_rate(amount_in_cents, open_credit_lines):
    """
    - Business rules
      - principal amount
        - amt < 10k or > 50k -> DENY
      - open credit lines
        - if open lines > 50 --> DENY
        - if open lines < 10 -> Offer 36mo @ 10%
        - if open lines <= 50 and >= 10 --> Offer 24mo @ 20%
    """

    if amount_in_cents < 1000000 or amount_in_cents > 5000000:
        return None, None

    if open_credit_lines < 10:
        return 36, 10
    if open_credit_lines >= 10 and open_credit_lines <= 50:
        return 24, 20
    return None, None
