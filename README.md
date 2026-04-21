# NFL Wide Receiver Efficiency Frontier
### Cap Spending vs. On-Field Production — Pittsburgh Steelers Deep Dive (2020–2025)

## Project Info
**Class** INFSCI 1530/2160 Data Mining (2231) 
**Semester** Spring 2026
**Instructor** Lingfei Wu
**Student** Ethan He (Eth69)

## Overview

This project maps five years of NFL play-by-play EPA data against salary cap commitments to evaluate wide receiver value. KMeans clustering (k=4) classifies every notable WR season from 2020–2025 into one of four archetypes: **Efficient Steal**, **Elite Earner**, **Cap Casualty**, or **Developmental**. The Pittsburgh Steelers are used as a case study.

## Files
 
| File | Description |
|------|-------------|
| `steelers_wr_efficiency_2020_2025.ipynb` | Full Jupyter notebook |
| `gen_figs.py` | Script to regenerate figures |
| `fig_scatter.png` | Main efficiency frontier scatter plot |
| `fig_trajectory.png` | Steelers EPA trajectory by player |
| `wr_cap_data.csv` | Cap hit data by player and season (2020–2025) — manually compiled from Spotrac |
| `NFL_WR_Efficiency_Report_Ethan_He.pdf` | Final project report |
 

## Data Sources
 
| Source | Description |
|--------|-------------|
| [nfl_data_py](https://github.com/nflverse/nfl_data_py) | Play-by-play EPA, ~270K rows per season (2020–2025). Downloaded automatically when running the notebook. |
| [Spotrac](https://www.spotrac.com) / [Over The Cap](https://overthecap.com) | WR cap hits by season (2020–2025). Manually compiled and saved as `wr_cap_data.csv` in this repo. |
 
> **Note:** The raw EPA play-by-play data (~1GB) is not included in this repository as it is downloaded automatically by `nfl_data_py` on first run. The cap hit data (`wr_cap_data.csv`) is included here as it was manually compiled and cannot be auto-downloaded.

## Setup

```bash
pip install nfl_data_py pandas numpy scikit-learn plotly matplotlib
jupyter notebook steelers_wr_efficiency_2020_2025.ipynb
```

To regenerate figures only:
```bash
python gen_figs.py
```

## Data Sources

- **EPA:** [nfl_data_py](https://github.com/nflverse/nfl_data_py) — play-by-play data (2020–2025)
- **Cap hits:** [Spotrac](https://www.spotrac.com) / [Over The Cap](https://overthecap.com)