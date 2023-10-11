# -Image-Inpainting

# Image Inpainting and Quality Evaluation

This project contains Python scripts for image inpainting and image quality evaluation. The inpainting script repairs damaged or missing regions in an image, while the evaluation script measures the similarity between two images using various metrics.

## Table of Contents

- [Image Inpainting](#image-inpainting)
  - [Usage](#usage-inpainting)
  - [Parameters](#parameters-inpainting)

- [Image Quality Evaluation](#image-quality-evaluation)
  - [Usage](#usage-evaluation)

- [Requirements](#requirements)
- [Authors](#authors)
- [License](#license)

## Image Inpainting

### Usage

To use the image inpainting script:

1. Ensure you have Python installed on your system.

2. Install the required libraries (NumPy and OpenCV) using pip:

3. Place your input image and mask in the same directory as the script.

4. Modify the script to specify the filenames of your input image and mask:

```python
img = cv2.imread("input_image.png")
roi = cv2.imread("mask.png")
```

## Run the inpainting script:
```
python image_inpainting.py
