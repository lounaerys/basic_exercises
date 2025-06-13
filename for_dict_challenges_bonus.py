"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime

import lorem


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages


if __name__ == "__main__":
    print(generate_chat_history())

def find_the_most_active_user(messages):
    user_messages = {}
    for message in messages: 
            user_id = message['sent_by']
            if user_id in user_messages:
                user_messages[user_id] += 1
            else:
                user_messages[user_id] = 1

    return max(user_messages, key=user_messages.get)


if __name__ == "__main__":
    chat_history = generate_chat_history()
    print(find_the_most_active_user(chat_history))

def find_the_most_answers(messages):
    user_answers = {}
    for message in messages:
        users_reply = message['reply_for']
        if users_reply is not None:
            if users_reply in user_answers:
                user_answers[users_reply] += 1
            else:
                user_answers[users_reply] = 1
               
    if not user_answers:
        return None
    
    return max(user_answers, key=user_answers.get)

if __name__ == "__main__":
    answers_history = generate_chat_history()
    print(find_the_most_answers(answers_history))
          
def most_views_messages(messages):
    user_views = {}
    for message in messages:
        user_id = message['sent_by']
        users_seen = message['seen_by']
        if user_id not in user_views:
            user_views[user_id] = []

        for viewer in users_seen:
            if viewer not in user_views[user_id]:
                user_views[user_id].append(viewer)

    max_user = None
    max_views = 0

    for user, viewers in user_views.items():
        if len(viewers) > max_views:
            max_views = len(viewers)
            max_user = user

    return max_user

if __name__ == "__main__":
    views_history = generate_chat_history()
    print(most_views_messages(views_history))

def prime_time(messages):
    morning = 0
    afternoon = 0
    evening = 0
    night = 0 

    for message in messages:
        hour = message['sent_at'].hour
        if 6 <= hour < 12:
            morning += 1
        elif 12 <= hour < 18:
            afternoon += 1
        elif 18 <= hour < 24:
            evening += 1
        else:
            night += 1 


    max_messages = max(morning, afternoon, evening)
    
    if max_messages == morning:
        return 'Больше всего сообщений было утром'
    elif max_messages == afternoon:
        return 'Больше всего сообщений было днем'
    elif max_messages == evening:
        return 'Больше всего сообщений было вечером'
    else:
        return 'Больше всего сообщений было ночью'

if __name__ == "__main__":
    prime_time_messages = generate_chat_history()
    print(prime_time(prime_time_messages))

def most_popular_thread(messages):
    thread = {}
    for message in messages:
        users_reply = message['reply_for']
        if users_reply is not None:
            if users_reply in thread:
                thread[users_reply] += 1
            else:
                thread[users_reply] = 1

    if not thread:
        return None
    
    return max(thread, key=thread.get)

if __name__ == "__main__":
    thread_answers = generate_chat_history()
    print(most_popular_thread(thread_answers))
