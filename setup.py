import setuptools


with open('requirement.txt', 'r') as f:
    install_requires = f.read().splitlines()


setuptools.setup(name='data-structures',
                 packages={'linked_list'},
                 install_requires=install_requires)
