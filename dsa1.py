# def get_string(x, y):
#     z = str(x) + str(y)
#     print(str(z))
#
# get_string('hello','world')
#
# def polynomial(x, p):
#     p1 = pow(x, p)
#     y = 4 + 5 * p1
#     if x>=0:
#         print(y)
#     else:
#         y=0
#         print(y)
#
# polynomial(-1,2)

# def divisibles(N, p):
#     if N>=0:
#         l = [i for i in range(0, N+1) if i % p == 0]
#         print(l)
#     elif N<0:
#         l = [i for i in range(0, 21) if i % p == 0]
#         print(l)
#     else:
#         print('incorrect argument')
#
# divisibles(6, 4)\

# def divisibles(s, N, p):
#     if N>=0:
#         l = [i for i in range(s, N+1) if i % p == 0]
#         print(l)
#     elif N<0:
#         l = [i for i in range(s, 21) if i % p == 0]
#         print(l)
#     else:
#         print('incorrect argument')
#
# divisibles(4, 5, 2)

#import intertools

def divisibo(N):
    l = []
    for i in range(N):
        # for (j=)
        if (i % 5 == 0) & (i % 7 == 0) & (i % 11 == 0):
            l.append(i)
    print(l)


divisibo(386)

def primes_uptoN(N):

    L = []
    for num in range(2, N):
        prime = True
        for i in range(2, num):
            if num%i==0:
                prime = False
        if prime:
            print(num)


primes_uptoN(50)