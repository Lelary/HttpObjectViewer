import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import time

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
        xylist.append([obj["x"]+i, obj["y"]+i])
        
    return xylist

def create_scatter(objlist, ax):
    plotlist = objlist_to_plotlist(objlist)
    scatter = plt.scatter(plotlist["x"], plotlist["y"], color=plotlist["color"])
    #ax.add_patch(scatter)
    return scatter

def update_scatter(i, scatter, objlist):
    xylist = objlist_to_xylist(objlist, i)
    scatter.set_offsets(xylist)
    return scatter

def create_animation(objlist):
    fig = plt.gcf()
    ax = plt.axes(xlim=(0,100), ylim=(0,100))
    ax.set_aspect('equal')
    
    scatter = create_scatter(objlist, ax)
    anim = animation.FuncAnimation(fig, update_scatter, fargs=(scatter, objlist,), frames=30, interval=50,)

    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('test')
    plt.show();

if __name__ == '__main__':
    objlist = [
        {'name':'a', 'x':10, 'y':10, 'color':'g'},
        {'name':'b', 'x':20, 'y':20, 'color':'r'},
        {'name':'c', 'x':30, 'y':30, 'color':'b'},
        ]
    create_animation(objlist)


