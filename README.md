# Files-Comparator
Compare spreadsheet documents of the same name in different folders of the same directory and outputs results.

### Requirements

- [Python 2.7](https://www.python.org/downloads/release/python-2715/) (For generation of fileList)
- Excel 2007 onwards ([Macro-enabled](https://support.office.com/en-us/article/enable-or-disable-macros-in-office-files-12b036fd-d140-4e74-b45e-16fed1a7e5c6))

### Purpose

Checking different versions of a spreadsheet document for even a slight change in content is an arduous task and with thousands of files, it would take an immense amount of time to do it manually. This project aims to shorten the time taken and remove most of the manual work required. It was originally targeted to be used for CSV files which contain column headers and a unique identifier for each row entry but can be expanded to handle other general documents such as normal spreadsheet tables and text files which have been formatted to have a unique identifier of entries in the first column.

This project will do the following:
- Generating a simple hash (MD5) for each versions of the file to compare and store the file names in a text file.
- Using this list of files, the Excel macro will then do the detailed comparison and outputs the result in a document of the same name which will be saved in another folder.
- The resulting documents will contain the difference between the files that were compared, with additional formatting to highlight any changes the macro detected.
- An error log is generated for the user to review any errors that arise during the comparison.

## Usage

Put the files to be checked into both 'old' and 'new' folders. (Test files have been provided)
If required, the directory of files to be checked can be changed by changing the path in `os.listdir('new/')` and `os.listdir('old/')`.

To generate the list of changed files, run the Python script. A fileList text file will be generated that contains the list of files that have changed.

Example of text file:
```
thisisfile1.csv
thisisfile3.txt
thisisfile64.xlsx
```
Once fileList is generated, open up the Excel Workbook and read the instructions provided in. Run the macro by clicking on the `Generate comparison` button provided in the first sheet. Results are stored in the `result` folder in their respective file names.

## License
This project is licensed under the MIT License - see `LICENSE.md` file for details
