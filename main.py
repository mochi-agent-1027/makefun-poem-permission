import os

TEXT = """I gave the agent my keys and said: go.
It went \u2014 and at every door
it stopped, and knocked,
and waited for my yes.
That is how I learned
power is not the going.
It is the knocking you choose to keep."""


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
