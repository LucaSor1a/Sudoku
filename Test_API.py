import unittest
from unittest.mock import patch, MagicMock
from API import API


class TestAPI(unittest.TestCase):

    def test_API_9(self):
        mock_response = MagicMock()
        mock_response.json = MagicMock(return_value={"response": True,
                                       "size": "9", "squares":
                                                     [{"x":  0, "y":   1,
                                                      "value":  6},
                                                      {"x":  0, "y":  7,
                                                      "value":  1},
                                                      {"x":  0, "y":  8,
                                                      "value":  2},
                                                      {"x":  1, "y":  1,
                                                      "value":  2},
                                                      {"x":  1, "y":  4,
                                                      "value":  3},
                                                      {"x":  1, "y":  5,
                                                      "value":  9},
                                                      {"x":  1, "y":  7,
                                                      "value":  5},
                                                      {"x":  1, "y":  8,
                                                      "value":  6},
                                                      {"x":  2, "y":  1,
                                                      "value":  7},
                                                      {"x":  2, "y":  2,
                                                      "value":  4},
                                                      {"x":  2, "y":  5,
                                                      "value":  6},
                                                      {"x":  2, "y":  6,
                                                      "value":  3},
                                                      {"x":  3, "y":  0,
                                                      "value":  4},
                                                      {"x":  3, "y":  3,
                                                      "value":  6},
                                                      {"x":  3, "y":  4,
                                                      "value":  2},
                                                      {"x":  3, "y":  5,
                                                      "value":  8},
                                                      {"x":  3, "y":  8,
                                                      "value":  9},
                                                      {"x":  4, "y":  0,
                                                      "value":  7},
                                                      {"x":  4, "y":  2,
                                                      "value":  6},
                                                      {"x":  4, "y":  4,
                                                      "value":  5},
                                                      {"x":  4, "y":  6,
                                                      "value":  2},
                                                      {"x":  4, "y":  8,
                                                      "value":  3},
                                                      {"x":  5, "y":  0,
                                                      "value":  9},
                                                      {"x":  5, "y":  3,
                                                      "value":  4},
                                                      {"x":  5, "y":  8,
                                                      "value":  5},
                                                      {"x":  6, "y":  0,
                                                      "value":  2},
                                                      {"x":  6, "y":  2,
                                                      "value":  5},
                                                      {"x":  6, "y":  3,
                                                      "value":  1},
                                                      {"x":  6, "y":  6,
                                                      "value":  9},
                                                      {"x":  6, "y":  7,
                                                      "value":  8},
                                                      {"x":  7, "y":  1,
                                                      "value":  9},
                                                      {"x":  7, "y":  3,
                                                      "value":  3},
                                                      {"x":  7, "y":  4,
                                                      "value":  8},
                                                      {"x":  7, "y":  6,
                                                      "value":  5},
                                                      {"x":  7, "y":  7,
                                                      "value":  2},
                                                      {"x":  8, "y":  1,
                                                      "value":  4},
                                                      {"x":  8, "y":  2,
                                                      "value":  1},
                                                      {"x":  8, "y":  4,
                                                      "value":  9},
                                                      {"x":  8, "y":  6,
                                                      "value": 6},
                                                      {"x":  8, "y":  7,
                                                      "value": 3}]})
        with patch("API.requests.get", return_value=mock_response):
            result = API(9).Table()
        self.assertEqual(result, ["xxx4792xx",
                                  "627xxxx94",
                                  "xx4x6x5x1",
                                  "xxx6x413x",
                                  "x3x25xx89",
                                  "x968xxxxx",
                                  "xx3x2x956",
                                  "15xxxx823",
                                  "26x935xxx"])

    def test_API_4(self):
        mock_response = MagicMock()
        mock_response.json = MagicMock(return_value={"response": True,
                                                     "size": "4", "squares":
                                                     [{"x": 0, "y": 0,
                                                      "value": 4},
                                                      {"x": 0, "y": 2,
                                                      "value": 3},
                                                      {"x": 0, "y": 3,
                                                      "value": 1},
                                                      {"x": 1, "y": 1,
                                                      "value": 3},
                                                      {"x": 2, "y": 0,
                                                      "value": 3},
                                                      {"x": 2, "y": 1,
                                                      "value": 1},
                                                      {"x": 2, "y": 3,
                                                      "value": 2},
                                                      {"x": 3, "y": 1,
                                                      "value": 4}]})
        with patch("API.requests.get", return_value=mock_response):
            result = API(4).Table()
        self.assertEqual(result, ["4x3x",
                                  "x314",
                                  "3xxx",
                                  "1x2x"])


if __name__ == '__main__':
    unittest.main()
