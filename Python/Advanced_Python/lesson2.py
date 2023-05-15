class Program:
    language = 'Python'

    def say_hello():
        print(f'Hello from {Program.language}')

print(Program.__dict__)
Program.say_hello()
print(getattr(Program, 'say_hello'))
print(Program.__dict__['language'])
p = Program()
p.version = 4.0 # created an Instance variable using the object
print(p.__class__)
print(type(p))
if isinstance(p, Program):
    print(True)
else:
    print(False)

print(p.__dict__)


class MyClass:
    __class__ = str # here we mess around with the __class__ attribute
m = MyClass()
print(type(m))
print(m.__class__)
print(isinstance(m, str))
print(isinstance(m, MyClass))