from sys import exit

# abort function to be used before functions that require libraries
def abort_early() -> None:
	input('\nIt appears that you are using an unsupported operating system. Please use Windows or Linux.\n\nPress Enter to exit.')
	exit()
