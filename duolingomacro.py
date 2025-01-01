import pyautogui as p
import random as r
import time as t
print('Make sure your tab is un-fullscreened, and you have Duolingo as your first tab!')
print('Please do not move your mouse or touch the keyboard anytime.')
rounds = int(input('How many times do you want us to do stories? (number)'))
i = 1
while i <= rounds:
    #duolingo opening
    if i == 1:
        p.click(x = 1750, y = 24)
    p.click(x = 150, y = 24)
    p.click(x = 137, y = 384)
    for i in range(20):
        p.press('down')
    p.click(x = 500, y = 1000)
    t.sleep(1)
    
    #opening the story
    story = r.randint(1,4)
    if story == 1:
        p.click(x = 800, y = 600)
        t.sleep(1)
        p.click(x = 800, y = 750)
        sussybaka = 7
    elif story == 2:
        p.click(x = 950, y = 550)
        t.sleep(1)
        p.click(x = 900, y = 750)
        sussybaka = 7
    elif story == 3:
        p.click(x = 800, y = 900)
        t.sleep(1)
        p.click(x = 900, y = 1060)
        sussybaka = 9
    elif story == 4:
        p.click(x = 900, y = 900)
        t.sleep(1)
        p.click(x = 900, y = 1060)
        sussybaka = 10

    #doing the story
    for lesgo in range (sussybaka):
        #pressing continue
        for asdfsadf in range(100):
            p.click(x = 1600, y = 1100)
            
        #doing the questions    
        for i in range(4):
            p.click(x = 600, y = i * 85 + 700)
            
        for i in range(4):
            p.click(x = 610, y = i * 100 + 610)
            
        for i in range(3):
            for j in range(22):
                p.click(x = j * 50 + 500, y = 750)
                
        for i in range(5):
            p.press(str(i + 1))
            for j in range(5):
                no1 = str(i + 1)
                if j == 4:
                    no2 = str(0)
                else:
                    no2 = str(j + 6)
                p.press(no1)
                p.press(no2)
        p.press('1')
    i += 1