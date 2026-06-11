from qr_code_generator import QRCodeGenerator

if __name__ == "__main__":
    url = "https://emirbasaran.com"
    generator = QRCodeGenerator(url, "output/qr_code.png")
    generator.generate()