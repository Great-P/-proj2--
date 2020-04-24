import random

random_list = ['a', 'c', 'g', 'u']
random_seq = ''

for i in range(56):
    random_seq += random_list[random.randint(0, 3)]

print(random_seq.upper())
