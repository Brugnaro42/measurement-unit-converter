# Measurement Unit Converter
![Language](https://img.shields.io/badge/language-Python-orange)
![Repo Version](https://img.shields.io/badge/version-v1.1-blue)

## 📜 Summary
This repository is dedicated to the corverter

## 🛠️ Fixes and improvements
The project is being developed, and the next necessary updates are:
- [x] Add first features;
- [x] Test the features;
- [x] Docstring everything that had been created;
    - [x] Track the features;
    - [x] Docstring them;
- [ ] Add new buches product's references
- [ ] Add new currencies


---
## 💻 Prerequisites
Before starting, make sure you have the following prerequisites:
- Install the Anaconda distribution from this [link](https://www.anaconda.com/);
- Install all requirements listed in `environment.yml` in a virtual or conda environment as follows:
```conda env create -f environment.yml```

---
## 📫 Contributing to the project
To contribute, follow these steps:
1. Clone this repository and create a new branch;
2. Make your changes to the project;
3. Commit your updates to your new branch;
4. Upload your changes to github;
5. Open a Pull Request pointing to the base used branch.

*obs1:* If you want to contribute or test a specific commit, you can do the following:
```
git clone https://<user>:<pwd>@https://github.ibm.com/Agro-Insights-AA/exploratory_analysis.git@<commit-hash>
```

*obs2:* Commit messages must obey semantic git, as described in the example:
```
<type>[optional scope]: <description>

[optional body]

[optional footer]
```
Other semantic git examples can be found at the link: [semantic git examples](https://www.conventionalcommits.org/en/v1.0.0/);

---
## 📁 Folder structure
The project is structured as described below:
```
├───data -> Store the data to be analyzed
│ ├───External      -> Data from 3rd party sources
│ ├───interim       -> Interim data that has been transformed
│ ├───processed     -> The final canonical datasets for modeling
│ └───raw           -> The original and immutable data dump
├───notebooks       -> Experiments and analysis are here
└───src             -> Successful experiments modularized in .py files
    ├───data        -> Used to do the ETL
    ├───features    -> Responsible for the main functionality of the repo
    ├───test        -> Test Cases created to verify functionality
    ├───models      -> Related to training, testing and creating ML models
    ├───utils       -> Useful features for other modules
    └───preview     -> Used for dataviz
```
*obs:* All data stored in the `/data/` folder is included in `.gitignore`;