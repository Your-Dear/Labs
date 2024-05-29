import requests
import pyttsx3
import pyaudio
import random
from vosk import Model, KaldiRecognizer
import os
import json
import shutil
from tkinter import Tk, Label
from PIL import Image, ImageTk
from io import BytesIO
import sys

engine = pyttsx3.init()
engine.setProperty('rate', 150)


if not os.path.exists("model/vosk-model-ru-0.22"):
    print("Model directory not found. Please download and extract the model correctly.")
    sys.exit(1)

try:
    model = Model("model/vosk-model-ru-0.22")
except KeyboardInterrupt:
    print("Model loading was interrupted.")
    sys.exit(1)
except Exception as e:
    print(f"An error occurred while loading the model: {e}")
    sys.exit(1)

rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

def initial_instructions():
    engine.say("Welcome to the Rick and Morty Assistant.")
    engine.say("Please start by asking for a random character using the command, 'random'.")
    engine.say("After that, you can use commands like 'save' to save the character's image, 'episode' to hear about their first episode,")
    engine.say("'show' to display the character's image, 'resolution' to know the image resolution, 'quote' for a character quote, and 'location' to get the character's last known location.")
    engine.runAndWait()
    
def handle_random_character():
    response = requests.get("https://rickandmortyapi.com/api/character")
    data = response.json()
    random_character = random.choice(data['results'])
    engine.say(f"Random character is {random_character['name']}")
    engine.runAndWait()
    return random_character

def handle_save_image(character):
    image_url = character['image']
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        with open(f"{character['name']}.jpg", 'wb') as f:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, f)
        engine.say(f"Image saved as {character['name']}.jpg")
    else:
        engine.say("Failed to save the image.")
    engine.runAndWait()

def handle_first_episode(character):
    first_episode_url = character['episode'][0]
    response = requests.get(first_episode_url)
    episode_data = response.json()
    engine.say(f"The first episode is {episode_data['name']}")
    engine.runAndWait()

def handle_show_image(character):
    engine.say(f"Showing image of {character['name']}")
    engine.runAndWait()
    image_url = character['image']
    response = requests.get(image_url)
    image_data = response.content
    image = Image.open(BytesIO(image_data))
    root = Tk()
    root.title(character['name'])
    tkimage = ImageTk.PhotoImage(image)
    label = Label(root, image=tkimage)
    label.pack()
    engine.say(f"Showing image of {character['name']}")
    engine.runAndWait()
    root.mainloop()

def handle_image_resolution(character):
    image_url = character['image']
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        with open("temp_image.jpg", 'wb') as f:
            response.raw.decode_content = True
            shutil.copyfileobj(response.raw, f)
        with Image.open("temp_image.jpg") as image:
            engine.say(f"The resolution is {image.size[0]} by {image.size[1]} pixels")
            engine.runAndWait()
        os.remove("temp_image.jpg")
    else:
        engine.say("Failed to obtain image resolution.")
        engine.runAndWait()

def handle_fact(character):
    status = character['status']  
    species = character['species']  
    fact_message = f"{character['name']} is a {species} and is currently {status}."
    engine.say(fact_message)
    engine.runAndWait()

def handle_location(character):
    location_url = character['location']['url']
    if location_url:
        response = requests.get(location_url)
        location_data = response.json()
        engine.say(f"{character['name']} was last known to be at {location_data['name']}.")
    else:
        engine.say(f"No known location for {character['name']}.")
    engine.runAndWait()


initial_instructions()  
while True:
    data = stream.read(4000, exception_on_overflow=False)
    if rec.AcceptWaveform(data):
        result = json.loads(rec.Result())
        command = result.get('text', '')
        print(f"Recognized command: {command}")

        if command == "случайный":
            character = handle_random_character()

        elif command == "сохранить":
            if 'character' in locals():
                handle_save_image(character)
            else:
                engine.say("Please select a character first by saying 'random'.")
                engine.runAndWait()

        elif command == "эпизод":
            if 'character' in locals():
                handle_first_episode(character)
            else:
                engine.say("Please select a character first by saying 'random'.")
                engine.runAndWait()

        elif command == "показать":
            if 'character' in locals():
                handle_show_image(character)
            else:
                engine.say("Please select a character first by saying 'random'.")
                engine.runAndWait()

        elif command == "разрешение":
            if 'character' in locals():
                handle_image_resolution(character)
            else:
                engine.say("Please select a character first by saying 'random'.")
                engine.runAndWait()

        elif command == "местоположение":
            if 'character' in locals():
                handle_location(character)
            else:
                engine.say("Please select a character first by saying 'random'.")
                engine.runAndWait()
        
        elif command == "факт":  
            if 'character' in locals():
                handle_fact(character)
            else:
                engine.say("Please select a character first by saying 'random'.")
                engine.runAndWait()

        else:
            engine.say("Command not recognized. Please try again.")
            engine.runAndWait()
