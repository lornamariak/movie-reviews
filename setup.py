from setuptools import setup,find_packages

setup(
    name="movie-reviews",
    version="0.0.2",
    author="Lorna Aine",
    author_email="lorna.aine@duke.edu",
    description="Generate sample movie reviews data for data science projects",
    url="https://github.com/lornamariak/movie-reviews",
    packages=find_packages(),
    package_data={"movie_reviews":["data/*.csv"]},
    classifiers= [  
                "Development Status :: 3 - Alpha",
                "Intended Audience :: Education",
                "License :: OSI Approved :: MIT License",
                "Natural Language :: English",
                "Programming Language :: Python :: 3",
                "Programming Language :: Python :: 3",
                "Programming Language :: Python :: 3.7",
                "Programming Language :: Python :: 3.8",
                "Programming Language :: Python :: 3.9",
                "Programming Language :: Python :: 3.10",
                "Programming Language :: Python :: 3.11",
                "Programming Language :: Python :: 3 :: Only"
    ],
    license="MIT",
    python_requires=">=3.6",
    install_requires = ["pandas>=1.4.4"]

)