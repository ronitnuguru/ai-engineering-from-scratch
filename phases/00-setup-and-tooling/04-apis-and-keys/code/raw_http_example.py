#!/usr/bin/env python3
"""
API Call Example - Raw HTTP (No SDK)

This shows what happens under the hood when you use an SDK.
Useful for debugging and understanding the API structure.
"""

import os
import urllib.request
import json

def main():
    # Check if API key is set
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("❌ ANTHROPIC_API_KEY not found in environment variables")
        print("\nTo set it up:")
        print("1. Get your key from https://console.anthropic.com/")
        print("2. Run: export ANTHROPIC_API_KEY='sk-ant-...'")
        return

    print("🔑 API key found, making raw HTTP request...\n")

    # API endpoint
    url = "https://api.anthropic.com/v1/messages"

    # Request headers
    headers = {
        "Content-Type": "application/json",
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
    }

    # Request body
    body = json.dumps({
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 256,
        "messages": [{
            "role": "user",
            "content": "What is a neural network in one sentence?"
        }],
    }).encode()

    print("📤 Sending request:")
    print(f"  URL: {url}")
    print(f"  Headers: {list(headers.keys())}")
    print(f"  Body: {json.loads(body)}\n")

    # Make the request
    req = urllib.request.Request(url, data=body, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(req) as resp:
            result = json.loads(resp.read())

            print("✅ Response received:\n")
            print(result["content"][0]["text"])
            print(f"\nTokens used: {result['usage']['input_tokens']} in, {result['usage']['output_tokens']} out")

            print("\n📥 Full response structure:")
            print(json.dumps(result, indent=2))

    except urllib.error.HTTPError as e:
        print(f"❌ HTTP Error {e.code}: {e.reason}")
        error_body = json.loads(e.read())
        print(f"Error details: {error_body}")

if __name__ == "__main__":
    main()
