import cv2
import numpy as np
from skimage.measure import ransac
from skimage.transform import AffineTransform

class StarCoordinates:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        self.color_image = cv2.imread(image_path)

    def get_coordinates(self, dp=1, min_dist=50, param1=100, param2=30, min_radius=1, max_radius=50):
        gray = cv2.medianBlur(self.image, 5)
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp, min_dist, param1=param1, param2=param2, minRadius=min_radius, maxRadius=max_radius)
        
        coordinates = []
        if circles is not None:
            circles = np.uint16(np.around(circles))
            for circle in circles[0, :]:
                x, y, r = circle
                b = int(np.mean(self.image[y, x]))
                coordinates.append((x, y, r, b))

        return coordinates
    
   

class StarMatcher:
    def __init__(self, image_path1, image_path2, threshold=50):
        self.star_coordinates1 = StarCoordinates(image_path1)
        self.star_coordinates2 = StarCoordinates(image_path2)
        self.coordinates1 = self.star_coordinates1.get_coordinates(threshold)
        self.coordinates2 = self.star_coordinates2.get_coordinates(threshold)

    def ransac_homography(self, coords1, coords2, threshold=10):
        coords1_xy = np.array(coords1)[:, :2]
        coords2_xy = np.array(coords2)[:, :2]

        model_robust, inliers = ransac((coords1_xy, coords2_xy), AffineTransform, min_samples=4, residual_threshold=threshold, max_trials=1000)
        return model_robust, inliers

    def match_stars(self, threshold=10):
        model, inliers = self.ransac_homography(self.coordinates1, self.coordinates2, threshold)
        matched_stars = []

        for i, inlier in enumerate(inliers):
            if inlier:
                matched_stars.append((self.coordinates1[i], self.coordinates2[i]))

        return matched_stars

    def draw_matched_lines(self, output_path, matched_stars, line_color=(0, 255, 0), thickness=1):
        image1 = self.star_coordinates1.color_image
        image2 = self.star_coordinates2.color_image

        h1, w1, _ = image1.shape
        h2, w2, _ = image2.shape

        max_height = max(h1, h2)
        combined_image = np.zeros((max_height, w1 + w2, 3), dtype=np.uint8)
        combined_image[:h1, :w1] = image1
        combined_image[:h2, w1:] = image2

        for match in matched_stars:
            coord1, coord2 = match
            start_point = (coord1[0], coord1[1])
            end_point = (coord2[0] + w1, coord2[1])
            cv2.line(combined_image, start_point, end_point, line_color, thickness)

        cv2.imwrite(output_path, combined_image)

if __name__ == "__main__":
    image_path1 = "/Users/aimayoun/Downloads/Ex1_test_101/ST_db1.png"
    image_path2 = "/Users/aimayoun/Downloads/Ex1_test_101/ST_db2.png"
    output_matched_lines = "/Users/aimayoun/Downloads/output_matched_lines.jpg"
    #output_path = "/Users/aimayoun/Downloads/output_coordinates.txt"
    star_matcher = StarMatcher(image_path1, image_path2)
    matched_stars = star_matcher.match_stars()
   # star_coordinates.save_coordinates(output_path)
    star_matcher.draw_matched_lines(output_matched_lines, matched_stars)

    for pair in matched_stars:
        print(f"Image 1: {pair[0]} | Image 2: {pair[1]}")

