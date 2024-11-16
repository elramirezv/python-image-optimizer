# Python Image Optimizer

This simple script allows you to optimize/compress a set of images.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```
python3 main.py
```

The script will look for images in the `input` folder (located in the same directory as the script) and create an `output` folder with the optimized images in WebP format.

The script supports the following image formats: PNG, JPG, JPEG, TIFF, BMP, GIF, and WebP.

## How it works

1. The script iterates over all files in the `input` folder and its subdirectories.
2. For each supported image file, it opens the image using the `PIL` library.
3. It saves the image in WebP format with the specified quality (default is 85) in the `output` folder, preserving the original folder structure.
4. The script prints the original and compressed file sizes, as well as the gain in megabytes and the percentage of reduction.
5. After processing all files, it prints a summary with the total number of files, original size, new size, gain, and percentage of reduction.

## Example output

```bash
input/image1.jpg
Original size: 2.34 Megabytes
Compressed size: 1.12 megabytes
Gain: 1.22 megabytes
input/folder/image2.png
Original size: 1.56 Megabytes
Compressed size: 0.78 megabytes
Gain: 0.78 megabytes
-----------------------------
           SUMMARY
-----------------------------
Files: 2
Original: 3.90 megabytes || New Size: 1.90 megabytes || Gain: 2.00 megabytes ~51.28% reduction
```

**Note:** The script assumes that the `input` folder exists in the same directory as the script. If the `output` folder doesn't exist, it will be created.

