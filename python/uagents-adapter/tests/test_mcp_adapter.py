"""Tests for MCP adapter functionality."""

import json
import unittest
from unittest.mock import Mock, patch, MagicMock
from uuid import uuid4

from uagents import Agent, Context
from uagents_adapter.mcp.adapter import MCPServerAdapter, serialize_messages, deserialize_messages
from uagents_adapter.mcp.protocol import CallTool, CallToolResponse, ListTools, ListToolsResponse


class TestMCPUtilities(unittest.TestCase):
    """Test MCP utility functions."""

    def test_serialize_messages_empty(self):
        """Test serialization of empty message list."""
        result = serialize_messages([])
        self.assertEqual(result, "[]")

    def test_serialize_messages_with_data(self):
        """Test serialization of messages with data."""
        messages = [{"type": "text", "content": "Hello"}]
        result = serialize_messages(messages)
        self.assertEqual(result, json.dumps(messages))

    def test_deserialize_messages_empty_string(self):
        """Test deserialization of empty string."""
        result = deserialize_messages("")
        self.assertEqual(result, [])

    def test_deserialize_messages_valid_json(self):
        """Test deserialization of valid JSON."""
        messages = [{"type": "text", "content": "Hello"}]
        json_str = json.dumps(messages)
        result = deserialize_messages(json_str)
        self.assertEqual(result, messages)

    def test_deserialize_messages_invalid_json(self):
        """Test deserialization handles invalid JSON."""
        with self.assertRaises(json.JSONDecodeError):
            deserialize_messages("invalid json")


class TestMCPServerAdapter(unittest.TestCase):
    """Test MCP server adapter."""

    def setUp(self):
        """Set up test fixtures."""
        self.mock_mcp_server = Mock()
        self.api_key = "test-api-key"
        self.model = "test-model"
        self.adapter = MCPServerAdapter(
            mcp_server=self.mock_mcp_server,
            asi1_api_key=self.api_key,
            model=self.model
        )

    def test_adapter_initialization(self):
        """Test adapter initializes with correct parameters."""
        self.assertEqual(self.adapter._mcp_server, self.mock_mcp_server)
        self.assertEqual(self.adapter._api_key, self.api_key)
        self.assertEqual(self.adapter._model, self.model)

    def test_adapter_has_required_attributes(self):
        """Test adapter has all required attributes."""
        required_attrs = ["_mcp_server", "_api_key", "_model", "_base_url"]
        for attr in required_attrs:
            self.assertTrue(hasattr(self.adapter, attr), f"Missing attribute: {attr}")


class TestMCPProtocolMessages(unittest.TestCase):
    """Test MCP protocol message types."""

    def test_list_tools_message(self):
        """Test ListTools message creation."""
        msg = ListTools()
        self.assertIsInstance(msg, ListTools)

    def test_list_tools_response_creation(self):
        """Test ListToolsResponse message creation."""
        tools = [{"name": "test_tool", "description": "A test tool"}]
        response = ListToolsResponse(tools=tools)
        self.assertEqual(response.tools, tools)

    def test_call_tool_message(self):
        """Test CallTool message creation."""
        tool_name = "test_tool"
        arguments = {"arg1": "value1"}
        msg = CallTool(name=tool_name, arguments=arguments)
        self.assertEqual(msg.name, tool_name)
        self.assertEqual(msg.arguments, arguments)

    def test_call_tool_response_success(self):
        """Test successful CallToolResponse creation."""
        content = [{"type": "text", "text": "Success"}]
        response = CallToolResponse(content=content, isError=False)
        self.assertEqual(response.content, content)
        self.assertFalse(response.isError)

    def test_call_tool_response_error(self):
        """Test error CallToolResponse creation."""
        content = [{"type": "text", "text": "Error occurred"}]
        response = CallToolResponse(content=content, isError=True)
        self.assertEqual(response.content, content)
        self.assertTrue(response.isError)


if __name__ == "__main__":
    unittest.main()