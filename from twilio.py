from twilio.rest import Client

# Your Twilio Account SID and Auth Token
account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
auth_token = 'YOUR_TWILIO_AUTH_TOKEN'

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Make a call
call = client.calls.create(
    to='+919325702118',  # The number you want to call
    from_='+14153902828',  # Your Twilio phone number
    url='http://demo.twilio.com/docs/voice.xml'  # URL for TwiML instructions
)

print(call.sid)  # Print call SID