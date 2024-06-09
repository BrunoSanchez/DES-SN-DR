#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  download_dessndr.py
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

import argparse
import logging
from .. import data

def main():
    parser = argparse.ArgumentParser(
        description="Command to download the data from DES-SN-5YR"
        )
    parser.add_argument("dest_folder", 
        help="The directory destination for the download", 
        type=str, 
    )
    parser.add_argument("-r", "--repo_url", 
        help="The github URL of the DES repo.", 
        type=str, 
        default=data.DES5YRDR_URL
    )

    args = parser.parse_args()

    data.clone_repo(
        repo_url=args.repo_url,
        dest_folder=args.dest_folder,
        )

if __name__ == "__main__":

    main()

