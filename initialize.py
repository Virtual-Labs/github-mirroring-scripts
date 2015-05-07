import os
import sys

os.system('mkdir Virtual-labs/')	
os.system('python get_repo_list.py ' + sys.argv[1])

result = os.path.exists('existing_github_repo_list.txt')
if result == False:
	os.system('python modify_input.py existing_github_repo_list.txt')
	os.system('python clone.py')
else:
	os.system('python modify_input.py latest_github_repo_list.txt')
	os.system('python clone_or_pull.py')
