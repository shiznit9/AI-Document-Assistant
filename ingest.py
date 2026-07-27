from pathlib import Path

from document_processing.document_loader import DocumentLoader
from document_processing.document_manager import DocumentManager

DOCUMENTS_DIRECTORY = Path("data/documents")


def main() -> None:

    print(f"Scanning '{DOCUMENTS_DIRECTORY}'...\n")

    for file_path in DOCUMENTS_DIRECTORY.iterdir():

        if not file_path.is_file():
            continue

        if not DocumentLoader.is_supported(file_path):
            print(f"Skipping unsupported file: {file_path.name}")
            continue

        print(f"Ingesting: {file_path.name}")

        DocumentManager.ingest(file_path)

    print("\nDocument ingestion completed.")


if __name__ == "__main__":
    main()