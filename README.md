# Deep Sea Coral Repository

# About this project

The data used in this project comes from the National Oceanic and Atmospheric Administration (NOAA) and is free to use as it is within the public domain. The data can found at NOAA's official website or the URL below.

https://www.kaggle.com/noaa/deep-sea-corals

"This dataset contains information about deep sea corals and sponges collected by NOAA and NOAA’s partners. Amongst the data are geo locations of deep sea corals and sponges and the whole thing is tailored to the occurrences of azooxanthellates - a subset of all corals and all sponge species (i.e. they don't have symbiotic relationships with certain microbes). Additionally, these records only consists of observations deeper than 50 meters to truly focus on the deep sea corals and sponges." [Source](https://www.kaggle.com/noaa/deep-sea-corals)

Please note that although this project uses data from NOAA, they do not endorse this project.

# Project Goal

The goal of this project is to draw insights about various coral in addition to the facilities and methods used to observe them.

# Data Dictionary 

[Source of original columns](https://www.kaggle.com/noaa/deep-sea-corals)

OriginalColumn (updated_name_after_prep): definition of data

location_accuracy	repository

CatalogNumber: Unique record identifier assigned by the Deep-Sea Coral Research and Technology Program.

DataProvider (data_provider): The institution, publication, or individual who ultimately deserves credit for acquiring or aggregating the data and making it available.

ScientificName (scientific_name): Taxonomic identification of the sample as a Latin binomial.

VernacularNameCategory (vernacular_name_category): Common (vernacular) name category of the organism.

TaxonRank (taxon_rank): Identifies the level in the taxonomic hierarchy of the ScientificName term.

ObservationDate (observation_date): Time as hh:mm:ss when the sample/observation occurred (UTC).

Latitude (latitude): Degrees north; Latitude in decimal degrees where the sample or observation was collected.

Longitude (longitude): Degrees east; Longitude in decimal degrees where the sample or observation was collected.

DepthInMeters (depth_meters): Best single depth value for sample as a positive value in meters.

DepthMethod (depth_method): Method by which best singular depth in meters (DepthInMeters) was determined. "Averaged" when start and stop depths were averaged. "Assigned" when depth was derived from bathymetry at the location. "Reported" when depth was reported based on instrumentation or described in literature.

Locality: A specific named place or named feature of origin for the specimen or observation (e.g., Dixon Entrance, Diaphus Bank, or Sur Ridge). Multiple locality names can be separated by a semicolon, arranged in a list from largest to smallest area (e.g., Gulf of Mexico; West Florida Shelf, Pulley Ridge).

IdentificationQualifier (identification_qualifier): Taxonomic identification method and level of expertise. Examples: “genetic ID”; “morphological ID from sample by taxonomic expert”; “ID by expert from image”; “ID by non-expert from video”; etc.

SamplingEquipment (sampling_equipment): Method of data collection. Examples: ROV, submersible, towed camera, SCUBA, etc.

Repository (repository): Institution that is credited with the observation.

RecordType (record_type): Denotes the origin and type of record. published literature ("literature"); a collected specimen ("specimen"); observation from a still image ("still image"); observation from video ("video observation"); notation without a specimen or image ("notation"); or observation from trawl surveys, longline surveys, and/or observer records ("catch record").

__Engineered Features__
gen_qual_method: Holds binned values of IdentificationQualifier (video, image, other)

depth_bin: Holds binned values of DepthInMeters. Values are binned by quartiles.

# Project Plan

- Acquire
    - Download data from Kaggle and save as CSV file
    - Import data into Jupyter Notebook via pandas and save as data frame

- Prepare
    - Prepare data as needed for exploration including but not limited to
        - Dropping unneeded columns
        - Converting all string column values to lower case
        - Updated column names
            - Convert to lower case
            - Change spaces ot underscores
            - Update terms to facilitate understanding
        - Update data types as needed to facilitate expected operations
        - Handle null values via imputing or dropping
        - Convert dates to datetime format if appropriate for exepected operations

- Exploration
    - Explore data to gather insights about coral and the data related to the methods used to observe them via 
        - Identifying min/max values of numerical columns
        - Creating visualizations that represents different facets of the data
            - Visualizations should include maps that reflect geographic data

- Conclusions
    - Summarize findings from exploration

# How to Reproduce

Download data into your working directory. (Link below)

https://www.kaggle.com/noaa/deep-sea-corals

Run the jupyter notebook.
