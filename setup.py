from setuptools import find_packages, setup

setup(
    name='Chance-Rollers',
    version='3.0',
    description='A simple die rolling game simulator',
    url='https://github.com/d26clarke/TBD',
    author='D.D. Clarke(thq3hn)',
    author_email='ddclarke1208@gmail.com',
    license='MIT',
    package_dir={"": "chanceRollers"},
    packages = find_packages(where="chanceRollers"),
    install_requires = ["numpy", "pandas"]  

)
