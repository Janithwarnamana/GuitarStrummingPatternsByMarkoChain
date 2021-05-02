from bpm_detector import BpmDetector

# time_signatures = ['3/4', '4/4']
# _ts_input = time_signatures[1]
# filename = "Perfect.mp3"
# _bpm_input = int(BpmDetector.detect_bpm(filename))
#
bpm_start = 60
step_size = 30
bpm_range = 0.0


class BpmClassifier:
    @staticmethod
    def get_pattern(bpm_input, ts_input):
        pattern = []
        if ts_input == "3/4":
            if bpm_input in range(bpm_start, bpm_start + step_size * 1):
                bpm_range = "First Set"
                pattern = [0, 1, 0]
                # print(bpm_range)
            elif bpm_input in range(bpm_start + step_size * 1, bpm_start + step_size * 2):
                bpm_range = "Second Set"
                pattern = [0, 1, 0]
                # print(bpm_range)
            elif bpm_input in range(bpm_start + step_size * 2, bpm_start + step_size * 3):
                bpm_range = "Third Set"
                pattern = [0, 1, 2]
                # print(bpm_range)
            elif bpm_input in range(bpm_start + step_size * 3, bpm_start + step_size * 4):
                bpm_range = "Fourth Set"
                pattern = [0, 1, 4]
                # print(bpm_range)
            else:
                bpm_range = "Out Of The Scope"
                # print(bpm_range)

        elif ts_input == "4/4":
            if bpm_input in range(bpm_start + step_size * 0, bpm_start + step_size * 1):
                bpm_range = "4/4 First Set"
                pattern = [0, 1, 2, 4]
            elif bpm_input in range(bpm_start + step_size * 1, bpm_start + step_size * 2):
                bpm_range = "4/4 Second Set"
                pattern = [0, 1, 2, 4]
            elif bpm_input in range(bpm_start + step_size * 2, bpm_start + step_size * 3):
                bpm_range = "4/4 Third Set"
                pattern = [0, 1, 2, 4]
            elif bpm_input in range(bpm_start + step_size * 3, bpm_start + step_size * 4):
                bpm_range = "4/4 Fourth Set"
                pattern = [0, 1, 2, 4]
            else:
                bpm_range = "Out Of The Scope"
                # print(bpm_range)
        return pattern
