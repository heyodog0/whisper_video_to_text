import os
import yt_dlp
import whisper

# Download audio from YouTube URLs
def download_audio(url_file):
    with open(url_file, 'r') as file:
        urls = file.read().splitlines()
    
    ydl_opts = {
        'format': 'm4a/bestaudio/best',
        'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'm4a'}]
    }
    
    for url in urls:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

# Transcribe audio files
def transcribe_audio(directory):
    model = whisper.load_model("base")
    os.chdir(directory)
    
    for file in os.listdir():
        if file.endswith(".m4a"):
            result = model.transcribe(file, fp16=False)
            with open(f"{os.path.splitext(file)[0]}.txt", "w") as f:
                f.write(result["text"])

# Main execution
if __name__ == "__main__":
    url_file = 'path/to/url_file.txt'
    output_directory = 'path/to/output_directory'
    
    download_audio(url_file)
    transcribe_audio(output_directory)