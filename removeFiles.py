# importing modules
import os
import shutil
import time

# main function
def main():

	# initializing the counts
	deleted_folders_count = 0
	deleted_files_count = 0

	# ask user for the path
	path = input("Which path do you want to delete a file/ files from? ")

	# specify the maximum number of days old a file/folder must be (to not get deleted)
	days = 30

	# a very large number of seconds minus the maximum number of seconds old a file/folder must be
	# this is the format we will get file/ folder age in
	# therefore a folder/file age lower than this 'seconds variable' must get deleted (too old)
	seconds = time.time() - days*24*60*60

	# checking whether the path exists
	if os.path.exists(path):

		# iterating over every folder and file in the path
		# root_folder equals main folder, folders equals subfolders, and files equals subfiles
		for root_folder, folders, files in os.walk(path):

			# checking if the main folder age is lower than seconds variable
			# if it is the folder is too old and will get deleted
			if seconds >= get_file_or_folder_age(root_folder):

				# removing the folder
				remove_folder(root_folder)
				deleted_folders_count += 1 # incrementing count

				# breaking after removing the main folder
				break

			else:

				# checking subfolders in the main folder
				for folder in folders:

					# folder path is made by joining main folder path and subfolder
					folder_path = os.path.join(root_folder, folder)

					# checking if the subfolder age is lower than seconds variable
					# if it is the folder is too old and will get deleted
					if seconds >= get_file_or_folder_age(folder_path):

						# removing the folder
						remove_folder(folder_path)
						deleted_folders_count += 1 # incrementing count


				# checking subfiles in the main folder
				for file in files:

					# file path is made by joining main folder path and subfile
					file_path = os.path.join(root_folder, file)

					# checking if the subfile age is lower than seconds variable
					# if it is the file is too old and will get deleted
					if seconds >= get_file_or_folder_age(file_path):

						# removing the file
						remove_file(file_path)
						deleted_files_count += 1 # incrementing count

		else:

			# if the path is not a folder
			# checking if the file age is lower than seconds variable
			# if it is the file is too old and will get deleted
			if seconds >= get_file_or_folder_age(path):

				# removing the file
				remove_file(path)
				deleted_files_count += 1 # incrementing count

	else:

		# file/folder is not found
		print(f'"{path}" is not found')

	print(f"Total folders deleted: {deleted_folders_count}")
	print(f"Total files deleted: {deleted_files_count}")


# function to remove folder
def remove_folder(path):

	# removing the folder
	if not shutil.rmtree(path):

		# success message
		print(f"{path} is removed successfully")

	else:

		# failure message
		print(f"Unable to delete the " + path)


# function to remove file
def remove_file(path):

	# removing the file
	if not os.remove(path):

		# success message
		print(f"{path} is removed successfully")

	else:

		# failure message
		print("Unable to delete the " + path)


# function to get file or folder age
def get_file_or_folder_age(path):

	# getting ctime of the file/folder
	# time will be in seconds
	ctime = os.stat(path).st_ctime

	# returning the time
	return ctime


# calling main function
main()