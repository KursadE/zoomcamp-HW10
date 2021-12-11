# zoomcamp-HW10


# Description of the problem

The model aims to classify 10 different animals which are listed as follows: dog, cat, horse, spyder, butterfly, chicken, sheep, cow, squirrel, elephant.

The dataset, total of 28K images, is taken from Kaggle: https://www.kaggle.com/alessiocorrado99/animals10

The pictures are divided into folders which are named in Italian. There is a python file that includes translation of categories: 'translate.py'. After downloading the data the folders names can be changed manually.

# Dataset

The dataset is not included in the repository as its size is more than 600mb. Therefore, it has to be downloaded from the Kaggle page.

The project is done on a Mac computer, with the OS being High Sierra. 

The default download folder for MacOS is "Downloads". After the download completed, the folder is moved to '/Users/Erol/Documents/HW10/' as 'archive/raw-img'. 

The naming of the dataset path is important as training and validation datasets are created using the path name in the code in 'notebook.ipynb'

# The files in the repository

Data preparation and analysis steps, training (multiple) models, tuning model performance and selecting and saving the best model are included in 'notebook.ipynb'.

The selected model is converted into a tensorflow lite version in 'tensorflow-model.ipynb', using the steps as told in the lecture.

The lite version of the model is also included in the repository as 'xception_v1.tflite'. The tensorflow version is not uploaded as it is a 86mb file, whereas the lite version is around 22mb.

'lambda_function.py' includes the steps to prepare for cloud deployment. A Docker file, 'Dockerfile' and and a test file, 'test.py' are also included in the repository.


# Notes on methodology

Convolutional neural network is used to classify the object. First, a model is developed using the sequential model structure provided in the homework. The accuracy on the validation dataset did not improve when multiple convolutional and dense layers were added. Therefore, a pretrained model is used, improving the accuracy dramatically.

Only train and validation datasets are used, meaning the dataset was divided into two parts, with train set being 80% of the dataset.

The final sequential model was trained for 25 epochs though its accuracy was increased when it was trained for more than that. However, the accuracy was still lower than that of the pretrained model, thus the number of epochs was set as 25 to reduce training time.

Xception model is used as the pretrained model. The model is first trained with the train set. Then the model was run to adjust the learning and dropout rates. The number of epochs was set to 5 in order to reduce training time since the accuracy rate on validation set was more than 90%. 

The final model is run with augmentation and the adjusted learning and dropout rates, and with 10 epochs.

# Instructions on how to run the project

For viewing and editing notebooks, Jupyter can be used. Other files can be viewed and edited on VS Code.

All libraries are used in the lecture and homework, therefore they are expected to be installed. If not, 'pip install' command can be used.

 'splitfolders' library is used to divide the dataset into two parts, which can be installed using 'pip install split-folders'.
 
The code sniplets obtained from 'stackoverflow' are indicated with their references in the 'notebook.ipynb'.

First, download all the dataset and all files into the same folder on your computer. Please, update the folder paths in 'notebook.ipynb' to be able to create training and validation datasets. The code above the 'EDA' title in the notebook should be updated according to the dataset path. The training and validation set should be in the same folder which contains all the other documents from the repository.

'Splitting Train & Validation Data' section divides dataset. The 'EDA' section shows the distribution of the classes. The initial training and other steps until the final training are put under the relevant sections and named accordingly in 'notebook.ipynb'. 

The final Xception model is trained and saved in the 'Training the Final Model with Augmentation' section.

'tensorflow-model.ipynb' notebook reduces the size of the model. It reduces the size of the final checkpoint named as 'xception_v1_05_0.975.h5', which is also included in the repository. This notebook also includes a test run on a sample picture link provided in the homework.

To create the container, on the Terminal screen one should go to the folder in which all the files reside. On Mac OS, while Docker is running as a separate program and with the working directory chosen, the command 'docker build -t xception_model .' should be run. After the container starts running, 'docker run -it --rm -p 8080:8080 xception_model:latest' should be typed on the terminal screen.

While the container is running, 'test.py' can be used to provide the model with sample pictures from the Internet. There are four links in the 'test.py', 3 of which are commented. On a new Terminal window, 'test.py' can be run by typing 'python test.py' command. 

'lambda_function.py' can be also be tested as it is done in lecture videos (ie. ipython, from lambda_function import lambda_handler...)
 
