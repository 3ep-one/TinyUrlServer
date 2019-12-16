from Redis import Redis


class UrlShortener:
    def __init__(self):
        self.redis = Redis()
        if not self.redis.does_key_exist('id'):
            self.redis.add_key_value('id', '1')

    def shorten_url(self, original_url):
        if (self.redis.does_key_exist(original_url)):
            url_id = int(self.redis.get_value_by_key(original_url))
            shorten_url = self.url_encoder(url_id)
        else:
            url_id = int(self.redis.get_value_by_key('id'))
            self.redis.add_key_value(original_url, url_id)
            shorten_url = self.url_encoder(url_id)
            self.redis.get_value_by_key(id)
            url_id += 1
            self.redis.add_key_value('id', str(url_id))
        return "short_url.com/"+shorten_url

    def url_encoder(self, id):
        characters = "0123456789abcdefghijklmnopqrstuvwxyz\
            ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        base = len(characters)
        encoden_url = []
        while id > 0:
            val = id % base
            encoden_url.append(characters[val])
            id = (id // base)
        return "".join(encoden_url[::-1])
