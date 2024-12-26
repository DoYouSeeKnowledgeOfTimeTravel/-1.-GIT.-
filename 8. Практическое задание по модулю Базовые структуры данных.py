# def average(*grds):
#     if not grds:  # Проверяем, переданы ли аргументы
#         return 0  # Если нет, возвращаем 0
#     total_sum = sum(grades[0])
#     count = len(grades[0])
#     return total_sum / count

# students = {'Johnny','Bilbo','Steve','Khendrik','Aaron'}
# students.update({'Pavel', 'Semen'})
# print(students)
# grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
# average_grade = (sum(grades[0]) / len(grades[0]),
#                  sum(grades[1]) / len(grades[1]),
#                  sum(grades[2]) / len(grades[2]),
#                  sum(grades[3]) / len(grades[3]),
#                  sum(grades[4]) / len(grades[4]))
# my_class = dict(zip(sorted(students), average_grade))
# print(my_class)

#grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
# result = average(grades)
# print("Среднее значение: ", result)

students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades = [[5,3,3,5,4], [2,2,2,3], [4,5,5,2], [4,4,3], [5,5,5,4,5]]

averages = []
for group in grades:
    average = sum(group) / len(group)
    averages.append(average)

result = dict(zip(sorted(students), averages))
print(result)

# for key,value in :
#     if name not in my_class:
#         my_class.update(f'{name}')
# print(my_class)

# if name in students:
#     print(f'{name} найден')

# def name(*imya):
#     if not imya:  # Проверяем, переданы ли аргументы
#         return 0  # Если нет, возвращаем 0
#     else:
#         return students
