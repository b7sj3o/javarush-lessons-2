import json
import logging

from openai import (
    APIConnectionError,
    APIStatusError,
    APITimeoutError,
    AsyncOpenAI,
    RateLimitError,
)

from config import settings


logger = logging.getLogger(__name__)

client = AsyncOpenAI(
    api_key=settings.OPENAI_API_KEY,
    timeout=settings.OPENAI_TIMEOUT
)



async def ask(system_prompt: str, user_message: str | None = None) -> list[str] | str | None:
    messages=[ {"role": "system", "content": system_prompt} ]

    if user_message:
        messages.append( {"role": "user", "content": user_message} )

    return await complete(messages)


async def ask_history(system_prompt: str, history: list[dict[str,str]]):
    messages=[
        {
            "role": "system",
            "content": system_prompt
        },
        *history
    ]
    return await complete(messages)


async def complete(messages: list[dict[str,str]]) -> list[str] | str | None:
    try:
        response = await client.chat.completions.create(
            model=settings.OPENAI_MODEL,
            messages=messages,
            reasoning_effort=settings.OPENAI_REASONING,
            max_completion_tokens=settings.OPENAI_MAX_TOKENS
        )
    except RateLimitError as e:
        logger.error(
            "Забагато спроб", e
        )
        return None
    except APITimeoutError as e:
        logger.error(
            "Сервер OpenAI не відповідає.", e
        )
        return None
    except APIConnectionError as e:
        logger.error(
            "Не вийшло з'єднтаись з OpenAI.", e
        )
        return None
    except APIStatusError as e:
        logger.error(
            "Трапилась помилка", e
        )
        return None
    except Exception as e:
        logger.error(e)
        return None

    content = response.choices[0].message.content or ""

    if not content:
        logger.warning("ChatGPT повернув порожню відповідь")
        return None


    if len(content) > 4096:
        result = []

        while content:
            part = content[:4096]
            content = content[4096:]
            result.append(part)

        return result

    return content

