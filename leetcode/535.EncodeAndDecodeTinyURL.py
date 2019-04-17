# coding: utf-8

'''
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
'''


class Codec:
    # 无状态，进来什么出来什么
    # def encode(self, longUrl):
    #     """Encodes a URL to a shortened URL.
    #
    #     :type longUrl: str
    #     :rtype: str
    #     """
    #
    #     return longUrl
    #
    # def decode(self, shortUrl):
    #     """Decodes a shortened URL to its original URL.
    #
    #     :type shortUrl: str
    #     :rtype: str
    #     """
    #
    #     return shortUrl

    # 使用hashtable存储
    def __init__(self):
        self.dict = {}
        self.count = 0
        self.urlPrefix = 'http://tinyurl.com/'

    def encode(self, longUrl):
        self.count += 1
        self.dict[self.count] = longUrl

        return '%s%s' % (self.urlPrefix, self.count)

    def decode(self, shortUrl):
        return self.dict[int(shortUrl.replace(self.urlPrefix, ''))]


if __name__ == '__main__':
    # Your Codec object will be instantiated and called as such:
    url = 'https://leetcode.com/problems/design-tinyurl'
    codec = Codec()
    assert url == codec.decode(codec.encode(url))
