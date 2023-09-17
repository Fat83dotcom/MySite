from django.utils.text import slugify
from random import SystemRandom
import string


def randomLetters(k) -> str:
    return ''.join(SystemRandom().choices(
        string.ascii_lowercase + string.digits,
        k=k
    ))


def slugfyNew(string, k) -> str:
    return f'{slugify(string)}-{randomLetters(k)}'
