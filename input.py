from pynput import mouse
from pynput.mouse import Button

# class to help collect user clicks
class MouseTracker:
    def __init__(self):
        self.clicks = []

    def on_click(self, x, y, button, pressed):
        if button == Button.right:
            return False
        if(pressed):
            self.clicks.append([x, y])

    def on_scroll(self, x, y, dx, dy):
        print("Scrolling not supported yet!")
        return False

    def get_clicks(self):
        with mouse.Listener(on_click=self.on_click, on_scroll=self.on_scroll) as listener:
            listener.join()
        return self.clicks

# gets user clicks until the user right clicks or scrolls
def get_mouse_positions():
    return MouseTracker().get_clicks()

def create_nonblock_listener(on_scroll):
    return mouse.Listener(on_scroll=on_scroll)
