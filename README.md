# NeuroPhoton: Contactless BCIs — Code & Companion Materials

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.16884337.svg)](https://doi.org/10.5281/zenodo.16884337)

**Title:** NeuroPhoton: A Theoretical Review and Modeling Framework for Contactless Brain–Computer Interfaces via Biophotonic, Electromagnetic, and Thermal Pathways

**Author / Creator:** Arvind Gyandatt Mishra

**Zenodo DOI:** 10.5281/zenodo.16884337
**Zenodo record:** https://zenodo.org/records/16884337

**License (Zenodo):** Creative Commons Attribution 4.0 International (CC BY 4.0)

## Description
This repository is a companion scaffold for the Zenodo preprint (NeuroPhoton). It provides:
- a machine-readable citation (`CITATION.bib` / `CITATION.cff`)
- quick-start instructions for reproducing simulation code (placeholder)
- a scripts folder to add reproduction scripts and analysis notebooks
- a `docs/` folder for supplementary notes

The Zenodo record includes the preprint PDF and is licensed CC BY 4.0. This repo does not include the PDF file; link to the canonical version on Zenodo above. If you wish to redistribute the PDF inside this repository, ensure you include the proper CC BY 4.0 attribution (see NOTICES.md).

## Contents (scaffold)
- `src/neurophoton/` — package for core models and utilities (placeholder)
- `scripts/` — reproducible scripts (e.g., run simulations, reproduce figures)
- `notebooks/` — Jupyter notebooks for exploration and figures
- `data/` — small example data
- `docs/` — extended notes, README for data provenance
- `CITATION.bib`, `CITATION.cff` — citation metadata (Zenodo DOI)
- `NOTICES.md` — license and attribution guidance

## Quick start (developer-ready scaffold)
1. Clone or unzip this repo and create a Python venv:

```bash
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
.venv\Scripts\activate    # Windows PowerShell
pip install -r requirements.txt
```

2. Add your simulation code to `src/neurophoton/` and tests in `tests/`. A simple placeholder `scripts/run_demo.py` is included to show structure.

3. Run tests (once implemented):
```bash
pytest -q
```

## License & attribution
The original preprint is available on Zenodo under **CC BY 4.0**. This repository's code is released under **MIT** by default — change as desired. See `NOTICES.md` for attribution guidance when including Zenodo content.

## Contact / maintainer
Arvind Gyandatt Mishra — https://www.linkedin.com/in/arvind-gyandatt-mishra-a6760a16b/
