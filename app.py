from classify import analyze_image
import streamlit as st
import tempfile
import os
import uuid

st.title("🧠 Jaw Width Classifier")


uploaded_file = st.file_uploader(
    "Завантажити фото", type=["jpg", "jpeg", "png", "webp"]
)


if uploaded_file:
    col1, col2 = st.columns(2)
    result = None
    temp_dir = tempfile.gettempdir()
    input_path = os.path.join(temp_dir, f"{uuid.uuid4()}.jpg")
    output_path = os.path.join(temp_dir, f"{uuid.uuid4()}_output.jpg")

    with open(input_path, "wb") as f:
        f.write(uploaded_file.read())

    status_text = st.empty()
    status_text.text("ℹ Зображення обробляється...")

    col1.image(
        input_path,
        caption="До класифікації",
        use_container_width=True,
    )

    try:
        result = analyze_image(input_path, output_path)
        col2.image(
            result["output_path"],
            caption="Результат класифікації",
            use_container_width=True,
        )

        st.markdown(
            f"""
        ### 🔍 Результат:
        - **Тип щелепи**: `{result['type']}`
        - **Впевненість**: `{result['confidence']:.2f}`
        """
        )

    except Exception as e:
        st.error(f"Помилка: {e}")

    status_text.empty()
