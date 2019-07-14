from pytg import Telegram
from pytg.utils import coroutine
tg      = Telegram(  telegram="./tg/bin/telegram-cli", pubkey_file="./tg/tg-server.pub")
receiver    = tg.receiver
QUIT = False
@coroutine
def main_loop():
  try:
    while not QUIT:
      msg = (yield) # it waits until it got a message, stored now in msg.
      if msg.text is None:
        continue
      print(msg.event)
      print(msg.text)
  except GeneratorExit:
    pass
  except KeyboardInterrupt:
    pass
  else:
    pass

receiver.start()
receiver.message(main_loop())