from screeninfo import get_monitors


def get_monitor_size() -> tuple:
    global SIZE, WIDTH, HEIGHT
    monitor = get_monitors()[0]
    SIZE = WIDTH, HEIGHT = monitor.width, monitor.height
    return SIZE


SIZE = WIDTH, HEIGHT = get_monitor_size()

IPADDRESS = "127.0.0.1"
PORT = 6677

color_main = (28, 172, 120)
additional_color = (186, 184, 108)
background_color = (18, 53, 36)
background = 'core/src/menu_bg1.jpg'
white = (255, 255, 255)
black = (0, 0, 0)

api_url = 'test/api_v1/'

white_dark = (150, 150, 150)
black_light = (100, 100, 100)
size = 110

red_cheker = 'core/src/red.png'
blue_cheker = 'core/src/pirpl.png'
hold = 'core/src/pyt.png'
red_chosen = 'core/src/red_chosen.png'
blue_chosen = 'core/src/pirpl_chosen.png'
green = 'core/src/green.png'
fonT = 'core/font.ttf'

field_start = [
	[ 1, 1, 1, 1, 0, 0, 0, 0],
	[ 1, 1, 1, 1, 0, 0, 0, 0],
	[ 1, 1, 1, 1, 0, 0, 0, 0],
	[ 0, 0, 0, 0, 0, 0, 0, 0],
	[ 0, 0, 0, 0, 0, 0, 0, 0],
	[ 0, 0, 0, 0, 2, 2, 2, 2],
	[ 0, 0, 0, 0, 2, 2, 2, 2],
	[ 0, 0, 0, 0, 2, 2, 2, 2] 
]