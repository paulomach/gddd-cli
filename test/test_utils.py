"""Test utils."""
import unittest

import utils


class TestUtils(unittest.TestCase):
    """Test utils."""

    def test_build_request_headers(self):
        """Test build header."""
        self.assertEqual(utils.build_request_headers("TEST"), {
            "User-Agent": "TEST",
        })

    def test_build_request_url(self):
        """Test build url."""
        self.assertEqual(utils.build_request_url(
            "google",
            "example.com",
            "user",
            "password",
            "1.2.3.4"), "https://user:password@google?hostname=example.com&myip=1.2.3.4")


if __name__ == "__main__":
    unittest.main()
