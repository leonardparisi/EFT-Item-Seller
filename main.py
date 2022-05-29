import pygetwindow
import time
from pynput.mouse import Button, Controller
from pynput import keyboard
from input import *
from ocr import *
from config import *

config = load_config()

def focus_game():
    pygetwindow.getWindowsWithTitle('EscapeFromTarkov')[0].activate()

def click_at_location(mouse, location, button = Button.left):
    mouse.position = location
    time.sleep(0.1)
    mouse.click(button)
    time.sleep(0.3)

def get_config_position(key):
    return get_relative_position(config[key])

def wait_until_can_list_item():
    offers_available = get_offers_available(get_config_position('current_offers_pos'),config['max_offers'])
    if offers_available > 0:
        return
    print("{}: Waiting for current offers to change...".format(offers_available))
    time.sleep(5)
    return wait_until_can_list_item()

def sell_items(item_positions):
    mouse = Controller()
    keyboard_controller = keyboard.Controller()
    click_at_location(mouse, get_config_position('close_offer_window'))
    time.sleep(0.25)
    for position in item_positions:
        wait_until_can_list_item()

        # click on 'add offer'
        click_at_location(mouse,get_config_position('open_add_offer_window'))

        # click on the item
        click_at_location(mouse,position)

        # right click it
        mouse.click(Button.right)
        time.sleep(.5)

        # click on filter by item
        mouse.move(10,70)
        time.sleep(0.5)
        mouse.click(Button.left)
        time.sleep(1)

        # get lowest price
        lowest_price = get_lowest_price(get_config_position('open_add_offer_window'))

        if lowest_price != None:
            next_lowest_price = int(lowest_price[0] * .98)

            click_at_location(mouse, get_config_position('add_to_price_list'))

            click_at_location(mouse, get_config_position('currency_input'))

            keyboard_controller.type(str(next_lowest_price))

            click_at_location(mouse, get_config_position('currency_dropdown'))

            mouse.move(0, lowest_price[1])
            time.sleep(0.1)
            mouse.click(Button.left)
            time.sleep(0.1)

            click_at_location(mouse, get_config_position('add_price'))
            click_at_location(mouse, get_config_position('place_offer'))
            print("Listed item...")
        else:
            print("Ignoring item...")
    click_at_location(mouse, get_config_position('close_offer_window'))

def kill_on_scroll(x, y, dx, dy):
    print("Killing program")
    exit(1)

def main():
    focus_game()
    create_nonblock_listener(kill_on_scroll).start()
    item_positions = get_mouse_positions()
    sell_items(item_positions,)

main()