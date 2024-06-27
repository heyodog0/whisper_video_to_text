import os
import whisper
import moviepy.editor as mpe
from tqdm import tqdm

print("Loading Whisper model...")
model = whisper.load_model("medium")
directory = "/Users/heyodogo/Documents/cascoglab/[TEND0013] Videos"

os.chdir(directory)
print(f"Changed directory to: {directory}")

print("Converting .m4v files to .mp3...")
for file in os.listdir():
    if file.endswith(".m4v"):
        audio = mpe.VideoFileClip(file).audio
        audio.write_audiofile(f"{file}.mp3")

print("Transcribing .mp3 files...")
for file in tqdm(os.listdir(), desc="Transcribing"):
    if file.endswith(".mp3"):
        result = model.transcribe(file, fp16=False)
        with open(f"{file}.txt", "w") as f:
            f.write(result["text"])


print("Process completed successfully!")