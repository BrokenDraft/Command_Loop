# Command_Loop

Command_Loop is a Python script that execute all commands in a file with command error handling and logs. 
It has only been tested in Linux.

How to :

$ ./Command_Loop.py [Line at which to start] [The file to read] Optionaly : [Time between commandes]

By default : 
the time between commands is 0.3 seconds, and on Error, it loops 10 times.
If the 10th attempt fails. the script wait 10 minutes.

In err_logs file, you will find the error messages and the line at which they occur.
In log_file file, you will find the stdout output of the commands.

The file needs to have all commands aligned vertically.
