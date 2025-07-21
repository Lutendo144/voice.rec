import sounddevice
from scipy.io.wavfile import write

def record_audio(duration):
    fs = 44100
    print("Recording...")
    record_voice = sounddevice.rec(int(duration * fs), samplerate=fs, channels=2)
    sounddevice.wait()
    print("Finished recording.")
    return record_voice, fs

def save_audio(file_name, audio_data, sample_rate):
    print("Saving audio to", file_name)
    write(file_name, sample_rate, audio_data)
    print("Audio saved successfully.")

def main():
    duration = int(input("Enter the time duration in seconds: "))
    audio_data, sample_rate = record_audio(duration)
    file_name = "out.wav"
    save_audio(file_name, audio_data, sample_rate)
    print("Please check", file_name)

if __name__ == "__main__":
    main()
