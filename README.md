# MSc IS Integration Project Code Repository
This repo contains the fully commented python code created for Michael Kainola's MSc IS Integration Project. This README provides an overview of the X files. It also details the prerequisite python modules and the set up instructions for the python notebook.

## Code
The code is organized into three folders - one for each of the two experiments and a third folder for common modules. Most of the code is provided in jupyter notebooks, which break the code out into smaller chunks, to improve the reader's understanding of the code.

### Experiment 1 - Launder Monitoring
1. <b>Launder Monitor</b> ([Launder_Monitor.ipynb](https://github.com/mscisintegrationproject/code/blob/main/Experiment%201%20-%20Launder%20Monitor/Launder_Monitor.ipynb "See Notebook")). This notebook demonstrates the key processing steps of the Launder Monitoring software. The camera image is loaded and a series of image processing techniques are applied to determine if there is buildup on the launder. If the quantified buildup is exceeded, an alert is generated.

2. <b>Launder Recorder</b> ([Launder_Record.ipynb](https://github.com/mscisintegrationproject/code/blob/main/Experiment%201%20-%20Launder%20Monitor/Launder_Record.ipynb "See Notebook")). This notebook includes the code used to record and save the video footage of the launder. Note that this code was designed to run on the Jetson Nano hardware, using a Raspberry Pi Camera Module. 

### Experiment 2 - TBRC Monitoring
1. <b>TBRC Monitor</b> ([TBRC_Monitor.ipynb](https://github.com/mscisintegrationproject/code/blob/main/Experiment%202%20-%20TBRC%20Monitor/TBRC_Monitor.ipynb "See Notebook")). This notebook demonstrates the key processing steps of the TBRC Monitoring software. The simulated temperature and luminosity data are loaded into the trained LSTM model, which then predicts the next 60 seconds of temperature measurements. If the predicted temperature measurements climb increase more than 10 degrees, an alert is generated. The code visualizes the predictions over a ten minute period.

2. <b>TBRC Recorder</b> ([TBRC_Record.ipynb](https://github.com/mscisintegrationproject/code/blob/main/Experiment%202%20-%20TBRC%20Monitor/TBRC_Record.ipynb "See Notebook")). This notebook includes the code used to record and save the video footage of the launder. While this code is similar to Launder_Record.ipynb, it also includes functionality to extract the luminosity of each frame, and save the luminosity values to csv. Note that this code was designed to run on the Jetson Nano hardware, using a Raspberry Pi Camera Module. 

3. <b>TBRC ROI Selection</b> ([TBRC_ROI_Selection.ipynb](https://github.com/mscisintegrationproject/code/blob/main/Experiment%202%20-%20TBRC%20Monitor/TBRC_ROI_Selection.ipynb "See Notebook")). This notebook demonstrates the key steps for selecting the ROI for the TBRC monitor. The goal of this exercise was to identify the ROI which had a luminosity measurement that best correlated with the TBRC temperature. The data from the 'best' ROI would later be used in training the TBRC forecasting model. Three candidate ROIs were provided by the site experts. This code quantifies the luminosity at all three ROIs, and then calculates the correlation with the TBRC temperature data.

4. <b>TBRC LSTM Model Training</b> ([TBRC_Model_Training.ipynb](https://github.com/mscisintegrationproject/code/blob/main/Experiment%202%20-%20TBRC%20Monitor/TBRC_Model_Training.ipynb "See Notebook")). This notebook demonstrates the key steps for training the TBRC temperature prediction LSTM model. A simulated dataset containing luminosity and temperature data is used to train the LSTM model. The model is then tested and the results are visualized. Lastly, the RMSE metric is calculated for the model.

5. <b>TBRC Data Simulator</b> ([TBRC_Data_Simulator.ipynb](https://github.com/mscisintegrationproject/code/blob/main/Experiment%202%20-%20TBRC%20Monitor/TBRC_Data_Simulator.ipynb "See Notebook")). This notebook demonstrates the key steps of the TBRC Data Simulator. This code accepts a cleaned sample dataset from the TBRC as an input and outputs a configurable number of simulated datasets, based on the original input. These simulated datasets are then used to train and test the LSTM model.

### Common Files


This repo contains the following files:

* item 1 [link1](http://example.com "See File").
* item 2 [link2](http://example.com "See File").
* item 3 [link3](http://example.com "See File").
* item 4 [link4](http://example.com "See File").

Note that this repo contains both the raw, fully commented python code as well as a python notebook where the code can be executed with step-by-step output. The prerequisites and set up instructions for the python notebook environment are below. 

## Prerequisites
Note that this project has several external dependencies, which must be installed for the code to execute. These dependenies are listed below, in alphabetical order. Environment setup instructions are provided in the next section.

* [OpenCV](https://opencv.org/) version x: a computer vision library
* [Numpy](https://numpy.org/) version x: a numerical computing library
* [Pandas](https://pandas.pydata.org/) version x: a data manipulation library

## Environment Setup Instructions
This section provides instructions on setting up a python environment, installing the required dependencies, and running the jupyter notebook.

<details>
<summary><b>First Time Setup</b> (expandable)</summary>

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
	 
</details>	 

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