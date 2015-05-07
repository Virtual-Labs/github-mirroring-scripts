import os
import sys

with open('existing_github_repo_list.txt' , 'r') as clone_url_list:
	cmd = ''
	for clone_url in clone_url_list:
		clone_url = clone_url.strip()
		repo_name = clone_url.split('/')[-1].split('.git')[0]
		cmd = 'git clone %s %s%s' % (clone_url, 'Virtual-labs/', repo_name)
		print cmd
		os.system(cmd)
