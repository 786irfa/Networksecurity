###the setup.py file is an essential part of packaging
 ##and distributing python projects.it is used by setuptools 
 ##to define the configuration of your projects such as it 
 ##metadata dependencies and more"
from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    '''
    this function will return list of requirement'''
    requirement_1st:List[str]=[]
    try:
        with open ("requirements.txt",'r')as file:
        ##read lines from the file
             lines=file.readlines()
        ##process each lines
             for line in lines:
                 requirement=line.strip()
            ##ignore the empty lines and -e.
                 if requirement and requirement!="-e .":
                     requirement_1st.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
         
    return requirement_1st
print(get_requirements())
setup(
    name="CYBERSECURITYDATA",
    version="0.0.1",
    author= 'Irfan',
    author_email="if476771@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)


        
    
    
    
    