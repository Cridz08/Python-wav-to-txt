from pydub import AudioSegment
import os
import speech_recognition as sr
r = sr.Recognizer() # Recognize

def aud_to_wav(input_file, output_file):
    audio = AudioSegment.from_file(input_file)
    audio.export(output_file, format="wav")
    print(f"{input_file} is converted to {output_file}")

if __name__ == "__main__":
    input_file = "Motivational Speech.mp3"
    output_file = "Motivational Speech.wav"

    if not os.path.isfile(input_file):
        print(f"{input_file} does not exist")
    else:
        aud_to_wav(input_file, output_file)
    print("Loading...")


with sr.AudioFile("Motivational Speech.wav") as source: #Open and Read and close the audio file
    A_udio = r.listen(source)  #Record
    try:
        text = r.recognize_google(A_udio) # Convert Audio to text
        print(text)
    except:
        print("Sorry try again")