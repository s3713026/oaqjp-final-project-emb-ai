import unittest
from EmotionDetection import emotion_detector as em


class TestEmotionDetection(unittest.TestCase):
    def testjoy(self):
        result = em("I am glad this happened")
        self.assertEqual(result["dominant_emotion"],"joy")

    def test_anger(self):
        result = em("I am really mad about this")
        self.assertEqual(result["dominant_emotion"],"anger")
    
    def test_disgust(self):
        result = em("I feel disgusted just hearing about this")
        self.assertEqual(result["dominant_emotion"],"disgust")
    
    def test_sadness(self):
        result = em("I am so sad about this	")
        self.assertEqual(result["dominant_emotion"],"sadness")

    def test_fear(self):
        result = em("I am really afraid that this will happen")
        self.assertEqual(result["dominant_emotion"],"fear")
if __name__ == "__main__":
    unittest.main()