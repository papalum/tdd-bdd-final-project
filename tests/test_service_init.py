"""
Tests for service initialization
"""

import unittest
import importlib
from unittest.mock import patch

import service


class TestServiceInit(unittest.TestCase):
    """Unit tests for service app initialization"""

    def test_init_db_failure(self):
        """Test that service exits with code 4 when DB initialization fails"""
        with patch("service.models.init_db", side_effect=Exception("fail")):
            with self.assertRaises(SystemExit) as context:
                importlib.reload(service)
            self.assertEqual(context.exception.code, 4)
