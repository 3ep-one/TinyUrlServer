import unittest
import mock
from UrlShortener import UrlShortener
from Redis import Redis
import re


class TestUrlShortner(unittest.TestCase):
    url_shortner = UrlShortener()

    def test_url_encoder_function(self):
        """
        Test url_encoder function behavior
        """
        encoded_url = self.url_shortner.url_encoder(10000000)
        self.assertEqual(encoded_url, 'oCba')

    @mock.patch.object(Redis, 'does_key_exist', return_value=True)
    @mock.patch.object(Redis, 'get_value_by_key', return_value=237)
    def test_shorten_url_key_exist(self, *_):
        """
        Test shorten_url when url already exist
        """
        url_key_id = self.url_shortner.shorten_url('test')
        regex_search = bool(re.search(r'.*/3f$', url_key_id))
        self.assertEqual(regex_search, True)

    @mock.patch.object(Redis, 'does_key_exist', return_value=False)
    @mock.patch.object(Redis, 'get_value_by_key')
    @mock.patch.object(Redis, 'add_key_value')
    @mock.patch.object(UrlShortener, 'url_encoder', return_value='aB3')
    def test_shorten_url_add_key(self, *_):
        """
        Test shorten_url when url doesn't exist
        """
        shotrened_url = self.url_shortner.shorten_url('test')
        regex_search = bool(re.search(r'.*/aB3$', shotrened_url))
        self.assertEqual(regex_search, True)


if __name__ == '__main__':
    unittest.main()
