from DogControllerSDK import DogControllerSDK
from constants import ACTION,GAIT
import time
with DogControllerSDK("http://localhost:5000",robot_ip="192.168.173.139") as dog:
    for i in range(2):
        dog.euler(1,0,0)
        time.sleep(1)
        dog.euler(-1,0,0)
        time.sleep(1)