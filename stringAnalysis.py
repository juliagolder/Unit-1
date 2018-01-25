#julia golder
#1/24/18
#stringAnalysis.py - 


text = input('Enter a sentence')
print
spaces = text.count(' ')
print('Your sentence has', spaces+1, 'words', (len(text)), 'characters', len(text)-spaces , 'letters')
character = input('What character would you like to search for?')
number_of_characters = text.count(character)
print('Your sentence has', number_of_characters , 'of the charcter', character) 
character.lower()
words = input('What word would you like to search for?')
number_of_words = text.count(words)
print('Your sentence has', number_of_words , 'of the word', words) 