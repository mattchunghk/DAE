from telethon import TelegramClient, sync
import pandas as pd

api_id = 25057595
api_hash = 'c116ec5e11b9018cbca5d457433c412a'
# Group name can be found in group link (Example group link : https://t.me/c0ban_global, group name = 'c0ban_global')
group_username = 'EAHK_Learning'
client = TelegramClient('session_name', api_id, api_hash).start()

# You will be asked to enter your mobile number- Enter mobile number with country code
# Enter OTP (For OTP check Telegram inbox)
participants = client.get_participants(group_username)

firstname = []
lastname = []
username = []
if len(participants):
    for x in participants:
        firstname.append(x.first_name)
        lastname.append(x.last_name)
        username.append(x.username)

# list to data frame conversion

data = {'first_name': firstname, 'last_name': lastname, 'user_name': username}

userdetails = pd.DataFrame(data)

# n number of messages to be extracted
chats = client.get_messages(group_username, 100)
# Get message id, message, sender id, reply to message id, and timestamp
message_id = []
message = []
sender = []
reply_to = []
time = []
if len(chats):
    for chat in chats:
        message_id.append(chat.id)
        message.append(chat.message)
        sender.append(chat.from_id)
        reply_to.append(chat.reply_to_msg_id)
        time.append(chat.date)
data = {'message_id': message_id, 'message': message,
        'sender_ID': sender, 'reply_to_msg_id': reply_to, 'time': time}
df = pd.DataFrame(data)

print(df)
print(userdetails)
