import pygame
from sys import exit
import random
import numpy as np
from core.scripts.config import SIZE, white, white_dark, black, black_light, size, color_main, additional_color, red_cheker, blue_cheker, green, blue_chosen, field_start, red_chosen, background_color
from core.scripts.buttons import Button
import pprint
import threading
import asyncio
import pygame
from pprint import pprint
import core.scripts.server as server


def start_server(loop, future):
    loop.run_until_complete(server.main(future))

def stop_server(loop, future):
    loop.call_soon_threadsafe(future.set_result, None)

field_with_figures = field_start
x = 0
y = 0

def check_winer():
    global field_with_figures
    if (
        all(x == 2 for x in field_with_figures[0][:4]) and
        all(x == 2 for x in field_with_figures[1][:4]) and
        all(x == 2 for x in field_with_figures[2][:4])
    ):
        print('Бот победил')
        pprint.pprint(field_with_figures)
        pygame.quit()
        exit()
    elif (
        all(x == 1 for x in field_with_figures[5][4:]) and
        all(x == 1 for x in field_with_figures[6][4:]) and
        all(x == 1 for x in field_with_figures[7][4:])
    ):
        print('игрок победил')
        pprint.pprint(field_with_figures)
        pygame.quit()
        exit()


def clear_field():
    global field_with_figures
    boardLength = 8
    for i in range(1,boardLength+1):
        for z in range(1,boardLength+1):
            if field_with_figures[i-1][z-1] == 9:
                field_with_figures[i-1][z-1] = 0  
            elif field_with_figures[i-1][z-1] == 8:
                field_with_figures[i-1][z-1] = 1
            elif field_with_figures[i-1][z-1] == 7:
                field_with_figures[i-1][z-1] = 2

def draw_field(gameDisplay: pygame.display, flag=0):
    global field_with_figures
    boardLength = 8
    gameDisplay.fill(background_color)
    pprint(field_with_figures)

    cnt = 0 
    buttons = []
    for i in range(1,boardLength+1):
        for z in range(1,boardLength+1):
            #check if current loop value is even
            if cnt % 2 == 0:
                if field_with_figures[i-1][z-1] == 9:
                    buttons.append(Button('', black, black_light, size*z, size*i, size, size, data = [i, z], image=green))
                elif field_with_figures[i-1][z-1] == 1:
                    buttons.append(Button('', black, black_light, size*z, size*i, size, size, data = [i, z], image=blue_cheker))
                elif field_with_figures[i-1][z-1] == 0:
                    buttons.append(Button('', black, black_light, size*z, size*i, size, size, data = [i, z]))
                elif field_with_figures[i-1][z-1] == 2:
                    buttons.append(Button('', black, black_light, size*z, size*i, size, size, data = [i, z], image=red_cheker))
                elif field_with_figures[i-1][z-1] == 8:
                    buttons.append(Button('', black, black_light, size*z, size*i, size, size, data = [i, z], image=blue_chosen))
                if field_with_figures[i-1][z-1] == 7:
                    buttons.append(Button('', black, black_light, size*z, size*i, size, size, data = [i, z], image=red_chosen))
                     
            else:
                if field_with_figures[i-1][z-1] == 9:
                    buttons.append(Button('', white, white_dark, size*z, size*i, size, size, data = [i, z],image=green))
                elif field_with_figures[i-1][z-1] == 1:
                    buttons.append(Button('', white, white_dark, size*z, size*i, size, size, data = [i, z],image=blue_cheker))
                elif field_with_figures[i-1][z-1] == 0:
                    buttons.append(Button('', white, white_dark, size*z, size*i, size, size, data = [i, z]))
                elif field_with_figures[i-1][z-1] == 2:
                    buttons.append(Button('', white, white_dark, size*z, size*i, size, size, data = [i, z],image=red_cheker))
                elif field_with_figures[i-1][z-1] == 8:
                    buttons.append(Button('', white, white_dark, size*z, size*i, size, size, data = [i, z],image=blue_chosen))
                elif field_with_figures[i-1][z-1] == 7:
                    buttons.append(Button('', white, white_dark, size*z, size*i, size, size, data = [i, z], image=red_chosen))
            cnt +=1
        #since theres an even number of squares go back one value
        cnt-=1

    buttons.append(Button('Выйти', color_main, additional_color, 1180, 100, 780, 100, data = [-1, -1]))
    return buttons

