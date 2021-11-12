import regex

text = "Prodej bytu 2+kk 37 m² (Loft)"

result = regex.sub(r'\([^)]*\)', '', text)

print(result.split())