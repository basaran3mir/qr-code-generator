# qr-code-generator

A clean and customizable QR code generator for Python with optional embedded branding logos. This project makes it easy to create high-quality QR codes with support for circular or square logo overlays, color customization, and portable output.

## Key features

- Generate QR codes from any text or URL
- Custom output size, colors, and border settings
- Embed a logo at the center of the QR code
- Supports circular and square logo shapes
- Saves generated QR codes as PNG files
- Simple Python API and example usage

## Getting Started

Follow these steps to get the project running locally.

### Prerequisites

- Python 3.11 or newer
- `pip` package manager

### Install

1. Clone the repository:

```bash
git clone https://github.com/basaran3mir/qr-code-generator.git
cd qr-code-generator
```

2. Create a virtual environment (recommended):

```bash
python -m venv venv
```

3. Activate the virtual environment:

- Windows:

```powershell
venv\Scripts\Activate.ps1
```

- macOS / Linux:

```bash
source venv/bin/activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Use the provided `examples/usage_example.py` script or import the generator into your own code.

### Example

```python
from qr_code_generator import QRCodeGenerator

url = "https://emirbasaran.com"

generator = QRCodeGenerator(
    data=url,
    output_path="output/qr_code_circle_logo.png",
    logo_shape="circle",
)
generator.generate()
```

### Example with square logo

```python
from qr_code_generator import QRCodeGenerator

url = "https://emirbasaran.com"

generator = QRCodeGenerator(
    data=url,
    output_path="output/qr_code_square_logo.png",
    logo_shape="square",
)
generator.generate()
```

## Project Structure

```
LICENSE
README.md
requirements.txt
examples/
  usage_example.py
output/
src/
  qr_code_generator.py
  res/
```

- `src/qr_code_generator.py` — main QR code generator implementation
- `examples/usage_example.py` — usage examples for generating QR codes
- `requirements.txt` — Python dependencies
- `src/res/` — default assets such as the included brand logo
- `output/` — generated QR code output files

## Configuration

The `QRCodeGenerator` constructor supports several configurable parameters:

- `data` (str): Text or URL encoded into the QR code
- `output_path` (str): Destination file path for the PNG output
- `version` (int): QR code version controlling data capacity
- `box_size` (int): Pixel size of each QR code box
- `border` (int): Border thickness around the QR code
- `fill_color` (str): QR code color
- `back_color` (str): Background color
- `brand_logo_path` (str): Custom logo file path
- `qr_size` (int): Final QR code image size in pixels
- `logo_size` (int): Logo badge size in pixels
- `logo_border` (int): Padding around the embedded logo
- `logo_shape` (str): `"circle"` or `"square"`

## Development

To make changes or extend the project:

1. Install the dependencies in a virtual environment.
2. Edit `src/qr_code_generator.py` or add new examples.
3. Test your changes by running the example script:

```bash
python examples/usage_example.py
```

4. Verify that output files are generated correctly in the `output/` folder.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with improvements, bug fixes, or feature ideas. Keep changes focused and include clear examples when adding new generator behavior.

## License

This project is licensed under the terms of the `LICENSE` file.

## Contact

For questions, feature requests, or bug reports, please open an issue in this repository.