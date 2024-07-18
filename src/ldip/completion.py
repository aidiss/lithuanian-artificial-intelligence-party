import litellm

OLLAMA_API_BASE = "http://localhost:11434"
OLLAMA_LLAMA3 = "ollama/llama3"
OLLAMA_CHAT_LLAMA3 = "ollama_chat/llama2"

GPT35_TURBO = "openai/gpt-3.5-turbo"
GPT4o_TURBO = "openai/gpt-4o"

CLAUDE35 = "anthropic/claude-3-5-sonnet-20240620"

MODEL = CLAUDE35


def complete(message, model=MODEL) -> str:
    messages = [{"role": "user", "content": message}]
    completion_response = litellm.completion(model, messages)
    content = completion_response.choices[0].message.content  # type: ignore
    return content
