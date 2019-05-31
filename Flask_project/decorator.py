def hello(func):
    def wrapper():
        print('HI')
        func()
        print('HI')
    return wrapper


@hello
def bye():
    print('BYE')
    print('BYE')

bye()