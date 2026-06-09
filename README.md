# Simple Linear Regression -- Debugging Practice

Coding 2 homework, companion to **Lecture 12: Simple Linear Regression**.

## The project

`analysis.ipynb` fits and interprets a one-predictor linear regression of salary on training hours using `data/career_outcomes.csv`. It follows the workflow from the
lecture:

1. Visualise salary against training hours.
2. Fit the regression and interpret the slope.
3. Predict salaries for new workers and inspect the residuals.

## Your task

This project does not yet work the way it should. Clone it, get it running, and read it
critically: make sure every step actually does what it claims to do and that the
conclusions it reaches are justified. Fix whatever you find.

Work like an analyst reviewing a colleague's notebook -- at each step, ask where this could
go wrong and whether you believe the numbers.

You may use an LLM to help, but treat its suggestions as drafts: check them against the
data and against what the lecture says a sound workflow looks like.

## Running it

```bash
uv sync
uv run jupyter lab        # open analysis.ipynb and run it top to bottom
```

To execute the whole notebook from the command line:

```bash
uv run jupyter nbconvert --to notebook --execute analysis.ipynb --stdout
```

## Data

`data/career_outcomes.csv` is a small synthetic teaching dataset; no downloads are needed.
