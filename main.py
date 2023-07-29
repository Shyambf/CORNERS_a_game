import pygame

from core.scripts.config import SIZE
from core.scripts.menu import introductory_menu, multiplayer_menu, single_player, multiplayer_menu_create
from core.scripts.game import game, two_players_game, WebSocket_game_server, WebSocket_game_client
from core.scripts.api import Api
import asyncio

pygame.init()  
pygame.fastevent.init() 

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
clock.tick(60)

now_screen = 'start'
api = Api()
while True:
    if now_screen == 'start':
        now_screen = introductory_menu(screen)
    if now_screen == 'Мультиплеер':
        now_screen = multiplayer_menu(screen)
    if now_screen == 'Одиночная игра':
        now_screen = single_player(screen)
    if now_screen == 'Game':
        now_screen = game(screen, api)
    if now_screen == '2p':
        now_screen = two_players_game(screen, api)
    if now_screen == 'Создать':
        now_screen = WebSocket_game_server(screen, api)
    if now_screen == 'Подключиться':
        now_screen = WebSocket_game_client(screen, api)