"""Terminal chat with the study-room desk assistant. You write this file.

Run it with:  uv run --env-file lmstudio.env python chat.py

Exercise 1: `agent` (a Pydantic AI agent) and `main()`, the chat loop.
Exercise 2: memory and the /new command.
Exercise 3: the X-Session-ID header.
"""
import os
from uuid import uuid4

from pydantic_ai import Agent
from pydantic_ai.exceptions import AgentRunError
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.openai import OpenAIProvider


model = OpenAIChatModel(
    os.environ["LLM_MODEL"],
    provider=OpenAIProvider(
        base_url=os.environ["LLM_BASE_URL"],
        api_key=os.environ["LLM_API_KEY"],
    ),
)

agent = Agent(
    model,
    instructions=(
        "You are the assistant at the library's study-room desk. "
        "Help with questions about studying and study rooms. "
        "Answer in at most three sentences. "
        "Do not invent room availability, bookings, or library rules."
    ),
)


def main():
    print("Study-room desk. Type /new for a new conversation and /quit to leave.")
    history = []
    session_id = uuid4().hex

    while True:
        try:
            text = input("you> ").strip()
        except (EOFError, KeyboardInterrupt):
            break

        if not text:
            continue
        if text == "/quit":
            break
        if text == "/new":
            history = []
            session_id = uuid4().hex
            print("New conversation.")
            continue

        try:
            result = agent.run_sync(
                text,
                message_history=history,
                model_settings={"extra_headers": {"X-Session-ID": session_id}},
            )
        except AgentRunError as error:
            print(f"desk> no usable answer: {error}")
            continue

        history = result.all_messages()
        print(f"desk> {result.output}")


if __name__ == "__main__":
    main()
