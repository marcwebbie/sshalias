#!/usr/bin/env python
import argparse
from os.path import expanduser, join


parser = argparse.ArgumentParser()
parser.add_argument("user", help="User on the ssh server")
parser.add_argument("host", help="Ssh server address")
parser.add_argument("-v","--verbose", help="Verbose output", action="store_true")
args = parser.parse_args()

sshconfig_text = '''
Host example
  User {}
  HostName {}
'''.format(args.user, args.host)

config_file_path = join(expanduser("~"), '.ssh/config_test')
with open(config_file_path, 'w+') as fb:
    fb.write(sshconfig_text)

if args.verbose:
    print(config_file_path)
    print(sshconfig_text)
