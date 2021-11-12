import regex

text = "13 739 348 Kč"

result = regex.sub(r'/\D+/g', '', text)

print(result)