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