import tiktoken

encoding = tiktoken.get_encoding("cl100k_base")

text = "Hello, how are you?"
tokens = encoding.encode(text)

print("Tokens:", tokens)
print("Token count:", len(tokens))

decoded = encoding.decode([9906, 11, 1268, 527, 499, 30])
print("Decode:", decoded)