import redis


class Redis:
    def __init__(self):
        self.redis_db = self.connect_to_redis()

    def connect_to_redis(self):
        return redis.Redis(
                            host='127.0.0.1',
                            port=6379,
                            password=None)

    def add_key_value(self, key, value):
        self.redis_db.set(key, value)

    def get_value_by_key(self, key):
        return self.redis_db.get(key)

    def does_key_exist(self, key):
        print(key)
        if(self.redis_db.exists(key)):
            return True
        return False

    def remove_key(self, key):
        self.redis_db.delete(key)
