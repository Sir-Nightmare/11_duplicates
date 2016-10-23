# 11_duplicates

This script finds duplicate files in folder and deletes them automatically.  
You can also choose manually which files to delete.  
You can run the script using following command: `python duplicates.py <path_to_folder> -d <arg>`

`-d <arg>` is optional. `<arg>` can take following values:
* `manual` -  (set by default) you will be able to choose what to delete or just show the list of duplicate files
* `old` - delete old duplicates **automatically**, only the newest file will be left
* `new` - delete new duplicates **automatically**, only the oldest file will be left

**_Using in Windows:_** oldest (newest) means that the file was **created** earlier (later) than all other files in duplicate group.  
**_Using in Unix:_** oldest (newest) means that the file was **modified** earlier (later) than all other files in duplicate group.

