from twilio.rest import Client
from secrets import sender, destination, account_sid, auth_token

client = Client(account_sid, auth_token)

def whatsapp_message(message_to_send:str, destination=destination, sender=sender):

    platform = 'whatsapp'
    destination = '{}:{}'.format(platform, destination)
    sender = '{}:{}'.format(platform, sender)

    message = client.messages.create(
                                from_ = sender,
                                body = message_to_send,
                                to = destination
                            )

    print(f'"{message_to_send}" sended to {destination} from {sender}')

if __name__ == '__main__':
    whatsapp_message('Hola Sam')