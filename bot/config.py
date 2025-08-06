import json

CONFIG_FILE = "config.json"
MESSAGE_FILE = "messages.json"

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

config = load_json(CONFIG_FILE)
messages = load_json(MESSAGE_FILE)

CHANNEL_ID = config.get("channel_id", 0)
USER_ID = config.get("user_id", 0)
TOKEN = config.get("token","none")
PREFIX = config.get("prefix","!")
COOLDOWN_SEC = config.get("cooldown_seconds",30)
SMS_CALL = config.get("enable_sms_call",False)
TWILIO_ENABLED = config.get("enable_twilio",False)
TWILIO_SID = config.get("twilio_account_sid","")
TWILIO_TOKEN = config.get("twilio_auth_token","")
TWILIO_PHONE_NUMBER = config.get("twilio_phone_number","")