import logging

from core import Message

logger = logging.getLogger(__name__)


class SlackAPI(object):
    def __init__(self, api):
        self.api = api

        # Client won't receive any messages if not authorized first
        self.bot_id = self.api.api_call('auth.test')['user_id']
        logger.debug('Authorized as %s', self.bot_id)

    def read(self):
        events = self.api.rtm_read()
        logger.debug('Received %d events from Slack', len(events))

        messages = []
        for event in events:
            is_text_message = event['type'] == 'message'
            not_authored_by_bot = event.get('user') != self.bot_id
            if is_text_message and not_authored_by_bot:
                m = Message(
                    text=event['text'],
                    channel=event['channel'],
                )
                messages.append(m)

        logger.debug('Passing %d text messages', len(messages))
        return messages

    def write(self, message):
        self.api.api_call(
            'chat.postMessage',
            channel=message.channel,
            text=message.text,
            as_user=True,  # This will show a user avatar in the message
        )


def open(token):
    """See https://slackapi.github.io/python-slackclient/ for reference"""
    # Lazyly import third party library and create a client object
    import slackclient
    client = slackclient.SlackClient(token)
    is_connected = client.rtm_connect(with_team_state=False)
    if not is_connected:
        raise RuntimeError('Failed to connect to Slack API')

    # Return custom file-like object
    return SlackAPI(client)
