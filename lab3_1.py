import re

#Задание 1

#test1
st = "X<|"
match = re.search(r'[:;X8=][-<][{]*[()O|\/P]$', st) 
itg = match[0] if match else 'Not found'
if itg == "X<|":
    print("test1 is okay")
else:
    print("test1 is false")

#test2
st = "X<8"
match = re.search(r'[:;X8=][-<][{]*[()O|\/P]$', st) 
itg = match[0] if match else 'Not found'
if itg == "Not found":
    print("test2 is okay")
else:
    print("test2 is false")

#test3
st = "8<{P"
match = re.search(r'[:;X8=][-<][{]*[()O|\/P]$', st) 
itg = match[0] if match else 'Not found'
if itg == "8<{P":
    print("test3 is okay")
else:
    print("test3 is false")

#test4
st = ";-|"
match = re.search(r'[:;X8=][-<][{]*[()O|\/P]$', st) 
itg = match[0] if match else 'Not found'
if itg == ";-|":
    print("test4 is okay")
else:
    print("test4 is false")

#test5
st = "=-{OO"
match = re.search(r'[:;X8=][-<][{]*[()O|\/P]$', st) 
itg = match[0] if match else 'Not found'
if itg == "Not found":
    print("test5 is okay")
else:
    print("test5 is false")


print("------------------------------------------------------------------------------------")
#Задание 2

#test1
st = "Вечер за окном. / Еще один день прожит. / Жизнь скоротечна..."
itg = ""
match = re.split(r' / ', st) 
if len(match) == 3:    
    itg = match[0] + " ? " + match[1] + " ? " + match[2] if match else 'Not found'
    st1 = itg.split(" ? ")[0]
    st2 = itg.split(" ? ")[1]
    st3 = itg.split(" ? ")[2]
    match1 = re.findall(r'[ауоыиэяюёеАУОЫИЭЯЮЕЁ]', st1) 
    itg1 = len(match1)
    match2 = re.findall(r'[ауоыиэяюёеАУОЫИЭЯЮЕЁ]', st2) 
    itg2 = len(match2)
    match3 = re.findall(r'[ауоыиэяюёеАУОЫИЭЯЮЕЁ]', st3) 
    itg3 = len(match3)
    if itg1 == 5 and itg2 == 7 and itg3 == 5:
        itg = "Хайку!"
    else:
        itg = "Не хайку."
else:
    itg = "Не хайку. Должно быть 3 строки."
if itg == "Хайку!":
    print("test1 is okay")
else:
    print("test1 is false")

#test2
st = "Просто текст"
itg = ""
match = re.split(r' / ', st) 
if len(match) == 3:    
    itg = match[0] + " ? " + match[1] + " ? " + match[2] if match else 'Not found'
    st1 = itg.split(" ? ")[0]
    st2 = itg.split(" ? ")[1]
    st3 = itg.split(" ? ")[2]
    match1 = re.findall(r'[ауоыиэяюёеАУОЫИЭЯЮЕЁ]', st1) 
    itg1 = len(match1)
    match2 = re.findall(r'[ауоыиэяюёеАУОЫИЭЯЮЕЁ]', st2) 
    itg2 = len(match2)
    match3 = re.findall(r'[ауоыиэяюёеАУОЫИЭЯЮЕЁ]', st3) 
    itg3 = len(match3)
    if itg1 == 5 and itg2 == 7 and itg3 == 5:
        itg = "Хайку!"
    else:
        itg = "Не хайку."
else:
    itg = "Не хайку. Должно быть 3 строки."
if itg == "Не хайку. Должно быть 3 строки.":
    print("test2 is okay")
else:
    print("test2 is false") 

#test3
st = "Как вишня расцвела! / Она с коня согнала / И князя-гордеца."
itg = ""
match = re.split(r' / ', st) 
if len(match) == 3:    
    itg = match[0] + " ? " + match[1] + " ? " + match[2] if match else 'Not found'
    st1 = itg.split(" ? ")[0]
    st2 = itg.split(" ? ")[1]
    st3 = itg.split(" ? ")[2]
    match1 = re.findall(r'[ауоыиэяюёеАУОЫИЭЯЮЕЁ]', st1) 
    itg1 = len(match1)
    match2 = re.findall(r'[ауоыиэяюёеАУОЫИЭЯЮЕЁ]', st2) 
    itg2 = len(match2)
    match3 = re.findall(r'[ауоыиэяюёеАУОЫИЭЯЮЕЁ]', st3) 
    itg3 = len(match3)
    if itg1 == 5 and itg2 == 7 and itg3 == 5:
        itg = "Хайку!"
    else:
        itg = "Не хайку."
