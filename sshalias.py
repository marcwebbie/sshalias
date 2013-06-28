#!/usr/bin/env python
import argparse
from os.path import expanduser, join

# Parse console arguments
parser = argparse.ArgumentParser()
parser.add_argument("alias", help="alias to the SSH server")
parser.add_argument("user", help="user on the SSH server")
parser.add_argument("host", help="SSH server address")
parser.add_argument("-v","--verbose", help="verbose output", action="store_true")
parser.add_argument("-t","--test", help="redirect output to standard stream", 
                    action="store_true")
args = parser.parse_args()

# Build file
config_file_path = join(expanduser("~"), '.ssh/config')
sshconfig_text = '''
Host {}
  User {}
  HostName {}
'''.format(args.alias, args.user, args.host)

if not args.test:
    with open(config_file_path, 'w+') as fb:
        fb.write(sshconfig_text)

if args.verbose or args.test:
    print(config_file_path)
    print(sshconfig_text)
