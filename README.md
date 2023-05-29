<a name="readme-top"></a>

<br />
<div align="center">
  <h3 align="center">Dilbert - Cascade Classifier</h3>

  <p align="center">
    The goal of this repository is to practically do the training of a haar cascade classifier with opencv, using dilbert's comic balloons as an example.    
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

First you need to download and have separate sections of each cartoon. It can be done using the scraper [comic-scaper by dottorm](https://github.com/dottorm/comic-scraper). Once downloaded and cutted we will place them in the undefined directory. Many, many images.

The undefined folder represents our sea where to fish. We will first have to start selecting positive gilberts, where gilber is present, and negatives where it is not present, placing them respectively in the 'positive_gilbert' and 'negative_gilbert' directories.

You can proceed with the execution of negative.py which provides the resizing to (100x100 pixels) and the conversion to grayscale of both the negatives and positives by placing them in the respective directories 'negative_dilbert_grayscale' and 'positive_dilbert_grayscale'. Furthermore, a 'negative.txt' file is created which lists all the negatives present in the directory, a file which will be used for training.

```python
python3 negative.py 
```

The next step is to prepare for the annotations of the positives, therefore manually identifying the coordinates of where Gilbert is present in the positives. In order to create a 'positive.txt' file where the dilbert coordinates will be specified. So we're going to move a sample of dilbert's positive images into the info folder. You can use a small python script that can help to move same random sample (asks the number of files to move)

```sh
python3 move_random_image.py
```

Then we use an opencv tool to create the annotations

```sh
opencv_annotation --annotations=positive.txt --images=info
```
After patiently noting the dilberts present. The number varies from the training result, therefore we are talking about hundreds or thousands, it depends on numerous factors such as the precision of the annotations and the variety of samples, etc... It is possible to proceed with the creation of the vector file of positives by

```sh
opencv_createsamples -info positive.txt -num 350 -w 24 -h 24 -vec positives.vect
```

350 may represent the number of previously noted positives.
Now you can start training

```sh
opencv_traincascade -data data -vec positives.vect -bg negative.txt -numPos 330 -numNeg 165 -numStages 14 -w 24 -h 24
```
Generally the number of negatives is half that of positives. The number of stages is proportional to the "accuracy", therefore it is essential to carry out several tests to avoid overtraining and obtain the right balance. At the end of the training a 'cascade.xml' file will be generated in the given directory. This will be fed to the 'detect.py' file to check for dilbert.

The detect.py file tries to detect whether or not all cartoons in the undefined folder have dilbert. The result of this processing is present in the 'detected_dilbert' folder.

<u><b>In this repositories there are only some sample images for each folder.</b></u>

![Dilbert detected](haar_cascade/detected_dilbert/2018-06-28_2.png?raw=true "Dilbert detected")

Next step detect Boss & Dilbert in the same panel! [dilbert-boss-cascade-classifier by GuiZ88](https://github.com/GuiZ88/dilbert-boss-cascade-classifier).

<p align="right">(<a href="#readme-top">back to top</a>)</p>