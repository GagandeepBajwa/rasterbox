import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rasterbox",
    version="0.0.1",
    author="Brad Crump",
    author_email="brad@breadcrumbbuilds.com",
    description="Semantic access of raster images and target labels associated with rasters",
    keywords = ["RASTER","IMAGES", "MACHINE","LEARNING"],
    install_requires=[
        'numpy'
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
