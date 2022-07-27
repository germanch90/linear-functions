from setuptools import setup

with open('requirements.txt') as f:
    deps = [dep for dep in f.read().split('\n') if dep.strip() != ''
            and not dep.startswith('-e')]
    install_requires = deps

setup(
    name='LinearFunctions',
    version='0.1',
    packages=['LinearFunction', 'FunctionCollection'],
    url='',
    license='',
    install_requires=install_requires,
    author='German Chaverri',
    author_email='germanch90@gmail.com',
    description='Package that allows linear functions to be computed from the input of two (x, y) points. '
                'Computes the equation and allows computing an X or Y value, when the counterpart is given. '
                'Also allows the possibility to graph the function.'
)
