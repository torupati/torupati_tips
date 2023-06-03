# Memo to Logging Datetime

Here, I want to veryfy 
1. write datetime in C in csv file.
2. read the csv file in python pandas.

For this purpose, I can use

- (C) Function gmtime to convert time_t to struct tm to pass strftime.
- (python) do_datetime of pandas is smart that convert strting of
  datetime if automatically converted into datetime64. One can spefify
  the time string format in the argument format="%Y...", but this is
  not necessary in this case.



https://stackoverflow.com/questions/26763344/convert-pandas-column-to-datetime


