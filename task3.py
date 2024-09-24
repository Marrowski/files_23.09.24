import pickle

shop = {
    'Computers': ['Asus', 'Micro-Star International', 'Dell', 'HewelettPackard'],
    'Monitors': ['AOC', 'Dell', 'LG', 'Samsung'],
    'Games': ['Assasin`s Creed', 'Dying Light', 'Minecraft', 'Sekiro'],
    'Films': ['Resident Evil', 'The Avengers', 'Alien', 'Hunter x Hunter'],
    'Vegetables': ['Pumpkin', 'Garlic', 'Onion', 'Cucumber', 'Radish']
}

serialized_data = pickle.dumps(shop)
print(serialized_data)

with open('shop_data.json', 'wb') as new_file:
    pickle.dump(shop, new_file)
