import os
from extract_text import extract_text_from_pdf
from segment_sections import segment_sections
from segment_requirements import extract_requirements
from extract_features import extract_features

from db.insert_document import insert_document
from db.insert_sections import insert_sections
from db.insert_requirements import insert_requirements
from db.insert_features import insert_features


INPUT_PDF = "data/input/OSMS_SRS.pdf"


def main():
    print("\n[START] SRS Segmentation Pipeline")

    if not os.path.exists(INPUT_PDF):
        raise FileNotFoundError(f"SRS file not found: {INPUT_PDF}")

    file_name = os.path.basename(INPUT_PDF)

    print("[0] Registering SRS document...")
    document_id = insert_document(file_name)

    print("[1] Extracting text from PDF...")
    text = extract_text_from_pdf(INPUT_PDF)

    print("[2] Segmenting SRS sections...")
    sections = segment_sections(text)

    print("[3] Saving sections to database...")
    insert_sections(document_id)

    print("[4] Extracting functional requirements...")
    functional_reqs = extract_requirements(
        sections.get("Functional Requirements", "")
    )

    print("[5] Saving requirements to database...")
    insert_requirements()

    print("[6] Extracting software features...")
    features = extract_features(functional_reqs)

    print("[7] Saving features to database...")
    insert_features()

    print("[END] Pipeline completed successfully")


if __name__ == "__main__":
    main()
