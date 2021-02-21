# establishing environment
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

def prep_corals(df):
    """
    Function accepts raw coral DF and returns it prepared for exploration.
    """
    # dropping specified columns
    df = df.drop(columns = ['CatalogNumber', 'SampleID', 'SurveyID', 'EventID', 'LocationAccuracy', 
                            'Station', 'Locality', 'DepthMethod', 'ScientificName', 'TaxonRank'])

    # dropping duplicate rows since all rows should have unique sample ids at a minimum
    df.drop_duplicates(inplace = True)

    # dropping all null values
    df = df.dropna()

    # converting ObservationDate to datetime format
    df['ObservationDate']= pd.to_datetime(df['ObservationDate'])

    # adding underscores to various column names
    df.columns = ['Data_Provider', 'Vernacular_Name_Category', 'Observation_Date', 'latitude', 
                  'longitude', 'Depth_Meters', 'Repository', 'Identification_Qualifier', 'Sampling_Equipment', 'Record_Type']

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