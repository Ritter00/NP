from django import template

register = template.Library()
value = 'написать, что необходимо подушка изменить оценку на платформе за это задание сторис'

@register.filter(name='censor')
def censor(value):
    cens_words = [
        'сторис',
        'подушка',
        'вещей',
        'Джо',
    ]
    for word in cens_words:
        if word in value:
            value = value.replace(word, '_#&#!!*&$_')
    return value

