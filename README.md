# Star Matching

A python implementation of a star matching algorithm for finding corresponding stars in two or more images.

## Features
- Uses the Hough Circle Transform to detect stars in an image
- Implements RANSAC to match corresponding stars between two images
- Draws lines connecting the matched stars in the two images

## Usage
To use the code, you need to provide the path to two images as input to the `StarMatcher` class. The code will then return a list of matched stars and also create an image with lines connecting the matched stars.

## Requirements
The code requires the following libraries:
- OpenCV
- Numpy
- scikit-image

To install the dependencies, run the following commands in your terminal:
pip install opencv-python
pip install numpy
pip install scikit-image

```python
image_path1 = "/path/to/image1.png"
image_path2 = "/path/to/image2.png"
output_matched_lines = "/path/to/output_matched_lines.jpg"

star_matcher = StarMatcher(image_path1, image_path2)
matched_stars = star_matcher.match_stars()
star_matcher.draw_matched_lines(output_matched_lines, matched_stars)
```

## Summarize
in this project we have to code an algorithm to match between stars in two images or more , trying to detect stars in the first image using CHT - use the OpenCv function HoughCircles(), it works in roughly analogous way, that loads an image(reduce noise by blur it)->applies the houghCircleTransform ->display the detecedd circle in the window. Then we impelement the ransac - a statistical approach for curbing outliers , to match between the corresponding stars in the images and to connect between them by drawing lines.
More information about the code: 
in the code we use an externalLibrary(Numpy), and OpenCv, and OpenSource(scikit-image), they all must be installed before running the code.
the star_coordinates library spilit --- 


![output_matched_lines](https://user-images.githubusercontent.com/58775369/233772729-f7c96396-83ab-4b7c-8f40-ae36f73dfc3d.jpg)
