def checkFn(args):
    switcher = {
        "true" : True,
        "false" : False,
        "equal" : None
    }

    return switcher.get(args)