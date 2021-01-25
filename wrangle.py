from prepare import prep_corals
import pandas as pd 

def wrangle_corals():

    # importing data
    df = pd.read_csv('deep_sea_corals.csv')

    # using prep_corals to prepare data
    df = prep_corals(df)

    return df