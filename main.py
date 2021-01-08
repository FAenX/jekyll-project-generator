#!/usr/bin/env python3
import sys
from subprocess import Popen, PIPE
import os

import argparse
from templates import templates 

def folder_prep(path):
    command = 'mkdir -p {0}'.format(path)     
    process = Popen(command, shell=True, stdout=PIPE)
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

def my_process(command):
    process = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    print(stdout, stderr)




if __name__ == '__main__':

    
    args = parseArgs()
    PROJECT_NAME = args.name

    curdir = os.path.abspath(os.path.curdir)
    appdir = os.path.join(curdir, PROJECT_NAME)
    folder_prep(appdir)
    os.chdir(appdir)

    print(os.path.abspath(os.path.curdir))

    DIR_INCLUDES="_includes"
    DIR_LAYOUTS="_layouts"
    DIR_ASSETS="assets"

    inc = folder_prep(DIR_INCLUDES)
    lay = folder_prep(DIR_LAYOUTS)
    scss = folder_prep(os.path.join(DIR_ASSETS, 'scss'))
    js = folder_prep(os.path.join(DIR_ASSETS, 'js'))
    images = folder_prep(os.path.join(DIR_ASSETS, 'images'))


    write_file('Gemfile', templates.gemfile.safe_substitute())
    write_file('_config.yml', templates.config.safe_substitute())
    write_file('index.html', templates.index_template.safe_substitute())
    write_file(
        os.path.join(DIR_INCLUDES, 'include_index.html'), 
        templates.include_html.safe_substitute())
    write_file(
        os.path.join(DIR_LAYOUTS, 'default.html'), 
        templates.default_layout.safe_substitute())
    

    j_install = 'gem install bundler'
    bundle = 'bundler exec bundle'

    my_process(j_install)
    my_process(bundle)
    
    
    print(scss)
    print(js)
    print(images)