import pandas as pd


def drop_unwanted_column(df: pd.DataFrame) -> pd.DataFrame:
    """
    remove rows that have column names. This error originated from
    the data collection stage.
    """
    unwanted_rows = df[df['retweet_count'] == 'retweet_count'].index
    df.drop(unwanted_rows, inplace=True)
    df = df[df['polarity'] != 'polarity']

    return df


def drop_duplicate(df: pd.DataFrame) -> pd.DataFrame:
    """
    drop duplicate rows
    """
    df.drop_duplicates(['screen_name', 'original_text', 'created_at'], keep="first")

    return df
