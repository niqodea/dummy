import unittest

from niqodea.dummy.client import Client


class TestClient(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://dummy.local"
        self.url_getter = lambda url: {"url": url}
        self.client = Client(self.base_url, self.url_getter)

    def test_get_data(self):
        data = self.client.get_data("get")
        self.assertEqual(data["url"], "http://dummy.local/get")


if __name__ == "__main__":
    unittest.main()
