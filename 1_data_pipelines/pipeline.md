# data pipelines

## Solution

The dataset file is to be dropped to landing folder before 1pm everyday.

Scheduler such as Window Task Scheduler can be used to schedule the daily run to ingest the data by triggering the the Python script to run.


## Ingestion

The Python script is designed to pickup multiple files in the landing folder.
It will load and transform the data and the incrementally load to the output csv.
The processed file will be archived with the datetime stamp appended to the file name.