# Способы вызова функции
def send_email(message, recipient, sender="university.help@gmail.com") -> object:
    suffix = ('.com', '.net', '.ru')   # Кортеж суффиксов ('.com', '.net', '.ru')
    a = recipient.endswith(suffix)     # Проверка на наличия суффикса в e-mail
    b = sender.endswith(suffix)
    a_ = "@" in recipient              # Проверка на наличия символа @ в e-mail
    b_ = "@" in sender
    if a == 0 or b == 0 or a_ == 0 or b_ == 0:  # Проверка на корректность e-mail отправителя и получателя.
        print("Невозможно отправить письмо с адреса ", sender, " на адрес ", recipient)
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender != "university.help@gmail.com" and sender != recipient:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient)
    else:
        print("Письмо успешно отправлено с адреса ", sender, " на адрес ", recipient)

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
#send_email('Вы видите это сообщение как лучший студент курса!', recipient='urban.fan@mail.ru', sender='urban.info@gmail.com')
#send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
#send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')



