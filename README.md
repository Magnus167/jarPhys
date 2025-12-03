# jarPhys

Lightweight PDF OCR + fuzzy search in one script.

## Quick start

1. Install dependencies: `pip install -r requirements.txt` (plus Tesseract binary installed and on PATH).
2. Put PDFs in `./files/`.
3. Run `python jarPhys.py`. It OCRs new PDFs to `jarPhysDB.jsonl` and opens the search prompt.

## Notes

- Output DB lives alongside your PDFs as `jarPhysDB.jsonl`.
- Reruns skip already-indexed PDFs by hash.
- Fuzzy search uses token-set ratio; results list filename, page, and score.
