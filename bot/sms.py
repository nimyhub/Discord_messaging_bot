from twilio.rest import Client
from bot.config import TWILIO_ENABLED, TWILIO_SID, TWILIO_TOKEN, TWILIO_PHONE_NUMBER

phone_number = None
twilio_client = Client(TWILIO_SID, TWILIO_TOKEN) if TWILIO_ENABLED and TWILIO_SID and TWILIO_TOKEN else None

async def send_sms(message: str):
    if not TWILIO_ENABLED or not twilio_client:
        print("Twilio not enabled or client not initialized.")
        return False
    if not phone_number:
        print("Phone number not set.")
        return False
    try:
        twilio_client.messages.create(
            to=phone_number,
            from_=TWILIO_PHONE_NUMBER,
            body=message
        )
        return True
    except Exception as e:
        print(f"Error sending SMS: {e}")
        return False

def set_phone_number(new_number: str):
    global phone_number
    phone_number = new_number
