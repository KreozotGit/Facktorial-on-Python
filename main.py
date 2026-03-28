num = int(input('Введите целое положительное число: '))
result = 1
if num >= 1:
    for i in range(1,num + 1):
        result *= i
    print(f'Факториал числа {num} равен {result}')
elif num == 0:
    print('Факториал нуля равен единице.')
else:
    print('Вы ввели отрицательное число.')