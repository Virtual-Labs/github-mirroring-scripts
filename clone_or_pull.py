import os

cmd = ''
with open('latest_github_repo_list.txt', 'r') as current_list:
	for line in current_list:
		repo_name = line.split('/')[-1].split('.git')[0]
		if line in open('existing_github_repo_list.txt').read():
			cmd = 'git --git-dir=%s%s%s %s' % ('/root/Virtual-labs/', repo_name, '/.git', 'pull')
			os.system(cmd)
		else:
			cmd = 'git clone %s %s%s' % (line.strip(), 'Virtual-labs/', repo_name)
			os.system(cmd)	
