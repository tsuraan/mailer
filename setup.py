from setuptools import setup
import sys

extra = {}
if sys.version_info >= (3,0):
    extra.update( use_2to3 = True )

setup (
    name = 'mailer',
    version = "0.7",
    description = "A module to send email simply in Python",
    author = "Ryan Ginstrom",
    url = "https://bitbucket.org/ginstrom/mailer",
    py_modules = ["mailer"],
    keywords = ["email", "smtp"],
    license = "MIT License",
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    **extra
)