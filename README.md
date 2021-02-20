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

Install prepare.py and/or wrangle.py file(s) into your working directory.

Download the data into your working directory. (Link below)

https://www.kaggle.com/noaa/deep-sea-corals

Run the jupyter notebook.

# Conclusions

### Generally, observations come from clusters around the world, most notably
- Southwest of Alaska
- East/Southeast of the U.S.
- South of Brasil
- Southeast of China
- Southeast of Australia
    

### The 5 institutions that have provided the most data for this data set are
- Monterey Bay Aquarium Research Institute (31%)
- NOAA alaska fisheries science center (13%)
- Hawaii undersea research laboratory (13%)
- NOAA, Olympic Coast Sanctuary (9%)
- NOAA, Southwest Center, Santa Cruz (9%)
    
    
### Approximately 46% of all of the data comes from NOAA facilities


### The areas of the world where different facilities made their observations can vary immensely
- NOAA's observations are all near Alaska
- The Monterey Bay Institute observations are all west of the U.S.
- The Hawaiian Lab's are unsurprisingly, near Hawaii
- The other facilities' observations are scattered around the world, namely
    - East/Southeast of the U.S.
    - Southof Brasil
    - Southeast of China
        

### The dates of the observations range from 1868-05-04 to 2016-03-27


### The areas where observations were made also varies greatly between 20-30 year time windows
- Observations from prior to 1900 are few and mostly to east of the U.S.
- Observations from 1900 - 1919 are mostly from east and southeast of China
- Observations from 1920 - 1949 are almost non-existent except for a few north of Brasil
- Observations from 1950 - 1979 are mostly
    - Between Brasil and the U.S.
    - South of Brasil
    - Southeast of Australia
- Observations from 1980 - 1999 are sprinkled around Alaska, Brasil, Australia
- Observations from 2000 and beyond are clustered
    - Southwest of Alaska
    - West and southeast of the U.S.
    - Southeast of Brasil
    - East of Australia


### The depths of the observations range 0 meters to 5303 meters

### Depth values were binned into 4 distinct ranges of depth and the following observations were made with regard to the binned coral's locations
- The shallowest coral (-.001m to 269m) were mainly found
    - Southwest of Alaska
    - Around the southeast coast of the U.S.
    - South of Brasil
    - Southeast of China
    - East of Russia

- Third deepest set of coral (269m to 563m) are scattered around the map with the largest cluster being near Antartica

- Second deepest set of coral (563m to 1089m) are also scattered around the map with no discernablely larger clusters in any particular areas

- Deepest set of coral (1089m to 5303m) were mainly found
    - To the east and west of the U.S.
    - Around Hawaii
    

### There are 10 different types of corals in the data (type in this case refers to vernacular name such as black coral, stone coral, etc.)


### The most common corals are as follows
- Gorgonian corals are the most common (56%)
- Soft corals are the second most common (16%)
- Black corals are the third most common (9%)
- Lace corals are the third most common (8%)
- All other corals make up 5% or less of the data


### The locations of the most common corals are as follows
- Gorgonian corals were found mostly
    - South of Brasil
    - Around Antartica
    - Scattered around the U.S., including Alaska
- Soft corals are all west of Alaska
- Black corals are clustered around the U.S. and west/southwest of the U.S.
- Lace corals are mostly near Alaska
    - There are a few smaller clusters near Florida, south of Brasil, and east/southeast of Australia
    

### The locations of the least common corals are as follows
- Stony Coral (Branching) were mainly near the northern coast of Brasil and near Florida
- Stony Coral (Cup) appear in many places, namely
    - Along the U.S. coasts
    - South of Brasil
    - Near Antartica
    - Southeast of China
    - East of Australia
- Stony (Unspecified) were mainly found near Alaska and the eastern coast of the U.S.
- Gold coral are very uncommon and mainly found near Hawaii
- Stoloniferan are mainly found near Hawaii

### The most common sampling equipment were as follows
- Vast majority of samples were collected using a ROV (Remotely Operated Vehicle) (63%)
- Submersibles were used the second most (20%)
- All other equipment was used in 6% or less of instances


### The most common qualification methods are as follows
- Videos qualified 70% of observations
- Images qualified 17% of observations
- Other methods qualified 12% of observations
- Combined, roughly 87% of the data was was qualified with either images or video



