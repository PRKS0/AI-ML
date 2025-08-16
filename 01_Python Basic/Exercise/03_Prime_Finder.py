# def get_primes(n):
#     prime_list = []
#     for x in range(n):
#         if x<2:
#             continue
#         elif x==2:
#             prime_list.append(2)
#         elif x>2:
#             i = 2
#             while i<x:
#                 if x%i == 0:
#                     break
#                 if i == x - 1:
#                     prime_list.append(x)
#                 i += 1
                    
                
#     return prime_list

# print(get_primes(40))
# print("finished")

# def get_primes(n):
#     prime_list = []
#     for x in range(2, n):
#         for i in range(2, x):
#             if x%i == 0:
#                 break
#             if i == x-1:
#                 prime_list.append(x)
#     return prime_list

# print(get_primes(20))

# def get_primes(n):
#     prime_list = []
#     for x in range(2, n):
#         for i in range(2, x):
#             if x % i == 0:
#                 break
#         else:
#             prime_list.append(x)
#     return prime_list

# print(get_primes(20))