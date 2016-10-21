# 11_duplicates

This script finds duplicate files in folder and deletes them automatically.  
You can also choose manually which files to delete.

You can run the script using following command: _python duplicates.py \<path_to_folder\> -d \<arg\>_

_-d \<arg\>_ is optional. _\<arg\>_ can take following values:  
*_manual_ - **(set by default)** you will be able to choose what to delete or just show the list of duplicate files  
*_old_ - delete old duplicates **automatically**, only the **newest** file will be **left**  
*_new_ - delete new duplicates **automatically**, only the **oldest** file will be **left**

_Using in Windows:_ Oldest (newest) means that the file was **created** earlier (later) than all other files in duplicate group.  
_Using in Unix:_ Oldest (newest) means that the file was **modified** earlier (later) than all other files in duplicate group.

