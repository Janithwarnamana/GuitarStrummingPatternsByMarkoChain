import librosa


from os import path
from pydub import AudioSegment

class BpmDetector:

    @staticmethod
    def detect_bpm(_filename):
        src = "uploads/"+_filename
        y, sr = librosa.load(src)
        bpm, _ = librosa.beat.beat_track(y=y, sr=sr)
        return bpm


# filename = "Perfect.mp3"
# print(BpmDetector.detect_bpm(filename))

# filename = "uploads/05 - Perfect - (www.songspksongspk.link).mp3"
#
# # # files
# src = "transcript.mp3"
# dst = "uploads/Perfect.wav"
#
# # convert wav to mp3
# sound = AudioSegment.from_mp3(filename)
# sound.export(dst, format="wav")
