import pytesseract
import cv2

class OCRProcessor:
    def __init__(self, lang="eng"):
        self.lang = lang

    def extract_text(self, image):
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = pytesseract.image_to_data(rgb_image, lang=self.lang, output_type=pytesseract.Output.DICT)
        boxes = []
        for i in range(len(results["text"])):
            text = results["text"][i].strip()
            if text:
                box = {
                    "text": text,
                    "left": results["left"][i],
                    "top": results["top"][i],
                    "width": results["width"][i],
                    "height": results["height"][i]
                }
                boxes.append(box)
        return boxes, rgb_image