from PIL import Image, ImageDraw, ImageFont

class TextOverlay:
    def __init__(self, font_path="arial.ttf", font_size=16):
        self.font = ImageFont.truetype(font_path, size=font_size)

    def draw_translations(self, image_array, boxes, translations):
        image = Image.fromarray(image_array)
        draw = ImageDraw.Draw(image)

        for box, translated in zip(boxes, translations):
            x, y, w, h = box["left"], box["top"], box["width"], box["height"]
            draw.rectangle([(x, y), (x + w, y + h)], outline="red", width=1)
            draw.text((x, y - 20), translated, fill="blue", font=self.font)

        return image