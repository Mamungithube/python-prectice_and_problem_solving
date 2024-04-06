# mega = ([2,3,4],[6,7,8,9])
# print(type(mega))
# import pyautogui
# from time import sleep
# sleep(3)
# for i in range(0,3):
#     pyautogui.write('I Love you', interval=0.25)
#     pyautogui.press('enter')
# import cv2
# cam = cv2.VideoCapture(0)
# while True:
#     _,frame = cam.read()
#     cv2.imshow('my cam',frame)
#     cv2.waitKey(1)

# numbers = [10, 20, 30, 40, 50]
# print(numbers[-4:-1])
# numbers = [9, 15, 2, 36]
# numbers[1:4] = [20, 14, 36]
# print(numbers)
# person_info = {"name": "Sakib", "salary": 80000}
# value = person_info.get("salary")
# print(value)
# try:
#     result =20//5
# except:
#     print("error happened")
# finally:
#     print("finally here")
# from math import *
# result=ceil(5.00001)
# print(result)
# num = lambda a:a*a
# print(num(2**2))
# lst = []
# n = int(input("Enter the number of elements: "))
# for i in range(n):
#     ele = int(input())
#     lst.append(ele)
# print(lst)
import pyautogui

def draw(size):    
    for i in range(1, size + 1):
        pyautogui.write('#' * i)
        pyautogui.press('enter')
size = int(input())
draw(size)
#else

# import pyautogui as pag

# n = int(input())
# for i in range(1,n+1):
#     pag.write('#' * i)
#     pag.press('enter')