# zoomcamp-HW10


# Description of the problem

The model aims to classify 10 different animals which are listed as follows: dog, cat, horse, spyder, butterfly, chicken, sheep, cow, squirrel, elephant.

The dataset, total of 28K images, is taken from Kaggle: https://www.kaggle.com/alessiocorrado99/animals10

The pictures are divided into folders which are named in Italian. There is a python file that includes translation of categories: 'translate.py'.

# Dataset

The dataset is not included in the repository as its size is more than 600mb. Therefore, it has to be downloaded from the Kaggle page.

The project is done on a Mac computer, with the OS being High Sierra. 

The default download folder for MacOS is "Downloads". After the download completed, the folder is moved to '/Users/Erol/Documents/HW10/' as 'archive/raw-img'. The naming of the dataset path is important as training and validation datasets are created using the path name in the code in 'notebook.ipynb'

# The files in the repository

Data preparation and analysis steps, training (multiple) models, tuning model performance and selecting and saving the best model are included in 'notebook.ipynb'.

The selected model is converted into a tensorflow lite version in 'tensorflow-model.ipynb', using the steps as told in the lecture.

The lite version of the model is also included in the repository as 'xception_v1.tflite'. The tensorflow version is not uploaded as it is a 86mb file, whereas the lite version is around 22mb.

'lambda_function.py' includes the steps to prepare for cloud deployment. A Docker file, 'Dockerfile' and and a test file, 'test.py' are also included in the repository.


# Notes on methodology

Convolutional neural network is used to classify the object. First, a model is developed using the sequential model structure provided in the homework. The accuracy on the validation dataset did not improve when multiple convolutional and dense layers were added. Therefore, a pretrained model is used, improving the accuracy dramatically.

The final sequential model was trained for 25 epochs though its accuracy was increased when it was trained for more than that. However, the accuracy was still lower than that of the pretrained model, thus the number of epochs was set as 25 to reduce training time.

Xception model is used as the pretrained model. The model is first trained with the train set. Then the model was run to adjust the learning and dropout rates.The number of epochs was set as 5 to reduce training time since the accuracy rate on validation set was more than 90%. 

The final model is run with augmentation and the adjusted learning and dropout rates, with 10 epochs.

# The files in the repository
  

