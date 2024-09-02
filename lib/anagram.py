# your code goes here!

class Anagram:
  def __init__(self,word):
    self.word = sorted(word.lower())

  def match(self,list_of_words):
    sorted_list_of_words = [sorted(possible_anagram.lower()) for possible_anagram in list_of_words]
    list_of_anagrams = [anagram for anagram in list_of_words if sorted_list_of_words[list_of_words.index(anagram)] == self.word]
    return list_of_anagrams
