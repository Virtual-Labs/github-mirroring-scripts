import json
import os
import sys

def get_all_repos():
	os.system(' curl -i "https://api.github.com/orgs/' + sys.argv[1] + '/repos?page=1&per_page=100" > owner.json')
	os.system(' curl -i "https://api.github.com/orgs/' + sys.argv[1] + '/repos?page=2&per_page=100" > second_page.json')
	remaining_URLs = ''

	with open('second_page.json', 'r') as remaining_list:
		remaining_URLs = remaining_list.read()

	with open('owner.json', 'a') as original_list:
		original_list.write(remaining_URLs)

	get_repo_urls()
	os.system('rm second_page.json')
def get_repo_urls():
	with open('owner.json') as input_file:   
		for line in input_file:
			key = line.split(':', 1)
			if key[0] == '    "clone_url"':
				repo_url = key[1]
				with open('repos_url.txt', 'a') as repo_data:
					repo_data.write(repo_url)

	os.system('rm owner.json')
	

get_all_repos()		
os.system('python modify_input.py ')	
