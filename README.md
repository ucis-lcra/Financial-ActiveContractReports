# Financial Active Contract Report

A Flask based project that allows the user to interact with the LogosDB to run a report
giving them the Active Contracts within the datas that they specificy.

# Project Overview
This project will allow a user to run a report from the Financial system database with two specificed dates. These dates the the *Contract Start Date* and *Contract Expiration Date*. 

Once these two dates are entered and the user presses the submit button. 
# Installation 
This will be updated during first production employment with screenshots of installation process. 

### **Create Python Virtual Environment**
From within the project directory run the following command

    python3 -m venv <name_of_virtualenv>

In this case, we would have ran 

    python3 -m venv active_contracts
### **Enter the Virtual Environment**

From the command line within the top level of the repository, you can use the following command to enter the Virtual Environment.

    active_contracts\Scripts\activate.bat
### **Install Needed Dependencies**
Within the main project directory, we can install the requirements with the following command

    pip install -r requirements.txt

### **Available Commands**
    
Allows the project to run in development mode.

    py app.py 

Once the project is up and running it can be accessed via the following link

    http://localhost:5000/
# Tech Stack
This project is built with the following tech stack:
* HTML
* Python
    * *Pip List - These are also listed in requirements.txt*
        * click           8.1.3
        * colorama        0.4.4
        * Flask           2.1.2
        * itsdangerous    2.1.2
        * Jinja2          3.1.2
        * MarkupSafe      2.1.1
        * numpy           1.22.3
        * pandas          1.4.2
        * pip             22.0.4
        * pyodbc          4.0.32
        * python-dateutil 2.8.2
        * pytz            2022.1
        * setuptools      58.1.0
        * six             1.16.0
        * Werkzeug        2.1.2
* SQL


# Links

- [Repo](https://github.com/ucis-jare/Financial-ActiveContractReports "<project-name> Repo")


## Directory Overview
* Main Directory        
`Holds the Git files, the Pip Freeze file and main App.py that will run the app`
    * Active Contracts  
    `Holds the Virtual Environment`
    * Scripts          
     `Holds the Python Scripts`
    * Static            
    `Holds the static CSS and Data files`
        * CSS           
        `Main CSS file in this folder`
        * Data          
        `Holds the created CSV Files`
    * Templates         
    `Holds the HTML files`



# Screenshots

### Main Menu
![Main Menu](/static/imgs/mainpage.png "Main Menu")

### Download Page
![Download Page](/static/imgs/downloadpage.png "Download Page")

### Downloading File
![Downloading File](/static/imgs/downloadfile.png "Downloading File")