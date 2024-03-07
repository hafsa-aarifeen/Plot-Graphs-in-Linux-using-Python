# Plot-Graphs-in-Linux-using-Python
**Plotting charts in an Excel sheet using the openpyxl module in a Linux environment by getting a CSV file as an input. This is done using a Python script. After creating the chart, connect the local machine to the Linux environment using WinSCP and download the required files.**

## Script Functionality

#### 01. User input   
* The script asks the user to input the following information:
    * Path to the CSV file.
    * output filename (including the .xlsx extension).
    * Preferred Title for the chart.

#### 02. Data Reading   
* The script uses the _Pandas_ library to read the data from the specified CSV file.   

#### 03. Workbook and Sheet Creation
* A new Excel workbook is created using the _Openpyxl library_.   
* A worksheet is created as the active sheet in the workbook.

#### 04. Data Importation
* The data from the _DataFrame_ is iterated over and appended to the worksheet row by row.

#### 05. Line Chart Creation
* A LineChart object is created using the Openpyxl library.

#### 06. Data Range Definition   
* The categories (X-axis) are referenced from the first column (column A) starting from row 2 and extending to the last row of data.
* The series (Y-axis) data points are referenced from columns B onwards (excluding column A) starting from row 1 and extending to the last row of data.

#### 07. Chart Data and Title   
* The data is added to the chart with titles automatically extracted from the first row of data.
* The chart title is set as per the user's input.
* A hardcoded style (number 10) is applied to the chart (you can customize this).

#### 08. Chart Placement
* The chart is added to the worksheet, anchored at the top-left corner of the cell specified by the output_cell variable, which is calculated based on the number of data columns.

#### 09. Output and Save   
* The final Excel file with the line chart is saved with the user-specified filename.
* A confirmation message is printed to the console, indicating the output file path.


## Steps to run the script    

#### 01.  Save the script as _csv_to_chart.py_    

#### 02. Place the CSV file in the same directory as the script   

#### 03. Open a terminal or command prompt and navigate to the directory.    

#### 04. Install the necessary Python libraries

* **sudo apt update**

   * This command updates the list of available packages on your system. It's essential to keep the package list updated before installing new packages to ensure you get the latest versions.

* **sudo apt install python3-pip**
   
   * This command installs the python3-pip package, which is the package manager for Python 3. It allows you to easily install and manage Python libraries.

* **pip install pandas openpyxl**

   * Finally, this command uses pip to install the specific libraries required by your script:
        pandas: A popular library for data analysis and manipulation in Python.
        openpyxl: A library for reading and writing data to Excel (.xlsx) files.    

#### 05. Run the script using _python csv_to_chart.py_    

#### 06. Enter the required input.
