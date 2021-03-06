# this script customizes and creates the .htaccess to correspond to the current directory

import os

def create_htaccess():
	f = open('./.htaccess','w') 
	# get directory path
	directory = os.getcwd() 

	# if linux
	if os.name == 'posix':
		dirname = directory[directory.rfind('/')+1:]
	# if windows
	elif os.name == 'nt':
		dirname = directory[directory.rfind("\\")+1:]
	else:
		exit('error occurred: couldnt determine the system this computer is on')

	
	
	f.write('''
	# http://codeigniter.com/wiki/mod_rewrite
	# make sure you change the root url on line 27 RewriteRule ^(.*)$ directory/index.php?/$1 [L]

	<IfModule mod_rewrite.c>
	    RewriteEngine On
	    RewriteBase /

	    #Removes access to the system folder by users.
	    #Additionally this will allow you to create a System.php controller,
	    #previously this would not have been possible.
	    #'system' can be replaced if you have renamed your system folder.
	    RewriteCond %{REQUEST_URI} ^system.*
	    RewriteRule ^(.*)$ /index.php?/$1 [L]
	    
	    #When your application folder isn't in the system folder
	    #This snippet prevents user access to the application folder
	    #Submitted by: Fabdrol
	    #Rename 'application' to your applications folder name.
	    RewriteCond %{REQUEST_URI} ^application.*
	    RewriteRule ^(.*)$ /index.php?/$1 [L]

	    #Checks to see if the user is attempting to access a valid file,
	    #such as an image or css document, if this isn't true it sends the
	    #request to index.php
	    RewriteCond %{REQUEST_FILENAME} !-f
	    RewriteCond %{REQUEST_FILENAME} !-d
	    RewriteRule ^(.*)$ '''+ dirname + '''/index.php?/$1 [L]
	</IfModule>

	<IfModule !mod_rewrite.c>
	    # If we don't have mod_rewrite installed, all 404's
	    # can be sent to index.php, and everything works as normal.
	    # Submitted by: ElliotHaughin

	    ErrorDocument 404 /index.php
	</IfModule>  
	''')
	f.close()

if __name__ == '__main__':
	create_htaccess()	

