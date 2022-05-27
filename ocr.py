import os
import pyautogui
import PIL
import easyocr

# image names
IMAGE_NAME = "screenshot"
IMAGE_PATH = '{0}.png'.format(IMAGE_NAME)

# lowest_price scale factors
lowest_price_width_factor = 7
lowest_price_height_factor = 10

def get_lowest_price(add_offer_pos, debug = True):
    # get screensize
    x2,y2 = pyautogui.size()
    x2,y2=int(str(x2)),int(str(y2))

    # change dimensions of screenshot to only fit the lowest price
    screenshot_width = x2 // lowest_price_width_factor
    screenshot_height = y2 // lowest_price_height_factor

    # save screenshot
    p = pyautogui.screenshot()
    p.save(IMAGE_PATH)

    # open image
    im = PIL.Image.open(IMAGE_PATH)

    # preprocess the image for OCR
    im = im.convert('L')                             # grayscale
    im = im.point(lambda x: 0 if x < 140 else 255)   # threshold (binarize)
    im = im.crop((add_offer_pos[0], add_offer_pos[1]+(y2/20), add_offer_pos[0]+screenshot_width, add_offer_pos[1]+screenshot_height))
    im.save(IMAGE_PATH, quality=100)

    text_reader = easyocr.Reader(['en']) #Initialzing the ocr

    # read the price
    results = text_reader.readtext(IMAGE_PATH)

    # delete the image once done 
    if debug == False:
        os.remove(IMAGE_PATH)

    # return the price (without currency symbol)
    # TODO: handle different currencies (NOT TESTED)
    for (bbox, text, prob) in results:
        if text != None and len(text) > 0:
            currency = text[-1]
            currency = currency.replace("0","@")
            currency_offset = 0
            # UNTESTED
            if "€" in currency:
                currency_offset = 120
            if "S" in currency or "$" in currency:
                currency_offset = 65
            return [int(text[:-1].replace(" ","")), currency_offset]