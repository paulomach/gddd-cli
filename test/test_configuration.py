"""Test configuration."""
import os
import unittest

import configuration


class TestConfiguration(unittest.TestCase):
    """Test configuration."""

    def test_configuration(self):
        """Test configuration."""
        self.assertEqual(configuration.DOMAIN, "home.paulmach.dev")
