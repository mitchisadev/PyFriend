import speech_recognition as sr
from gtts import gTTS 

class Speech:

    def __init__(self, detect_length : int) -> None:
        self.detect_length = detect_length
        self.recognizer = sr.Recognizer() #audio recongnition
    
    def record(self) -> None:

        with sr.Microphone() as source:
            print("Adjusting noise ")
            self.recognizer.adjust_for_ambient_noise(source, duration = 1)
            print("Recording for {} seconds".format(self.detect_length))
            recorded_audio = self.recognizer.listen(source, timeout = self.detect_length)
            print("Done recording")

        try:
            print("Recognizing the text")
            return self.recognizer.recognize_google(recorded_audio, language="en-US")

        except Exception as ex:
            return ex
    