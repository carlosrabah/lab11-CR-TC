menu = {}

def reformat(data):
    if type(data) == list:
        for item in data:
            reformat(item)

    elif type(data) == dict:
        for key, value in data.items():
            if key == "type":
                item = value
                if item in menu:
                    pass
                else:
                    menu[item] = {}
            elif key == "name":
                name = value
                menu[item][name] = 0
            else:
                price = value
                menu[item][name] = price

    return menu

def nth(data, n):
    if n < 0:
        return None
    elif n == 0:
        return data[0]
    else:
        data = data[1]
        if data is None:
            return None
        else:
            return nth(data, n-1)

def where(data):
    count = 0

    if type(data) == dict:
        for key in data:
            if key == "Waldo":
                count += 1
            count += where(data[key])

    elif type(data) == list:
        for item in data:
            count += where(item)

    elif type(data) == str:
        if data == "Waldo":
            count += 1

    return count