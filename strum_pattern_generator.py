from bpm_classification import BpmClassifier
from bpm_detector import BpmDetector
from pattern_mapper import PatternMapper
from response_dictionary import ResponseDictionary


class StrumPatternGenerator:

    @staticmethod
    def generate_pattern(song, time_signature):
        true_bpm = BpmDetector.detect_bpm(song)
        int_bpm = int(true_bpm)
        pattern = BpmClassifier.get_pattern(int_bpm, time_signature)
        mapper_map = PatternMapper.map(pattern)
        interval = (1000/(true_bpm/60.00))
        ResponseDictionary(interval, int_bpm, mapper_map)
        return ResponseDictionary(interval, int_bpm, mapper_map)
