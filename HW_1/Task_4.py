# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
text = int(input())
if text == 1:
    print("x > 0 and y > 0")
elif text == 2:
    print("x < 0 and y > 0")
elif text == 3:
    print("x < 0 and y < 0")
elif text == 4:
    print("x > 0 and y < 0")
else:
    print("вы ввели неверный номер четверти")

