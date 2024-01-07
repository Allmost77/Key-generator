import random
import string
def generate(key_lenght, use_digits=True, use_special_chars=False):
    letters = string.ascii_lowercase
    if use_digits:
        letters += string.digits
    if use_special_chars:
        letters += string.punctuation

    rand_string = ''.join(random.choice(letters) for i in range(key_lenght))
    return rand_string