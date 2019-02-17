from deeppavlov.skills.pattern_matching_skill import PatternMatchingSkill
from deeppavlov.agents.default_agent.default_agent import DefaultAgent
from deeppavlov.agents.processors.highest_confidence_selector import HighestConfidenceSelector

from core import Message


class CachedAgent(object):
    _instance = None

    @classmethod
    def get_agent(cls):
        """Singleton"""
        if cls._instance is None:
            cls._instance = cls._build_agent()
        return cls._instance

    def _build_skills():
        hello = PatternMatchingSkill(
            responses=['Hello world!'],
            patterns=["hi", "hello", "good day"],
        )
        bye = PatternMatchingSkill(
            ['Goodbye world!', 'See you around'],
            patterns=["bye", "chao", "see you"],
        )
        fallback = PatternMatchingSkill(
            ["I don't understand, sorry", 'I can say "Hello world!"'],
        )
        return [hello, bye, fallback]

    @staticmethod
    def _build_agent():
        return DefaultAgent(
            CachedAgent._build_skills(),
            skills_selector=HighestConfidenceSelector(),
        )


def process_many(messages):
    """Bulk messages processing with deeppavlov.ai"""
    if not messages:
        return []  # Fast return

    requests = [m.text for m in messages]

    # Actual work is here
    agent = CachedAgent.get_agent()
    responses = agent(requests)

    # Return a list of messages to original channels
    return [
        Message(
            text=response_text,
            channel=original.channel,
        )
        for original, response_text in zip(messages, responses)
    ]
