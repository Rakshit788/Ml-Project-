from setuptools import setup, find_packages



HYPHEN_E_DOT = '-e .'

def  get_requirmwnts(filepath : str) ->list: 
    '''
    This function will return a list of requirements
    '''
    requirements =  [] 
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()

        if HYPHEN_E_DOT in requirements: 
            requirements.remove(HYPHEN_E_DOT)
    
    requirements = [req.replace('\n', '') for req in requirements]

    return requirements
    


setup(
    name='my_package',
    version='0.1.0',
    author='Rakshit', 
    author_email='rakshitchopra788@gmail.com' , 
    packages=find_packages(),
    install_requires=get_requirmwnts('requirement.txt'),
)
    