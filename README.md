# Simple-Python-Command-Handler
A Simple Python Command Handler

This project was designed to be a neat and simple way to run different python files from the command line. 

**To run the command handler simply type: python3 main.py <commandname>**

If you don't supply a command name, the program will list all available commands that are stored in the commands directory. Giving a valid name will result in the python script being executed.

Modules of the commands are stored in the commands/modules directory. This is so the main file cannot directly call upon these scripts, and it also stops the module scripts from showing up in the available commands list.
