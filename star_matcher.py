import cv2
import numpy as np
from scipy.spatial import distance_matrix
from sklearn.metrics.pairwise import cosine_similarity


class StarMatcher:
    def __init__(self, image_path1, image_path2, threshold=50):
        self.star_coordinates1 = StarCoordinates(image_path1)
        self.star_coordinates2 = StarCoordinates(image_path2)
        self.coordinates1 = self.star_coordinates1.get_coordinates(threshold)
        self.coordinates2 = self.star_coordinates2.get_coordinates(threshold)

    def normalize_coordinates(self, coordinates):
        max_x = max(coord[0] for coord in coordinates)
        max_y = max(coord[1] for coord in coordinates)
        max_r = max(coord[2] for coord in coordinates)
        max_b = max(coord[3] for coord in coordinates)

        return [(coord[0] / max_x, coord[1] / max_y, coord[2] / max_r, coord[3] / max_b) for coord in coordinates]

    def match_stars(self, similarity_threshold=0.9):
        normalized_coordinates1 = self.normalize_coordinates(self.coordinates1)
        normalized_coordinates2 = self.normalize_coordinates(self.coordinates2)

        similarity_matrix = cosine_similarity(normalized_coordinates1, normalized_coordinates2)
        matched_stars = []

        for i in range(similarity_matrix.shape[0]):
            for j in range(similarity_matrix.shape[1]):
                if similarity_matrix[i, j] >= similarity_threshold:
                    matched_stars.append((self.coordinates1[i], self.coordinates2[j]))

        return matched_stars
