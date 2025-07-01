import pandas as pd

def load_csv(path):
    """CSV 파일을 불러와 pandas DataFrame으로 반환"""
    return pd.read_csv(path)

def save_csv(df, path):
    """DataFrame을 CSV 파일로 저장"""
    df.to_csv(path, index=False)