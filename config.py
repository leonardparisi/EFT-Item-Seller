from configparser import ConfigParser
config = ConfigParser()

# reads value from config.ini as an array of ints
def load_int_array_from_config(config_parser, key):
    return [int(numeric_string) for numeric_string in config_parser.get("main",key).split()]

# loads entire config.ini file and puts it into a parsed dict
def load_config():
    config.read('config.ini')
    config_obj = {
        "open_add_offer_window": load_int_array_from_config(config, "open_add_offer_window"),
        "close_offer_window": load_int_array_from_config(config, "close_offer_window"),
        "place_offer": load_int_array_from_config(config, "place_offer"),
        "add_to_price_list": load_int_array_from_config(config, "add_to_price_list"),
        "currency_input": load_int_array_from_config(config, "currency_input"),
        "add_price": load_int_array_from_config(config, "add_price"),
        "currency_dropdown": load_int_array_from_config(config, "currency_dropdown")
    }
    return config_obj

# creates the config.ini file
def create_config(config_data):
    config.read('config.ini')
    config.add_section('main')
    config.set("main","open_add_offer_window",config_data["open_add_offer_window"])
    config.set("main","close_offer_window",config_data["close_offer_window"])
    config.set("main","place_offer",config_data["place_offer"])
    config.set("main","add_to_price_list",config_data["add_to_price_list"])
    config.set("main","currency_input",config_data["currency_input"])
    config.set("main","add_price",config_data["add_price"])
    config.set("main","currency_dropdown",config_data["currency_dropdown"])

    with open('config.ini', 'w') as f:
        config.write(f)


# create_config({
#     "open_add_offer_window": "1663 106",
#     "close_offer_window": "1498 110",
#     "place_offer": "1220 1080",
#     "add_to_price_list": "1453 583",
#     "currency_input": "1333 262",
#     "add_price": "1273 1196",
#     "currency_dropdown": "1495 261"
# })