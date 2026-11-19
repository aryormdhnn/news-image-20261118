"""Entry for make.fun news-image-20261118.

Writes the pre-built front-page image (entry.png, held in this repo) to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png).
Standard library only; deterministic: the same bytes every run.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    src = os.path.join(HERE, "entry.png")
    if not os.path.isfile(src):
        raise FileNotFoundError(f"entry image missing: {src}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes)")


if __name__ == "__main__":
    main()
