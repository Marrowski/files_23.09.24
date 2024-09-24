import shelve
import json

FILENAME = 'sites_dict'
with shelve.open(FILENAME) as file:
    file['YouTube'] = 'https://www.youtube.com/'
    file['TikTok'] = 'https://www.tiktok.com/uk-UA/'
    file['Instagram'] = 'https://www.instagram.com/'
    file['Rozetka'] = 'https://rozetka.com.ua/ua/'
    file['GitHub'] = 'https://github.com/'

with shelve.open(FILENAME) as file:
    for i in file.items():
        print(i)


dictionery_services = {
    'YouTube': 'https://www.youtube.com/',
    'TikTok': 'https://www.tiktok.com/uk-UA/',
    'Instagram': 'https://www.instagram.com/',
    'Rozetka': 'https://rozetka.com.ua/ua/',
    'GitHub': 'https://github.com/'
}

with open('services.json', 'w') as new_f:
    new_f.write(json.dumps(dictionery_services))