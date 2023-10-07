# ಠ_ಠ MAIN ಠ_ಠ

import sys
sys.path.append('./environment')
sys.path.append('./arm')
sys.path.append('./policy')
sys.path.append('./posterior')

import numpy as np
import pickle

from environment.MAB import MAB
from arm.Gaussian import Gaussian
from arm.TruncatedGaussian import TruncatedGaussian
from arm.Uniform import Uniform
from arm.Exponential import Exponential
from numpy import *
from matplotlib.pyplot import *

from policy.UCBVan import UCBVan
from policy.MARS import MARS
from policy.Thompson import Thompson
from policy.BootstrapUCB import BootstrapUCB
from policy.BESAMULTI import BESAMULTI

from Evaluation import *
from posterior.GaussianVar1 import GaussianVar1
from posterior.GaussianVar2 import GaussianVar2

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728','#9467bd']
e_colors = ['#8db8d9', '#ffb27d', '#9ed89e', '#de8280','#c5b0d5']

graphic = 'yes'
store_data = 'no'

scenario = 5
nbRep = 2000
horizon = 2000

# ╔═════════════╦══════════════════════════════════════════╦════════════════════════╗
# ║   Scenario  ║                  Figure                  ║        Location        ║
# ╠═════════════╬══════════════════════════════════════════╬════════════════════════╣
# ║  Scenario 1 ║                 Figure 2a)               ║      Main paper        ║
# ║  Scenario 2 ║                 Figure 2b)               ║      Main paper        ║
# ║  Scenario 3 ║                  Figure 3                ║      Main paper        ║
# ║  Scenario 4 ║                  Figure 1                ║ Supplementary material ║
# ║  Scenario 5 ║                  Figure 2                ║ Supplementary material ║
# ╚═════════════╩══════════════════════════════════════════╩════════════════════════╝

if scenario == 1:
    env = MAB([Gaussian(p,1) for p in [1, 1/2, 1/3, 1/4, 1/5]])
    policies = [UCBVan(env.nbArms, 1), Thompson(env.nbArms,GaussianVar1),MARS(env.nbArms),BootstrapUCB(env.nbArms)]

elif scenario == 2:
    env = MAB([Gaussian(p,1) for p in [1, 1/2, 1/3, 1/4, 1/5]])
    policies = [UCBVan(env.nbArms,2), Thompson(env.nbArms,GaussianVar2),MARS(env.nbArms),BootstrapUCB(env.nbArms)]

elif scenario == 3:
    env = MAB([Uniform(p) for p in [1, 1/2, 1/3, 1/4, 1/5]])
    policies = [UCBVan(env.nbArms, 1), Thompson(env.nbArms,GaussianVar1),MARS(env.nbArms),BootstrapUCB(env.nbArms)]
    
elif scenario == 4:
    env = MAB([TruncatedGaussian(p) for p in [1, 1/2, 1/3, 1/4, 1/5]])
    policies = [UCBVan(env.nbArms, 1), Thompson(env.nbArms,GaussianVar1),MARS(env.nbArms),BootstrapUCB(env.nbArms)]

elif scenario == 5:
    env = MAB([Exponential(1./p) for p in range(1, 6)])
    K = env.nbArms
    policies = [BESAMULTI(env.nbArms),UCBVan(env.nbArms, 1), Thompson(env.nbArms,GaussianVar1),MARS(env.nbArms),BootstrapUCB(env.nbArms)]

tsav = ((np.linspace(10,horizon-1,200)).astype(int))

if graphic == 'yes':
    figure(1)

k = 0

dic_save_data = {}

for policy in policies:
    ev = Evaluation(env, policy, nbRep, horizon, tsav)
    print("mean reward",ev.meanReward())

    varRegret = ev.varRegret()
    meanRegret = ev.meanRegret()
    dic_save_data[policy.__class__.__name__] = (tsav,meanRegret,varRegret)

    if graphic == 'yes':
        errorbar(1+tsav, meanRegret, yerr=varRegret/1000.0, color = colors[k],ecolor=e_colors[k], elinewidth=3, capsize=0)
        xlabel('Round')
        ylabel('Regret')
    k = k+1


if graphic == 'yes':
    legend([policy.__class__.__name__ for policy in policies], loc=0)
    title('Average regret for various policies')
    show()

if store_data == 'yes':
    if scenario == 1:
        file_name = 'fig2a.pkl'
    elif scenario == 2:
        file_name = 'fig2b.pkl'
    elif scenario == 3:
        file_name = 'fig3.pkl'
    elif scenario == 4:
        file_name = 'fig1_supplementary_material.pkl'
    elif scenario == 5:
        file_name = 'fig2_supplementary_material.pkl'

    file_path = "stored_simulation/" + file_name
    f = open(file_name,"wb")
    pickle.dump(dic_save_data,f)
    f.close()
