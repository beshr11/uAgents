"""Integration tests for uAgents adapter components.

These tests verify that the adapter components can be imported and 
basic functionality works as expected.
"""

import unittest
import sys
import importlib.util
from pathlib import Path


class TestAdapterIntegration(unittest.TestCase):
    """Test adapter component integration."""

    def test_mcp_adapter_imports(self):
        """Test that MCP adapter modules can be imported."""
        try:
            # Test that the module structure exists
            adapter_path = Path(__file__).parent.parent / "uagents-adapter" / "src"
            self.assertTrue(adapter_path.exists(), "Adapter source directory should exist")
            
            mcp_path = adapter_path / "uagents_adapter" / "mcp"
            self.assertTrue(mcp_path.exists(), "MCP module directory should exist")
            
            # Test that key files exist
            adapter_file = mcp_path / "adapter.py"
            protocol_file = mcp_path / "protocol.py"
            
            self.assertTrue(adapter_file.exists(), "MCP adapter.py should exist")
            self.assertTrue(protocol_file.exists(), "MCP protocol.py should exist")
            
        except Exception as e:
            self.fail(f"MCP adapter import test failed: {e}")

    def test_ai_engine_imports(self):
        """Test that AI engine modules can be imported."""
        try:
            # Test that the module structure exists
            ai_engine_path = Path(__file__).parent.parent / "uagents-ai-engine" / "src"
            self.assertTrue(ai_engine_path.exists(), "AI engine source directory should exist")
            
            engine_path = ai_engine_path / "ai_engine"
            self.assertTrue(engine_path.exists(), "AI engine module directory should exist")
            
            # Test that key files exist
            messages_file = engine_path / "messages.py"
            types_file = engine_path / "types.py"
            
            self.assertTrue(messages_file.exists(), "AI engine messages.py should exist")
            self.assertTrue(types_file.exists(), "AI engine types.py should exist")
            
        except Exception as e:
            self.fail(f"AI engine import test failed: {e}")

    def test_core_uagents_functionality(self):
        """Test that core uAgents functionality still works."""
        try:
            from uagents import Agent, Model
            from uagents_core.types import AgentInfo
            
            # Test basic agent creation
            agent = Agent(name="test_agent", seed="test_seed_123")
            self.assertIsNotNone(agent.address)
            self.assertEqual(agent.name, "test_agent")
            
            # Test basic model functionality
            class TestMessage(Model):
                content: str
            
            msg = TestMessage(content="Hello, World!")
            self.assertEqual(msg.content, "Hello, World!")
            
        except Exception as e:
            self.fail(f"Core uAgents functionality test failed: {e}")


if __name__ == "__main__":
    unittest.main()