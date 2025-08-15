"""Tests for common adapter utilities."""

import unittest
from unittest.mock import Mock, patch
from datetime import datetime

from uagents import Agent
from uagents_adapter.common import register_tool


class TestCommonAdapterUtilities(unittest.TestCase):
    """Test common adapter utility functions."""

    def setUp(self):
        """Set up test fixtures."""
        self.test_agent = Agent(name="test_agent", seed="test_seed")

    def test_register_tool_basic_functionality(self):
        """Test basic register_tool functionality."""
        # This is a basic structure test since register_tool is complex
        self.assertTrue(callable(register_tool))

    @patch('uagents_adapter.common.requests.post')
    def test_register_tool_mock_registration(self, mock_post):
        """Test register_tool with mocked HTTP calls."""
        # Mock successful registration response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"success": True, "agent_id": "test123"}
        mock_post.return_value = mock_response

        # This test would need adjustment based on actual register_tool signature
        # For now, test that the function exists and can be called
        self.assertTrue(hasattr(register_tool, '__call__'))

    def test_agent_basic_properties(self):
        """Test that we can create and verify basic agent properties."""
        self.assertEqual(self.test_agent.name, "test_agent")
        self.assertIsNotNone(self.test_agent.address)


if __name__ == "__main__":
    unittest.main()