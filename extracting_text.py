def extract_text_from_ppt(ppt_path: str) -> str:
    prs = Presentation(ppt_path)
    full_text = ""
    for slide in prs.slides:
        for shape in slide.shapes:
            if hasattr(shape, "text"):
                full_text += shape.text + " "
    return full_text.strip()
