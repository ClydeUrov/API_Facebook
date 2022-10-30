import os
import requests
import facebook
from dotenv import load_dotenv
import time
import random
import logging


def main():
    load_dotenv()

    group=os.environ["GROUP_ID"]
    graph=facebook.GraphAPI(access_token=os.environ["FACEBOOK_TOKEN"])

    used = []
    pages = 2691
    while len(used) != pages:
        try:
            number = random.randint(0,pages)
            if number not in used:
                used.append(number)
                response = requests.get(
                    f"https://xkcd.com/{number}/info.0.json"
                )
                response.raise_for_status()
                message = response.json()['alt']
                image = response.json()['img']
                graph.put_object(group, 'feed', message=message, link=image)
                time.sleep(86400)
        except requests.ConnectionError:
            time.sleep(30)
        except Exception as err:
            logging.warning("Бот упал с ошибкой:")
            logging.warning(err, exc_info=True)

if __name__ == '__main__':
    main()
