import object_animation
import http_client
import object_manager
import time
import threading

def http_client_thread(objmgr):
    namelist = ['r','g','b']
    objmgr.objlist = http_client.query_objects('127.0.0.1:8000', '/', namelist)
    for _ in range(10):
        objmgr.objlist = http_client.query_objects('127.0.0.1:8000', '/', namelist)
        time.sleep(1)


if __name__ == '__main__':
    objmgr = object_manager.object_manager([])   

    t = threading.Thread(target=http_client_thread, args=(objmgr,), daemon=True) 
    t.start()

    object_animation.create_animation(objmgr)
