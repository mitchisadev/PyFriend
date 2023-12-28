import cv2
import screeninfo

class Display: # this obj is meant to control the screen display

    happy = cv2.imread('face-happy.png', cv2.IMREAD_ANYCOLOR)
    sad = cv2.imread('face-sad.png', cv2.IMREAD_ANYCOLOR)
    angry = cv2.imread('face-angry.png', cv2.IMREAD_ANYCOLOR)

    def __init__(self) -> None:
        self.screen = screeninfo.get_monitors()[0]
        self.width = self.screen.width
        self.height = self.screen.height

    def show_full_screen_image(self, name, image): #makes image full screen 
        cv2.destroyAllWindows()
        cv2.namedWindow(name, cv2.WINDOW_NORMAL)
        cv2.moveWindow(name, self.screen.x - 1, self.screen.y - 1)
        cv2.setWindowProperty(name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow(name, image)
        cv2.waitKey(0)