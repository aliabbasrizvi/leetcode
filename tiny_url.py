import hashlib
import random

class Codec:

  def __init__(self):
    self.url_map = {}

  def get_random_string(self, long_url):
    random_str = hashlib.md5(long_url + str(random.random())).hexdigest()
    return random_str[:6]

  def encode(self, longUrl):
    """Encodes a URL to a shortened URL.

    :type longUrl: str
    :rtype: str
    """
    random_str = self.get_random_string(longUrl)
    while self.url_map.get(random_str) is not None:
      random_str = self.get_random_string(longUrl)

    self.url_map[random_str] = longUrl
    return random_str

  def decode(self, shortUrl):
    """Decodes a shortened URL to its original URL.

    :type shortUrl: str
    :rtype: str
    """
    return self.url_map.get(shortUrl)
