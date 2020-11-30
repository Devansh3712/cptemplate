from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
 
setup( 
        name ='cptemplate',
        version = '1.1',
        author ='Devansh Singh', 
        author_email ='devanshamity@gmail.com', 
        url ='https://github.com/Devansh3712/cptemplate', 
        description ='competitive programming template', 
        long_description = long_description, 
        long_description_content_type ="text/markdown", 
        license ='MIT',
        packages = ["cp"],
        include_package_data = True,
        entry_points = {
        	"console_scripts": [
        		"cptemplate=cp.__main__:cptemplate",
        	]
        },
        classifiers = [
            "Programming Language :: Python :: 3", 
            "License :: OSI Approved :: MIT License", 
            "Operating System :: OS Independent", 
        ],
        install_requires = [
          'click==7.1.2',
          'numpy==1.19.4'
        ],
) 