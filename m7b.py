def parse_student(str):
    student = {}
    student["id"] = int(str[0:8])
    student["name"] = str[8:-4]
    student["birthdate"] = str[-4:-2] + "/" + str[-2:]
    return student

def count_items(my_list):
    item_counts = {}

    for item in my_list:
        if item not in item_counts:
            item_counts[item] = my_list.count(item)

    return item_counts

def list_fighters(my_dict):
    my_set = set()
    for key in my_dict:
        my_set.add(key)
        my_set.update(my_dict[key].get("loss"))
        my_set.update(my_dict[key].get("win"))

    my_list = list(my_set)
    my_list.sort()
    return my_list