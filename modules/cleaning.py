# Helper functions for data extraction and cleaning

import pandas as pd

# extracts a data frame for a specific college
def extract_college(file, college):

    df = pd.read_csv(file)

    return df
