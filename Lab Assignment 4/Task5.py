def _count_lines_in_file(path: str) -> int:
    """Return the number of lines in the given file path."""
    with open(path, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)

def count_lines_in_file(path: str) -> int:
    """
    Return the number of lines in the given .txt file path.
    Appends '.txt' if the extension is omitted and raises exceptions on error.
    """
    if not path:
        raise ValueError("path must be a non-empty string")
    path = path.strip().strip('"\'')
    if not path.lower().endswith(".txt"):
        path += ".txt"
    return _count_lines_in_file(path)

def count_lines_from_user_input(prompt: str = "Enter path to a .txt file: ") -> int:
    """
    Prompt the user for a .txt filename (or path), open it and return the number of lines.
    The function will append '.txt' if the user omits the extension and will retry on errors.
    """
    while True:
        try:
            user_input = input(prompt).strip().strip('"\'')
        except (KeyboardInterrupt, EOFError):
            raise  # let caller handle interruption

        if not user_input:
            print("No filename entered. Please try again.")
            continue

        if not user_input.lower().endswith(".txt"):
            user_input += ".txt"

        try:
            return _count_lines_in_file(user_input)
        except FileNotFoundError:
            print(f"File not found: {user_input}")
        except IsADirectoryError:
            print(f"Path is a directory, not a file: {user_input}")
        except Exception as e:
            print(f"Error opening file: {e}")

if __name__ == "__main__":
    try:
        count = count_lines_from_user_input()
        print(count)
    except Exception:
        print("Operation cancelled or failed.")
