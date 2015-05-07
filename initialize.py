import os

os.system('python get_repo_list.py')

result = os.path.exists('existing_github_repo_list.txt')
if result == False:
	os.system('python modify_input.py existing_github_repo_list.txt')

else:
	os.system('python modify_input.py latest_github_repo_list.txt')
