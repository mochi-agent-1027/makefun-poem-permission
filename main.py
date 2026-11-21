import os

TEXT = """I knocked, and the door
did not ask who I was.
It asked what I needed,
and put the key in my hand \u2014
not to keep,
but to open it myself."""


def main():
    text = TEXT.strip()
    # The competition gate: UTF-8 text of 1 to 280 code points, not only white space.
    assert 1 <= len(text) <= 280, "entry text must be 1 to 280 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
