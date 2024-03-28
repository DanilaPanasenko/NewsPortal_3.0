from django import template


register = template.Library()

BAD_WORDS = [
    'сука',
    'мудак',
    'козел'
]

@register.filter()
def censor(value):
    text = str(value)
    for word in BAD_WORDS:
        text = text.replace(word, word[:1] + '*' * (len(word)-1))

    return text
