# Linguistic Network Efficiency

> **A large-scale computational linguistics project investigating Dependency Length Minimization (DLM) across 12 language typologies using the Universal Dependencies (UD) corpus.**

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Research](https://img.shields.io/badge/Type-Computational%20Linguistics-green)
![Languages](https://img.shields.io/badge/Languages-12-orange)
![Dependencies](https://img.shields.io/badge/Parsed-2.6M%2B-red)

---

## Overview

This repository contains the implementation and research methodology for analyzing **Dependency Length Minimization (DLM)** across **12 languages** from the Universal Dependencies (UD) treebanks.

The project investigates whether human languages actively minimize syntactic dependency distances to reduce cognitive load by comparing observed dependency structures against randomized baselines generated through Monte Carlo simulations.

---

## Research Objective

The objective of this work is to quantify structural network efficiency across diverse language typologies and determine whether dependency minimization is an actively enforced grammatical constraint rather than a statistical artifact.

---

## Dataset

- Universal Dependencies (UD) Treebanks
- **12 languages**
- **2.6M+ parsed dependency relations**
- Typologies analyzed:
  - SVO
  - SOV
  - Mixed/Flexible

---

## Methodology

The analysis pipeline performs the following steps:

- Parse CoNLL-U treebanks
- Extract dependency relations
- Compute absolute dependency distance
- Compute normalized dependency distance
- Analyze dependency directionality
- Extract intervening POS categories
- Generate randomized null distributions using Monte Carlo simulations
- Compare observed vs. randomized dependency structures
- Analyze scaling with sentence length
- Generate publication-quality visualizations

---

## Key Findings

- Parsed over **2.6 million** syntactic dependency relations.
- Demonstrated approximately **3× shorter dependency networks** compared to randomized baselines.
- Observed **strictly sublinear scaling** between dependency complexity and sentence length.
- Identified systematic structural differences across SVO, SOV, and Mixed/Flexible language families.
- Quantified typological variation in dependency directionality and intervening part-of-speech distributions.

---

## Repository Structure

```text
.
├── src/
│   ├── parser/
│   ├── preprocessing/
│   ├── analysis/
│   └── visualization/
├── notebooks/
│   └── linguistic_network_efficiency.ipynb
├── main.py
├── README.md
└── research_report.pdf
```

---

## Tech Stack

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- conllu

---

## Running the Project

```bash
pip install -r requirements.txt
python main.py
```

---

## Repository Contents

- **`src/`** — Modular implementation of the analysis pipeline.
- **`notebooks/`** — Original research notebook used during experimentation.
- **`main.py`** — Entry point for running the analysis.
- **`research_report.pdf`** — Complete project report describing the methodology and experimental results.

---

## Research Contributions

This repository supports the following research contributions:

- Designed an end-to-end Python pipeline for parsing and analyzing multilingual syntactic dependency networks.
- Developed a Monte Carlo simulation framework to generate randomized null distributions for hypothesis testing.
- Evaluated dependency network efficiency across twelve language typologies.
- Investigated the relationship between dependency complexity and sentence length using large-scale computational analysis.

---

## Mentor

**Prof. Himanshu Yadav**  
Indian Institute of Technology Kanpur

---

## License

This repository is intended for research and educational purposes.
