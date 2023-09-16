from django.core.exceptions import ValidationError


def validatePng(image) -> bool:
    if not image.name.lower().endswith('.png'):
        raise ValidationError('A imagem deve ser obrigatoriamente ".png"')
