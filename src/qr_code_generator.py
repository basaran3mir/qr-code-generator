import qrcode
from pathlib import Path
from PIL import Image, ImageDraw, ImageOps

class QRCodeGenerator:
    def __init__(self, data, output_path="output/qr_code.png", version=3, box_size=20, border=2,
                 fill_color="black", back_color="white", brand_logo_path=None,
                 qr_size=500, logo_size=150, logo_border=10, logo_shape="circle"):
        self.data = data
        self.output_path = Path(output_path)
        self.version = version
        self.box_size = box_size
        self.border = border
        self.fill_color = fill_color
        self.back_color = back_color
        self.qr_size = qr_size
        self.logo_size = logo_size
        self.logo_border = logo_border
        self.logo_shape = logo_shape.lower()
        if self.logo_shape not in {"circle", "square"}:
            raise ValueError("logo_shape must be either 'circle' or 'square'")
        self.brand_logo_path = Path(brand_logo_path) if brand_logo_path else (
            Path(__file__).resolve().parent / "res" / "brand-logo.png"
        )

    def _prepare_logo(self):
        logo_path = self.brand_logo_path
        if not logo_path.exists():
            raise FileNotFoundError(f"Brand logo not found at {logo_path}")

        inner_size = self.logo_size - (2 * self.logo_border)
        logo = Image.open(logo_path).convert("RGBA")
        logo = ImageOps.fit(logo, (inner_size, inner_size), Image.Resampling.LANCZOS)

        badge = Image.new("RGBA", (self.logo_size, self.logo_size), (255, 255, 255, 0))
        badge_draw = ImageDraw.Draw(badge)

        if self.logo_shape == "circle":
            mask = Image.new("L", (inner_size, inner_size), 0)
            mask_draw = ImageDraw.Draw(mask)
            mask_draw.ellipse((0, 0, inner_size, inner_size), fill=255)
            logo.putalpha(mask)
            badge_draw.ellipse((0, 0, self.logo_size - 1, self.logo_size - 1), fill=(255, 255, 255, 255))
        else:
            badge_draw.rectangle((0, 0, self.logo_size - 1, self.logo_size - 1), fill=(255, 255, 255, 255))

        badge.paste(logo, (self.logo_border, self.logo_border), logo)
        return badge

    def _embed_logo(self, img):
        img = img.convert("RGBA")
        if img.size != (self.qr_size, self.qr_size):
            img = img.resize((self.qr_size, self.qr_size), Image.Resampling.LANCZOS)

        logo = self._prepare_logo()
        pos = (
            (self.qr_size - self.logo_size) // 2,
            (self.qr_size - self.logo_size) // 2,
        )
        img.paste(logo, pos, logo)
        return img

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
        img = self._embed_logo(img)

        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        img.save(self.output_path)
        print(f"[INFO] QR code saved to {self.output_path.resolve()}")