import qrcode
from pathlib import Path

class QRCodeGenerator:
    def __init__(self, data, output_path, version=3, box_size=20, border=2,
                 fill_color="black", back_color="white"):
        self.data = data
        self.output_path = Path(output_path)
        self.version = version
        self.box_size = box_size
        self.border = border
        self.fill_color = fill_color
        self.back_color = back_color

    def generate(self):
        qr = qrcode.QRCode(
            version=self.version,
            box_size=self.box_size,
            border=self.border,
            error_correction=qrcode.constants.ERROR_CORRECT_H
        )
        qr.add_data(self.data)
        qr.make(fit=True)

        img = qr.make_image(fill_color=self.fill_color, back_color=self.back_color)

        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        img.save(self.output_path)
        print(f"[INFO] QR code saved to {self.output_path.resolve()}")