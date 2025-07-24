import cv2
import numpy as np
from pathlib import Path
from paddleocr import PaddleOCR

def draw_results(image_path, ocr_result):
    """Draw bounding boxes on the image"""
    img = cv2.imread(image_path)
    
    Path("data/output").mkdir(parents=True, exist_ok=True)
    output_path = "data/output/ocr_result.jpg"
    
    for line in ocr_result:
        bbox, (text, confidence) = line
        
        box = np.array(bbox).astype(np.int32)
        cv2.polylines(img, [box], True, (0, 255, 0), 2)
        cv2.putText(img, f"{text} ({confidence:.2f})", 
                    (box[0][0], box[0][1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
    
    cv2.imwrite(output_path, img)

# Use the lightweight PP-OCRv5 Mobile model for Japanese
image_path = 'data/sample_jp.jpg'  # replace with your image path
ocr = PaddleOCR(
    use_angle_cls=True,
    lang='japan',             # use 'japan' for Japanese text
    det_db_box_thresh=0.3,    # optional tweak for detection sensitivity
    use_gpu=False,
    show_log=False
)

result = ocr.ocr(image_path, cls=True)
draw_results(image_path, result[0])

