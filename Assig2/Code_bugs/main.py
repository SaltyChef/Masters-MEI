from tkinter import *  
import csv
import cv2
from roboflow import Roboflow
from Drone import Drone

from Master import Master
from utils.Utils import Utils


# main.py
# authors: Diogo Rosário, João Raposo
# Description:  This file retrieves the trained Roboflow models using the provided APIs and performs predictions 
#               on a specified test (image_path). Subsequently, the master agent is invoked to compile and process all images 
#               without overlap, ensuring the best possible identification of each corresponding drone.
#               Additionally, the file manages the post-processing steps by saving the master agent's results in a CSV file named 
#               "mastersResults.csv" for future reference. Furthermore, it provides real-time visibility by printing the obtained 
#               results directly to the console during execution.


image_path = "mastersTests/test-10.jpg"
predicitonA_path = "predictions/predicitonA.jpg"
predicitonB_path = "predictions/predicitonB.jpg"
predicitonC_path = "predictions/predicitonC.jpg"
predictionM_path = "predictions/predictionM.jpg"
confidence = 51
overlap = 0

#Loading models of each drone
rfA = Roboflow(api_key="usQXRh13NGjn2HK6BwFP")
project1 = rfA.workspace().project("drone-a-tb89u")
modelA = project1.version(2).model

rfB = Roboflow(api_key="usQXRh13NGjn2HK6BwFP")
project2 = rfB.workspace().project("drone-b-xkvry")
modelB = project2.version(1).model

rfC = Roboflow(api_key="usQXRh13NGjn2HK6BwFP")
project3 = rfC.workspace().project("drone-c-hytyd")
modelC = project3.version(5).model

# Drones Reputation / confidence 
drone_A_confidence = 0.1
drone_B_confidence = 0.5
drone_C_confidence = 0.5

# Open a csv file called "mastersResults.csv" and write the results of the identifications processed by the master.
# In this format: 'A - Cars', 'A - Houses', 'A - Trees', 'B - Cars', 'B - Houses', 'B - Trees','C - Cars', 'C - Houses', 'C - Trees','A Reputation','B Reputation','C Reputation'

csv_filename = 'masterResults.csv'
with open(csv_filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['A - Cars', 'A - Houses', 'A - Trees', 
                    'B - Cars', 'B - Houses', 'B - Trees',
                    'C - Cars', 'C - Houses', 'C - Trees',
                    'A Reputation','B Reputation','C Reputation'])
                    
    ################################################################
    #################### DRONE A ###################################
 
    predictA = modelA.predict(image_path, confidence=confidence, overlap=overlap)
    drone_A = Drone("A", drone_A_confidence, predictA.json())
    predictA.save(predicitonA_path)
    drone_A.saveInCsv()

    ################################################################
    #################### DRONE B ###################################

    predictB = modelB.predict(image_path, confidence=confidence, overlap=overlap)
    drone_B =  Drone("B", drone_B_confidence, predictB.json())
    predictB.save(predicitonB_path)
    drone_B.saveInCsv()

    ################################################################
    #################### DRONE C ###################################

    predictC = modelC.predict(image_path, confidence=confidence, overlap=overlap) 
    drone_C = Drone("C", drone_C_confidence, predictC.json())
    predictC.save(predicitonC_path)
    drone_C.saveInCsv()

    ################################################################
    ####################### CALCULATION ############################
    ################################################################
    
    master = Master(drone_A, drone_A , drone_C)

    clone_img = cv2.imread(image_path)
    masterImage = clone_img.copy()  

    # Draw the result identifications
    for box in master.identifications:
        Utils.addLabel(masterImage, box.x, box.y, box.width, box.height, box.class_type, box.confidence, box.drone)

    cv2.imwrite(predictionM_path, masterImage) 
    print(str(len(master.identifications)))