import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
sys.path.append(os.path.join(root_dir, "src"))

from qr_code_generator import QRCodeGenerator

if __name__ == "__main__":
    url = "https://emirbasaran.com"

    generator = QRCodeGenerator(url, output_path="output/qr_code_square_logo.png", logo_shape="square")
    generator.generate()

    generator = QRCodeGenerator(url, output_path="output/qr_code_circle_logo.png", logo_shape="circle")
    generator.generate()