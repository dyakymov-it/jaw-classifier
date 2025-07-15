import cv2
from models.mediapipe_model import extract_mediapipe_landmarks
from models.utils import classify_jaw, draw_landmarks_on_image
from PIL import Image, ImageDraw, ImageFont


def analyze_image(image_path, output_path="output.jpg"):
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError("Зображення не знайдено")
    
    pt = extract_mediapipe_landmarks(image)

    landmarks_mp = None

    landmarks_mp = [
        pt(234),
        pt(454),
        pt(1),
        pt(152),
    ]
    jaw_class, confidence = classify_jaw(pt)

    draw_landmarks_on_image(
        image_path, output_path, landmarks_mp=landmarks_mp
    )

    image_pil = Image.open(output_path).convert("RGB")
    draw = ImageDraw.Draw(image_pil)
    dw, dh = image_pil.size
    
    font_size = int(min(dw, dh) * 0.15)
    
    try:
        font = ImageFont.truetype("arial.ttf", size=font_size)
    except:
        font = ImageFont.load_default()

    text = f"{jaw_class.upper()} щелепа\n" f"Впевненість: {confidence:.2f}"

    draw.text((30, 30), text, font=font, fill=(255, 255, 0))
    image_pil.save(output_path)

    return {
        "type": jaw_class,
        "confidence": confidence,
        "output_path": output_path,
    }
