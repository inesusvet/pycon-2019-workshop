
@snap[north]
![](assets/datarobot-logo.png)
@snapend

@snap[west]
![](assets/pycon-logo.png)
@snapend

@snap[east]
Are you ready, kids?
@snapend

@snap[south]
gitpitch.com/inesusvet/pycon-2019-workshop
@snapend

---?image=assets/clean-title.png&size=cover
@title[title]
# Build your first chat bot
## in three hours

#### 2nd edition

by You and Ivan Styazhkin @ DataRobot

+++
@title[why]
# Why? What? When?
> Ensure happiness and productivity of your colleagues

> Always be developing yourself

Are two of nine DataRobot's Core Values

---
@title[disclaimer]
## Slang

![what was it?](assets/redis-ca.jpg)

+++
## Pair programming

![make a friend](assets/knight-move.jpg)

---
@title[trains]
# Trains

![here comes the train!](assets/trains.jpg)

+++
## Tracks

![hold on tight!](assets/train-on-wobbly-tracks.jpg)

---
@title[queues]
# Queues

![a queue](assets/queue.jpeg)

+++
## Factories

![back and forth](assets/toyota-queues.jpg)

---
@title[brain]
# Brain

![machines](assets/hack-your-brain.jpg)

---
@title[abstract]
## Plan of attack

- ????

+++
## Plan of attack

0. Connect to the _API_
1. Read messages from _API_
2. Process new messages
  - Decide if we need to respond
  - Compose the response messages
3. Send responses if any
4. Repeat
5. ????
6. PROFIT!!!!

+++
## Is the API important?

- Slack
- Telegram
- any other

+++
## Clean Architecture

![layers](assets/layers.jpg)

by Uncle Bob Martin

---
@title[setup]
### Setup a python

Test that python interpreter is ready

`$ python --version`

+++
### Python virtual environment

