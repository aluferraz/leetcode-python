import collections
import random
import string
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Codec:

    def __init__(self):
        self.urls = []
        self.url_map = collections.defaultdict(str)
        self.pos = 0

    def generate_url(self):

        exists = True
        url_str = ''
        while exists:
            url = []
            for i in range(8):
                letter = chr(random.randrange(26) + ord('a'))
                digit = str(random.randrange(10))
                if i % 2 == 0:
                    url.append(letter)
                else:
                    url.append(digit)
            url_str = 'https://a.com/' + ''.join(url)
            exists = self.url_map[url_str] != ""
        return url_str

    def get_url(self):
        if self.pos == len(self.urls):
            for _ in range(10):
                self.urls.append(self.generate_url())
        url = self.urls[self.pos]
        self.pos += 1
        return url

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        url = self.get_url()
        self.url_map[url] = longUrl
        return url

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.url_map[shortUrl]

        # Your Codec object will be instantiated and called as such:


# codec = Codec()
# codec.decode(codec.encode(url))
# leetcode submit region end(Prohibit modification and deletion)


class EncodeAndDecodeTinyurl(Codec):
    pass
