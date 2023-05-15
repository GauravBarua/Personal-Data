# Objects and Classes
class Person:
    pass

print(type(Person)) # <class 'type'>

# Even though this is an empty class it already has some attributes given by python
print(Person.__name__)

# creating the instance
p = Person()
print(type(p))   # <class '__main__.Person'>

print(p.__class__) # same as type

print(isinstance(p, Person))  # returns Boolean value (T or F)

# Defining Attributes in Classes
class MyClass:
    language = 'Python'
    version = '3.6'

# Retrieving Attribute values from Objects
# Using getattr():
print(getattr(MyClass, 'language'))  # If attribute exists it will return it
# print(getattr(MyClass, 'x'))  # If it doesn't exists then it will raise an AttributeError
print(getattr(MyClass, 'x', 'N/A')) # To by pass the error u can give a default value also

# Using dot notation (shorthand)
print(MyClass.language)


# Setting Attribute values in objects
setattr(MyClass, 'version', '3.7')
print(getattr(MyClass, 'version'))
setattr(MyClass, 'x', 100)
print(getattr(MyClass, 'x'))

# Where is the state stored? In a Dictionary
print(MyClass.__dict__)
print(type(MyClass.__dict__))  # <class 'mappingproxy'>

# Deleting Attributes
delattr(MyClass, 'x')  
# or
del MyClass.version
print(MyClass.__dict__)