# MSc IS Integration Project Code Repository
This repo contains the following files:

* item 1 [link1](http://example.com "See File").
* item 2 [link2](http://example.com "See File").
* item 3 [link3](http://example.com "See File").
* item 4 [link4](http://example.com "See File").

## Prerequisites
Note that this project has several external dependencies, which must be installed for the code to execute. These dependenies are listed below, in alphabetical order. Environment setup instructions are provided in the next section.

* [OpenCV](https://opencv.org/) version x: a computer vision library
* [Numpy](https://numpy.org/) version x: a numerical computing library
* [Pandas](https://pandas.pydata.org/) version x: a data manipulation library

## Environment Setup Instructions

#### First Time Setup
1. Download and extract project locally
2. Navigate to project directory:

    ````Cd C:\Users\Mike\OneDrive\Desktop\Final_Code````

3. Install Jupyter Lab

    ````pip install jupyter jupyterlab````

4. Install iPyKernal
   
    ````python
    pip install ipykernel
    ````

5. Install iPyKernel in project's python environment
	
    ````python -m ipykernel install --name=env_final````
6. Install OpenCV
    
    ````pip install opencv-python````
	 
	 
#### Run the code in Jupyter Notebook

1. Navigate to the project directory in command line.
2. Activate the project environment

    ````sh
    env_final\Scripts\activate
    ````
3. Launch the Jupyter Notebook

    ````sh
    jupyter notebook
    ````

4. Navigate to http://localhost:8888/lab
