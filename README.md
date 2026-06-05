# QR Code Generator

**Key features**

- Generate QR codes from any text or URL.
- Customize QR code appearance with fill and background colors.
- Control QR matrix version, box size, and border width.
- High error correction mode for reliable scanning.
- Automatic output directory creation when saving files.

## Getting Started

This project provides a simple Python-based QR code generator using the `qrcode` library.
It is designed for developers who need a lightweight utility to create QR codes programmatically.

### Prerequisites

- Python 3.8 or newer
- `pip` package manager
- Recommended: a Python virtual environment

### Install

1. Clone the repository:

   ```bash
   git clone https://github.com/basaran3mir/qr-code-generator.git
   cd qr-code-generator
   ```

2. Create and activate a virtual environment:

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the example script from the project root:

```bash
python src/usage_example.py
```

This will generate a QR code image at `output/qr_code.png` using the default URL.

### Use the generator directly

```python
from qr_code_generator import QRCodeGenerator

url = "https://basaran3mir.github.io/"
generator = QRCodeGenerator(
    data=url,
    output_path="output/qr_code.png",
    version=3,
    box_size=20,
    border=2,
    fill_color="black",
    back_color="white",
)
generator.generate()
```

## Project Structure

- `LICENSE` - Project license file (MIT License).
- `README.md` - Project documentation.
- `requirements.txt` - Python dependencies.
- `output/` - Default folder for generated QR code images.
- `src/qr_code_generator.py` - Main QR code generator implementation.
- `src/usage_example.py` - Example script showing how to use the library.

## Configuration

The `QRCodeGenerator` class exposes the following configuration parameters:

- `data` (str): The text or URL encoded into the QR code.
- `output_path` (str): File path for the generated image.
- `version` (int): QR code version/size (higher values increase capacity).
- `box_size` (int): Pixel size of each QR code box.
- `border` (int): Border width around the QR code.
- `fill_color` (str): Color of the QR code modules.
- `back_color` (str): Background color for the QR code image.

The generator automatically creates the necessary output directories when saving the image.

## Development

1. Activate the virtual environment:

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

2. Install dependencies if needed:

   ```bash
   pip install -r requirements.txt
   ```

3. Run or modify the example script:

   ```bash
   python src/usage_example.py
   ```

4. Update `src/qr_code_generator.py` to add customization, validation, or extended support.

## Contributing

Contributions are welcome. To contribute:

- Fork the repository.
- Create a feature branch.
- Add clear documentation and test any changes.
- Open a pull request with a description of your improvements.

Please follow clean coding practices and keep the implementation and example usage easy to understand.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

- GitHub: [basaran3mir](https://github.com/basaran3mir)
- Project: qr-code-generator
