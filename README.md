# _QR Code Generator_

A clean, professional Python utility for generating branded QR codes with embedded logos and customizable styling.

**Key features**

- Generate high-quality QR codes directly from URLs or text
- Embed a centered logo in either a circular or square badge
- Customize QR size, border, colors, and error correction
- Save output as PNG files in a dedicated `output/` directory
- Simple Python API with defaults for rapid use

## Getting Started

Follow these instructions to set up the project locally and generate QR codes.

### Prerequisites

- Python 3.10 or newer
- Git (optional, for cloning the repository)
- A virtual environment tool such as `venv`

### Install

1. Clone the repository:

```bash
git clone https://github.com/yourusername/qr-code-generator.git
cd qr-code-generator
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
# Windows PowerShell
venv\Scripts\Activate.ps1
# Windows CMD
venv\Scripts\activate.bat
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the example script from the repository root:

```bash
python src/usage_example.py
```

This will generate two QR codes in the `output/` directory with both square and circular logo styles.

You can also use the generator directly in your own script:

```python
from qr_code_generator import QRCodeGenerator

generator = QRCodeGenerator(
    data="https://example.com",
    output_path="output/my_qr.png",
    version=4,
    box_size=20,
    border=2,
    fill_color="black",
    back_color="white",
    logo_shape="circle",
)
generator.generate()
```

## Project Structure

- `LICENSE` - project license file
- `README.md` - project documentation
- `requirements.txt` - Python dependency list
- `output/` - generated QR code artifacts
- `src/` - source code directory
  - `qr_code_generator.py` - main QR code generator implementation
  - `usage_example.py` - example usage script
  - `res/` - resources directory containing the default brand logo

## Configuration

The `QRCodeGenerator` constructor supports these options:

- `data` - string content to encode in the QR code
- `output_path` - destination file path for the generated PNG
- `version` - QR code version, which affects data capacity
- `box_size` - pixel size of each QR module
- `border` - width of the QR border in modules
- `fill_color` - color used for the QR modules
- `back_color` - background color for the QR code
- `brand_logo_path` - optional path to a custom logo image
- `qr_size` - final QR image size in pixels
- `logo_size` - size of the embedded logo badge
- `logo_border` - padding between the logo and badge edge
- `logo_shape` - `circle` or `square`

## Development

To contribute or modify the project:

1. Activate the virtual environment.
2. Install or update dependencies with `pip install -r requirements.txt`.
3. Edit code in `src/qr_code_generator.py`.
4. Test changes by running `python src/usage_example.py` or writing your own script.

## Contributing

Contributions are welcome. Please follow these steps:

- Open an issue to discuss a feature or bug.
- Fork the repository and create a feature branch.
- Submit a pull request with a clear description of your changes.

## License

This project is licensed under the terms defined in the `LICENSE` file.

## Contact

For questions, feature requests, or bug reports, please open an issue in this repository.
