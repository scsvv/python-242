from variables import text

text = text.split(' ')

new_text = list()
longest_word = ''
vowels = ["", 0] 

for word in text:
    word = word.replace(',', '').replace('.', '').replace('\n', '')
    new_text.append(word)

    if len(word) > len(longest_word):
        longest_word = word

    counting = word.count('a') + word.count('e') + word.count('i') + word.count('o') + word.count('u') + word.count('y')
    if counting > vowels[1]:
        vowels[0], vowels[1] = word, counting

text = new_text
del new_text

print(text)

print(f'Количество слов в текстe: {len(text)}')
print(f'Самое длинное слово в тексте имеет {len(longest_word)} букв и это слово {longest_word}')
print(f'Найбольшее количество гласных букв используется  {vowels[1]} букв и это слово {vowels[0]}')