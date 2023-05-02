from PIL import ImageGrab
import keyboard
import numpy as np
import pyautogui

# TODO:
#  - Find all blue, red, and yellow
#  - Prioritize blue, red, and yellow
#  - Move to shape while tracking with cursor
#  - Stay on shape until its gone

# Constants
BLUE_PENTAGON_COLOR = (118, 141, 252)
RED_TRIANGLE_COLOR = (252, 118, 119)
YELLOW_SQUARE_COLOR = (255, 232, 105)


def find_closest_pixel(screenshot_np, color):
    pixels = np.where(np.all(screenshot_np == color, axis=-1))
    if len(pixels[0]) > 0:
        # initialize closest center and distance
        closest_shape = None
        closest_distance = float('inf')
        
        # loop through each pixel
        for i in range(len(pixels[0])):
            
            x, y = pixels[1][i], pixels[0][i]
            
            # calculate distance to target point
            distance = np.sqrt((x - 960)**2 + (y - 580)**2)
            
            # update closest shape and distance if necessary
            if distance < closest_distance:
                closest_shape = (x, y)
                closest_distance = distance
        
        return closest_shape
    
    return None


def move_cursor(x, y):
    pyautogui.keyUp('down')
    pyautogui.moveTo(x, y)


def all_keys_up():
    pyautogui.keyUp('down')
    pyautogui.keyUp('up')
    pyautogui.keyUp('left')
    pyautogui.keyUp('right')
    

def move_to_shape(x, y):
    if x > 1920/2:
        all_keys_up()
        pyautogui.keyDown('right')
    if  x < 1920/2:
        all_keys_up()
        pyautogui.keyDown('left')
    if y > 1080/2:
        all_keys_up()
        pyautogui.keyDown('down')
    if y < 1080/2:
        all_keys_up()
        pyautogui.keyDown('up')


def main():
    pyautogui.confirm("start diepbot?", "diepbot", buttons=["yes", "no"])
    
    while True:
        screenshot = ImageGrab.grab()
        print("screenshot captured")
        screenshot_np = np.array(screenshot)

        closest_blue_center = find_closest_pixel(screenshot_np, BLUE_PENTAGON_COLOR)
        if closest_blue_center:
            move_cursor(closest_blue_center[0], closest_blue_center[1])
            
            if (860 <= closest_blue_center[0] <= 1060) or (480 <= closest_blue_center[1] <= 780):
                move_to_shape(closest_blue_center[0], closest_blue_center[1])
            continue
        
        closest_red_center = find_closest_pixel(screenshot_np, RED_TRIANGLE_COLOR)
        if closest_red_center:
            move_cursor(closest_red_center[0], closest_red_center[1])
            
            if (860 <= closest_red_center[0] <= 1060) or (480 <= closest_red_center[1] <= 780):
                move_to_shape(closest_red_center[0], closest_red_center[1])
            continue
        
        closest_yellow_center = find_closest_pixel(screenshot_np, YELLOW_SQUARE_COLOR)
        if closest_yellow_center:
            move_cursor(closest_yellow_center[0], closest_yellow_center[1])
            
            if (860 <= closest_yellow_center[0] <= 1060) or (480 <= closest_yellow_center[1] <= 780):
                move_to_shape(closest_yellow_center[0], closest_yellow_center[1])
            continue
        
        print("No pixel found")

        if keyboard.is_pressed('q'):
            exit(0)
            
        pyautogui.keyDown('down')


if __name__ == "__main__":
    main()
