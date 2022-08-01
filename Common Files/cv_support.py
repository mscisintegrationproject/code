# Description: Support functions for launder monitoring and TBRC monitoring code
# Author: Michael Kainola
# Date: July 31, 2022

import csv #for importing and exporting csv files
from datetime import datetime #for getting timestamp of measurement
import os #for deleting the csv file
import cv2 #required for drawing rectangles

# global variable used for storing the curent file name; accessed by multple functions
curr_filename = ""


# load the PI data; used in visualizing the temperature data from PI
def importPIData():
    
    fn = 'Inputs/historian_temperature_data.csv' #filename
    # provide feedback to the user
    print ("Reading historian (temperature) data from: " + fn + "\n")
    
    # create list to store data
    PI_DATA = []
    
    # open reader
    with open(fn, 'r') as read_obj:
    
        # grab first row and skip it (header)
        csv_reader = csv.reader(read_obj)
        header = next(csv_reader)

        # check if file is empty
        if header != None:
            
            # iterate over each row
            for row in csv_reader:
                
                # append the row to the list
                PI_DATA.append(row)
    
    return PI_DATA # return the list of PI data


# function to create csv file for storing video luminosity data
def createVideoDataFile(filename):
    global curr_filename
    
    # set filename
    curr_filename = filename
    
    # set headers
    fields = ["FRAME","ROI1","ROI2","ROI3","IMAGE","TIMESTAMP"]
    
    # create file with headers
    with open(curr_filename, "a+", newline="") as csvfile:
    
        # create csv writer object
        csvwriter = csv.writer(csvfile)

        # write the field headers
        csvwriter.writerow(fields)
    
    
# function to write luminosity data to file created by function createVideoDataFile
def writeVideoData(rows):
    global curr_filename
    
    # write luminosity row data to csv
    with open(curr_filename, "a+", newline="") as csvfile:
    
        # create csv writer object
        csvwriter = csv.writer(csvfile)

        # write the row data
        csvwriter.writerows(rows)
       
    
# function to read luminosity data from csv and print the results; used primarily for debugging
def readVideoData():
    global curr_filename
    
    # provide feedback to user about operation
    print ("Reading file: " + curr_filename + "\n")
    
    # open the reader
    with open(curr_filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        
        #create collection from the data, print the results
        for row in csvReader:
            print(row)
            
    return


# custom region of interest (roi) class; contains basic properties to describe the roi
class Roi:
    
    #function to initialize object
    def __init__(self, name, left, top, width, height):
        self.name = name
        self.left = int(left)
        self.top = int(top)
        self.width = int(width)
        self.height = int(height)
        

# function to import the ROI coordinates from csv
def readROICoords(filename):
    
    # provide feedback to the user
    print ("Reading ROI coordinates from: " + filename + "\n")
    
    # create array to store the roi data
    rois = []
    
    # create file reader
    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        
        # skip the header row; we don't want this in the data
        next(csvReader)
        
        #create the collection
        for row in csvReader:
            r = Roi(row[0],row[1],row[2],row[3],row[4],)
            rois.append(r)
    
    return rois # return the list of roi coordinates

# function to create gstreamer object for TBRC recorder
def gstreamer_pipeline(
    
    # set dimensions for capture / display
    capture_width=640,
    capture_height=480,
    display_width=640,
    display_height=480,
    framerate=10,
    flip_method=0,
):
    # return the gstreamer object; without explicit exposure settings
    return (
        "nvarguscamerasrc ee-mode=2 ee-strength=0 tnr-mode=2 tnr-strength=1 aelock=true wbmode=0 awblock=true ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )

# function to create gStreamer object for granulation process, uses explicit exposure settings
def gstreamer_pipeline_granulation(
    
    # set dimensions for capture / display
    capture_width=640,
    capture_height=480,
    display_width=640,
    display_height=480,
    framerate=10,
    flip_method=0,
):
    # return the gstreamer object; WITH explicit exposure settings
    return (
        "nvarguscamerasrc ee-mode=2 ee-strength=0 tnr-mode=2 tnr-strength=1 aelock=true gainrange='1 1' ispdigitalgainrange='1 1' wbmode=0 awblock=true exposuretimerange='300000 300000' ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )

# function to draw roi for visualization purposes

def drawROI(col, roi, color):
    
    # create main rectangle
    col = cv2.rectangle(col,pt1=(roi.left,roi.top),pt2=(roi.left+roi.width,roi.top+roi.height),color=color,thickness=3)
    
    # create rectangle to go behind ROI label
    col = cv2.rectangle(col,pt1=(roi.left-2,roi.top-26),pt2=(roi.left+50,roi.top),color=color,thickness=-1)
    
    # label the ROI
    cv2.putText(col, roi.name, (roi.left, roi.top-6), cv2.FONT_HERSHEY_SIMPLEX, .7, (255,255,255), 2)
    
    return col # return the image