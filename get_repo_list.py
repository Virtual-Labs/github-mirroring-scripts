import json
import os
import sys

def get_all_repos():
	os.system('curl -i "https://api.github.com/orgs/' + sys.argv[1] + '/repos?per_page=200" > owner.json')
	get_repo_urls()
	
def get_repo_urls():
	with open('owner.json') as input_file:
		count = 0    
		for line in input_file:
			key = line.split(':', 1)
			if key[0] == '    "clone_url"':
				repo_url = key[1]
				with open('repos_url.txt', 'a') as repo_data:
					repo_data.write(repo_url)

	os.system('rm owner.json')
	

get_all_repos()			
