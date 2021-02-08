from url_utils import gen_from_urls
from pprint import pprint

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
