def send_email(message, *recipient, sender="university.help@gmail.com"):
    ver_sender = sender.endswith(('.com', '.net', '.ru')) and '@' in sender
    for i in recipient:
        ver_recipient = i.endswith(('.com', '.net', '.ru')) and '@' in i
    if sender == i:
        print("Нельзя отправить письмо самому себе!")
    elif not ver_sender or not ver_recipient:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {i}")
    elif sender == "university.help@gmail.com":
        print( f"Письмо успешно отправлено с адреса {sender} на адрес {i}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {i}.")
        return

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.fan@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
