calls=0
def count_calls():
    global calls
    calls+=1
def string_info(string):
     new=len(string)
     count_calls()
     return(string.lower() ,string.upper() ,new)
     string_info('arMagEddon')

def is_contains( string , list_to_search):
     a = string.lower()
     count_calls()
     for i in list_to_search:
        b = i.lower()
        if a == b:
             return True
     else:
         return False






print(string_info('Capybara'))
print(string_info('ArMageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycLe', ['recycling', 'cyclic'])) # No matches

print(calls)