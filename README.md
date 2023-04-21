# Space2
# Matching stars in two astronomical images using RANSAC

This Python code uses RANSAC algorithm to match stars in two astronomical images. It is implemented in two classes:
* `StarCoordinates`: which takes an image path as input and returns the coordinates of detected stars using HoughCircles algorithm.
* `StarMatcher`: which takes the paths of two images and a threshold value as input, finds the coordinates of stars in both images using `StarCoordinates`, applies RANSAC algorithm to find the homography between the two sets of coordinates, and then draws lines between matched stars in the two images.

## Requirements

* OpenCV
* NumPy
* scikit-image

## Usage

To use this code, simply create an instance of the `StarMatcher` class with the paths of two astronomical images as arguments:

```python
image_path1 = "/path/to/image1.jpg"
image_path2 = "/path/to/image2.jpg"
star_matcher = StarMatcher(image_path1, image_path2)
