import random

def get_random_position(dim, min, max):
    pos = []
    for _ in range(dim):
        pos.append(random.randint(min, max))
    return pos

def get_obj_with_xy_position(name, min, max):
    pos = get_random_position(2, min, max)
    obj = {'name':name, 'x':pos[0], 'y':pos[1]}
    return obj

def get_obj_list_with_xy_position(nameList, min, max):
    objlist = []
    for prop in nameList:
        pos = get_random_position(2, min, max)
        obj = {'name':prop['name'], 'x':pos[0], 'y':pos[1], 'color':prop['color']}
        objlist.append(obj)
    return objlist

if __name__ == '__main__':
    namelist = [
            {'name':'a', 'color':'r'},
            {'name':'b', 'color':'g'},
            {'name':'c', 'color':'b'},
            {'name':'d', 'color':'y'},
            {'name':'e', 'color':'k'}
    ]
    
    objlist = get_obj_list_with_xy_position(namelist, 1, 100)
    print(objlist)
