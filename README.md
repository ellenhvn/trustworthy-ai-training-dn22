# trustworthy-ai-training-dn22

# About this training

Experience practical tools and best practices to apply in your daily work with a specific focus on AI explainability and AI fairness to answer questions such as: 
* How do you explain your AI's decisions to your user? 
* How to explain a single prediction? Or even an entire model? 
* When and how is your AI fair? 

# Where to start

First, make sure you have your local environment set up following the steps listed below in the set-up section. 

For this training we will not focus on data preparation, exploration and model training and you can simply use the already cleaned data and trained model (xxx model).
If you want to explore these areas a bit more, you can check out xxxx. 

After the data preparation and model training steps, the tutorial is split into three independent parts:
* 1. Explainability
* 2. Fairness
* 3. Model monitoring and drift 

It is recommended to work through them in the given order but you don't necessarily have to. 

Ultimately, you can run a Streamlit app to show your created explainability artefacts. 

# Structure

Structure of the repo

    .
    ├── src                     # Source files for scripts (e.g. train a model)
    ├── data                    # Raw and/or pre-processed data (for this tutorial we have the data already stored and processed)
    ├── notebooks               # Jupyter notebooks for exploration
    ├── model                   # Where to save model artifacts
    └── README.md
    └── requirements.txt

# Get started 

# Use case and data 

![Alt text](assets/img/Use Case.png "Use Case Personas")

* We use a credit approval example case with different personas involved: the bank customer, the loan approval officer & supervisor, and regulatory bodies. 

* Original data: https://archive.ics.uci.edu/ml/datasets/statlog+(german+credit+data)

# Useful links & further reading 
* AIX360: 
* AIF360:
* Awesome Ethical ML: 
* OpenScale Tutorial: 


__Author:__ Ellen Hoeven, Lead Data Scientist IBM Client Engineering DACH (ellen.hoeven@ibm.com) 

This tutorial was developed for Data Natives 2022. 

Copyright © IBM Corp. 2022