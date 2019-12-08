# dish_extraction_sentiment_analysis

The project requires jupyter notebook, pycharm to run. 

1. Download and install as specified in https://jupyter.org/install & https://www.jetbrains.com/pycharm/download/ <br/>

2. Clone the repository<br/>
	  * git clone https://github.com/karangm-dev/dish_extraction_sentiment_analysis.git<br/>

3. Cd into the directory<br/>
	  * cd dish_extraction_sentiment_analysis<br/>

4. Import into Pycharm with a virtual environement creation option. 
    
5. Install the libraries from requirements file<br/> 
	  * pip install -r requirements.txt<br/>
    
6. Create a Kernel to run for Jupyter notebook<br/> 
	  * ipython kernel install --user --name=dish_extraction_sentiment_analysis<br/>  

7. To run the .ipynb program in the notebook<br/> 
	  * Open src/*.ipynb with kernel dish_extraction_sentiment_analysis and run<br/> 
    
8. To run the program in the Pycharm<br/> 
    * Open src/*.py and run with RUN option in Pycharm<br/> 
    
9. Create the input folder and download 

https://docs.google.com/spreadsheets/d/128wcaDoLqtlyk-HiWGyJL0yq7FrW3vC8iyf6_BD1jrE/edit?usp=sharing
https://docs.google.com/spreadsheets/d/1TZ2qMNOhl8bA-BVgQg5SC_m3DFKPd5Q4pBBveRIgqco/edit?usp=sharing
https://docs.google.com/spreadsheets/d/1WPO7_8pXT8izsEIOkDl3B0Vyu5RtiMhb-5sNNnATN8g/edit?usp=sharing
https://docs.google.com/spreadsheets/d/1y3yQXfcAEgHEXTuO2C8r_K4h5x-3317oGnT3G4z0cSo/edit?usp=sharing
https://docs.google.com/spreadsheets/d/1kcU7QT668l_d70IgsF83EpLWRHLzryr6a5lAXZLFLFU/edit?usp=sharing
https://docs.google.com/spreadsheets/d/1Zuh1J9bwpPo2mobIuWQxMG38O9GgMl4mvfV_8j_LLRI/edit?usp=sharing

10. Create an account in GCP and credential file as explained in https://cloud.google.com/dialogflow/docs/quick/setup. While creating service account, enable Dialogflow Admin & Dialogflow Client permissions. Download the credentials and set environment variable GOOGLE_APPLICATION_CREDENTIALS vartiable for the runner in Pycharm.

11. Run src/dish_sentiment_analysis_app.py to generate pickle files as output.

12. Run src/evaluation.py to calculate precision and recall scores and gernerate visualizations.












