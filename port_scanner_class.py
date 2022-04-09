# !python3
# Socket transforms Unix system call and library interfaces for sockets into objects that Python can work with
import socket 

# Subprocess allows the program to run subprocess on the system terminal, in this case the MacOS terminal ZSH
import subprocess

# Sys is the standard python library for interacting with the operating system.
import sys

# Datetime allows for... timekeeping. It can be used to let you know how long requests and processes took to complete.
from datetime import datetime

class Port_Scanner:
	# Initialize Scanner variables
	def __init__(self):
		self.remote_host = ""
		# Output kept in list for future functionality
		# TODO: Add print functionality to store output as file
		self.output = []
		self.scan_time = 0


	# Clear the terminal screen to maximize legibility
	def clear_screen(self) -> None:
		subprocess.call('clear', shell=True)

	# Prompt the user for a host to scan
	# TODO: Add input sanitization for remote host entry
	# TODO: Allow for custom port ranges
	def get_remote_host(self) -> None:
		remote_host_temp = input("Enter an remote host to scan: ")
		self.remote_host = socket.gethostbyname(remote_host_temp)
		print("Target locked in.")

	# Banner to entertain people while the program is running
	def scan_banner(self) -> None:
		print("*"* 80)
		print(" "*34 + "Scanning... " + " "*34)
		print("*"* 80)

	def scan(self) -> None:
		# Get start time to see how long program ran
		start_time = datetime.now()
		self.clear_screen()
		# Title screen
		print("\n\n\n" + "*"*30 + "\tSuper Simple Python Port Scanner\t" + "*"*30 + "\n\n\n")
		try:
			self.get_remote_host()
			print(f"Scanning... Go make some tea, this could take a while")
			for port in range(1, 100):
				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				result = sock.connect_ex((self.remote_host, port))
				if result == 0:
					self.output.append(f"Port {port}\tOpen")
				sock.close()
		except KeyboardInterrupt:
			print("\nGuess you changed your mind...")
			sys.exit()
		
		except socket.gaierror:
			# TODO: Add option to try again.
			print("Hostname could not be resolved.")
			sys.exit()
		
		except socket.error:
			print("Couldn't connect to host")
			sys.exit()

		self.scan_time = datetime.now() - start_time

		print(f"Results:")
		for port in self.output:
			print(port)
		if not self.output:
			print("\nNo open ports.")
		
		print(f"\nScan completed in: {self.scan_time}")