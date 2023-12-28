from display import Display
from speech import Speech

def main():

    speechHandler = Speech(4)
    displayHandler = Display()

    result = speechHandler.record()
    
    match result:
        
        case 'happy':
            displayHandler.show_full_screen_image(result, displayHandler.happy)
        case 'sad':
            displayHandler.show_full_screen_image(result, displayHandler.sad)
        case 'angry':
            displayHandler.show_full_screen_image(result, displayHandler.angry)
    

if __name__ == '__main__':
    main()