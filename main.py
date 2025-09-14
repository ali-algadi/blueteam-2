my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_num = []
odd_num = []
#for num in my_list:
for i in range (len(my_list)):
    if my_list[i] % 2 == 0:
        even_num.append(i)
    else:
        odd_num.append(i)
print(even_num)
print(odd_num)