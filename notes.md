Project setup


Start by creating a new folder for the project and open it in the VSCode
Write a main.py file for testing it. Maybe print(”Hello World!”)
Now Open terminal. Shortcut ctrl + shift + ```
Ensure it is in powershell. Or open it in powershell manually
Type the following command to create a new virtual environment
python -m venv myenv
Once it is created click on yes button for the prompt asking to add the virtual interpreter to the workspace  folder
Now, activate the scripts
\myenv\Scripts\Activate.ps1
Now add a .gitignore file to ignore the myenv folder
Now create and Initialize a repository

- what is pyodbc
    - it is a driver (connectivity) btw python & db
    - list of tuples we are getting from database
- why we need cursor
    - large amount of data row wise without buffering
    - ram usage will be increased
    - large data(time+RAM)
    - Its like a bucket
    - CRUD -> we use .execute
    - Session mintainenance -> .close once quering is completed we close the connection
- developer experience
- seed data

- what is instance variable

- Breaking into DAO and Entity
- extensibility
    - every body can build on template
    - step by step process no confusion
- modularity
- readability

- ctrl+p to search file

when there is confusion which method to use then we use super

when there is no constructor in child class then base class constructor will be called.