else:
    itg = "Не хайку. Должно быть 3 строки."
if itg == "Не хайку.":
    print("test3 is okay")
else:
    print("test3 is false")

#test4
st = "еееее / еееееее / еееее"
itg = ""
match = re.split(r' / ', st) 
if len(match) == 3:    
    itg = match[0] + " ? " + match[1] + " ? " + match[2] if match else 'Not found'
    st1 = itg.split(" ? ")[0]
    st2 = itg.split(" ? ")[1]
    st3 = itg.split(" ? ")[2]
    match1 = re.findall(r'[ауоыиэяюёеАУОЫИЭЯЮЕЁ]', st1) 
    itg1 = len(match1)
    match2 = re.findall(r'[ауоыиэяюёеАУОЫИЭЯЮЕЁ]', st2) 
    itg2 = len(match2)
    match3 = re.findall(r'[ауоыиэяюёеАУОЫИЭЯЮЕЁ]', st3) 
    itg3 = len(match3)
    if itg1 == 5 and itg2 == 7 and itg3 == 5:
        itg = "Хайку!"
    else:
        itg = "Не хайку."
else:
    itg = "Не хайку. Должно быть 3 строки."
if itg == "Хайку!":
    print("test4 is okay")
else:
    print("test4 is false")

#test5
st = "еееее / ееееее"
itg = ""
match = re.split(r' / ', st) 
if len(match) == 3:    
    itg = match[0] + " ? " + match[1] + " ? " + match[2] if match else 'Not found'
    st1 = itg.split(" ? ")[0]
    st2 = itg.split(" ? ")[1]
    st3 = itg.split(" ? ")[2]
    match1 = re.findall(r'[ауоыиэяюёеАУОЫИЭЯЮЕЁ]', st1) 
    itg1 = len(match1)
    match2 = re.findall(r'[ауоыиэяюёеАУОЫИЭЯЮЕЁ]', st2) 
    itg2 = len(match2)
    match3 = re.findall(r'[ауоыиэяюёеАУОЫИЭЯЮЕЁ]', st3) 
    itg3 = len(match3)
    if itg1 == 5 and itg2 == 7 and itg3 == 5:
        itg = "Хайку!"
    else:
        itg = "Не хайку."
else:
    itg = "Не хайку. Должно быть 3 строки."
if itg == "Не хайку. Должно быть 3 строки.":
    print("test5 is okay")
else:
    print("test5 is false")


print("------------------------------------------------------------------------------------")
#Задание 3

#test1
st = "students.spam@yandex.ru"
match = re.search(r'([a-z0-9._]+)@([a-z.]+\.[a-z]+)', st) 
itg1 = match[0] if match else 'Not found'
if itg1 == st:
    itg = re.split(r'@', itg1)[1]
else:
    itg = "Fail!"
if itg == "yandex.ru":
    print("test1 is okay")
else:
    print("test1 is false")

#test2
st = "example@example"
match = re.search(r'([a-z0-9._]+)@([a-z.]+\.[a-z]+)', st) 
itg1 = match[0] if match else 'Not found'
if itg1 == st:
    itg = re.split(r'@', itg1)[1]
else:
    itg = "Fail!"
if itg == "Fail!":
    print("test2 is okay")
else:
    print("test2 is false")

#test3
st = "example@example.com"
match = re.search(r'([a-z0-9._]+)@([a-z.]+\.[a-z]+)', st) 
itg1 = match[0] if match else 'Not found'
if itg1 == st:
    itg = re.split(r'@', itg1)[1]
else:
    itg = "Fail!"
if itg == "example.com":
    print("test3 is okay")
else:
    print("test3 is false")

#test4
st = "example@@example.com"
match = re.search(r'([a-z0-9._]+)@([a-z.]+\.[a-z]+)', st) 
itg1 = match[0] if match else 'Not found'
if itg1 == st:
    itg = re.split(r'@', itg1)[1]
else:
    itg = "Fail!"
if itg == "Fail!":
    print("test4 is okay")
else:
    print("test4 is false")

#test5
st = "example@mail.com"
match = re.search(r'([a-z0-9._]+)@([a-z.]+\.[a-z]+)', st) 
itg1 = match[0] if match else 'Not found'
if itg1 == st:
    itg = re.split(r'@', itg1)[1]
else:
    itg = "Fail!"
if itg == "mail.com":
    print("test5 is okay")
else:
    print("test5 is false")