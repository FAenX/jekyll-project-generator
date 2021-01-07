#!/usr/bin/env python3
import sys
import subprocess
import os

import argparse
from string import Template
from templates import index, include_index, default_layout




def folder_prep(path):
    command = 'mkdir -p {0}'.format(path)     
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    process.wait()
    if process.returncode == 0:
        return 'created folder {0}'.format(path)
    else:
        sys.stderr.write('error creating folder {0}'.format(path))
        sys.exit(1)

def write_file(filename, content):
    with open(filename, 'w') as _file:
        _file.write(content)
        _file.close()


# parse
# terminal argument parser
def parseArgs():
    # create a parser  
    parser = argparse.ArgumentParser(description='generate jekyll project.')  
    parser.add_argument("name", help="project name")
    args = parser.parse_args()
    return args






if __name__ == '__main__':

    args = parseArgs()
    PROJECT_NAME = args.name


    DIR_INCLUDES=os.path.join(PROJECT_NAME, "_includes")
    DIR_LAYOUTS=os.path.join(PROJECT_NAME, "_layouts")
    DIR_ASSETS=os.path.join(PROJECT_NAME, "assets")
    
    inc = folder_prep(DIR_INCLUDES)
    lay = folder_prep(DIR_LAYOUTS)
    scss = folder_prep(os.path.join(DIR_ASSETS, 'scss'))
    js = folder_prep(os.path.join(DIR_ASSETS, 'js'))
    images = folder_prep(os.path.join(DIR_ASSETS, 'images'))

    write_file(os.path.join(PROJECT_NAME,'index.html'), index.index_template.safe_substitute())
    write_file(os.path.join(DIR_INCLUDES, 'include_index.html'), include_index.include_html.safe_substitute())
    write_file(os.path.join(DIR_LAYOUTS, 'default.html'), default_layout.default_layout.safe_substitute())

    print(scss)
    print(js)
    print(images)