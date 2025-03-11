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
