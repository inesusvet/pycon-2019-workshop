class Message(object):
    def __init__(self, text, channel):
        self.text = text
        self.channel = channel

    def __repr__(self):
        return '<Mesage in %s: "%s">' % (self.channel, self.text)
