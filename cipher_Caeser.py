lower_cyrillic = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т",
                  "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
upper_cyrillic = ["А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т",
                  "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я"]
number_ = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


def encrypted_caeser(str_, shift=3):
    result = ""
    for x in str_:
        if x in lower_cyrillic:
            indx = lower_cyrillic.index(x) % len(lower_cyrillic)
            result += lower_cyrillic[(indx+shift) % len(lower_cyrillic)]
        elif x in upper_cyrillic:
            indx = upper_cyrillic.index(x) % len(upper_cyrillic)
            result += upper_cyrillic[(indx+shift) % len(upper_cyrillic)]
        elif x in number_:
            indx = number_.index(x) % len(number_)
            result += number_[(indx+shift) % len(number_)]
        else:
            result += x
    return result


def decrypted_caeser(str_, shift=3):
    result = ""
    for x in str_:
        if x in lower_cyrillic:
            indx = lower_cyrillic.index(x) % len(lower_cyrillic)
            result += lower_cyrillic[(indx-shift) % len(lower_cyrillic)]
        elif x in upper_cyrillic:
            indx = upper_cyrillic.index(x) % len(upper_cyrillic)
            result += upper_cyrillic[(indx-shift) % len(upper_cyrillic)]
        elif x in number_:
            indx = number_.index(x) % len(number_)
            result += number_[(indx-shift) % len(number_)]
        else:
            result += x
    return result


print(encrypted_caeser(str(input('Введите строку для шифрования: '))))
print(decrypted_caeser(str(input('Введите строку для дешифрования: '))))
