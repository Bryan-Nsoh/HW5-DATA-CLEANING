# README

## What the original code was

* Hard coded input file name data.csv
* All work in global scope with no functions
* Manual loops for mean and standard deviation
* Little documentation and no error handling

## What I changed

* Split into functions: `load_data`, `compute_stats`, `sample_rows`, `plot_values`, `main`
* Used Pandas for mean and population standard deviation (`std(ddof=0)`)
* Added basic validation for missing file, empty data, missing column, and nonnumeric values
* Added short docstrings and type hints

## Why this improves readability and maintainability

* Each function has a single job which makes the code easier to read and modify
* Vectorized operations are simpler and less error prone than manual loops
* Validation produces clear errors instead of silent failures

## How this helps a collaborator or future me

* Functions can be reused and tested in isolation
* Clear errors make debugging faster
* The intent of each step is visible from names and docstrings

## Tests required by the assignment

Run `good_python.py` with the following inputs.

1. Failure case: empty input
   Create `data.csv` with only a header:

```
value
```

Expected: prints `Error: The input CSV is empty.`

2. Failure case: missing required column
   Create `data.csv` with a wrong header:

```
wrong
1
2
```

Expected: prints `Error: Missing required column: 'value'`
