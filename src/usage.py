from qr_code_generator import QRCodeGenerator

def run(data, output_flie):
    generator = QRCodeGenerator(data, output_flie)
    generator.generate()

if __name__ == "__main__":
    run("https://basaran3mir.github.io/", "src/output/qr_code.png")