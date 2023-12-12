translator = {
    'яблоко': 'apple',
    'солнце': 'sun',
    'сегодня': 'today',
    'привет': 'hi',
    'здравствуйте': 'hello',
    'пока': 'bye',
    'до свидания': 'good bye',
    'в': 'in',
    'на': 'on',
    'человек': 'human',
    'трава': 'grass',
    'страна': 'country',
    'идти': 'go',
    'бежать': 'run',
    'магазин': 'shop',
    'видеть': 'see',
    'понимать': 'understand',
    'бегать': 'run',
    'веселье': 'fun',
    'хлеб': 'bread',
    'луна': 'moon',
    'погода': 'weather',
    'хорошо': 'good'
}

rus_str = input("Введите строку на русском языке: ")
eng_str = ""

for word in rus_str.split():
    try:
        eng_str += translator[word] + " "
    except KeyError:
        eng_str += word + " "

print(eng_str)

