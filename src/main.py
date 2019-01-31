import example_animation
import example_client
import objmanager
import time
import threading

def http_client_thread(objmgr):
    namelist = ['r','g','b']
    objlist = example_client.example_post('127.0.0.1:8000', '/', namelist)
    for i in range(10):
        objmgr.objlist = example_client.example_post('127.0.0.1:8000', '/', namelist)
        time.sleep(1)


if __name__ == '__main__':
    objmgr = objmanager.objmanager([])   

    t = threading.Thread(target=http_client_thread, args=(objmgr,)) 
    t.start()

    example_animation.create_animation(objmgr)
