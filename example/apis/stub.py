import logging

from core import Message

logger = logging.getLogger(__name__)


class StubAPI(object):
    def read(self):
        """Always return one new message"""
        logger.debug('Fake read from stub API')
        return [
            Message(
                text='I am a teapot!',
                channel=0,
            )
        ]

    def write(self, message):
        logger.debug('Fake write to stub API')
        logger.info(message.text)


def open(token):
    """Returns stub API file-like object"""
    return StubAPI()
