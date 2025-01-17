import io
import pprint
import re
word = 'tExt'
class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        punct = [',', '.', '=', '!', '?', ';', ':', ' - ']

        for filename in self.file_names:
            with open(filename, "r", encoding='utf-8') as file:
                content = file.read().lower()
                for j in punct:
                    content = content.replace(j, '')
                    contents = content.split()
                    all_words[filename] = contents
                return all_words


    def find(self, word):
        for name, contents in self.get_all_words().items():
            if word.lower() in contents:
                    result = name,contents.index(word.lower()) + 1
                    return result




    def count(self, word):
        for name, contents in self.get_all_words().items():
            if word.lower() in contents:
                rezult = name,contents.count(word.lower())
                return rezult



finder2 = WordsFinder('test_file.txt')
finder3 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder2.get_all_words()) # Все слова
print(finder3.get_all_words())
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего



