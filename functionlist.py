##CALLABLE COMMANDS

def pingcommand():
    return "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

def helprender(jsondata):
    return str(jsondata["commands"].keys()).replace("dict_keys(","").replace("])","]")
    
