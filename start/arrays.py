names = ["Jacek", "Paweł", "Jan", "Wiktor", "Bartosz", "Ania", "Dominika"]

for name in names:
    print(name)

print(names[2])
print(names[-1])
print(names[2:])
print(names[-4:-1])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 24, 5, 1, 2, 3]
maximum = numbers[0]
numbers.append(10)
numbers.insert(2, 10)
numbers.remove(7)
numbers.sort()

numbers2 = numbers.copy()
numbers2.clear()
print("list numbers2 =  " + str(numbers2))

print("how many items '1' in list? " + str(numbers.count(1)))

print("is 50 in numbers? " + str(50 in numbers))

for number in numbers:
    if number > maximum:
        maximum = number

print(maximum)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][1])

for row in matrix:
    for item in row:
        print(item)

print("------------------------- exercise with remove the repeat items ----------------------")

number_list = [1, 2, 315, 5, 1, 2, 3, 1, 3, 1, 23, 1, 1, 3, 1, 2, 3, 1, 14]
non_repeat_list = []
for item in number_list:
    if not item in non_repeat_list:
        non_repeat_list.append(item)
print(non_repeat_list)
