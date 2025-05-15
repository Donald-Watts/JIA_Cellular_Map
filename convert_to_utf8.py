import sys
from pathlib import Path

# Usage: python convert_to_utf8.py <file1> [<file2> ...]

def convert_file(filepath, fallback_encodings=["cp1252", "latin-1"]):
    path = Path(filepath)
    try:
        content = path.read_text(encoding="utf-8")
        print(f"{filepath}: Already UTF-8.")
        return
    except UnicodeDecodeError:
        for enc in fallback_encodings:
            try:
                content = path.read_text(encoding=enc)
                print(f"{filepath}: Read with fallback encoding '{enc}'.")
                break
            except UnicodeDecodeError:
                continue
        else:
            print(f"{filepath}: Could not decode with fallback encodings.")
            return
    # Write back as UTF-8
    path.write_text(content, encoding="utf-8")
    print(f"{filepath}: Converted to UTF-8.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_to_utf8.py <file1> [<file2> ...]")
        sys.exit(1)
    for file in sys.argv[1:]:
        convert_file(file) 