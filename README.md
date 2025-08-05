# Discord Messaging Bot

A configurable Discord bot that sends messages and pings a specified user both via DM and in a channel. It supports command cooldowns and external configuration via `config.json`.

---

## Features

- Sends messages to a specified user via DM and public channel.
- Configurable via a single JSON file (`config.json`).
- Command cooldown to prevent spamming.
- Easily extendable for custom channel messages.

---

## Installation

# 1. Clone the Repository

```bash
    git clone https://github.com/nimyhub/Discord_messaging_bot.git
    cd Discord_messaging_bot
```

# 2. Create a Virtual Environment (optional but recommended)

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

# 3. Install Dependencies

```bash
pip install -U discord.py python-dotenv
```

## Configuration

Before running the bot, create a `config.json` file in the project directory. This file stores essential configuration details such as bot token, user ID, and channel settings.

Example `config.json` structure:

```json
{
  "token": "YOUR_BOT_TOKEN_HERE",
  "user_id": 123456789012345678,
  "channel_id": 123456789012345678,
  "prefix": "!",
  "cooldown_seconds": 30
}
```

- `token`: Your bot's authentication token (keep this secret).
- `user_id`: The Discord user ID of the person to DM/ping.
- `channel_id`: The ID of the default channel where the bot sends messages.
- `prefix`: The command prefix (e.g., `"!"`).
- `cooldown_seconds`: Minimum time between commands from the same user.

## Author
**Nikolai Myrstad** 
- Information Engineering Student  
- GitHub: [https://github.com/nimyhub](https://github.com/nimyhub)
---

## License

This project is licensed under the [MIT License](LICENSE).
