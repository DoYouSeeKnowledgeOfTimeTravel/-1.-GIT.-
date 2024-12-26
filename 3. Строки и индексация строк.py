peremennaya = 'Arbiter'
print(peremennaya[0])
print(peremennaya[-6])
print(peremennaya[4:])
print(peremennaya[::-1])
if len(peremennaya) % 2 == 1:
    print(peremennaya[len(peremennaya) // 2:])
else:
    print('Число символов в тексте должно быть нечётным.')

# if len(peremennaya[2:]) % 2 == 0:
   # print(peremennaya[2:])

# else:
   # print('Число символов в тексте должно быть нечётным.')

# print(example[len(example) // 2:])