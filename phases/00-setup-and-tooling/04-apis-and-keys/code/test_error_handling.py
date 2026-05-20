#!/usr/bin/env python3
"""
API Error Handling Examples

Tests common API errors so you know what they look like.
"""

from anthropic import Anthropic, APIError, AuthenticationError, RateLimitError

def test_invalid_key():
    """Test what happens with a wrong API key."""
    print("Test 1: Invalid API Key")
    print("-" * 50)

    try:
        client = Anthropic(api_key="sk-ant-invalid-key-123")
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=100,
            messages=[{"role": "user", "content": "Hello"}]
        )
    except AuthenticationError as e:
        print(f"✅ Caught AuthenticationError (expected)")
        print(f"   Message: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

    print()

def test_invalid_model():
    """Test what happens with a wrong model name."""
    import os

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Test 2: Skipped (no API key)\n")
        return

    print("Test 2: Invalid Model Name")
    print("-" * 50)

    try:
        client = Anthropic(api_key=api_key)
        response = client.messages.create(
            model="claude-nonexistent-model",
            max_tokens=100,
            messages=[{"role": "user", "content": "Hello"}]
        )
    except APIError as e:
        print(f"✅ Caught APIError (expected)")
        print(f"   Message: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

    print()

def test_valid_request():
    """Test a valid request if API key is available."""
    import os

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Test 3: Skipped (no API key)\n")
        return

    print("Test 3: Valid Request")
    print("-" * 50)

    try:
        client = Anthropic(api_key=api_key)
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=50,
            messages=[{"role": "user", "content": "Say 'API working!'"}]
        )
        print(f"✅ Success: {response.content[0].text}")
    except Exception as e:
        print(f"❌ Error: {e}")

    print()

if __name__ == "__main__":
    print("=== API Error Handling Tests ===\n")
    test_invalid_key()
    test_invalid_model()
    test_valid_request()
    print("=== Tests Complete ===")
