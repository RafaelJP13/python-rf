# Padrão
def soma(num1: int, num2: int, num3: int):
    return num1 + num2 + num3;

# Com args
def soma_args(*args: int) -> None:
    print(args)
    print(sum(args))

# Com kwargs
def greeting(**kwargs: object) -> None:
    name, age, city = kwargs.values()
    print(kwargs)
    print(f"Meu nome é {name}, tenho {age} anos, e moro em {city}!")

greeting(
    name= "Rafael",
    age= 20,
    city= "São Vicente",
)

