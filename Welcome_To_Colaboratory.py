# Databricks notebook source
# MAGIC %md
# MAGIC <a href="https://colab.research.google.com/github/fflory/test/blob/master/Welcome_To_Colaboratory.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# COMMAND ----------

# MAGIC %md
# MAGIC <img height="45px" src="https://colab.research.google.com/img/colab_favicon.ico" align="left" hspace="10px" vspace="0px">
# MAGIC 
# MAGIC <h1>Welcome to Colaboratory!</h1>
# MAGIC 
# MAGIC Colaboratory is a free Jupyter notebook environment that requires no setup and runs entirely in the cloud.
# MAGIC 
# MAGIC With Colaboratory you can write and execute code, save and share your analyses, and access powerful computing resources, all for free from your browser.

# COMMAND ----------

# MAGIC %md
# MAGIC my text

# COMMAND ----------

#@title Introducing Colaboratory
#@markdown This 3-minute video gives an overview of the key features of Colaboratory:
from IPython.display import YouTubeVideo
YouTubeVideo('inN8seMm7UI', width=600, height=400)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Getting Started
# MAGIC 
# MAGIC The document you are reading is a  [Jupyter notebook](https://jupyter.org/), hosted in Colaboratory. It is not a static page, but an interactive environment that lets you write and execute code in Python and other languages.
# MAGIC 
# MAGIC For example, here is a **code cell** with a short Python script that computes a value, stores it in a variable, and prints the result:

# COMMAND ----------

seconds_in_a_day = 24 * 60 * 60
seconds_in_a_day

# COMMAND ----------

# MAGIC %md
# MAGIC To execute the code in the above cell, select it with a click and then either press the ▷ button to the left of the code, or use the keyboard shortcut "⌘/Ctrl+Enter".
# MAGIC 
# MAGIC All cells modify the same global state, so variables that you define by executing a cell can be used in other cells:

# COMMAND ----------

seconds_in_a_week = 7 * seconds_in_a_day
seconds_in_a_week

# COMMAND ----------

# MAGIC %md
# MAGIC For more information about working with Colaboratory notebooks, see [Overview of Colaboratory](/notebooks/basic_features_overview.ipynb).

# COMMAND ----------

# MAGIC %md
# MAGIC ## More Resources
# MAGIC 
# MAGIC Learn how to make the most of Python, Jupyter, Colaboratory, and related tools with these resources:
# MAGIC 
# MAGIC ### Working with Notebooks in Colaboratory
# MAGIC - [Overview of Colaboratory](/notebooks/basic_features_overview.ipynb)
# MAGIC - [Guide to Markdown](/notebooks/markdown_guide.ipynb)
# MAGIC - [Importing libraries and installing dependencies](/notebooks/snippets/importing_libraries.ipynb)
# MAGIC - [Saving and loading notebooks in GitHub](https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb)
# MAGIC - [Interactive forms](/notebooks/forms.ipynb)
# MAGIC - [Interactive widgets](/notebooks/widgets.ipynb)
# MAGIC 
# MAGIC ### Working with Data
# MAGIC - [Loading data: Drive, Sheets, and Google Cloud Storage](/notebooks/io.ipynb) 
# MAGIC - [Charts: visualizing data](/notebooks/charts.ipynb)
# MAGIC - [Getting started with BigQuery](/notebooks/bigquery.ipynb)
# MAGIC 
# MAGIC ### Machine Learning Crash Course
# MAGIC These are a few of the notebooks from Google's online Machine Learning course. See the [full course website](https://developers.google.com/machine-learning/crash-course/) for more.
# MAGIC - [Intro to Pandas](/notebooks/mlcc/intro_to_pandas.ipynb)
# MAGIC - [Tensorflow concepts](/notebooks/mlcc/tensorflow_programming_concepts.ipynb)
# MAGIC - [First steps with TensorFlow](/notebooks/mlcc/first_steps_with_tensor_flow.ipynb)
# MAGIC - [Intro to neural nets](/notebooks/mlcc/intro_to_neural_nets.ipynb)
# MAGIC - [Intro to sparse data and embeddings](/notebooks/mlcc/intro_to_sparse_data_and_embeddings.ipynb)
# MAGIC 
# MAGIC ### Using Accelerated Hardware
# MAGIC - [TensorFlow with GPUs](/notebooks/gpu.ipynb)
# MAGIC - [TensorFlow with TPUs](/notebooks/tpu.ipynb)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Machine Learning Examples: Seedbank
# MAGIC 
# MAGIC To see end-to-end examples of the interactive machine learning analyses that Colaboratory makes possible, check out the [Seedbank](https://research.google.com/seedbank/) project.
# MAGIC 
# MAGIC A few featured examples:
# MAGIC 
# MAGIC - [Neural Style Transfer](https://research.google.com/seedbank/seed/neural_style_transfer_with_tfkeras): Use deep learning to transfer style between images.
# MAGIC - [EZ NSynth](https://research.google.com/seedbank/seed/ez_nsynth): Synthesize audio with WaveNet auto-encoders.
# MAGIC - [Fashion MNIST with Keras and TPUs](https://research.google.com/seedbank/seed/fashion_mnist_with_keras_and_tpus): Classify fashion-related images with deep learning.
# MAGIC - [DeepDream](https://research.google.com/seedbank/seed/deepdream): Produce DeepDream images from your own photos.
# MAGIC - [Convolutional VAE](https://research.google.com/seedbank/seed/convolutional_vae): Create a generative model of handwritten digits.
