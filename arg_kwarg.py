

def total(*arg):
    return sum(arg)

def info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")


print(total(3,8,9))

info(name="Mou",age=26)