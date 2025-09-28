from PIL import Image, ImageDraw, ImageFont
import os

# ===== SETTINGS =====
input_folder = r"C:\Users\DeWeNi\Desktop\MaduuProject\MaduuPhotos"
output_folder = r"C:\Users\DeWeNi\Desktop\MaduuProject\photos_with_footer"
os.makedirs(output_folder, exist_ok=True)

footer_text = "Maduu BamBoo Blinds"
font_path = r"C:\Windows\Fonts\arial.ttf"
font_size = 50

bamboo_path = r"C:\Users\DeWeNi\Desktop\MaduuProject\bamboo.png"

for file_name in os.listdir(input_folder):
    if file_name.lower().endswith((".png", ".jpg", ".jpeg")):
        img_path = os.path.join(input_folder, file_name)
        img = Image.open(img_path).convert("RGBA")
        draw = ImageDraw.Draw(img)
        width, height = img.size
        font = ImageFont.truetype(font_path, font_size)

        # Text size
        bbox = draw.textbbox((0,0), footer_text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        # Position bottom center
        x = (width - text_width)/2
        y = height - text_height - 50

        # Shadow effect
        for dx in [-2,2]:
            for dy in [-2,2]:
                draw.text((x+dx, y+dy), footer_text, font=font, fill="black")

        # Main text
        draw.text((x, y), footer_text, font=font, fill="white")

        # Overlay bamboo leaves
        if os.path.exists(bamboo_path):
            bamboo = Image.open(bamboo_path).convert("RGBA")
            bamboo_width = int(text_width*1.2)
            ratio = bamboo_width / bamboo.width
            bamboo_height = int(bamboo.height * ratio)
            bamboo = bamboo.resize((bamboo_width, bamboo_height), Image.ANTIALIAS)
            bx = int((width - bamboo_width)/2)
            by = int(y - bamboo_height + 10)
            img.alpha_composite(bamboo, dest=(bx, by))

        # Save final image
        img = img.convert("RGB")
        img.save(os.path.join(output_folder, file_name))

print("✅ Footer + bamboo logo added to all images successfully!")
