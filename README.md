# Star Matching

A python implementation of a star matching algorithm for finding corresponding stars in two or more images.

## Features
- Uses the Hough Circle Transform to detect stars in an image
- Implements RANSAC to match corresponding stars between two images
- Draws lines connecting the matched stars in the two images

## Usage
To use the code, you need to provide the path to two images as input to the `StarMatcher` class. The code will then return a list of matched stars and also create an image with lines connecting the matched stars.

```python
image_path1 = "/path/to/image1.png"
image_path2 = "/path/to/image2.png"
output_matched_lines = "/path/to/output_matched_lines.jpg"

star_matcher = StarMatcher(image_path1, image_path2)
matched_stars = star_matcher.match_stars()
star_matcher.draw_matched_lines(output_matched_lines, matched_stars)
