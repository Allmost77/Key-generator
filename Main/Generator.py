import random
import string
def generate(key):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(key))
    return rand_string