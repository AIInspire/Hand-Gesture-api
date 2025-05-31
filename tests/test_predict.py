import unittest
import numpy as np
import sys
import os

# Add app/ to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from predict import predict_gesture, normalize_landmarks

class TestGestureModel(unittest.TestCase):

    def setUp(self):
        # Example: 21 hand landmarks (each has x, y, z) = 63 values
        self.raw_features = [
            239.69, 196.50, 4.57e-07, 257.55, 185.60, -0.0196, 268.26, 165.43, -0.0276,
            254.83, 151.53, -0.0335, 238.44, 149.77, -0.0393, 261.42, 136.81, -0.0200,
            275.22, 113.67, -0.0331, 282.60, 97.60, -0.0436, 287.21, 84.60, -0.0512,
            244.44, 132.11, -0.0217, 249.48, 103.70, -0.0314, 251.90, 84.30, -0.0408,
            252.84, 68.67, -0.0473, 229.33, 135.49, -0.0254, 226.06, 109.84, -0.0376,
            225.14, 92.36, -0.0492, 224.24, 77.77, -0.0567, 215.12, 145.81, -0.0306,
            202.49, 130.02, -0.0444, 194.20, 118.72, -0.0510, 187.23, 108.07, -0.0544
        ]

    def test_normalize_landmarks_shape(self):
        normalized = normalize_landmarks(self.raw_features)
        self.assertEqual(len(normalized), 63)
        self.assertIsInstance(normalized, list)

    def test_predict_output_type(self):
        encoded, label = predict_gesture(self.raw_features)
        self.assertIsInstance(encoded, (int, np.integer))
        self.assertIsInstance(label, str)

    def test_predict_valid_label(self):
        _, label = predict_gesture(self.raw_features)
        self.assertTrue(len(label) > 0)  # Non-empty label expected

if __name__ == "__main__":
    unittest.main()
