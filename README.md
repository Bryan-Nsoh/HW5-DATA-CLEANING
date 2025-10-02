# README

## What the original code was

* Hard coded input file name `data.csv`
* All work in global scope with no functions
* Manual loops for mean and standard deviation
* Little documentation and no error handling

## What I changed

* Split into functions: `load_data`, `compute_stats`, `sample_rows`, `plot_values`, `main`
* Added short docstrings and type hints
* Used Pandas for mean and population standard deviation (`std(ddof=0)`)
* Added basic validation for missing file, empty data, missing column, and nonnumeric values
* Replaced manual random indexing with `DataFrame.sample`

## Why this improves readability and maintainability

* Each function has a single job which makes the code easier to read and modify
* Vectorized operations are simpler and less error prone than manual loops
* Validation produces clear errors instead of silent failures

## How this helps a collaborator or future me

* Functions can be reused and tested in isolation
* Clear names and docstrings show intent
* Failures are explicit and faster to debug

## How to run

Place a CSV named `data.csv` in the same folder as `good_python.py`. The file must contain a column named `value`.

Run:

```bash
python good_python.py
```

Output includes:

* The average of the `value` column
* The population standard deviation of that column
* A printed sample of rows
* A simple line plot of the values

## Tests included

Inline assertions are defined in `_tests()` and are executed before `main()` runs.

* Success case: `compute_stats` on `[1, 2, 3, 4]` checks mean `2.5` and population stdev `1.1180`
* Failure case: `compute_stats` on an empty `value` column must raise `ValueError`

If tests pass, nothing extra is printed. If a test fails, an `AssertionError` is raised.
