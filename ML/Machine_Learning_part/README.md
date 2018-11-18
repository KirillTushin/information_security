# Machine-Learning-approach-for-Malware-Detection
To run use ```python malware_cheker.py PATH_TO_FILE```.

The script needs weights, calculated during learning. In file ```training/malware-classification.ipynb``` 6 different models are trained and the best one is saved in ```best_classifier```. In ```file_examples/``` you can find malwares (need to unpack) and noraml, uninfected files.

Dependencies
============

* pandas ```pip install pandas```
* numpy ```pip install numpy```
* pickle ```pip install pickle```
* scipy ```pip install scipy```
* scikit ```pip install -U scikit-learn```
