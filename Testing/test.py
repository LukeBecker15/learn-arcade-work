# Create functions

# Why create functions?
# Make code easier to read
# Abstract our code
# Re-use
# Divide complex problem into a small one
# Make code easier to maintain


def print_hello():
    print("Hello")



def print_goodbye():
    print("Goodbye")

def print_number(my_number):
    print(my_number)

def add_numbers(a, b):
    return a + b


def main():
    print_hello()
    print_goodbye()
    print_number(12)
    print_number(6)
    result = add_numbers(12, 5)
    print(result)

if __name__ == "__main__":
    main()
# def add_numbers(a, b):
# print(a + b)
# add_numners(12, 5) this will print 17

def volume_cylinder(radius, height):
    pi = 3.14
    volume = pi * radius ** 2 * height
    return volume

result = volume_cylinder(3, 6) * 6
print(result)