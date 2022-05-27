from locale import currency
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

def sell_items(item_positions):
    mouse = Controller()
    keyboard_controller = keyboard.Controller()
    click_at_location(mouse, config['close_offer_window'])
    time.sleep(0.25)
    for position in item_positions:
        # wait until you can place an offer
        # TODO

        # click on 'add offer'
        click_at_location(mouse,config['open_add_offer_window'])
        print("open offer window")

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
        print("search prices")

        # get lowest price
        print("Reading lowest price")
        lowest_price = get_lowest_price(config['open_add_offer_window'])
        next_lowest_price = int(lowest_price[0] * .98)
        print("lowest price: {}".format(lowest_price[0]))

        if lowest_price != None:

            click_at_location(mouse, config['add_to_price_list'])

            click_at_location(mouse, config['currency_input'])

            keyboard_controller.type(str(next_lowest_price))

            click_at_location(mouse, config['currency_dropdown'])

            mouse.move(0, lowest_price[1])
            time.sleep(0.1)
            mouse.click(Button.left)
            time.sleep(0.1)

            click_at_location(mouse, config['add_price'])
            click_at_location(mouse, config['place_offer'])

    click_at_location(mouse, config['close_offer_window'])

def main():
    focus_game()
    item_positions = get_mouse_positions()
    sell_items(item_positions,)

main()