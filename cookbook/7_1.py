def func(x: int, *args, y: str, **kwargs) -> None:
    print(x)
    print(args)
    print(y)
    print(kwargs)


a = 8
func(10, 'str', a, 20.2, y='linbao', size='large', quantity=6)

print(func.__annotations__)
