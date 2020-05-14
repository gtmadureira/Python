from typing import Generator
import requests


def gen_from_urls(urls: tuple) -> Generator:
    """Url's request generator.

    Arguments:
        urls {tuple} -- tuple of urls

    Yields:
        Iterator[tuple] -- return a tuple with responses from each request
    """

    for resp in (requests.get(url) for url in urls):
        yield len(resp.content), resp.status_code, resp.url
