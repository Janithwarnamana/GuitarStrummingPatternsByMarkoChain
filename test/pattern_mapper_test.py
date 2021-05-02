from pattern_mapper import PatternMapper
import unittest


class PatternMapperTest(unittest.TestCase):
    def test_map_whenNumericArrayWithElements_returnTextPattern(self):
        pattern = [0, 1, 2, 4]
        expected = ['D', '&', 'v', 'v^']
        actual = PatternMapper.map(pattern)
        self.assertEqual(actual, expected)

    def test_map_whenEmptyArray_returnEmptyArray(self):
        pattern = []
        expected = []
        actual = PatternMapper.map(pattern)
        self.assertEqual(actual, expected)
