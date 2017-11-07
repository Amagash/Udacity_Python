# make sure you run in python 3
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACa467ed678a2067bf67ec284dbbf55c2e"
# Your Auth Token from twilio.com/console
auth_token  = "df59ff35658616dee86c228a96ac7abf"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+33621110251",
    from_="+33756799395",
    body="coucou ! ")

print(message.sid)