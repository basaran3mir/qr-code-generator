from qr_code_generator import QRCodeGenerator

if __name__ == "__main__":
    url = "https://emirbasaran.com"

    generator = QRCodeGenerator(url, output_path="output/qr_code_square_logo.png", logo_shape="square")
    generator.generate()

    generator = QRCodeGenerator(url, output_path="output/qr_code_circle_logo.png", logo_shape="circle")
    generator.generate()