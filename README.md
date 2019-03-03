# Opencv-Face-Detection

Clone and unzip the repository.

Collect your pictures. You will need 2 or more pictures for every person.

The first folder should be structured as follows.

	Name: training-data
	Contents: 1 sub folder per person.
	
		Sub folder 1:
			Name: s1
			Content: Pictures labeled 1.jpg,2.jpg etc.
			
		Sub folder 2:
			Name: s2
			Content: Pictures labeled 1.jpg,2.jpg etc.
	
The second folder should be structured as follows.

	Name: test-data
	Contents: Two test pictures, named test1.jpg and test2.jpg
	
The picture part is done! Now to move on to the code.

Their are 2 programs in the repository, TrainingClassifier.py and facerecognizer_run.py
The first one, TrainingClassifier.py, will train a model to detect the specific face. The second one, facerecognizer_run.py will be using that model to find faces.


		
