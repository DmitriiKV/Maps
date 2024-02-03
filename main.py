from pprint import pprint
import os
import sys
import pygame

import requests

dolg = input()
shir = input()
delta = input()
map_request = f"http://static-maps.yandex.ru/1.x/?ll={shir},{dolg}&spn={delta},{delta}&l=sat"

response_map = requests.get(map_request)

if not response_map:
    print("ERROR")
    print(map_request)
    print(response_map.status_code, response_map.reason)
    sys.exit(1)

map_file = "map.png"
with open(map_file, 'wb') as file:
    file.write(response_map.content)
    print(file)

pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()
os.remove(map_file)
