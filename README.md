# datamining_code
Used for make life easier when dealing with pre/post processing of the data. Mainly use pandas and mathlib library using python, and data analysis using mySQL sql.

## Python
### probe.py
    Used to generate 11000 row of instruments in csv format for the purpose of probing kaggle for specific instruments

### autofill_playmethod.py
    Used to identify the instruments in the training dataset and prepopulate the playmethod fields [string, blown, struck_Hrm], depending on the rules stated in the array. 

 ### autofill_class.py
    Used to identify the instruments in the training dataset and prepopulate the class1 and class2 fields [string, blown, struck_Hrm], depending on the rules stated in the array.

## mySQL

### auto_import.sql
    Used to speedup the import process over the wizard

### analysis_for_dataset.sql

    Multiple queries to analyse the attributes and instances relations in both test and train dataset. 
