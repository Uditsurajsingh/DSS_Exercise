from setuptools import setup, find_packages

setup(
    name='math_quiz',  # Replace with your package name
    version='0.1.0',  # Specify your package version
    packages=find_packages(),  # Automatically discover and include all packages
    install_requires=[
        # List your dependencies here
    ],
    author='Udit Suraj Singh',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Uditsurajsingh/DSS_Exercise.git',  # Replace with your GitHub repository URL
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
        # Add other classifiers as needed
    ],
)
