from qr_code_generator import QRCodeGenerator

if __name__ == "__main__":
    generator = QRCodeGenerator("https://basaran3mir.github.io/", "output/qr_code.png")
    generator.generate()