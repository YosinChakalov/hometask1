# -- match case

# 1
# num = int(input())
# match num:
#     case 1:print("понедельник")
#     case 2:print("вторник")
#     case 3:print("среда")
#     case 4:print("четверг")
#     case 5:print("пятница")
#     case 6:print("суббота")
#     case 7:print("воскресенье")

# 2
# daytime = int(input())
# match daytime:
#     case 1:print("утро")
#     case 2:print("день")
#     case 3:print("вечер")
#     case 4:print("ночь")

# 3
# month = int(input())
# match month:
#     case 1:print("Январь")
#     case 2:print("Февраль")
#     case 3:print("Март")
#     case 4:print("Апрель")
#     case 5:print("Май")
#     case 6:print("Июнь")
#     case 7:print("Июль")
#     case 8:print("Август")
#     case 9:print("сентябрь")
#     case 10:print("Октябрь")
#     case 11:print("Ноябрь")
#     case 12:print("Декабрь")

# 4
# symb = input()
# numb1 = int(input())
# numb2 = int(input())
# match symb:
#     case "add":print("=",numb1+numb2)
#     case "subtract":print("=",numb1-numb2)
#     case "multiply":print("=",numb1*numb2)
#     case "divide":print("=",numb1//numb2)

# 5
# Mark = input()
# match Mark:
#     case "A":print("Отлично")
#     case "B":print("Хорошо")
#     case "C":print("Удовлетворительно")
#     case "D":print("Плохо")
#     case "F":print("Неудовлетворительно")

# -- If else

# 1
# EvenOrOdd = int(input())
# if EvenOrOdd%2==0:
#     print("чётное")
# elif EvenOrOdd%3==0:
#     print("нечётное")

# 2
# Amount = int(input())
# Currency = input()
# if Currency=="USD" or Currency=="usd":
#     print(Amount*87)
# elif Currency=="EUR" or Currency=="eur":
#     print(Amount*95)
# elif Currency=="RUB" or Currency=="rub":
#     print(Amount*1.2)

# 3
# Side1 = int(input())
# Side2 = int(input())
# Side3 = int(input())
# if Side1==Side2 and Side1==Side3:
#     print("Равносторонний")
# elif Side1!=Side2 and Side1==Side3 or Side1==Side2 and Side1!=Side3 or Side1!=Side2 and Side2==Side3:
#     print("Равнобедренный")
# else:
#     print("Разносторонний")

# 4
# num1 = int(input())
# num2 = int(input())
# symb = input()
# if num1==0 and num2==0:
#     print("divider and divisor can't be 0")
# elif symb=="+":
#     print("=",num1+num2)
# elif symb=="-":
#     print("=",num1-num2)
# elif symb=="*":
#     print("=",num1*num2)
# elif symb=="/":
#     print("=",num1/num2)

# 5
# Login = input()
# Password = int(input())
# if Login=="admin" and Password==12345:
#     print("вход успешен")
# elif Login!="admin" and Password==12345:
#     print("Нет такого пользователя")
# elif Login=="admin" and Password!=12345:
#     print("Неверный пароль")

# 6
# Numb = int(input())
# if Numb>=10 and Numb<=20 or Numb>=30 and Numb<=40:
#     print("OK")
# else:
#     print("Out of range")

# 7
# Year = int(input())
# if  Year%400==0:
#     print("високосный")
# elif Year%100==0:
#     print("не високосный")
# elif Year%4==0:
#     print("високосный")
# else:
#     print("не високосный")

# 8
# Age = int(input())
# if Age<0:
#     print("ошибка")
# elif Age<=2:
#     print("Младенец")
# elif Age<=12:
#     print("Ребёнок")
# elif Age<=17:
#     print("Подросток")
# elif Age<=59:
#     print("Взрослый")
# else:
#     print("Пенсионер")

# 9
# Amount = int(input())
# if Amount<10000 and Amount>20000:
#     print("=",Amount-(Amount*0.1))
# elif Amount>20000 and Amount<50000:
#     print("=",Amount-(Amount*0.2))
# else:
#     print("=",Amount-(Amount*0.3))

#10

# -- input output

# 1
# num1 = int(input())
# num2 = int(input())
# print("=",num1+num2)

# 2
# Length = int(input())
# width = int(input())
# print("Perimetre =",2*(Length+width))
# print("Area =",Length*width)

# 3
# Radius = int(input())
# print("Length =",2*3.14*Radius)
# print("Area =",3.14*(Radius*Radius))

# 4
# numb1 = int(input())
# numb2 = int(input())
# numb3 = int(input())
# print((numb1+numb2+numb3)//3)

# 5
# numb1 = int(input())
# numb2 = int(input())
# numb3 = int(input())
# print(numb3,numb2,numb1)

# 6
# Amount = int(input())
# print("sum in Rub =", Amount*100)

# 7
# numb1 = int(input())
# numb2 = int(input())
# if numb1>numb2:
#     print(numb1)
# elif numb2>numb1:
#     print(numb2)
# else:
#     print("they're equal")

# 8
# numb = int(input())
# percentage = int(input())
# print("Result =",(percentage/100)*numb)

# 9
# Base = int(input())
# Height = int(input())
# print("Area of triangle is",0.5*Base*Height)

#10
# time = int(input())
# hour = time//3600
# minute = (time//60)%10
# second = time%60
# print(f"{hour} hour {minute} minute {second} second")

#11
# time = int(input())
# hour = time//3600
# minute = time//60%60
# second = time%60
# print(f"{hour} hour {minute} minute {second} second")

# 12
# hour = int(input())
# minute = int(input())
# print((hour*60)+minute)

# 13
# hour1 = int(input())
# minute1 = int(input())
# hour2 = int(input())
# minute2 = int(input())
# print("time difference is",(hour2*60+minute2)-(hour1*60+minute1),"minutes")
