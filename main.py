from decorators import get_time

@get_time
def foo(n : int = 0):
    return n if n >= 100 else foo(n+1)
# Hello, world!
print(foo())