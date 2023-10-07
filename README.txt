## Maximum Average Randomly Sampled: A Scale Free and Non-parametric Algorithm for Stochastic Bandits

These files have been tested and verified to work with Python 3.10.6

Files included in the current release:

├── Evaluation.py
├── README.txt
├── Result.py
├── arm/
│   ├── Arm.py
│   ├── Exponential.py
│   ├── Gaussian.py
│   ├── TruncatedGaussian.py
│   ├── Uniform.py
│   ├── __init__.py
├── environment/
│   ├── Environment.py
│   ├── MAB.py
│   ├── __init__.py
├── main.py                            >> *** This is the main entry point of the simulation ***
├── plot_stored_simulation.ipynb       >> The pickle files stored in the directory "stored_simulation" are plotted here.
├── policy/
│   ├── BESA.py
│   ├── BESAMULTI.py                   >> BESA Approach
│   ├── BootstrapUCB.py                >> Bootstrap Upper Confidence Bound (UCB) policy 
│   ├── IndexPolicy.py
│   ├── MARS.py                        >> **** Policy Maximum Average Randomly Sampled (MARS) poroposed in the paper ****
│   ├── Policy.py
│   ├── Thompson.py                    >> Method Thompson Sampling policy
│   ├── UCBVan.py                      >> Vanilla Upper Confidence Bound (UCB) policy 
│   ├── __init__.py 
├── posterior/
│   ├── GaussianVar1.py
│   ├── GaussianVar2.py
│   ├── Posterior.py
│   ├── __init__.py
└── stored_simulation/                 >>  The output of the main.py file was saved in pickle files and stored in this location.


#Installation

To install the required dependencies for this Python package, please follow these steps:

- Make sure you have Python 3.x installed on your system.
- Run the following command to install the dependencies listed in the requirements.txt file:
>> pip install -r requirements.txt

This command will automatically install all the necessary packages.