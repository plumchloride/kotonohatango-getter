import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kotonohagetter",
    version="0.0.1",
    author="rikito ohnishi",
    author_email="ohnishi.rikito@gmail.com",
    description='A package for visualization of aggregate data of players in "Kotoha Tango"',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/plumchloride/kotonohatango-getter",
    project_urls={
        "Bug Tracker": "https://github.com/plumchloride/kotonohatango-getter",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    py_modules=['kotonohatango-getter'],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    entry_points = {
        'console_scripts': [
            'kotonohagetter = kotonohagetter:main'
        ]
    },
)
