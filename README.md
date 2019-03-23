# FindWord
Personal code I have written to find a lost corrupted word file text 

So this short script has few steps we have to perform in order to make it work :)
First and foremost, if we accidentally deleted our word file- we have to restore it! I used minitool(gooled it)
Func: rename_files_ziprar:
After Finding the possible options and placed them in my desired directory, I have renamed the .doc files into ..zip 
since doc file is actually a directory!
unzip_displace:
later on, I have Extracted all the Files and Logged all the data to catch all the possible failed extractions 
Investigation+read_xml:
In the end- I searched for each and every folder for the word.xml file since this file is the one that contains all text data of the word file,
and when I found one- I have ran on every line of that XML to search for a specific word that I know to exist in the word file itself.


