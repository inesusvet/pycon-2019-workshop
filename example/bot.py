import argparse
import collections
import logging
import time

import brain

logger = logging.getLogger(__name__)


def main(api, sleep_time=5):
    logger.debug('Initializing two message queues')
    incoming = collections.deque()
    outgoing = collections.deque()

    logger.info('Staring infinite loop now')
    while True:
        logging.debug('Reading new messages')
        new_messages = api.read()
        if not new_messages:
            logger.debug('No new messages. Sleeping for %d seconds now', sleep_time)
            time.sleep(sleep_time)
            continue

        logger.debug('Putting %d new messages to the incoming queue', len(new_messages))
        incoming.extend(new_messages)

        logger.debug('Processing %d messages from the incoming queue', len(incoming))
        while incoming:  # While there are incoming messages left
            message = incoming.popleft()
            responses = brain.process(message)
            if responses:
                logger.debug('Putting %d response messages to the outgoing queue', len(responses))
                outgoing.extend(responses)

        logger.debug('Sending %d messages from the outgoing queue', len(outgoing))
        while outgoing:
            message = outgoing.popleft()
            logger.debug('Sending a message to %s: %r', message.channel, message.text)
            api.write(message)


def load_api(name):
    """Do not use importlib.import_module() here for better clarity"""
    if name == 'telega':
        from apis import telega
        return telega.open(args.token)

    elif name == 'slack':
        from apis import slack
        return slack.open(args.token)

    # Fallback to stub API class
    from apis import stub
    return stub.open(args.token)


def _build_arg_parser():
    """See documentation on argparse module for reference"""
    parser = argparse.ArgumentParser(
        description='Example of a chat bot which is able to work with different APIs')
    parser.add_argument('api', choices=['telega', 'slack'], help='Which API use to fetch and sent messages')
    parser.add_argument('token', help='Auth token to use to connect')
    parser.add_argument('-v', '--verbose', action='store_true', help='Change logging level to DEBUG')
    parser.add_argument('--sleep', type=int, default=1, help='How long to sleep in cycle')
    return parser


if __name__ == '__main__':
    parser = _build_arg_parser()
    args = parser.parse_args()

    logging_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(
        level=logging_level,
        format='%(asctime)s %(levelname)s %(message)s',
    )

    api = load_api(args.api)
    try:
        main(api, sleep_time=args.sleep)
    except KeyboardInterrupt:
        logger.error('Stopping the process by KeyboardInterrupt')

    except Exception as ex:
        logger.exception('Fatal failure')
        exit(1)
