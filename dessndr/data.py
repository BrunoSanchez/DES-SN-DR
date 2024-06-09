#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  data.py
#
#  Copyright 2024 bruno <bsanchez@cppm.in2p3.fr>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#

import os
import subprocess

# Remote address
DES5YRDR_URL = """https://github.com/des-science/DES-SN5YR"""

# Local download
DES5YRDR_DATA_ROOT = os.getenv("DES5YRDR_DATA_ROOT")
DES5YRDR_DATA = os.getenv("DES5YRDR_DATA")
if DES5YRDR_DATA_ROOT is None:
    DES5YRDR_DATA_ROOT = os.path.join(os.getenv("HOME"), "DES5YRDR_DATA_ROOT")
    DES5YRDR_DATA = os.path.join(DES5YRDR_DATA_ROOT, "DES-SN5YR")

def clone_repo(repo_url=DES5YRDR_URL, dest_folder=DES5YRDR_DATA_ROOT):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    
    repo_name = repo_url.split('/')[-1].replace('.git', '')
    clone_path = os.path.join(dest_folder, repo_name)
    
    if os.path.exists(clone_path):
        print(f"{clone_path} already exists. Skipping cloning.")
    else:
        subprocess.run(['git', 'clone', repo_url, clone_path], check=True)
    
    os.environ['DES5YRDR_DATA'] = clone_path
    print(f"Repository cloned to: {clone_path}")
    print(f"You should set environment variables for it to be found system wide") 
    print("In bash for example this would be done with two commands: \n")
    print(f"export DES5YRDR_DATA_ROOT={os.path.abspath(dest_folder)}")
    print(f"export DES5YRDR_DATA={os.path.abspath(os.path.join(dest_folder, 'DES-SN5YR'))}")
