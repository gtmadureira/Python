from typing import Generator
from pprint import pprint
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


if __name__ == '__main__':

    # Test:

    urls = ('http://www.globo.com', 'http://www.uol.com.br',
            'http://www.r7.com', 'http://www.nasa.gov',
            'http://www.terra.com.br', 'http://www.ig.com.br',
            'http://www.usatoday.com', 'http://www.cnn.com',
            'http://www.dell.com')

    print()
    for resp_len, status, url in gen_from_urls(urls):
        print(resp_len, '->', status, '->', url)
    print()

    print()
    urls_res = {url: size for size, _, url in gen_from_urls(urls)}
    pprint(urls_res)
    print()
