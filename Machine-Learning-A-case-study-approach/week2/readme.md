Predicting house prices

In this module, we focused on using regression to predict a continuous value (house prices) from features of the house (square feet of living space, number of bedrooms,...). We also built an iPython notebook for predicting house prices, using data from King County, USA, the region where the city of Seattle is located.

In this assignment, we are going to build a more accurate regression model for predicting house prices by including more features of the house. In the process, we will also become more familiar with how the Python language can be used for data exploration, data transformations and machine learning. These techniques will be key to building intelligent applications.

Follow the rest of the instructions on this page to complete your program. When you are done, instead of uploading your code, you will answer a series of quiz questions (see the quiz after this reading) to document your completion of this assignment. The instructions will indicate what data to collect for answering the quiz.

Learning outcomes

Execute programs with the iPython notebook
Load and transform real, tabular data
Compute summaries and statistics of the data
Build a regression model using features of the data
Resources you will need

You will need to install the software tools or use the free Amazon EC2 machine. Instructions for both options are provided in the reading for Module 1.

Download the data and starter code to use GraphLab Create

Before getting started, you will need to download the dataset and the starter iPython notebook that we used in the module.

Download the house sales pricing dataset here, in SFrame format: home_data.gl.zip
Download the house price prediction notebook from the module here: Predicting house prices.ipynb
Save both of these files in the same directory (where you are calling iPython notebook from) and unzip the data file. Not sure where to save the files? See this guide.
Note that there is a bug in GraphLab Create 1.6.0, where the scatter plots don't show up in the notebook. Please upgrade to a newer version, if you have 1.6.0.
Now you are ready to get started!

Note: If you would rather use other ML tools...

You are welcome to use any ML tool for this course, such as scikit-learn. Though, as discussed in the intro module, we strongly recommend you use IPython Notebook and GraphLab Create. (GraphLab Create is free for academic purposes.)

If you are choosing to use other packages, we still recommend you use SFrame, which will allow you to scale to much larger datasets than Pandas. (Though, it's possible to use Pandas in this course, if your machine has sufficient memory.) The SFrame package is available in open-source under a permissive BSD license. So, you will always be able to use SFrames for free.

If you are not using SFrame, here is the dataset for this assignment in CSV format, so you can use Pandas or other options out there: home_data.csv

Watch the video and explore the iPython notebook on predicting house prices

If you haven’t done so yet, before you start, we recommend you watch the video where we go over the iPython notebook on predicting house prices from this module. You can then open up the iPython notebook we used and familiarize yourself with the steps we covered in this example.

