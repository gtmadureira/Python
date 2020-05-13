# pyright: reportMissingImports=false

from url_utils import gen_from_urls

urls = ('http://www.globo.com', 'http://www.uol.com.br',
        'http://www.r7.com', 'http://www.nasa.gov',
        'http://www.terra.com.br', 'http://www.ig.com.br',
        'http://www.usatoday.com', 'http://www.cnn.com',
        'http://www.dell.com')

for rest_len, status, url in gen_from_urls(urls):
    print(rest_len, '->', status, '->', url)
