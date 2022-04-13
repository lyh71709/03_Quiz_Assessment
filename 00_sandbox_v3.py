import csv

# pokemon_list = []
# dataset = open("pokemon.csv")
# csvreader = csv.reader(dataset)
# for row in csvreader:
#     pokemon_list.append(row)
# dataset.close()

with open('pokemon.csv') as file:
    content = file.readlines()
pokemon_list = content[1:]
print(pokemon_list)