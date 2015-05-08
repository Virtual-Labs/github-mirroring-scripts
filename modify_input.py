import os
import sys

with open('repos_url.txt', 'rw') as raw_input_file:
	for line in raw_input_file:
                line = line[2:-3]
                with open('list_of_repos.txt', 'a') as refined_input_file:
                        refined_input_file.write(line + '\n')
        os.system('rm repos_url.txt')
