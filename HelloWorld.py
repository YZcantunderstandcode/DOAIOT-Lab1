import random
import string

for thing in range(1000):
    print("Hello, World!")


    def generate_password(length=12):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        return password

    print(generate_password())


    random_number = random.randint(1, 100)
    print(f"Random number: {random_number}")