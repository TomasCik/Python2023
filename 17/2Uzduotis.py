
# def fibonaci_generatorius():
#     a = 0
#     b = 1
#
#     while True:
#         if a == 0:
#            print("0")
#         if b == 1:
#            print("1")
#
#         c = a + b
#         a = b
#         b = c
#         yield c
# gen = fibonaci_generatorius()
#
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))







def fibonaci(num = None):
    num = abs(num)

    if num == 0:
        print("0")
    elif num == 1:
        print("1")
    else:
        a = 0
        b = 1
        for x in range(1, num):
            c = a+b
            a = b
            b = c
        print(c)

# fibonaci(15)

gen = fibonaci()
#
print(next(gen))







# l = [0,1]
# # def fibonaci(n):
# #     n = abs(n)
# #     if n < len(l):
# #         print(l[n])
# #     else:
# #         for i in range(len(l), n+1):
# #             suma = l[i-1] + l[i-2]
# #             l.append(suma)
# #         print(l[n])
# #
# # fibonaci(3)
#













