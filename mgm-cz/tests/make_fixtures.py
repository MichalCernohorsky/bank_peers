"""Vygeneruje binarni fixtures (PDF), ktere nejde ulozit jako text.

Spoustet jen pri zmene fixtures:  python3 tests/make_fixtures.py
Vysledne soubory jsou commitnute, takze testy bezi offline bez tohoto skriptu.
"""
from __future__ import annotations

from pathlib import Path

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def build_pdf(lines: list[str]) -> bytes:
    """Minimalni jednostrankove PDF s textovou vrstvou a spravnym xref."""
    content = "BT /F1 12 Tf 72 740 Td 14 TL\n"
    for line in lines:
        escaped = line.replace("\\", r"\\").replace("(", r"\(").replace(")", r"\)")
        content += f"({escaped}) Tj T*\n"
    content += "ET"
    stream = content.encode("latin-1")

    objects = [
        b"<</Type/Catalog/Pages 2 0 R>>",
        b"<</Type/Pages/Kids[3 0 R]/Count 1>>",
        b"<</Type/Page/Parent 2 0 R/MediaBox[0 0 612 792]"
        b"/Contents 4 0 R/Resources<</Font<</F1 5 0 R>>>>>>",
        b"<</Length " + str(len(stream)).encode() + b">>\nstream\n" + stream + b"\nendstream",
        b"<</Type/Font/Subtype/Type1/BaseFont/Helvetica/Encoding/WinAnsiEncoding>>",
    ]

    out = bytearray(b"%PDF-1.4\n")
    offsets = []
    for i, body in enumerate(objects, start=1):
        offsets.append(len(out))
        out += f"{i} 0 obj\n".encode() + body + b"\nendobj\n"

    xref_at = len(out)
    out += f"xref\n0 {len(objects) + 1}\n".encode()
    out += b"0000000000 65535 f \n"
    for off in offsets:
        out += f"{off:010d} 00000 n \n".encode()
    out += (
        f"trailer\n<</Size {len(objects) + 1}/Root 1 0 R>>\nstartxref\n{xref_at}\n".encode()
        + b"%%EOF\n"
    )
    return bytes(out)


def build_scanned_pdf() -> bytes:
    """PDF bez textove vrstvy - simuluje sken, ze ktereho nejde nic vytahnout."""
    objects = [
        b"<</Type/Catalog/Pages 2 0 R>>",
        b"<</Type/Pages/Kids[3 0 R]/Count 1>>",
        b"<</Type/Page/Parent 2 0 R/MediaBox[0 0 612 792]/Contents 4 0 R>>",
        b"<</Length 0>>\nstream\n\nendstream",
    ]
    out = bytearray(b"%PDF-1.4\n")
    offsets = []
    for i, body in enumerate(objects, start=1):
        offsets.append(len(out))
        out += f"{i} 0 obj\n".encode() + body + b"\nendobj\n"
    xref_at = len(out)
    out += f"xref\n0 {len(objects) + 1}\n".encode() + b"0000000000 65535 f \n"
    for off in offsets:
        out += f"{off:010d} 00000 n \n".encode()
    out += (
        f"trailer\n<</Size {len(objects) + 1}/Root 1 0 R>>\nstartxref\n{xref_at}\n".encode()
        + b"%%EOF\n"
    )
    return bytes(out)


def main() -> None:
    FIXTURES.mkdir(parents=True, exist_ok=True)
    (FIXTURES / "pravidla-v1.pdf").write_bytes(build_pdf([
        "Pravidla akce Pozvani pratel",
        "Odmena za doporuceni cini 500 Kc pro doporucujiciho.",
        "Doporuceny ziska 500 Kc.",
        "Maximalne 10 doporucenych rocne.",
        "Akce plati do 31. 12. 2026.",
    ]))
    (FIXTURES / "pravidla-v2.pdf").write_bytes(build_pdf([
        "Pravidla akce Pozvani pratel",
        "Odmena za doporuceni cini 750 Kc pro doporucujiciho.",
        "Doporuceny ziska 500 Kc.",
        "Maximalne 10 doporucenych rocne.",
        "Akce plati do 31. 12. 2026.",
    ]))
    (FIXTURES / "sken-bez-textu.pdf").write_bytes(build_scanned_pdf())
    print(f"fixtures zapsany do {FIXTURES}")


if __name__ == "__main__":
    main()
