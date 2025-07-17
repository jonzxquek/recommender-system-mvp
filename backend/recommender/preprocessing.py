import pandas as pd

def load_data(filepath):
    
    """
    Load and preprocess product data
    """

    df = pd.read_csv(filepath)
    df.dropna(subset=['title', 'description'], inplace=True) #Remove missing rows
    print("Columns found:", df.columns.tolist())

    return df



