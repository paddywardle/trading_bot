from src.notification.SlackClient import SlackClient

if __name__ == "__main__":

    slack = SlackClient(message="Hello again")

    slack.send_message()