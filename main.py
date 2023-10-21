book_path = 'books/frank.txt'

def get_book_text(path):
  with open(path) as f:
    return f.read()

def get_num_words(text):
  words = text.split()
  return len(words)

def get_num_letters(text):
  chars = {}
  for c in text:
      lowered = c.lower()
      if lowered in chars:
          chars[lowered] += 1
      else:
          chars[lowered] = 1
  return chars

# take the second element for sort
def take_second(elem):
    return elem[1]

def main():
  print(f"--- Begin report of {book_path} ---")
  file_content = get_book_text(book_path)
  count_words = get_num_words(file_content)
  print(f"{count_words} words found in the document")
  count_chars = get_num_letters(file_content)
  new_dict = dict(sorted(count_chars.items(), key=take_second, reverse=True))
  print("")
  for char in new_dict:
    if char.isalpha():
      print(f"The {char} character was found {new_dict[char]} times")
  print("--- End report ---")

main()




