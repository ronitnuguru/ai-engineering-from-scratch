#!/usr/bin/env python3
"""
API Call Example - Using the Anthropic SDK

This is the recommended way to call APIs - using the official SDK.
It handles authentication, retries, and error handling for you.
"""

import os
from anthropic import Anthropic

def main():
    # Check if API key is set
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("❌ ANTHROPIC_API_KEY not found in environment variables")
        print("\nTo set it up:")
        print("1. Get your key from https://console.anthropic.com/")
        print("2. Run: export ANTHROPIC_API_KEY='sk-ant-...'")
        print("   OR create a .env file with: ANTHROPIC_API_KEY=sk-ant-...")
        return

    print("🔑 API key found, making request...\n")

    # Initialize the client
    client = Anthropic(api_key=api_key)

    # Make the API call
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=256,
        messages=[{
            "role": "user",
            "content": "What is a neural network in one sentence?"
        }]
    )

    # Print the response
    print("✅ Response received:\n")
    print(response.content[0].text)
    print(f"\nTokens used: {response.usage.input_tokens} in, {response.usage.output_tokens} out")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\nCommon issues:")
        print("- Invalid API key")
        print("- No credits remaining")
        print("- Network connection issues")
