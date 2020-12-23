
def nth_fib(n , cache=None):
    if not cache:
        cache = [0 for _ in range(n+1)]
    if n < 2:
        return n
    elif cache[n] > 0:
        return cache[n]
    else:
        cache[n] = nth_fib(n-1, cache) + nth_fib(n-2, cache)
        return cache[n]

print(nth_fib(6))
# runtime complexity = O(n)


def mul_o_twos(n, cache=None):
    if not cache:
        cache = [0 for _ in range(n+1)]
    else:
        cache[n] = mul_o_twos(n, cache) + mul_o_twos(n, cache)
        return cache[n]

print(mul_o_twos(2))