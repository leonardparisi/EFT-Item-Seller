from configparser import ConfigParser
config = ConfigParser()

# reads value from config.ini as an array of ints
def load_int_array_from_config(config_parser, key):
    return [float(numeric_string) for numeric_string in config_parser.get("main",key).split()]

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
        "currency_dropdown": load_int_array_from_config(config, "currency_dropdown"),
        "current_offers_pos": load_int_array_from_config(config, "current_offers_pos"),
        "max_offers": int(config.get("main","max_offers"))
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
    config.set("main","current_offers_pos",config_data["current_offers_pos"])
    config.set("main","max_offers",config_data["max_offers"])
    

    with open('config.ini', 'w') as f:
        config.write(f)


# create_config({
#     "open_add_offer_window" : "0.649609375 0.07361111111111111",
#     "close_offer_window" : "0.58515625 0.0763888888888889",
#     "place_offer" : "0.4765625 0.75",
#     "add_to_price_list" : "0.567578125 0.4048611111111111",
#     "currency_input" : "0.520703125 0.18194444444444444",
#     "add_price" : "0.497265625 0.8305555555555556",
#     "currency_dropdown" : "0.583984375 0.18125",
#     "current_offers_pos" : "0.215625 0.0423611111111111",
#     "max_offers" : 2
# })