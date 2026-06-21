"""Compare responses from several FreeLLMShare-compatible models.

Usage:
    pip install openai
    export OPENAI_API_KEY="your-free-llmshare-key"
    python multi_model.py
"""
import os

from openai import OpenAI

api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise SystemExit("Set OPENAI_API_KEY before running this example.")

client = OpenAI(base_url="https://aiapiv2.pekpik.com/v1", api_key=api_key)
models = ["gpt-5.5", "claude-sonnet-4-6", "deepseek-chat", "mistral-medium-latest"]
question = "Explain quantum computing in one paragraph."

for model in models:
    print(f"\n{'='*50}\n{model}\n{'='*50}")
    try:
        r = client.chat.completions.create(model=model, messages=[{"role": "user", "content": question}])
        print(r.choices[0].message.content)
    except Exception as e:
        print(f"Error: {e}")
