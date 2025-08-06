import random
import asyncio
from bot.config import messages

async def send_message(category: str, receiver, context_vars: dict):
    versions = messages.get(category, {})
    if not versions:
        print(f"No templates found for category: {category}")
        return

    if isinstance(versions, dict):
        version_key = str(random.randint(1, len(versions)))
        sequence = versions.get(version_key, [])
        for step in sequence:
            text = step["text"].format(**context_vars)
            await receiver.send(text)
            await asyncio.sleep(step.get("delay", 0))
    elif isinstance(versions, list):
        chosen_text = random.choice(versions).format(**context_vars)
        await receiver.send(chosen_text)
    else:
        print(f"Unexpected template format for category: {category}")

async def get_sms_message(category: str, context_vars: dict) -> str:
    versions = messages.get(category, {})
    if not versions:
        print(f"No templates found for category: {category}")
        return None

    return random.choice(versions).format(**context_vars)