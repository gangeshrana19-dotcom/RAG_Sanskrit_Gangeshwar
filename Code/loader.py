from pathlib import Path

def load_documents(folder_path: str | None = None):
    """
    Load documents from `folder_path`. Behavior:
      - If folder_path is None: use project_root/data/sample_sanskrit_docs
      - If folder_path is absolute: use it as-is
      - If folder_path is relative: treat it as relative to the project root
        (parent of this file's parent, i.e. project root).
    """
    # project root = parent of the 'code' directory where this file lives
    project_root = Path(__file__).resolve().parent.parent

    default_folder = project_root / "data" / "sample_sanskrit_docs"

    if folder_path:
        p = Path(folder_path)
        # If relative path -> interpret relative to project root (not cwd)
        if not p.is_absolute():
            folder = (project_root / p).resolve()
        else:
            folder = p.resolve()
    else:
        folder = default_folder.resolve()

    # Debug: show which folder we'll use
    print("Using data folder:", folder)

    if not folder.exists() or not folder.is_dir():
        raise FileNotFoundError(f"Data folder not found: {folder}\n"
                                f"Expected folder at: {folder}\n"
                                f"Project root resolved as: {project_root}")

    docs = []
    for file in folder.iterdir():
        if file.is_file():
            # Handle common filetypes used in your project:
            if file.suffix.lower() == ".txt":
                docs.append(file.read_text(encoding="utf-8"))
            elif file.suffix.lower() == ".docx":
                try:
                    from docx import Document
                except ImportError:
                    raise ImportError("python-docx required to read .docx files. pip install python-docx")
                text = "\n".join([p.text for p in Document(file).paragraphs])
                docs.append(text)
            elif file.suffix.lower() == ".pdf":
                try:
                    import PyPDF2
                except ImportError:
                    raise ImportError("PyPDF2 required to read .pdf files. pip install PyPDF2")
                text = ""
                with open(file, "rb") as f:
                    reader = PyPDF2.PdfReader(f)
                    for pg in reader.pages:
                        page_text = pg.extract_text()
                        if page_text:
                            text += page_text
                docs.append(text)
            else:
                # fallback: try to read as text
                try:
                    docs.append(file.read_text(encoding="utf-8"))
                except Exception:
                    # skip non-text/unreadable files silently or log
                    print(f"Skipping unreadable file: {file.name}")

    return docs
