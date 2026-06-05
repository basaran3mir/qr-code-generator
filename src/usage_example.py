from qr_code_generator import QRCodeGenerator

if __name__ == "__main__":
    url = "https://basaran3mir.github.io/"
    generator = QRCodeGenerator(url, "output/qr_code.png")
    generator.generate()