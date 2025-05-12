# DS\_girafe — Data Science Course Labs & Competitions

<p align="center">
  <img src="https://img.shields.io/badge/Status-Learning--Repo-blue?style=flat-square" alt="status badge">
  <img src="https://img.shields.io/badge/Python-3.9+-yellow?style=flat-square" alt="python badge">
  <img src="https://img.shields.io/github/last-commit/MakVlad2003/DS_girafe?style=flat-square" alt="last commit badge">
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="license badge">
</p>

> **Purpose:** A collection of laboratory works and Kaggle‑style contests completed within the **DS Girafe** data‑science training programme (MIPT, spring 2025).

---

## Table of Contents

1. [Repository Overview](#repository-overview)
2. [Quick Start](#quick-start)
3. [Environment](#environment)
4. [Folder Guide](#folder-guide)
5. [Useful Scripts](#useful-scripts)
6. [Contributing](#contributing)
7. [License](#license)

---

## Repository Overview

This repo is organised as a chronological archive of my progress through the **DS Girafe** curriculum:

```
DS_girafe/
├── LAB_1/          # Python & Numpy warm‑up notebook
├── LAB_2/          # Exploratory Data Analysis (Pandas, seaborn)
├── LAB_3/          # Intro to ML: scikit‑learn pipelines & metrics
├── Contest_1/      # Housing‑price regression challenge (tabular)
├── Contest_2/      # Image‑classification challenge (CNN baseline)
├── .gitignore
└── .gitattributes
```

<details>
<summary>What’s inside each folder?</summary>

* **LAB\_1** – vectorised operations, broadcasting, basic plotting.
* **LAB\_2** – data‑cleaning case study, feature engineering, correlation heat‑maps.
* **LAB\_3** – training/validation split, grid‑search, model interpretability.
* **Contest\_1** – LightGBM & CatBoost baselines, feature importance, CV.
* **Contest\_2** – Torchvision ResNet‑18 fine‑tune, albumentations, TTA.

</details>

---

## Quick Start

```bash
# clone and enter the repo
$ git clone https://github.com/MakVlad2003/DS_girafe.git && cd DS_girafe

# create a fresh environment (conda recommended)
$ conda create -n girafe python=3.9 -y
$ conda activate girafe

# install core dependencies
auth=$GITHUB_TOKEN   # optional to increase API rate‑limit
$ pip install -r requirements.txt  # auto‑generated from notebooks

# open the desired lab
$ jupyter lab LAB_2/LAB_2.ipynb
```

> **Tip:** GPU experiments for `Contest_2` require PyTorch ≥ 2.2 with CUDA; see [`Contest_2/README.md`](Contest_2/README.md) for details.

---

## Environment

A minimal `environment.yml` is provided for reproducibility:

```yaml
name: girafe
channels:
  - conda-forge
  - pytorch
dependencies:
  - python=3.9
  - jupyterlab
  - numpy
  - pandas
  - scikit-learn
  - matplotlib
  - seaborn
  - lightgbm
  - catboost
  - pytorch::pytorch
  - torchvision
  - albumentations
```

Install via `conda env create -f environment.yml`.

---

## Folder Guide

| Folder      | Format              | Key files                                                | Outcome                          |
| ----------- | ------------------- | -------------------------------------------------------- | -------------------------------- |
| `LAB_1`     | `.ipynb`            | `LAB_1.ipynb`                                            | Basics of numerical Python       |
| `LAB_2`     | `.ipynb`            | `LAB_2.ipynb`                                            | Full EDA on Titanic‑like dataset |
| `LAB_3`     | `.ipynb`            | `LAB_3.ipynb`                                            | End‑to‑end ML workflow           |
| `Contest_1` | notebooks & `.py`   | `eda.ipynb`, `lgbm_baseline.ipynb`, `make_submission.py` | Top‑30% leaderboard score        |
| `Contest_2` | notebooks & scripts | `train.py`, `predict.py`, `utils.py`                     | \~85 % accuracy on validation    |

---

## Useful Scripts

* `Contest_1/make_submission.py` – trains LightGBM with optimal params and saves `submission.csv`.
* `Contest_2/train.py` – command‑line training interface (see `--help` for args).
* `Contest_2/predict.py` – generate predictions on a folder of images.

---

## Contributing

Improvement ideas, bug fixes, and alternative model approaches are welcome:

1. Fork the repo and create your branch `git checkout -b feat/new-lab`.
2. Commit your changes with clear messages.
3. Open a PR – please follow the existing code‑style (PEP 8 + black).

---

## License

Distributed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

---

<p align="center">🚀 Happy Learning!</p>