See [the installation guide](https://virtualenv.pypa.io/en/latest/installation/)

Create new _virtual environment_

`$ virtualenv bot-venv`

+++
### Activate it

- `$ source bot-env/bin/activate`
- Test it!
- `(bot-env) $ which python`
- `(bot-env) $ which pip`

+++
## Extra tools

`(bot-env) $ pip install bpython`

`$ pip install --user bpython`

---
### Bootstrap

- Create a new _module_
- Test it! `$ python mybotfile.py`
- ???
- No news? It's **good** news!
- Now let's build a _core_

---
@title[message]
## Message

> Whose properties one Message have?

- Text of the message
- ????

+++
## Message!

- Create a `class` to hold those attributes
- Test it!
- Extra: add `__repr__` _method_
- Now let's build a _walking skeleton_

+++
### Example

```python
class Message(object):
    def __init__(self, text):
        self.text = text
```

---
@title[skeleton]
## Skeleton

![different kinds](assets/animal-skeletons.jpg)

+++
## Keep It Simple

- Execution ready `if __name__ == '...'`
- One function `def main()`
- Two queues of messages (incoming, outgoing)
- File-like interface for API interaction

+++
## Main

- Create new _function_ with one _argument_ and immediate `return`
- Test it!

+++
## Queue (a conveyor)

![assembling-line](assets/assembling-line.jpg)

+++
## Queues aka FIFO!

_First In - First Out_

- `[]` aka `list()`
  - `.append()`
  - `.pop(0)`

- `collections.deque()`
  - `.append()`
  - `.popleft()`

+++
### Example

```python
def main():
    incoming = []
    outgoing = []
    return

if __name__ == '__main__':
    main()
```

---
@title[files]
## File is simple

- `fh = open('..', 'rw')`
- `fh.read()`
- `fh.write(text)`
- `fh.seek(0)`
- `fh.tell()`
- `fh.close()`

+++
## File is too much

- `fh = open('..', 'rw')`
- `fh.read()`
- `fh.write(text)`
- ~`fh.seek(0)`~
- ~`fh.tell()`~
- ~`fh.close()`~

---
@title[stubs]
## API stubs!

- `open` function which returns _stub instance_
- And _stub_ class with two methods
  - `read` returns new messages from API
  - `write` takes a message list to send them to API

+++
### Example

```python
def open():
    return StubAPI()

class StubAPI(object):
    def read(self):
        return [Message('Que tal?')]

    def write(self, messages):
        pass
```

---
@title[brain]
## Brain

![brain](assets/brain.png)

+++
## Brain

- _Keep It Simple_ again
- `def process(messages)`
- `def echo(message)`
- `def teapot()`

+++
## Processor

- Build a function which takes a list of messages and returns a new list of response messages
- Pass message to other functions
- Test it!

+++
### Compose an answer

- Build a `teapot` function with hardcoded answer
- Test it!
- Make an `echo` function which just repeats
- Test it!

+++
### Distinguish addressed messages

- Create a function which looks for bot's ID in the text
- Respond only to addressed messages
- Test it!

+++
### Extract a command

- Threat first word of the text as _a command_
- Respond to messages with a specific command only
- Test it!

+++
### Repeat

- Add two more commands and new responses
- Test it!
- Extra: Pass author's name as message's attribute

---
@title[rails]
## Transport lines

![this is complex](assets/brain-excersises.jpg)

---
@title[slack]
### Register a new slack bot

Welcome to the [PyCon slack team](https://join.slack.com/t/pycon-by/shared_invite/enQtNTM1NzY3Mzg0MTUwLTQ4ZTU3ZGE4MWM4MWQ1YzkyODRiZjg4NDZiYWZmNGNmY2NjYTYxNzQzMGRkNDExYjkwMjZjMzQwNDFjZDQxMmQ)

Go to apps [registration page](https://api.slack.com/apps)

My token `xoxb-...-...`

+++
@title[telegram]
### Register a new telegram bot

Ask @BotFather about it

Here goes some [docs](https://core.telegram.org/bots#6-botfather) about it

---
@title[name]
### What about the name?

<iframe width="560" height="315" src="https://www.youtube.com/embed/z-elPdgxWL0?rel=0&amp;controls=0&amp;showinfo=0" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

---
## Documentation links

- TBD

---
@title[connect]
### Connect my bot to API

- Install [slackclient](https://slackapi.github.io/python-slackclient/) package with `pip`
- Import `slackclient`
- Create `open` function
- Initialize `slackclient.SlackClient` object with token
- Test it!

+++
### Connect to Slack

- Try to connect with `.rtm_connect()` call ([docs](https://slackapi.github.io/python-slackclient/real_time_messaging.html#connecting-to-the-rtm-api))
- Get user ID by `.api_call('auth.test')` call
- Test it!

+++
### Connected!

Bot is online while this python script runs

![excellent!](assets/excellent.jpg)

+++
### Connect to Telegram

- Install [python-telegram-bot](https://python-telegram-bot.org/) package with `pip`
- Import `telegram`
- Create `open` function
- Initialize `telegram.Bot` object with token
- Test it!

+++
### Build TelegramAPI class

- `open` function to initialize
- `read` to fetch messages
- `write` to send messages

---
@title[listen]
### Listen to events

- Try one `read` and one `print` per script run
- Test it!

+++
### Listen to events

- Wrap `.rtm_read()` into endless `while` cycle
- Test it!
- Stop it by `Ctrl + C`

---
@title[respond]
### Send answer back

- Extract a channel ID from the message
- Use `.api_call('chat.postMessage')` call
- Test it!

---
### Invite the bot to a channel

- Make sure that answers posted to the right channel
- Test it!

---
# Just did it
Hip-hip, Hooray!

---
@title[references]
## References

- https://api.slack.com/methods
- https://slackapi.github.io/python-slackclient
- https://core.telegram.org/bots
- https://python-telegram-bot.org/
- https://en.wikipedia.org/wiki/SOLID

---
@title[thank you]
## Thank you

![dinner time](assets/dinner-time.jpg)
