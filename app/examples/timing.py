import time


def c_to_f(c):
    return c * 9/5 +32


def time_it(fx, args):
    t0 = time.time()
    val = fx(*args)
    # time.sleep(1)
    t1 = time.time()
    print(t1-t0)
    return val


# Recursion, call himself in his body
# 3D printer prints 3D printer
# break big problem into small pieces

# a*b
# a*b = a + a*(b-1)
# def a_b(a, b):
#     if b == 1:
#         return a
#     else:
#         return a + a_b(a, b-1)

# n! = n * (n-1)!
# if n == 1, return 1
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)

# fab 0, 1, 1, 2, 3, 5, 8, ...
def fab(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fab(n-1) + fab(n-2)


print(fab(0))
# ------move tower
# def print_move(fr, to):
#     print(f"move from {fr} to {to}.")
#
#
# def towers(n, fr, to, spare):
#     if n == 1:
#         print_move(fr, to)
#     else:
#         towers(n-1, fr, spare, to)
#         towers(1, fr, to, spare)
#         towers(n-1, spare, to, fr)
#
# towers(3, "fr", "to", "spare")