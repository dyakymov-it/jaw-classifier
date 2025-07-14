import cv2
import mediapipe as mp
import numpy as np

def extract_mediapipe_landmarks(image):
    h, w = image.shape[:2]
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    mp_face_mesh = mp.solutions.face_mesh
    with mp_face_mesh.FaceMesh(static_image_mode=True) as face_mesh:
        result = face_mesh.process(rgb)

    if not result.multi_face_landmarks:
        return None

    face = result.multi_face_landmarks[0].landmark

    def pt(index):
        lm = face[index]
        return np.array([lm.x * w, lm.y * h])

    return pt