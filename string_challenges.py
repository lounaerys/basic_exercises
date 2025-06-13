# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = 'аеёиоуыэюя'
vowels_count = 0

for letter in word.lower():
    if letter in vowels:
        vowels_count += 1

print(vowels_count)

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
words = sentence.split()

print(len(words))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
words = sentence.lower().split()
for letter in words:
    print(letter[0])

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
sentence_no_spaces = sentence.replace(' ', '')
words = sentence.split()

print(len(sentence_no_spaces) / len(words))
