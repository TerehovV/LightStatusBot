from config import token, CHANNEL_NAME, ip, status_on, status_off
from router_status import get_status
from bot_messages import light_on_message, light_off_message
from RingBufferStatus import RingBuffer
import telebot
import threading


bot = telebot.TeleBot(token)
buf = RingBuffer(4)
status = [True, True, True, True]

def main():
    global status
    threading.Timer(15.0, main).start()
    buf.append(get_status(ip))
    session = buf.get()
    if status != session:
        if session == status_on:
            bot.send_message(chat_id=CHANNEL_NAME, text=light_on_message())
        elif session == status_off:
            bot.send_message(chat_id=CHANNEL_NAME, text=light_off_message())
        else:
            pass
    else:
        pass
    status[:] = session[:]


if __name__ == '__main__':
    main()
    bot.polling(none_stop=True)
