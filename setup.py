from distutils.core import setup
import mailer

setup (name='mailer',
       version=mailer.__version__,
       description=mailer.__description__,
       author=mailer.__author__,
       py_modules=["mailer"])