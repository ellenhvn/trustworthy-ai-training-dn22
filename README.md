# trustworthy-ai-training-dn22

# About this training

Experience practical tools and best practices to apply in your daily work with a specific focus on AI explainability and AI fairness to answer questions such as: 
* How do you explain your AI's decisions to your user? 
* How to explain a single prediction? Or even an entire model? 
* When and how is your AI fair? 
* How to embed this in ML systems?

This training covers the following aspects of trustworthy AI:
- Explainability
- Fairness

It does not cover:
- Robustness
- Privacy
- Transparency 

For more information and reading materials on those, please refer to [useful links and further reading](#useful-links-and-further-reading)

<p>
    <img src="assets/img/Trustworthy AI Overview.png"/>
</p>

The focus of this training is understanding the methods and concepts behind explainability and fairness, not focusing on specific tools or products.

# Where to start

First, make sure you have your local environment set up following the steps listed below in the [set-up section](#setup). 

For this training we will __not__ focus on data preparation, exploration and model training, and you can simply use the 
already cleaned data and trained model which are stored in the data and model directories.

The tutorial consists of the following parts:
* Explainability, where we will use Shap and ELI5 to understand local and global explainability.
* Fairness, where we will use the IBM Research AIF360 package to calculate fairness metrics and mitigate bias.

The notebooks are independent from one another and you don't need to work through them in a given order.
We will not be able to cover all content together during the workshop, but you can use these notebooks for future reference. 

# Setup

**If you run into issues during the local setup, you can view the html versions of the notebooks to follow along!** 
(or view the notebooks here on Github) 

Clone this repository on your local machine by typing the following on a terminal *(or by using one 
of the other options available via the green Code button)* & navigate to the cloned repo.

```
git clone git@github.com:ellenhvn/trustworthy-ai-training-dn22.git
```
```
cd path/to/the/folder/trustworthy-ai-training-dn22
```

For the environment set-up you can use Conda or pip, following either one of the two options listed below as you prefer.

### Environment set-up: Option 1 (Conda)

```
conda env create -f environment.yml
conda activate dn-tai-env
```

### Environment set-up: Option 2 (Pip)

```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Alternatively, create an environment yourself with the following packages:
- Pandas
- Numpy
- Jupyter
- Shap
- sklearn
- eli5
- aif360
- matplotlib

# Structure

Structure of the repo

    .
    ├── assets                  
    │   └─── img                
    ├── config                  
    ├── data                    
    │   └─── raw
    │   └─── preprocessed      
    ├── models                 
    ├── notebooks               
    ├── src                    
    │   └─── features           
    │   └─── models
    └── README.md
    └── environment.yaml
    └── requirements.txt

# Use case and data

Loans form an integral part of banking operations. 
However, not all the loans are promptly returned and hence it is important for a bank to closely monitor and 
understand loan applications so that they know which loans to reject and which to approve.

For this workshop we use the German credit data set 
(https://archive.ics.uci.edu/ml/datasets/statlog+(german+credit+data)). 
It contains details of 1000 loan applicants with 20 attributes and the classification whether an applicant is 
considered a "good" or a "bad" credit risk (target).

# Useful links and further reading 

During this tutorial we do not cover all aspects of trustworthy ML. Here are some useful links for further 
reading on the topics. The AIX360 and AIF360 links also contain demos where you can easily explore different
explainability and fairness algorithms. 

* AIX360: http://aix360.mybluemix.net/ 
* AIF360: http://aif360.mybluemix.net/
* OpenScale Tutorial: https://developer.ibm.com/tutorials/getting-started-with-watson-openscale/
* Awesome Production ML: https://github.com/EthicalML/awesome-production-machine-learning
* Awesome ML Interpretability: https://github.com/jphall663/awesome-machine-learning-interpretability
* Interpretable ML Book: https://christophm.github.io/interpretable-ml-book/

__Author:__ Ellen Hoeven, Lead Data Scientist IBM Client Engineering DACH

This tutorial was developed for Data Natives 2022. 
The tutorial builds upon internal training material for a workshop of multiple days on trustworthy AI for data scientists.
If you are interested in learning more about this, please reach out! 

Copyright © IBM Corp. 2022