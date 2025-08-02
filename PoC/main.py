from image_translator.ocr import OCRProcessor
from image_translator.translator import TextTranslator
from image_translator.overlay import TextOverlay
import os

def main():
    input_path = "data/sample_image.jpg"
    output_path = "output/translated_image.jpg"

    # Load image
    image = cv2.imread(input_path)

    # Initialize components
    ocr = OCRProcessor()
    translator = TextTranslator(target_lang="ko")
    overlay = TextOverlay()

    # Extract text boxes
    boxes, rgb_image = ocr.extract_text(image)

    # Translate text
    translations = [translator.translate(box["text"]) for box in boxes]

    # Draw overlay
    result_image = overlay.draw_translations(rgb_image, boxes, translations)

    # Save result
    os.makedirs("output", exist_ok=True)
    result_image.save(output_path)
    print(f"Translation complete. Saved to {output_path}")

if __name__ == "__main__":
    main()
