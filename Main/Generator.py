from cryptography.fernet import Fernet
def generate():
    key = Fernet.generate_key()
    return key