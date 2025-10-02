# good_python.py

from pathlib import Path
from typing import Tuple

import matplotlib.pyplot as plt
import pandas as pd


def load_data(csv_path: Path, required_column: str = "value") -> pd.DataFrame:
    """
    Load a CSV file into a DataFrame and validate it contains the required column.

    Parameters
    ----------
    csv_path : Path
        Path to the CSV file.
    required_column : str
        Name of the column that must exist in the CSV.

    Returns
    -------
    pd.DataFrame
        Loaded DataFrame.

    Raises
    ------
    FileNotFoundError
        If the file does not exist.
    ValueError
        If the file is empty or the required column is missing.
    """
    if not csv_path.exists():
        raise FileNotFoundError(f"File not found: {csv_path}")

    df = pd.read_csv(csv_path)

    if df.empty:
        raise ValueError("The input CSV is empty.")

    if required_column not in df.columns:
        raise ValueError(f"Missing required column: '{required_column}'")

    return df


def compute_stats(df: pd.DataFrame, column: str = "value") -> Tuple[float, float]:
    """
    Compute the mean and population standard deviation of a numeric column.

    Parameters
    ----------
    df : pd.DataFrame
        Data containing the target column.
    column : str
        Column to summarize.

    Returns
    -------
    Tuple[float, float]
        Mean and population standard deviation.

    Raises
    ------
    ValueError
        If the selected column has no numeric values.
    """
    series = pd.to_numeric(df[column], errors="coerce").dropna()
    if series.empty:
        raise ValueError(f"Column '{column}' has no numeric values.")
    mean = float(series.mean())
    stdev = float(series.std(ddof=0))
    return mean, stdev


def sample_rows(df: pd.DataFrame, n: int = 5, replace: bool = True) -> pd.DataFrame:
    """
    Sample rows from the DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        Source data.
    n : int
        Number of rows to sample.
    replace : bool
        Sample with replacement if True.

    Returns
    -------
    pd.DataFrame
        Sampled rows.
    """
    n = max(0, int(n))
    if df.empty or n == 0:
        return df.iloc[0:0]
    return df.sample(n=n, replace=replace, random_state=None)


def plot_values(df: pd.DataFrame, column: str = "value", title: str = "Values") -> None:
    """
    Plot the specified column.

    Parameters
    ----------
    df : pd.DataFrame
        Source data.
    column : str
        Column to plot.
    title : str
        Plot title.
    """
    plt.plot(df[column])
    plt.title(title)
    plt.show()


def _tests() -> None:
    """
    Minimal inline tests.
    Runs a success case and a failure case.
    """
    # success case
    df_ok = pd.DataFrame({"value": [1, 2, 3, 4]})
    m, s = compute_stats(df_ok)
    assert abs(m - 2.5) < 1e-9
    assert round(s, 4) == 1.1180  # population stdev

    # failure case
    try:
        compute_stats(pd.DataFrame({"value": []}))
        raise AssertionError("expected ValueError on empty input")
    except ValueError:
        pass


def main() -> None:
    csv_path = "data.csv"
    column = "value"
    samples = 5

    try:
        data = load_data(Path(csv_path), required_column=column)
        avg, stdev = compute_stats(data, column=column)

        print("average is", avg)
        print("std dev is", stdev)

        print("sample rows:")
        sampled = sample_rows(data, n=samples, replace=True)
        for _, row in sampled.iterrows():
            print(row)

        plot_values(data, column=column, title="Values")
    except (FileNotFoundError, ValueError) as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    _tests()
    main()
