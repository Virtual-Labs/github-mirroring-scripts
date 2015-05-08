import os
import sys

os.system('python get_repo_list.py ' + sys.argv[1])
os.system('python backup.py ' + sys.argv[1])
