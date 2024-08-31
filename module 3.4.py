def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if root_word.lower() in i.lower() or i.lower() in root_word.lower():
            same_words.append(i)
    return same_words


result1 = single_root_words('гиТ', 'грит', 'хабгит', 'бргитоа', 'болГит','БаГит')
result2 = single_root_words('рыба', 'рыбак', 'рыбный', 'рыбачить', 'рыбалка')
print(result1)
print(result2)