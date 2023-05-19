import random

for x in range(3):
    betkokie_skaiciai = random.randint(1, 6);
    print(betkokie_skaiciai)
    if x == 5:
        print("Pralaimėjai!")
        break
    else:
        print("Laimėjai!")



 # Užduotis nr. 4
# print("Sugeneruoti skaiciai: ")
# for x in range(3):
#     rand_num = random.randint(1, 6)
#     print(rand_num)
#     if rand_num == 5:
#         print("Pralaimejai")
#         break
# else: print("Laimejai")