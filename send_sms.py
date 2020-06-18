from twilio.rest import Client

 #Your Account SID from twilio.com/console
account_sid = "AC0f37f2e570f6072e6042ced3632b24f8" #your account SID from twilio console

 #Your Auth Token from twilio.com/console
auth_token  = "01eb4f6cb676b1949b46fef3e833db95" #your auth token from twilio console

client = Client(account_sid, auth_token)
message = client.messages.create(
to="9046513819",
from_="9045695580",
body="Hello from your Computer")

print(message.sid) #To print sid 