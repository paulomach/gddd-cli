"""Test configuration."""
import os
import unittest


class TestConfiguration(unittest.TestCase):
    """Test configuration."""

    def setUp(self):
        """Set up."""
        os.environ['DOMAIN'] = "example.com"

    def test_configuration(self):
        """Test configuration."""
        import configuration
        self.assertEqual(configuration.DOMAIN, "example.com")
