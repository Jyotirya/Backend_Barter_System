import string, random

ALLOWED_CHARACTERS = string.ascii_letters + string.digits + "!@#$%"

def generate_id(length = 8):
    return ''.join(random.choices(ALLOWED_CHARACTERS, k=length))