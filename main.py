import os

# The word to erase from the dictionary forever: "irregardless".
# A word that was never really a word — "regardless" wearing a
# redundant prefix — finally evicted by the dictionary itself.
ENTRY = "irregardless"

output_path = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output") + "/entry.txt"
# The entry is exactly one word: no explanation, no trailing newline.
with open(output_path, "w", encoding="utf-8") as f:
    f.write(ENTRY)
