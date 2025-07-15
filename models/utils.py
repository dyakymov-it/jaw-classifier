import numpy as np
import cv2


def classify_jaw(landmarks):
    left_jaw = np.array(landmarks(234))
    right_jaw = np.array(landmarks(454))
    top_face = np.array(landmarks(1))
    chin = np.array(landmarks(152))

    width = np.linalg.norm(right_jaw - left_jaw)
    height = np.linalg.norm(top_face - chin)

    if not width or not height:
        raise ValueError(f"")

    ratio = width / height

    if ratio < 1.6:
        jaw_type = "вузька"
        confidence = (1.6 - ratio) / 0.2
    elif ratio > 1.8:
        jaw_type = "широка"
        confidence = (ratio - 1.8) / 0.2
    else:
        jaw_type = "середня"
        confidence = 1 - abs(ratio - 1.7) / 0.1

    confidence = max(0.0, min(1.0, confidence))

    return jaw_type, confidence


def draw_landmarks_on_image(
    image_path, output_path, landmarks_mp=None
):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Не вдалося завантажити зображення: {image_path}")

    if landmarks_mp is not None:
        for x, y in landmarks_mp:
            cv2.circle(image, (int(x), int(y)), 3, (0, 255, 0), -1)


    cv2.imwrite(output_path, image)
    return image

