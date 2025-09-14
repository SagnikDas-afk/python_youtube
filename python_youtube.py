import speech_recognition as sr
import pyttsx3
import yt_dlp
from playsound import playsound
import os



# ======= Update this with your ffmpeg.exe path =======
ffmpeg_path = r"C:\Users\hp\Downloads\ffmpeg-8.0-essentials_build\bin\ffmpeg.exe"

def download_song(text):
    engine.say(f" Searching for: {text} on YouTube...")
    ydl_opts = {
        'format':'bestaudio/best',
        'outtmpl':'song.%(ext)s',
        'quiet': True,
        'ffmpeg_location':ffmpeg_path,  # specify FFmpeg location
        'postprocessors':[{
            'key':'FFmpegExtractAudio',
            'preferredcodec':'mp3',
            'preferredquality':'192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([f"ytsearch1:{text}"])
            print(" Downloaded as song.mp3")
        except Exception as e:
            print(" Failed to download:", e)

def play_song():
    filename = "song.mp3"
    if os.path.exists(filename):
        print("Playing song...")
        playsound(filename)
    else:
        print("Song file not found!")

if __name__ == "__main__":
    r=sr.Recognizer()

with sr.Microphone() as source:
    print("Listing ...")
    audio=r.listen(source)

try:
    text = r.recognize_google(audio)
    print("Transcription : ",text)
except:
    print("Didn't got it")
    text = input("Enter a song name: ")
engine = pyttsx3.init()
engine .runAndWait()
 
    
    # Remove old song file if exists
if os.path.exists("song.mp3"):
    os.remove("song.mp3")
    
download_song(text)
play_song()