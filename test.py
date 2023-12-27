import sys 
import cv2
import screeninfo
import speech_recognition as sr

screen = screeninfo.get_monitors()[0]
width = screen.width
height = screen.height

happy = cv2.imread('face-happy.png', cv2.IMREAD_ANYCOLOR)
sad = cv2.imread('face-sad.png', cv2.IMREAD_ANYCOLOR)
angry = cv2.imread('face-angry.png', cv2.IMREAD_ANYCOLOR)

recognizer = sr.Recognizer() #audio recongnition

def full_screen_image(name, sc, image): #makes image full screen 
    cv2.namedWindow(name, cv2.WINDOW_NORMAL)
    cv2.moveWindow(name, sc.x - 1, sc.y - 1)
    cv2.setWindowProperty(name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow(name, image)

while True:

    with sr.Microphone() as source:
        print("Adjusting noise ")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Recording for 4 seconds")
        recorded_audio = recognizer.listen(source, timeout=4)
        print("Done recording")

    try:
        print("Recognizing the text")
        ask = recognizer.recognize_google(recorded_audio, language="en-US")

        print("Decoded Text : {}".format(ask))

    except Exception as ex:
        print(ex)

    if ask == 'happy':  
        cv2.destroyAllWindows()  
        full_screen_image('happy', screen, happy)
        cv2.waitKey(0)
    elif ask == 'angry':
        cv2.destroyAllWindows() 
        full_screen_image('angry', screen, angry)
        cv2.waitKey(0)
    elif ask == 'sad':
        cv2.destroyAllWindows() 
        full_screen_image('sad', screen, sad)
        cv2.waitKey(0)
    else:
        sys.exit()
 