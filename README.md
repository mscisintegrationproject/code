# MSc IS Integration Project Code Repository
This repo contains the fully commented python code created for Michael Kainola's MSc IS Integration Project. This README provides an overview of the eight key code files and direct links to each of these files. This README also details the prerequisite python modules and the set up instructions for the python notebooks.

## Code Files
The code files are organized into three folders - one for each of the two experiments and a third folder for common modules. Most of the code is provided in jupyter notebook format (.ipynb). The only exception to this is one custom python module - cv_support.py. 

### Experiment 1 - Launder Monitoring
1. <b>Launder Monitor</b> ([Launder_Monitor.ipynb](https://github.com/mscisintegrationproject/code/blob/main/Experiment%201%20-%20Launder%20Monitor/Launder_Monitor.ipynb "See Notebook")). This notebook demonstrates the key processing steps of the Launder Monitoring software. The camera image is loaded and a series of image processing techniques are applied to determine if there is buildup on the launder. If the quantified buildup is exceeded, an alert is generated.

2. <b>Launder Recorder</b> ([Launder_Record.ipynb](https://github.com/mscisintegrationproject/code/blob/main/Experiment%201%20-%20Launder%20Monitor/Launder_Record.ipynb "See Notebook")). This notebook includes the code used to record and save the video footage of the launder. Note that this code was designed to run on the Jetson Nano hardware, using a Raspberry Pi Camera Module. 

### Experiment 2 - TBRC Monitoring
3. <b>TBRC Monitor</b> ([TBRC_Monitor.ipynb](https://github.com/mscisintegrationproject/code/blob/main/Experiment%202%20-%20TBRC%20Monitor/TBRC_Monitor.ipynb "See Notebook")). This notebook demonstrates the key processing steps of the TBRC Monitoring software. The simulated temperature and luminosity data are loaded into the trained LSTM model, which then predicts the next 60 seconds of temperature measurements. If the temperature is predicted to climb by more than 10 degrees in the 60 second window, an alert is generated. The code visualizes the predictions over a ten minute period.

4. <b>TBRC Recorder</b> ([TBRC_Record.ipynb](https://github.com/mscisintegrationproject/code/blob/main/Experiment%202%20-%20TBRC%20Monitor/TBRC_Record.ipynb "See Notebook")). This notebook includes the code used to record and save the video footage of the launder. While this code is similar to Launder_Record.ipynb, it also includes functionality to extract the luminosity of each frame, and save the luminosity values to csv. Note that this code was designed to run on the Jetson Nano hardware, using a Raspberry Pi Camera Module. 

5. <b>TBRC ROI Selection</b> ([TBRC_ROI_Selection.ipynb](https://github.com/mscisintegrationproject/code/blob/main/Experiment%202%20-%20TBRC%20Monitor/TBRC_ROI_Selection.ipynb "See Notebook")). This notebook demonstrates the key steps for selecting the ROI for the TBRC monitor. The goal of this exercise was to identify the ROI which had a luminosity measurement that best correlated with the TBRC temperature. The data from the 'best' ROI would later be used in training the TBRC forecasting model. Three candidate ROIs were provided by the site experts. This code quantifies the luminosity at all three ROIs, and then calculates the correlation with the TBRC temperature data.

6. <b>TBRC LSTM Model Training</b> ([TBRC_Model_Training.ipynb](https://github.com/mscisintegrationproject/code/blob/main/Experiment%202%20-%20TBRC%20Monitor/TBRC_Model_Training.ipynb "See Notebook")). This notebook demonstrates the key steps for training the TBRC temperature prediction LSTM model. A simulated dataset containing luminosity and temperature data is used to train the LSTM model. The model is then tested and the results are visualized. Lastly, the RMSE metric is calculated for the model.

7. <b>TBRC Data Simulator</b> ([TBRC_Data_Simulator.ipynb](https://github.com/mscisintegrationproject/code/blob/main/Experiment%202%20-%20TBRC%20Monitor/TBRC_Data_Simulator.ipynb "See Notebook")). This notebook demonstrates the key steps of the TBRC Data Simulator. This code accepts a cleaned sample dataset from the TBRC as an input and outputs a configurable number of simulated datasets, based on the original input. These simulated datasets are then used to train and test the LSTM model.

### Common Files
8. <b>CV Support</b> ([cv_support.py](https://github.com/mscisintegrationproject/code/blob/main/Common%20Files/cv_support.py "See Code")). This custom python module provides support functions for streaming video data, saving video data, importing various csv files and drawing on images. 

## Prerequisites
Note that this project has several external dependencies, which must be installed for the code to execute. These key dependenies are listed below, in alphabetical order. Environment setup instructions are provided in the next section.

* [ipykernel](https://pypi.org/project/ipykernel/): This is the iPython Kernel for Jupyter. This module must be installed in order to be able to specify that Jupyter Lab use a specific virtual environment. 
* [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/): Jupyter Lab is an interactive web-based development environment. A significant portion of this project's development took place in Jupyter Lab.  
* [matplotlib](https://matplotlib.org/): One of the most popular visualization libraries for Python. Matplotlib is used extensively in this project to visualize application output.
* [Numpy](https://numpy.org/): Numpy is a numerical computing library for Python. It is used throughout this project for data organization and manipulation.
* [OpenCV](https://opencv.org/): One of the most popular computer vision libraries. OpenCV is used in this project for reading video data and image processing.
* [Pandas](https://pandas.pydata.org/): Pandas is a data analysis and manipulation tool. It is used in this project to shape data for visualization and modelling.
* [pickle](https://docs.python.org/3/library/pickle.html): Pickle allows for the serializing / deserializing of Python objects. Pickle is used in this project for saving / loading LSTM models to disk.
* [seaborn](https://seaborn.pydata.org/): Another python visualization library. Seaborn is used specifically for creating correlation matrices in this project.
* [scikit-learn](https://scikit-learn.org/stable/): Scikit-learn is a Python machine learning library. Scikit-learn is used in this project to support model training and evaluation (calculating RMSE).
* [Tensorflow](https://www.tensorflow.org/) / [Keras](https://keras.io/): Tensorflow is a machine learning library. Keras is built ontop of Tensorflow with the purpose of simplifying machine learning experiments. Both are used in this project for training and then leveraging the TBRC LSTM model.

## Environment Setup Instructions
This section provides instructions on setting up a python environment, installing the required dependencies, and loading the jupyter notebook. Note that this application was developed and tested on version Python 3.8.

1. <b>Download and extract project locally</b>
2. <b>Open command line</b>
3. <b>Navigate to project directory, for example:</b>

    ````cd C:\Users\user1\code````

4. <b>While in the project directory, create a new python virutal environment:</b>

    ````Python3 -m venv env_mscis````

5. <b>Activate the virtual environment:

    ````env_mscis\Scripts\activate````

6. <b>Using the python package installer (pip), install required packages to the virtual environment using the python configuration file:</b>
    
    ````pip install -r requirements.txt````

7. <b>Using the python package installer (pip), install OpenCV:</b>

    ````pip install opencv-python````

    Note: If opencv fails to install with a wheel build error, run the code below and then install opencv again:

    ````pip install --upgrade pip setuptools wheel````

8. <b>Launch the Jupyter Notebook</b>

    ````jupyter notebook````

9. <b>Open a browser and navigate to Jupyter Lab:</b>
   
    ````http://localhost:8888/lab````
    
    
<br>

    
[Back to top of README](https://github.com/mscisintegrationproject/code#msc-is-integration-project-code-repository)