def game(gameDisplay: pygame.display, api):
    global field_with_figures, x, y
    move = bool(random.getrandbits(1))

    if (True if random.random() > 0.5 else False):
        print(move)
        field_with_figures = api.ai_move(field_with_figures) 
    buttons = draw_field(gameDisplay)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit() 
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.mouse_on_btn(*pygame.mouse.get_pos()):
                        if field_with_figures[button.get_data()[0]][button.get_data()[1]] in [1]:
                            x = button.get_data()[1]
                            y =  button.get_data()[0]
                            clear_field()
                            field = api.search_moves(field_with_figures, button.get_data()[1], button.get_data()[0])
                        

                            field_with_figures = field
                            buttons = draw_field(gameDisplay)
                        if field_with_figures[button.get_data()[0]][button.get_data()[1]] == 9:
                            field_with_figures[button.get_data()[0]][button.get_data()[1]] =  field_with_figures[y][x]
                            field_with_figures[y][x] = 0
                            check_winer()
                            clear_field()
                            field_with_figures = api.ai_move(field_with_figures)
                            check_winer()
                            buttons = draw_field(gameDisplay)
                        if button.text_btn == 'Выйти':
                            field_with_figures = field_start
                            return 'Одиночная игра'
        for button in buttons:
            button.draw(gameDisplay, *pygame.mouse.get_pos())
        pygame.display.flip()

def two_players_game(gameDisplay: pygame.display, api):
    global field_with_figures, x, y
    buttons = draw_field(gameDisplay)
    move = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                ar = []
                for button in buttons:
                    if button.mouse_on_btn(*pygame.mouse.get_pos()):
                        if button.text_btn == 'Выйти':
                            field_with_figures = field_start
                            return 'Мультиплеер'
                        if move:
                            ar = [1]
                        else:
                            ar = [2]

                        if field_with_figures[button.get_data()[0]][button.get_data()[1]] in ar:
                            x = button.get_data()[1]
                            y =  button.get_data()[0]
                            clear_field()
                            field = api.search_moves(field_with_figures, button.get_data()[1], button.get_data()[0])


                            field_with_figures = field
                            buttons = draw_field(gameDisplay)
                        if field_with_figures[button.get_data()[0]][button.get_data()[1]] == 9:
                            field_with_figures[button.get_data()[0]][button.get_data()[1]] =  field_with_figures[y][x]
                            field_with_figures[y][x] = 0
                            check_winer()
                            clear_field()
                            move = not(move)
                            buttons = draw_field(gameDisplay)
                        
        for button in buttons:
            button.draw(gameDisplay, *pygame.mouse.get_pos())
        pygame.display.flip()


def game_multiplayer(gameDisplay: pygame.display, api):
    global field_with_figures, x, y
    buttons = draw_field(gameDisplay)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.mouse_on_btn(*pygame.mouse.get_pos()):
                        if field_with_figures[button.get_data()[0]][button.get_data()[1]] == 1:
                            x = button.get_data()[1]
                            y =  button.get_data()[0]
                            clear_field()
                            field = api.search_moves(field_with_figures, button.get_data()[1], button.get_data()[0], 0)

                            field_with_figures = field
                            buttons = draw_field(gameDisplay, 1)
                        if field_with_figures[button.get_data()[0]][button.get_data()[1]] == 9:
                            field_with_figures[button.get_data()[0]][button.get_data()[1]] =  field_with_figures[y][x]
                            field_with_figures[y][x] = 0
                            check_winer()
                            clear_field()
                            field_with_figures = api.ai_move(field_with_figures)
                            check_winer()
                            buttons = draw_field(gameDisplay, 1)
                        if button.text_btn == 'Выйти':
                            return 'Одиночная игра'
        for button in buttons:
            button.draw(gameDisplay, *pygame.mouse.get_pos())
        pygame.display.flip()

