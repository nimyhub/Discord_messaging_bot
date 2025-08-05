# Discord Messaging Bot

A configurable Discord bot that sends messages and pings a specified user both via DM and in a public channel. It supports command cooldowns and external configuration via JSON files.

---

## Features

- Sends messages to a specified user via DM and public channel.
- Fully configurable via `config.json` and `messages.json`.
- Supports command cooldowns to prevent spamming.
- Easily extendable for custom messages and behaviors.

---
## Usage Example

![Bot Demo](https://github.com/nimyhub/Discord_messaging_bot/blob/2a6eced2fae805d4bd9aa5fb727bbb74dda51974/Media/example.gif?raw=true)

In a Discord channel:

```
!summon GET IN HERE
```

- Sends a DM to the configured user: `"Get over here - from {author}"`
- Posts a sequence of ping messages in the configured channel.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/nimyhub/Discord_messaging_bot.git
cd Discord_messaging_bot
```

### 2. Create a Virtual Environment (optional but recommended)

```bash
python -m venv venv
```

On Windows:

```bash
venv\Scripts\activate
```

On Unix/Mac:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

The bot uses two configuration files:

- `config.json`: Contains bot token, user/channel IDs, command prefix, and cooldown settings.
- `messages.json`: Stores all DM and ping messages sent by the bot.

**Start by copying the example files:**

```bash
cp config.example.json config.json
cp messages.example.json messages.json
```

Then open `config.json` and replace the placeholder values:

```json
{
  "token": "YOUR_BOT_TOKEN_HERE",
  "user_id": 123456789012345678,
  "channel_id": 123456789012345678,
  "prefix": "!",
  "cooldown_seconds": 30
}
```

And open `messages.json` to customize the message templates for:

- `dm_messages`: Template messages sent via DM when the `!summon "message"` command is **used with a message**. `{author}` and `{message}` placeholders are replaced dynamically.
- `dm_no_messages`: Default fallback messages sent via DM when the `!summon` command is **used without a message**. These do not require dynamic substitution but can include `{author}`, can not include `{message}`.
- `server_ping_messages`: Sequences of messages sent publicly in the channel to get the user's attention.

These messages can include variables like `<@{user_id}>`, `{author}`, or `{message}` and will be formatted automatically.

To customize messages:
- Edit the message arrays in `messages.json`.
- Each message or message sequence is indexed and picked randomly at runtime.
- Make sure message formatting and placeholders match the expected format.

---

## Example Message Entry

```json
"dm_no_messages": [
  "GET YOUR ASS ON!",
  "Petter, the IKEA meatballs are under siege.",
  "An incoming missile is headed for your Magic collection. Text 'I'm here' to {author}."
]
```

```json
"server_ping_messages": {
  "1": [
    {"text": "<@{user_id}> WAKE", "delay": 1},
    {"text": "<@{user_id}> UP", "delay": 1},
    {"text": "<@{user_id}> NOW", "delay": 1}
  ]
}
```

---

## Tech Stack

- Python 3.x
- [discord.py](https://discordpy.readthedocs.io/en/stable/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- JSON for external message/config management

---

## Author

**Nikolai Myrstad**  
Information Engineering Student  
GitHub: [https://github.com/nimyhub](https://github.com/nimyhub)

---

## License

This project is licensed under the [MIT License](LICENSE).
