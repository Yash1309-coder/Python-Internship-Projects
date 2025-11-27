from twilio.rest import Client

account_sid = "ACe5854aebda418827f557f15355434806"
auth_token = "0e1d99da384fe6eeba0b10b1cd3c4e2a"
client = Client(account_sid, auth_token)
message = client.messages.create(
    body="Bhai so ja ! kl prectical hai",
    from_="+18648081664",   # Your Twilio number
    to="+919053318341"     # Receiver number
)
print("SMS Sent! Message SID:", message.sid)
