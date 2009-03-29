#coding: UTF8
"""
Generates documentation using epydoc

"""

import os
from string import Template
import shutil
import glob
from AnalyzeAssist.setup import clean_dir
import sys
import subprocess

def run_command(command):
    
    proc = subprocess.Popen(command,
                            shell=True, 
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE
                           )

    for line in proc.stdout:
        print line.strip().decode("sjis").encode("utf-8")
        sys.stdout.flush()

    for line in proc.stderr:
        print line.strip().decode("sjis").encode("utf-8")
        sys.stderr.flush()

    assert not proc.returncode
    
NAME = "mailer" # DRY violation!
DOT_PATH = os.path.abspath("/program files/att/graphviz/bin/dot.exe")

def gen_api_docs():
    """Generates documentation files"""
    
    print
    print "*" * 30
    print "Generating documentation..."
    base_dir = os.path.dirname(__file__)
    api_dir = os.path.join(base_dir, "apidocs")
    
    # Get rid of the old documentation
    clean_dir(api_dir)
    
    os.chdir(base_dir)

    run_command(' '.join([r'epydoc.py',
                               '--html',
                               '-v',
                               r'-o "%s"' % api_dir,
                               '--name=%s' % NAME,
                               '--graph all',
                               r'--dotpath "%s"' % DOT_PATH,
                               '--exclude=use_mailer',
                               '--exclude=makedocs',
                               '--debug',
                               r'"%s"' % base_dir]))

    print "Finished generating documentation!"
    print "*" * 30
    print

def main():
    """generate API documentation and manual"""
    
    gen_api_docs()

if __name__ == '__main__':
    from AnalyzeAssist import streamencode
    sys.stdout = streamencode.OutStreamEncoder(sys.stdout, "utf-8")
    sys.stderr = streamencode.OutStreamEncoder(sys.stderr, "utf-8")
    main()
