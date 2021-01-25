# establishing environment
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

def prep_corals(df):
    # dropping specified columns
    df = df.drop(columns = ['CatalogNumber', 'SampleID', 'SurveyID', 'EventID', 'Station', 'Locality'])

    # dropping all null values
    df = df.dropna()

    # converting ObservationDate to datetime format
    df['ObservationDate']= pd.to_datetime(df['ObservationDate'])

    # adding underscores to various column names
    df.columns = ['Data_Provider', 'Scientific_Name', 'Vernacular_Name_Category', 'Taxon_Rank', 
    'Observation_Date', 'latitude', 'longitude', 'Depth_Meters','Depth_Method', 
    'Location_Accuracy', 'Repository', 'Identification_Qualifier', 'Sampling_Equipment', 
    'Record_Type']

    # lower casing all column names
    df.columns = df.columns.str.lower()

    # lower casing all string values
    df = df.applymap(lambda string:string.lower() if type(string) == str else string)

    # filtering out all rows with negative meters
    df = df[df.depth_meters >= 0]

    # filtering out all creatures that are not corals
    df = df[df.vernacular_name_category.str.contains('coral') & (df.vernacular_name_category.str.contains('hydrozoan') == False)]

    # returning df
    return df