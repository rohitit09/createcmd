from setuptools import setup
import setuptools


setup(
    name="createprojectcmd", # Replace with your own username
    # py_modules=['packaging_tutorial/createproject'],
    install_requires=['cmd2'],
    scripts=['createprojectcmd'],
    python_requires='>=3.6'
)



# to install in local go to  setup directory then

#pip install -e .

######### or #########

#python setup.py sdist
#sudo python setup.py install
#now in local wiht createproject commad use can run this project


# run from cmd
# manet@Documents$ createproject
# Welcome to create project shell
# cretae project >


# import inside python
# >>> import createproject
# >>> c=createproject.CmdLineApp()
# >>> import sys
# >>> sys.exit(c.cmdloop())
# Welcome to create project shell
# cretae project >