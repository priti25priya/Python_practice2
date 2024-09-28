# if __name__=="__main__": If the python interpreter is running that module (the source file) as the
# main program, it sets the special __name__ variable to have a value “__main__”.
# If this file is being imported from another module, __name__ will be set to the module’s name.
# Module’s name is available as value to __name__ global variable.
print ("Always executed")

if __name__ == "__main__":
	print ("Executed when invoked directly")
else:
	print ("Executed when imported")
