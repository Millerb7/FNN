import librosa
import librosa.display
import matplotlib.pyplot as plt

def create_spectrogram(wav_file, save_path):
    # Load the audio file
    audio, sample_rate = librosa.load(wav_file, sr=None)

    # Generate the spectrogram
    S = librosa.feature.melspectrogram(y=audio, sr=sample_rate, n_mels=128, fmax=8000)

    # Convert to log scale
    S_dB = librosa.power_to_db(S, ref=np.max)

    # Plot and save the spectrogram
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(S_dB, sr=sample_rate, x_axis='time', y_axis='mel', fmax=8000)
    plt.colorbar(format='%+2.0f dB')
    plt.title('Mel-frequency spectrogram')
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

# Example usage
wav_file = '../data/train/wav'  # Replace with your wav file path
save_path = '../data/train/spectrogram'  # Replace with your save file path
create_spectrogram(wav_file, save_path)
