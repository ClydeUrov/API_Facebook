import logging
import os
import random

import facebook
import requests
from dotenv import load_dotenv


def upload_to_facebook(message, image):
    graph = facebook.GraphAPI(access_token=os.environ["FACEBOOK_TOKEN"])
    graph.put_object(
            os.environ["GROUP_ID"], "feed", message=message, link=image
        )


def main():
    load_dotenv()
    try:
        response = requests.get('https://xkcd.com/info.0.json')
        response.raise_for_status()
        total_comics = response.json()["num"]

        comic_number = random.randrange(total_comics)
        response = requests.get(
            f"https://xkcd.com/{comic_number}/info.0.json"
        )
        response.raise_for_status()
        comic = response.json()

        upload_to_facebook(comic["alt"], comic["img"])

    except Exception:
        logging.exception(msg='Бот упал с ошибкой:')


if __name__ == "__main__":
    main()
