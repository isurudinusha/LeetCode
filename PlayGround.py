short = "My Haley"
long = "My name is Haley"

for word in short:
    result = long.split(word)
result = [item for item in result if item]
print(result)

