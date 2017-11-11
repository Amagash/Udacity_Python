# make sure you run in python 3
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "SID"
# Your Auth Token from twilio.com/console
auth_token  = "author token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="phone number",
    from_="phone number",
    body="coucou ! ")

print(message.sid)