from guitar_data import guitar_strums


class PatternMapper:

    @staticmethod
    def map(numeric_array):
        if len(numeric_array) > 0:
            pattern_array = [0 for i in range(len(numeric_array))]
            for i, val in enumerate(numeric_array):
                pattern_array[i] = guitar_strums[val]
            return pattern_array
        else:
            return []
