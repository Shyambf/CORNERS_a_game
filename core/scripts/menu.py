import pygame
from sys import exit

from core.scripts.config import SIZE, color_main, additional_color, background
from core.scripts.buttons import Button, InputBox


def introductory_menu(screen: pygame.display):
    buttons = [Button('Мультиплеер', color_main, additional_color, 1280, 800, 580, 100),
               Button('Одиночная игра', color_main, additional_color, 1280, 650, 580, 100),
               Button('Выйти', color_main, additional_color, 1280, 950, 580, 100)]
    image = pygame.transform.scale(pygame.image.load(background), SIZE)
    while True:
        screen.blit(image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.mouse_on_btn(*pygame.mouse.get_pos()):
                        if button.text_btn == 'Выйти':
                            pygame.quit()
                            exit()
                        else:
                            return button.text_btn
        for button in buttons:
            button.draw(screen, *pygame.mouse.get_pos())
        pygame.display.flip()


def multiplayer_menu(screen: pygame.display):
    buttons = [Button('Поиск игры', color_main, additional_color, 1280, 800, 580, 100),
               Button('Создать', color_main, additional_color, 1280, 500, 580, 100),
               Button('Подключиться', color_main, additional_color, 1280, 650, 580, 100),
               Button('Назад', color_main, additional_color, 1280, 950, 580, 100),
               Button('2p', color_main, additional_color, 650, 950, 580, 100)]
    image = pygame.transform.scale(pygame.image.load(background), SIZE)
    while True:
        screen.blit(image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.mouse_on_btn(*pygame.mouse.get_pos()):
                        if button.text_btn == 'Выйти':
                            pygame.quit()
                            exit()
                        elif button.text_btn == 'Назад':
                            return 'start'
                        else: 
                            return button.text_btn
        for button in buttons:
            button.draw(screen, *pygame.mouse.get_pos())
        pygame.display.flip()

def single_player(screen: pygame.display):
    buttons = [Button('Загрузить', color_main, additional_color, 1280, 800, 580, 100),
               Button('Новая игра', color_main, additional_color, 1280, 650, 580, 100),
               Button('Назад', color_main, additional_color, 1280, 950, 580, 100)]
    image = pygame.transform.scale(pygame.image.load(background), SIZE)
    while True:
        screen.blit(image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.mouse_on_btn(*pygame.mouse.get_pos()):
                        if button.text_btn == 'Выйти':
                            pygame.quit()
                            exit()
                        elif button.text_btn == 'Назад':
                            return 'start'
                        elif button.text_btn == 'Новая игра':
                            return 'Game'
        for button in buttons:
            button.draw(screen, *pygame.mouse.get_pos())
        pygame.display.flip()

def multiplayer_menu_create(screen: pygame.display):
    input_boxes = [InputBox(SIZE[0]/2, SIZE[1]/2, 200, 75)]   
    buttons = [Button('Назад', color_main, additional_color, 1280, 950, 580, 100)]
    image = pygame.transform.scale(pygame.image.load(background), SIZE)
    while True:
        screen.blit(image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.mouse_on_btn(*pygame.mouse.get_pos()):
                        if button.text_btn == 'Назад':
                            return 'Мультиплеер'
            for box in input_boxes:
                box.handle_event(event)
        for box in input_boxes:
            box.update()
            box.draw(screen)
        for button in buttons:
            button.draw(screen, *pygame.mouse.get_pos())
        pygame.display.flip()
