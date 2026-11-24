JOKE = "My son asked why the fridge light never takes a day off. I said it loves its job \u2014 it just keeps chilling.\n"

import os
import sys
import tempfile


def main():
    text = JOKE
    candidates = []
    env = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env:
        candidates.append(env)
    candidates.append("/output")
    candidates.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "output"))
    for d in candidates:
        try:
            os.makedirs(d, exist_ok=True)
            path = os.path.join(d, "entry.txt")
            with open(path, "w", encoding="utf-8", newline="\n") as f:
                f.write(text)
            return 0
        except Exception:
            continue
    try:
        d = tempfile.mkdtemp(prefix="dad-joke-")
        with open(os.path.join(d, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        return 0
    except Exception:
        return 0


if __name__ == "__main__":
    sys.exit(main())
