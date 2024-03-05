# Plot-Graphs-in-Linux-using-Python
**Plotting charts in an Excel sheet using the openpyxl module in a Linux environment. This is done using a Python script. After creating the chart connect the local machine with the Linux environment using WinSCP and download the required files.**

## Script Functionality

### User input   
The script prompts the user for the following information:   
   Path to the CSV file.   
   Desired output filename (including the .xlsx extension).   
   Title for the line chart.

## Steps to run the script?

### 01. Install the necessary Python libraries
First, need to install the necessary libraries to run the script in the Linux environment.

   _**1. sudo apt update**_

   This command updates the list of available packages on your system. It's essential to keep the package list updated before installing new packages to ensure you get the latest versions.

   _**2. sudo apt install python3-pip**_
   
   This command installs the python3-pip package, which is the package manager for Python 3. It allows you to easily install and manage Python libraries.

   _**3. pip install pandas openpyxl**_

   Finally, this command uses pip to install the specific libraries required by your script:
      pandas: A popular library for data analysis and manipulation in Python.
      openpyxl: A library for reading and writing data to Excel (.xlsx) files.
