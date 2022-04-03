cubes = [x**3 for x in range (100) if x%2 !=0]
print('Создан список кубов нечетных чисел {}'.format(cubes))
my_numbers_sum = 0
my_numbers_sum_list = []

for i in range (len(cubes)):
    my_str = str(cubes[i])
    my_list = list(my_str)
    for i in range(len(my_list)):
        my_list[i] = int(my_list[i])
        # вычисляем сумму чисел
        my_numbers_sum = sum(my_list)
        print(my_numbers_sum)

        #сумма чисел делится нацело на 7
        if my_numbers_sum % 7 == 0:
            print('Сумма чисел, делящихся на 7 : ', my_numbers_sum)
            my_numbers_sum_list.append(my_numbers_sum)
print('Список чисел, делящихся на 7 (задание 1) : ', my_numbers_sum_list)

# добавляем 17 и заново вычесляем сумму тех чисел из списка, сумма которых делится нацело на 7

cubes = [(x**3)+17 for x in range(100) if x%2 ==0]
print('Создан список кубов нечетных чисел  {]'.format(cubes))
my_numbers_sum = 0
my_numbers_sum_list_even_numbers = []

for i in range(len(cubes)):
    my_str = str(cubes)
    my_list = list(my_str)
for i in range(len(my_list)):
    my_list[i] = int(my_list[i])
    #вычесляем сумму чисел
    my_numbers_sum = sum(my_list)
    print(my_numbers_sum)
    # сумму делим нацело на 7
    if my_numbers_sum % 7 == 0:
        print('Сумма чисел, делящихся на 7 (задание 1): ', my_numbers_sum_list)
        my_numbers_sum_list_even_numbers.append(my_numbers_sum)
print('Список чисел, делящихся на 7 (задание 1) : ', my_numbers_sum_list_even_numbers)





