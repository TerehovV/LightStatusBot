import random


messages_on = ['✅ Свет дали ! Зарядите павербанки !',
               '✅ Тушите свечи, свет вернулся ;)',
               '✅ 220 вернулось в розетки !']
messages_off = ['⭕ Свет отключили. Время книг !',
                '⭕ Свет отключили. Настало время настольных игр !',
                '⭕ Свет пропал, ждем подключения']

def light_on_message():
    random_message_on = random.choice(messages_on)
    return random_message_on

def light_off_message():
    random_message_off = random.choice(messages_off)
    return random_message_off


