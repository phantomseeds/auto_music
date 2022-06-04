import win32api
import win32con
import time

# 针对 everyonepiano 无法读取 pynput 的模拟输入，改用 win32api 实现

key_map = {
    "1": 50, "2": 51, "3": 52, "4": 53, "5": 54, "6": 55, "7": 56,
    "A": 65, "B": 66, "C": 67, "D": 68, "E": 69, "F": 70, "G": 71, "H": 72, "I": 73, "J": 74,
    "K": 75, "L": 76, "M": 77, "N": 78, "O": 79, "P": 80, "Q": 81, "R": 82, "S": 83, "T": 84,
    "U": 85, "V": 86, "W": 87, "X": 88, "Y": 89, "Z": 90,
    'ENTER': 13, 'SHIFT': 16, 'CTRL': 17,'ALT': 18,'SPACE': 32}

keyboard_map=[
    ['A', 'S', 'D', 'F', 'G', 'H', 'J']
    ,['Q', 'W', 'E', 'R', 'T', 'Y', 'U']
    ,['1', '2', '3', '4', '5', '6', '7']
]

play_file='./千本樱.ystone'

def release_key(key_code):
    win32api.keybd_event(key_code, win32api.MapVirtualKey(key_code, 0), 
                         win32con.KEYEVENTF_KEYUP, 0)
 
 
def press_key(key_code):
    win32api.keybd_event(key_code, win32api.MapVirtualKey(key_code, 0), 0, 0)

def press_and_release_key(key_code):
    press_key(key_code)
    release_key(key_code)

time.sleep(3)
with open(play_file) as f:
    lines=f.readlines()
    for x in lines:
        x=eval(x)
        if x[0]=='delay':
            time.sleep(x[1])
        elif x[0]=='note':
            for key in x[1]:
                press_and_release_key(key_map.get(keyboard_map[key[0]][key[1]]))


