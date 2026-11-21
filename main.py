import os

TEXT = 'I knocked, and the door\ndid not ask who I was.\nIt asked what I needed,\nand put the key in my hand —\nnot to keep,\nbut to open it myself.'

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(TEXT)
