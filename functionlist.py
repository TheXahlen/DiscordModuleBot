##CALLABLE COMMANDS
def helprender(jsondata):
    return str(jsondata["commands"].keys()).replace("dict_keys(","").replace("])","]")
    