def WebSocket_game_server(gameDisplay: pygame.display, api):
    websock = None
    loop = asyncio.get_event_loop()
    future = loop.create_future()
    thread = threading.Thread(target=start_server, args=(loop, future))
    thread.start()
    
    global field_with_figures, x, y
    buttons = draw_field(gameDisplay)
    buttons.append(Button('Сервер', color_main, additional_color, 1180, 300, 780, 100, data = [-1, -1]))
    move = False
    while True:
        for event in pygame.fastevent.get():
            if event.type == pygame.QUIT:
                print("Stoping event loop")
                print("Waiting for termination")
                stop_server(loop, future)
                thread.join()
                print("Shutdown pygame")
                pygame.quit()
                exit()
            if event.type == server.EVENTTYPE:
                    # вывод строки в консоль
                    field_with_figures = list(np.array([int(event.message[0][i]) for i in range(64)]).reshape((8, 8)))
                    websock = event.message[1]
                    buttons = draw_field(gameDisplay)
                    buttons.append(Button('Сервер', color_main, additional_color, 1180, 300, 780, 100, data = [-1, -1]))
                #field_with_figures = list(np.array([list(event).message.contents[i] for i in range(64)]).reshape((8, 8)))
                    move = not(move)
            if event.type == pygame.MOUSEBUTTONDOWN:
                ar = []
                for button in buttons:
                    if button.mouse_on_btn(*pygame.mouse.get_pos()):
                        if button.text_btn == 'Выйти':
                            field_with_figures = field_start
                            stop_server(loop, future)
                            thread.join()
                            return 'Мультиплеер'
                        if move:
                            ar = [1]

                        if field_with_figures[button.get_data()[0]][button.get_data()[1]] in ar:
                            x = button.get_data()[1]
                            y =  button.get_data()[0]
                            clear_field()
                            field = api.search_moves(field_with_figures, button.get_data()[1], button.get_data()[0])


                            field_with_figures = field
                            buttons = draw_field(gameDisplay)
                            buttons.append(Button('Сервер', color_main, additional_color, 1180, 300, 780, 100, data = [-1, -1]))
                        if field_with_figures[button.get_data()[0]][button.get_data()[1]] == 9:
                            field_with_figures[button.get_data()[0]][button.get_data()[1]] =  field_with_figures[y][x]
                            field_with_figures[y][x] = 0
                            check_winer()
                            clear_field()
                            move = not(move)
                            buttons = draw_field(gameDisplay)
                            buttons.append(Button('Сервер', color_main, additional_color, 1180, 300, 780, 100, data = [-1, -1]))
                            asyncio.run(server.send_map(list(np.array(field_with_figures).flatten()), websock))
                            move = False
        for button in buttons:
            button.draw(gameDisplay, *pygame.mouse.get_pos())
        pygame.display.flip()

                        

def WebSocket_game_client(gameDisplay: pygame.display, api):
    global field_with_figures, x, y
    buttons = draw_field(gameDisplay)
    buttons.append(Button('Клиент', color_main, additional_color, 1180, 300, 780, 100, data = [-1, -1]))
    move = True
    while True:
        for event in pygame.fastevent.get():
            if event.type == pygame.QUIT:
                print("Stoping event loop")
                print("Waiting for termination")
                print("Shutdown pygame")
                pygame.quit()
                exit()
            if event.type == server.EVENTTYPE:
                    # вывод строки в консоль
                field_with_figures = event.message

                #field_with_figures = list(np.array([list(event).message.contents[i] for i in range(64)]).reshape((8, 8)))
                move = not(move)
                buttons = draw_field(gameDisplay)
                buttons.append(Button('Клиент', color_main, additional_color, 1180, 300, 780, 100, data = [-1, -1]))
            if event.type == pygame.MOUSEBUTTONDOWN:
                ar = [1]
                for button in buttons:
                    if button.mouse_on_btn(*pygame.mouse.get_pos()):
                        if button.text_btn == 'Выйти':
                            field_with_figures = field_start

                            return 'Мультиплеер'
                        if move:
                            ar = [2]

                        if field_with_figures[button.get_data()[0]][button.get_data()[1]] in ar:
                            x = button.get_data()[1]
                            y =  button.get_data()[0]
                            clear_field()
                            field = api.search_moves(field_with_figures, button.get_data()[1], button.get_data()[0])


                            field_with_figures = field
                            buttons = draw_field(gameDisplay)
                            buttons.append(Button('Клиент', color_main, additional_color, 1180, 300, 780, 100, data = [-1, -1]))
                        if field_with_figures[button.get_data()[0]][button.get_data()[1]] == 9:
                            field_with_figures[button.get_data()[0]][button.get_data()[1]] =  field_with_figures[y][x]
                            field_with_figures[y][x] = 0
                            check_winer()
                            clear_field()
                            move = not(move)
                            buttons = draw_field(gameDisplay)
                            buttons.append(Button('Клиент', color_main, additional_color, 1180, 300, 780, 100, data = [-1, -1]))
                            server.client(field_with_figures)
        for button in buttons:
            button.draw(gameDisplay, *pygame.mouse.get_pos())
        pygame.display.flip()