from display import Display
from speech import Speech

def main():

    speechHandler = Speech(4)
    displayHandler = Display()

    result = speechHandler.record()
    
        
    if result == 'happy':
        displayHandler.show_full_screen_image(result, displayHandler.happy)
    elif result == 'sad':
        displayHandler.show_full_screen_image(result, displayHandler.sad)
    elif result == 'angry':
        displayHandler.show_full_screen_image(result, displayHandler.angry)
    

if __name__ == '__main__':
    main()