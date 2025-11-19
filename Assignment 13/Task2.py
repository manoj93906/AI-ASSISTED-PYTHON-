from pathlib import Path


def read_file(filename: str) -> str:
    """Read file contents with proper error handling."""
    try:
        file_path = Path(filename)
        with file_path.open("r", encoding="utf-8") as source:
            return source.read()
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"File not found: {filename}") from exc
    except OSError as exc:
        raise OSError(f"Failed to read file: {filename}") from exc

