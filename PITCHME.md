@title[title]
# Build your first slack bot
## in three hours

#### 2nd edition

by You and Ivan Styazhkin @ DataRobot

+++
@title[why]
# Why?
> Ensure happiness and productivity of your colleagues

> Always be developing yourself

Are two of nine DataRobot's Core Values

---
# Trains

![here comes the train!](assets/trains.jpg)

+++
## Tracks

![hold on tight!](assets/train-on-wobbly-tracks.jpg)

---
# Queues

![a conveyor](assets/assembling-line.jpg)

+++
## Factories

![back and forth](assets/toyota-queues.jpg)

---
# Brain

![processor](assets/nervous2.jpg)

+++
## Hack

![machines](assets/hack-your-brain.jpg)

---
@title[abstract]
## Plan of attack

0. Connect to the API
1. Read messages from API
2. Process all messages
  - Decide if we need to respond
  - Compose the response message
3. Send responses if required
4. Repeat from **1**
5. ????
6. PROFIT!!!!

---
@title[setup]
### Setup a python

Test that python is ready

`$ python --version`

+++
### Python virtual environment

See [the installation guide](https://virtualenv.pypa.io/en/latest/installation/)

Create new virtual environment

`$ virtualenv bot-venv`

+++
### Activate it

`. bot-env/bin/activate`

Test it!

`(bot-env) $ which python`

`(bot-env) $ which pip`

---
## Tools

`(bot-env) $ pip install bpython`

`$ pip install --user bpython`

---
@title[bootstrap]
### Bootstrap

- Create a new python file
- Test it! `python mybotfile.py`
- ???
- No news? It's good news!
- Now let's build a skeleton

---
@title[skeleton]
## Skeleton

![different kinds](assets/animal-skeletons.jpg)

+++
## Skeleton

- `if __name__ == '__main__':`
- `def main():` which
- Two queue of messages (incoming, outgoing)
- `import brain`
- `import transport`

+++
## Main

- Create new function with _one argument_ and immediate `return`
- Test it!

+++
## Queues

![queues](assets/queue.jpeg)

+++
## Queues aka FIFO

_First In - First Out_

- `[]` aka `list()`
  - `.append()`
  - `.pop(0)`

- `collections.deque()`
  - `.append()`
  - `.popleft()`

+++
## Imports

- Create an empty python file aka _module_
- Add `import` statement
- Test it!
- Repeat it for another module

---
## Message

> Whose properties one Message have?

- Text of the message

+++
## Message

- Create a `class` to hold those attributes
- Test it!
- Extra: add `__repr__` method

---
@title[brain]
## Brain

![brain](assets/nexosis-brain.jpg)

+++
## Brain

- _Keep It Simple_ for start
- `def process()`
- `def echo()`
- `def teapot()`

+++
## Processor

- Build a function which takes one message and returns a list of response messages
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
- Respond only to addressed messages for now
- Test it!

+++
### Extract a command

- Threat first word of the text as _a command_
- Respond to messages with a specific command only
- Test it!
- Extra: Extract author's name from the message

---
### Repeat

- Add two more commands and new responses
- Test it!

---
@title[rails]
## Transport tracks

![this is complex](assets/brain-excercises.jpg)

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
### Listen to events

- Try one `read` and one `print` per script run
- Test it!

+++
### Listen to events

- Wrap `.rtm_read()` into endless `while` cycle
- Test it!
- Stop it by `Ctrl + C`

---
### Send answer back

- Extract a channel ID from the message
- Use `.api_call('chat.postMessage')` call
- Test it!

---
### Invite it into a channel

- Make sure that answers posted to the right channel
- Test it!

---
# Just did it
Hip-hip, Hooray!

---
@title[references]
## References

- https://api.slack.com/methods
- https://github.com/slackapi/python-slackclient
- https://core.telegram.org/bots
- https://github.com/python-telegram-bot/python-telegram-bot/

---
@title[thank you]
# Thank you

![dinner time](assets/dinner.gif)

+++
@title[references]
# Links

- https://en.wikipedia.org/wiki/SOLID
- https://slackapi.github.io/python-slackclient
- https://python-telegram-bot.org/
