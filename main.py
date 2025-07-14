from classify import analyze_image
import uuid


def start(input_path):
    result = None
    output_path = f"{uuid.uuid4()}_output.jpg"

    result = analyze_image(input_path, output_path)

    return {
        "output_path": result["output_path"],
        "type": result["type"],
        "confidence": result["confidence"],
    }