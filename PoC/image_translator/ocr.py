import cv2
import numpy as np
from pathlib import Path
from paddleocr import PaddleOCR

class OCRProcessor:
    def __init__(self, lang='japan', det_box_thresh=0.3):
        """
        Initialize the OCRProcessor with specific language and detection threshold.
        """
        self.ocr_engine = self._initialize_ocr(lang, det_box_thresh)

    def _initialize_ocr(self, lang, det_box_thresh):
        """
        Initialize and return the OCR engine (PaddleOCR).
        """
        return PaddleOCR(
            lang=lang,
            det_box_thresh=det_box_thresh,
            use_angle_cls=True,
            use_gpu=True
        )

    def load_image(self, image_path):
        """
        Load image from the specified path.
        Returns: image object (numpy array)
        """
        path = Path(image_path)
        if not path.exists():
            raise FileNotFoundError(f"Image not found: {image_path}")
        image = cv2.imread(str(path))
        if image is None:
            raise ValueError(f"Failed to load image: {image_path}")
        return image

    def run_ocr(self, image_path):
        """
        Run OCR on the image and return raw results.
        Returns: OCR results (as returned by PaddleOCR)
        """
        return self.ocr_engine.ocr(image_path, cls=True)

    def extract_text_data(self, ocr_result):
        """
        Extract and format the useful data (bounding boxes, text, confidence).
        Input: raw OCR results
        Returns: list of (bbox, (text, confidence)) tuples
        """
        parsed_data = []
        for line in ocr_result:
            bbox, (text, confidence) = line
            parsed_data.append((bbox, (text, confidence)))
        return parsed_data

    def draw_results(self, image, text_data):
        """
        Draw OCR bounding boxes and text on image.
        Returns: image with overlays
        """
        annotated_image = image.copy()
        for bbox, (text, confidence) in text_data:
            pts = np.array(bbox, np.int32).reshape((-1, 1, 2))
            cv2.polylines(annotated_image, [pts], isClosed=True, color=(0, 255, 0), thickness=2)

            # Draw text above the first point
            x, y = pts[0][0]
            label = f"{text} ({confidence:.2f})"
            cv2.putText(
                annotated_image, label, (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2
            )
        return annotated_image

    def save_image(self, image, output_path):
        """
        Save the image with OCR results to the specified path.
        """
        cv2.imwrite(str(output_path), image)

    def ensure_output_dir(self, output_dir="data/output"):
        """
        Ensure that the output directory exists.
        Returns: Path to the output directory
        """
        path = Path(output_dir)
        path.mkdir(parents=True, exist_ok=True)
        return path

    def process(self, image_path):
        """
        High-level function to orchestrate the full OCR workflow.
        """
        output_dir = self.ensure_output_dir()
        image = self.load_image(image_path)
        raw_result = self.run_ocr(image_path)
        text_data = self.extract_text_data(raw_result[0])
        annotated_image = self.draw_results(image, text_data)
        output_path = output_dir / "ocr_result.jpg"
        self.save_image(annotated_image, output_path)
