import os
from pathlib import Path
from PIL import Image

QUALITY = 85

def compress(location: Path):
    total_original = 0
    total_compressed = 0
    total_gain = 0
    total_files = 0

    for path in location.rglob("*"):
        if path.is_dir():
            continue

        if path.suffix.lower() not in ('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif', 'webp'):
            continue

        input_path = path
        relative_path = path.relative_to(location)
        out_path = location.parent / "output" / relative_path.parent
        os.makedirs(out_path, exist_ok=True)
        filename = path.name.split(".")[0]

        out_file = out_path / f"{filename}.webp"

        try:
            with Image.open(input_path) as img:
                original_size = input_path.stat().st_size / (1024 ** 2)
                total_original += original_size
                print(f"{input_path}\nOriginal size: {original_size:.2f} Megabytes")
                img.save(out_file, format="WEBP", optimize=True, quality=QUALITY)

                with Image.open(out_file) as _compressed_img:
                    compressed_size = out_file.stat().st_size / (1024 ** 2)
                    total_compressed += compressed_size
                    gain = original_size - compressed_size
                    total_gain += gain
                    total_files += 1
                    print(f"Compressed size: {compressed_size:.2f} megabytes\nGain: {gain:.2f} megabytes")

        except Exception as e:
            print(f"Error processing {input_path}: {e}")

    print("-" * 90)
    print("SUMMARY".center(90))
    print(f"Files: {total_files}")
    print(
        f"Original: {total_original:.2f} megabytes || New Size: {total_compressed:.2f} megabytes"
        f" || Gain: {total_gain:.2f} megabytes ~{(total_gain / total_original) * 100:.2f}% reduction"
    )

if __name__ == "__main__":
    start_path = Path(__file__).parent / "input"
    compress(start_path)
