"""
Small demo: how to programmatically update HTML/CSS using with open() and try/except.

This demonstrates a safe pattern for file edits: back up the original, then write the updated content.
"""
from pathlib import Path


def write_file(path: Path, content: str) -> bool:
    """Write `content` to `path` using a context manager and handle errors."""
    try:
        with path.open('w', encoding='utf-8') as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"Failed to write {path}: {e}")
        return False


def read_file(path: Path) -> str | None:
    try:
        with path.open('r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Failed to read {path}: {e}")
        return None


def backup_and_replace(path: Path, new_content: str) -> bool:
    backup = path.with_suffix(path.suffix + '.bak')
    try:
        # Make a backup first
        if path.exists():
            with path.open('r', encoding='utf-8') as f:
                original = f.read()
            with backup.open('w', encoding='utf-8') as b:
                b.write(original)

        # Now write the new content
        return write_file(path, new_content)
    except Exception as e:
        print(f"Error backing up or replacing {path}: {e}")
        return False


if __name__ == '__main__':
    base = Path(__file__).parent
    html = base / 'task1.html'
    css = base / 'task2.css'

    print('Reading files')
    h = read_file(html)
    c = read_file(css)

    if h and c:
        print('Files readable — everything looks good.\n')
    else:
        print('One or more files could not be read — aborting.\n')

    # Example: append a small comment to the CSS file safely
    if c is not None:
        new_css = c + '\n/* Updated by refactor_demo.py — safe write */\n'
        if backup_and_replace(css, new_css):
            print('CSS updated (backup created).')
        else:
            print('Failed to update CSS.')
