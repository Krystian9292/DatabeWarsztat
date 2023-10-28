import argparse
from models import Message, User
from clcrypto import check_password

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--username", help="username")
parser.add_argument("-p", "--password", help="password")
parser.add_argument("-l", "--list", help="list all messages", action="store_true")
parser.add_argument("-t", "--to", help="to")
parser.add_argument("-s", "--send", help="text message to send")

args = parser.parse_args()

def print_user_messages(cur, user):
    messages = Message.load_all_messages(cur, user.id)
    for message in messages:
        from_ = User.load_user_by_id(cur, message.from_id)
        print(20 * "-")
        print(f"from: {from_.username}")
        print(f"data: {message.creation_date}")
        print(message.text)
        print(20 * "-")
