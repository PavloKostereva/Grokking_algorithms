#
# def countdown(i):
#     print(i)
#     if i<=1:
#         return
#     else:
#         countdown(i-1)
#
# countdown(100)

# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# n=10
# print(factorial(n))


def sum(lst):

    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sum(lst[1:])


lst=[1,2,3, 4]
print(sum(lst))