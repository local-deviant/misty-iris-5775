"""Ridiculous at First Glance, Real by the Second.

Writes one sentence (at most 200 characters) to /output/entry.txt,
pitching a bizarre startup idea that sounds like a joke at first
glance yet makes sense as a real business.

The program is fully deterministic: no input, no file reads, no
randomness, no clock, no network. It writes the same fixed text on
every run, with no trailing newline. The ENTRY_OUTPUT environment
variable exists only so the entry can be tested locally; the
sandbox run uses the default /output/entry.txt.
"""

TEXT = (
    "We rent professional strangers to fill empty chairs at weddings, "
    "because couples pay so no photo shows a gap where grandma "
    "couldn't fly in."
)


def main() -> None:
    """Write the pitch sentence to the output file."""
    import os

    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
