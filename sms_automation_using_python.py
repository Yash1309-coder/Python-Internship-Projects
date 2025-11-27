from twilio.rest import Client

account_sid = "enter sid"
auth_token = "ente auth
client = Client(account_sid, auth_token)
message = client.messages.create(
    body="Bhai so ja ! kl prectical hai",
    from_="+18648081664",   # Your Twilio number
    to="+919053318341"     # Receiver number
)
print("SMS Sent! Message SID:", message.sid)

