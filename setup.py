from setuptools import setup, find_packages

setup(
    name="2048-game",
    version="1.0.0",
    description="2048 puzzle game built with Python and Pygame",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "pygame>=2.5.2",
        "kivy>=2.2.0",
        "kivymd>=1.1.1",
    ],
    python_requires=">=3.8",
    entry_points={
        'console_scripts': [
            '2048-game=main:main',
        ],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Games/Entertainment :: Puzzle Games",
    ],
)
