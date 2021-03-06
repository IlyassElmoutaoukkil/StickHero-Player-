from ppadb.client import Client as AdbClient
from PIL import Image
import numpy
import math
import time

client = AdbClient(host="127.0.0.1", port=5037)

devices = client.devices()

MyMobile=devices[0]
def Start():
    Screenshot=MyMobile.screencap()

    with open('screenshot.png','wb') as f:
        f.write(Screenshot)
    
    f.close()

    MyImage=Image.open('screenshot.png')

    MyImage=numpy.array(MyImage,dtype=numpy.uint8)

    PexilDistance=0;
    firstRow=True
    firstRowBorder=0
    lastRowBorder=0
    startWithBlackness=False
    StartPoint=0
    if(MyImage[1500][1][0]+MyImage[1500][1][1]+MyImage[1500][1][2]==0):
        startWithBlackness=True

    
    if(not startWithBlackness):
        for x in range(0,710):
            if(not (MyImage[1500][x][0]+MyImage[1500][x][1]+MyImage[1500][x][2]==0) and  (MyImage[1500][x+1][0]+MyImage[1500][x+1][1]+MyImage[1500][x+1][2]==0)):
                StartPoint=x+1
                break
            

    for x in range(StartPoint,710):
        
        if(MyImage[1500][x][0]+MyImage[1500][x][1]+MyImage[1500][x][2]==0 and not (MyImage[1500][x+1][0]+MyImage[1500][x+1][1]+MyImage[1500][x+1][2]==0)):
            if(firstRow):
                firstRowBorder=x+1
                firstRow=False
        elif (not (MyImage[1500][x][0]+MyImage[1500][x][1]+MyImage[1500][x][2]==0) and  (MyImage[1500][x+1][0]+MyImage[1500][x+1][1]+MyImage[1500][x+1][2]==0)):
            lastRowBorder=x+1
            break
        

    Pexils=lastRowBorder-firstRowBorder

    Swipe=(Pexils/0.6500000000)
    # 826.379974326059, 

    if(Pexils<3):
        Start()


    # MyMobile.shell('input touchscreen swipe 660 660 660 660 500')
    if(Pexils<120):
        MyMobile.shell('input touchscreen swipe 660 660 660 660 ' +str(int(Swipe)+20))
        print('[S] Distance is '+str(Pexils)+'| Swipe Time Is: '+str(int(Swipe+20)))
        time.sleep(1.9)
        Start()
    else:
        MyMobile.shell('input touchscreen swipe 660 660 660 660 ' +str(int(Swipe+8)))

        print('[B] Distance is '+str(Pexils)+'| Swipe Time Is: '+str(int(Swipe+8)))
        time.sleep(2.3)
        Start()

    
    


Start()