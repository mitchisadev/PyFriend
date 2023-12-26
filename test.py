import sys 
import cv2
import screeninfo

screen = screeninfo.get_monitors()[0]
width = screen.width
height = screen.height

happy = cv2.imread('face-happy.png', cv2.IMREAD_ANYCOLOR)
sad = cv2.imread('face-sad.png', cv2.IMREAD_ANYCOLOR)
angry = cv2.imread('face-angry.png', cv2.IMREAD_ANYCOLOR)

def full_screen_image(name, sc, image): #makes image full screen 
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.moveWindow(name, sc.x - 1, sc.y - 1)
    cv2.setWindowProperty(name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow(name, image)

while True:
    ask = input('make daddy happy ;) \n')
    if ask == 'happy':  
        cv2.destroyAllWindows()  
        full_screen_image('pussy', screen, happy)
        cv2.waitKey(0)
    elif ask == 'angry':
        cv2.destroyAllWindows() 
        full_screen_image('pussy', screen, angry)
        cv2.waitKey(0)
    elif ask == 'sad':
        cv2.destroyAllWindows() 
        full_screen_image('pussy', screen, sad)
        cv2.waitKey(0)
    else:
        sys.exit()
    cv2.waitKey(0)
 