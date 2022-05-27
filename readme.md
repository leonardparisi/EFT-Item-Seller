# Pre-requisites

- Install Python3.8
    - Run `pip -m virtualenv env
    - Open PowerShell in directory and run:
        ```
        ./env/Scripts/Activate.ps1 
        pip install -r requirements.txt
        ```
- Install [AutoHotkey](https://www.autohotkey.com/download/ahk-install.exe)

# Configuration

You must create your `config.ini` file. This file contains information about where certain UI elements are located. To do this, uncomment the following from the `config.py` file:
```
create_config({
    "open_add_offer_window": "1663 106",
    "close_offer_window": "1526 112",
    "place_offer": "1240 1086",
    "add_to_price_list": "1483 589",
    "currency_input": "1333 262",
    "add_price": "1273 1196"
})
```

My resolution might be different from yours so you need to record the coordinates of the UI elements in that config object. To do this, open the `macro.ahk` file by double clicking it. This should start the macro -- pressing CNTRL+T should print out the coordinates of your mouse. Make sure you have the game open and in focus. From there, hover over each UI element with your mouse and use the macro to record the mouse position. Enter the coordinates into the config object (with the format `X Y`). Once the argument for `create_config` has your updated information, run `create_config` with `python config.py`. After running it, you should see a `config.ini` file. Once that's done, delete/comment the call to `create_config` again so this doesnt get run every time the script accesses the config file. 

# Usage

- Run the runner.ahk file
- Press Cntrl+d, click on items you want to sell, right click to end selection