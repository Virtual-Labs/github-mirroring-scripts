import os
import sys

filename = sys.argv[1]

with open('repos_url.txt', 'rw') as raw_input_file:
	for line in raw_input_file:
                line = line[2:-3]
                with open(sys.argv[1], 'a') as refined_input_file:
                        refined_input_file.write(line + '\n')
        os.system('rm repos_url.txt')
