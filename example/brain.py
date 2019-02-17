# -*- coding: utf-8 -*-
import logging

from core import Message
from love import random_confession

logger = logging.getLogger(__name__)


def echo(message):
    """Just respond with the same message"""
    return [message]


def foolproof(message):
    """This processor don't like D-word"""
    if u'дурак' in message.text.lower():
        return [Message(u'Сам дурак', message.channel)]


def love_talk(message):
    """This processor generates two messages in response"""
    if 'love' in message.text.lower():
        channel = message.channel
        language, confession = random_confession()
        return [
            Message(
                confession,
                channel,
            ),
            Message(
                'This means "I love you" in %s language' % language,
                channel,
            ),
        ]


def process(message):
    responses = foolproof(message)
    if responses:
        return responses

    responses = love_talk(message)
    if responses:
        return responses

    # Default reponse - just echoing
    return echo(message)
