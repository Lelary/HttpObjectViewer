import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import time
import object_manager

def objlist_to_plotlist(objlist):
    plotlist = {
        "x":[],
        "y":[],
        "color":[],
        "alpha":[]
    };

    for obj in objlist:
        plotlist["x"].append(obj["x"])
        plotlist["y"].append(obj["y"])
        plotlist["color"].append(obj["color"])
    
    return plotlist
    
def objlist_to_xylist(objlist, i):
    xylist = []

    for obj in objlist:
        xylist.append([obj["x"], obj["y"]])
        
    return xylist

def create_scatter(objmanager, ax):
    plotlist = objlist_to_plotlist(objmanager.objlist)
    scatter = plt.scatter(plotlist["x"], plotlist["y"], color=plotlist["color"])
    #ax.add_patch(scatter)
    return scatter

def update_scatter(i, scatter, objmanager):
    xylist = objlist_to_xylist(objmanager.objlist, i)
    scatter.set_offsets(xylist)
    return scatter

def create_animation(objmanager):
    fig = plt.gcf()
    ax = plt.axes(xlim=(0,100), ylim=(0,100))
    ax.set_aspect('equal')
    
    scatter = create_scatter(objmanager, ax)
    anim = animation.FuncAnimation(fig, update_scatter, fargs=(scatter, objmanager,), frames=30, interval=50,)

    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('test')
    plt.show()

def test_thread(objmgr):
    for _ in range(10):
        for obj in objmgr.objlist:
            obj['x'] = obj['x'] + 10;
            
        time.sleep(1)

if __name__ == '__main__':
    import threading

    objlist = [
        {'name':'r', 'x':10, 'y':10, 'color':'g'},
        {'name':'g', 'x':20, 'y':20, 'color':'r'},
        {'name':'b', 'x':30, 'y':30, 'color':'b'},
        ]
        
    objmgr = object_manager.object_manager(objlist)   

    t = threading.Thread(target=test_thread, args=(objmgr,), daemon=True) 
    t.start()

    create_animation(objmgr)


