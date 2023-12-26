import random
import string

def generate(key):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(key))
    return rand_string

# Пример использования
generated_key = generate(8)
print("Generated key:", generated_key)
