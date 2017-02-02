#from pymouse import PyMouse
from time import sleep

from AppKit import NSEvent
from Quartz.CoreGraphics import CGEventCreateMouseEvent
from Quartz.CoreGraphics import CGEventPost
from Quartz.CoreGraphics import kCGEventMouseMoved
from Quartz.CoreGraphics import kCGEventLeftMouseDown
from Quartz.CoreGraphics import kCGEventLeftMouseDown
from Quartz.CoreGraphics import kCGEventLeftMouseUp
from Quartz.CoreGraphics import kCGMouseButtonLeft
from Quartz.CoreGraphics import kCGHIDEventTap
from Quartz.CoreGraphics import CGDisplayPixelsHigh

from time import sleep
#import os
import webbrowser
import subprocess

def mouseEvent(type, posx, posy):
        theEvent = CGEventCreateMouseEvent(
                    None, 
                    type, 
                    (posx,posy), 
                    kCGMouseButtonLeft)
        CGEventPost(kCGHIDEventTap, theEvent)

def mousemove(posx,posy):
        mouseEvent(kCGEventMouseMoved, posx,posy);

def mouseclick():
		x,y = position()
        # uncomment this line if you want to force the mouse 
        # to MOVE to the click location first (I found it was not necessary).
        #mouseEvent(kCGEventMouseMoved, posx,posy);
		mouseEvent(kCGEventLeftMouseDown, x,y);
		mouseEvent(kCGEventLeftMouseUp, x,y);

def position():
        loc = NSEvent.mouseLocation()
        return loc.x, CGDisplayPixelsHigh(0) - loc.y


sleep_time = .00025

def sign(number):
	if number>0:
		return 1
	elif number == 0:
		return 0
	else:
		return -1

#bresenham's line algorithm
def move_the_mouse(x1,y1):
  #m = PyMouse()

  x1 = int(x1)
  y1 = int(y1)

  pos = position()
  x0 = int(pos[0])
  y0=int(pos[1])

  if x1 == x0:
  	if y1 > y0:
  		iterr = range(y0,y1)
  	else:
  		iterr = reversed(range(y1,y0))
  	for y in iterr:
  		mousemove(x0,y)
  		sleep(sleep_time)

  else:

	  error = 0
	  deltax = float(x1 - x0)
	  deltay = float(y1 - y0)
	  slope = abs(deltay / deltax)

	  cury = y0

	  if x1 > x0:
	  	iterr = range(x0,x1)
	  else:
	  	iterr = reversed(range(x1,x0))

	  for x in iterr:
	  	mousemove(x,cury)
	  	sleep(sleep_time)
	  	error += slope
	  	while error >= .5:
	  		mousemove(x,cury)
	  		sleep(sleep_time)
	  		cury += sign(y1-y0)
	  		error -= 1

change_space = '''
osascript -e 'tell application "System Events" to key code 124 using control down'
'''
command_i = '''
osascript -e 'tell application "System Events" to key code 34 using command down'
'''

subprocess.call(change_space,shell=True)

num_photos = 221

for i in range(num_photos):
	sleep(1)
	subprocess.call(command_i,shell=True)
	sleep(1.5)
	move_the_mouse(715,38)
	mouseclick()
	sleep(1.5)
	move_the_mouse(1292,320)
	mouseclick()
	sleep(1.5)
	move_the_mouse(1387,708)
	mouseclick()
	sleep(1.5)
	move_the_mouse(459,316)
	mouseclick()
	sleep(1.5)
	move_the_mouse(670,180)
	mouseclick()
	sleep(1.5)
	move_the_mouse(1050,560)
	mouseclick()
	sleep(1.5)
	move_the_mouse(144,10)
	mouseclick()
	sleep(1.5)
	move_the_mouse(1376,241)
	mouseclick()