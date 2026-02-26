# stan_konta = input("Podaj stan konta: ")
# stan_konta = int(stan_konta) + 500*2
# print(stan_konta)

# x = 9
# y = x/2
# x = x**(1/2)
# print(y)
# print(x)

# temperature = 15
# happy = False
# if temperature > 10 or happy:
#     print("Idź na spacer")
# elif temperature > -10 and happy:
#     print("Zostań w domu, ale idź na balkon")
# else:
#     print("Zostań w domu")

# oceny = [5, 4, 3, 2, 1]

# # for i in range(len(oceny)):
# #     print(oceny[i], end=" ")

# # for ocena in oceny:
# #     print(ocena, end=" ")

# for i, ocena in enumerate(oceny):
#     if i%2 == 0 and ocena >= 3:
#         print(i, ocena)

# for i, ocena in enumerate(oceny):
#     oceny[i] += 1

# oceny.extend([5, 5, 5])
# oceny.insert(3, 6)

# oceny.sort()

# print(oceny)

# from copy import deepcopy


# oceny_all = [[1,2,3,4,5],[6,6,6],[3,4,3]]

# for student in oceny_all:
#     for ocena in student:
#         print(ocena, end=" ")
#     print()

# oceny2 = deepcopy(oceny_all)
# oceny2[0][0] = 10
# print(oceny_all)

# oceny = [5, 4, 3, 2, 1, 2, 4, 5]
# oceny_set = set(oceny)  #unikalne wartości z listy oceny
# print(oceny_set)

# oceny_2 = [3,4,5,6,3,2,1,3]
# oceny_2_set = set(oceny_2)
# print(oceny_set.difference(oceny_2_set))  #różnica zbiorów
# print(oceny_set.intersection(oceny_2_set))  #część wspólna zbiorów

# print(list(oceny_set))

oceny_slownik = {}
oceny_slownik["Marek"] = [5, 4, 3]
oceny_slownik["Ania"] = [5, 5, 5]
oceny_slownik["Kasia"] = [3, 4, 5]

print(oceny_slownik["Marek"])

for student, oceny in oceny_slownik.items():
    print(student, oceny)