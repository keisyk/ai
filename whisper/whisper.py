from openai import OpenAI
import requests

def download_mp3(url, save_path):
    try:
        response = requests.get(url, stream=True)
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        print(f"Downloaded MP3 file and saved to {save_path}")
    except Exception as e:
        print(f"Failed to download: {str(e)}")

url = "https://zadania.aidevs.pl/data/mateusz.mp3"
save_path = "whisper-file.mp3"

download_mp3(url, save_path)

client = OpenAI()

audio_file= open(save_path, "rb")
transcript = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file,
  response_format="text"
)

print(transcript)

