def invert(dictionary = {}):
   dictionary_keys = dictionary.keys()
   dictionary_val = list(dictionary.values())
   dictionary_val.sort(reverse=True)
   dictionary = dict(zip(dictionary_keys,dictionary_val))
   return dictionary

my_dict = { 'apple': 1, 'b': 2, 'c': 3, 'dog': 4 }
inverted_dict = invert(my_dict)
print(inverted_dict)

my_other_dict = { 'a': 1, 'b': 2, 'c': 3 }
inverted_other_dict = invert(my_other_dict)
print(inverted_other_dict)

