#определяем сколько раз будет выполняться программа
n = int(input ("Введите количество пользователей:"))
k = 0
person = []
while k<n:
#определяем ФИ пользователя, родной город и город проживания
    person.append ("[" + input( "Введите своё имя:"))
    person.append (input( "Введите свою фамилию:"))
    person.append (input ( "Введите родной город:"))
    person.append (input ( "Введите город проживания:"))
#команды с числами - определяем ИМТ пользователя
    m = input( "Введите свой вес в кг:" )
    h = input( "Введите свой рост в м:" )
    I = float(m)/float(h)**2
    I = round (I, 2)
    if I<16:
        person.append (f"Ваш ИМТ: {I} - Выраженный дефицит массы тела]")
    if I>=16 and I<=18.5:
        person.append (f"Ваш ИМТ: {I} - Недостаточная масса тела]")
    if I>18.5 and I<25:
        person.append (f"Ваш ИМТ: {I} - Нормальная масса тела]")
    if I>=25 and I<=30:
        person.append (f"Ваш ИМТ: {I} - Избыточная масса тела]")
    if I>30 and I<35:
        person.append (f"Ваш ИМТ: {I} - Ожирение первой степени]")
    if I>=35 and I<=40:
        person.append (f"Ваш ИМТ: {I} - Ожирение второй степени]")
    if I>40:
        person.append (f"Ваш ИМТ: {I} - Ожирение третьей степени]")
    k +=1
    persons = tuple(person)
for el in persons:
    print (el)