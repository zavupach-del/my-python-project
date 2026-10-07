words = [f"str{i}" for i in range(10)]
print(words)                         # ['str0', 'str1', ..., 'str9']

long_words = [word for word in words if len(word) > 5]
print(long_words)