import pyautogui
import cv2
import keyboard

from time import sleep

class Clicker:
  def __init__(self,img1,img2,speed):
   self.img1 = img1
   self.img2 = img2
   self.speed = speed
   pyautogui.FAILSAFE = True

  def collect_click(self):
    try:
     collectButton = pyautogui.locateOnScreen(self.img1,confidence=0.9)
     x,y = pyautogui.center(collectButton)
     pyautogui.click(x=x, y=y)
    except:
     if(pyautogui.position == (100,100)):
      pass
     else:
      pyautogui.moveTo(x=100,y=100)
     
     

  def create_click(self):
    try:
     createButton = pyautogui.locateOnScreen(self.img2,confidence=0.9)
     x,y = pyautogui.center(createButton)
     pyautogui.click(x=x, y=y)
    except:
     if(pyautogui.position() == (100,100)):
      pass
     else:
      pyautogui.moveTo(x=100,y=100)


if __name__ == "__main__":
 sleep(2)
 clicker = Clicker(img1="image/buda.png",img2="image/aoda.png",speed=0.4)

 running = True

 while running:
  if keyboard.is_pressed("l"):
    running = not running

  clicker.collect_click()
  clicker.create_click()
   
