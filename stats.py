def get_count_words(file_contents):
    return len(file_contents.split())

def get_characters_dictionary(file_contents):
  char_dictionary = {}
  for char in file_contents:
    char = char.lower()
    char_dictionary[char] = char_dictionary.get(char, 0) + 1
  return char_dictionary

def sort_characters_dictionary_and_count(characters_dictionary):
  sorted_dictionary_and_count = []
  for char, count in characters_dictionary.items():
    if char.isalpha():
      sorted_dictionary_and_count.append(f"{char}: {count}")
  sorted_dictionary_and_count.sort()
  return sorted_dictionary_and_count
