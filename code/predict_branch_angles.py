import numpy as np
import pandas as pd
import math as m
import matplotlib.pyplot as plt

# simulation = 'C:\\Users\\u1056\\Fracture_Project_simulations\\PULLING\\Classic_numerical_Example\\example_analysis_data.SIF'
simulation = 'C:\\Users\\u1056\\Fracture_Project_simulations\\PULLING\\Classic_numerical_Example\\example_analysis_data_initial_lower_insertion.SIF'
#everything should be in units of MPa and mm


def get_KI(sim_df):
    KIs = sim_df['KI']
    return KIs.mean()

def get_KII(sim_df):
    KIIs = sim_df['KII']
    return KIIs.mean()

def get_Jx(KI, KII, E, nu):
    Jx = np.zeros(4)
    Jx[0] = (((1 - nu**2)/(4*E)) * (KI**2 + KII**2)) + (((1 - nu**2)/(np.pi*E)) * (KI* KII))
    Jx[1] = (((1 - nu**2)/(4*E)) * (KI**2 + KII**2)) - (((1 - nu**2)/(np.pi*E)) * (KI* KII))
    Jx[2] = (((1 - nu**2)/(4*E)) * (KI**2 + KII**2)) + (((1 - nu**2)/(np.pi*E)) * (KI* KII))
    Jx[3] = (((1 - nu**2)/(4*E)) * (KI**2 + KII**2)) - (((1 - nu**2)/(np.pi*E)) * (KI* KII))
    return Jx

def get_Jy(KI, KII, E, nu):
    Jy = np.zeros(4)
    Jy[0] = (((1 - nu**2)/(2*np.pi*E)) * (-KI**2 + KII**2)) - (((1 - nu**2)/(2*E)) * (KI* KII))
    Jy[1] = (((1 - nu**2)/(2*np.pi*E)) * (KI**2 - KII**2)) - (((1 - nu**2)/(2*E)) * (KI* KII))
    Jy[2] = (((1 - nu**2)/(2*np.pi*E)) * (KI**2 - KII**2)) + (((1 - nu**2)/(2*E)) * (KI* KII))
    Jy[3] = (((1 - nu**2)/(2*np.pi*E)) * (-KI**2 + KII**2)) + (((1 - nu**2)/(2*E)) * (KI* KII))
    return Jy

E = 32000 #MPa
nu = 0.2 #poisson ratio
Gc = 0.0001

sim_df = pd.read_csv(simulation)
sim_df = sim_df.drop(0, axis=0)
KI = get_KI(sim_df)
KII = get_KII(sim_df)
# KII = 0

Jx = get_Jx(KI, KII, E, nu)
Jy = get_Jy(KI, KII, E, nu)

""" get the equation for G based on the Jx and Jy calculations """
two_secondaries = False
if(Jy[0] > 0 and Jy[1] < 0):
    G_upper = lambda alpha: Jx[0] * np.cos(alpha) + Jy[0] * np.sin(alpha)
    G_lower = lambda alpha: Jx[1] * np.cos(alpha) + Jy[3] * np.sin(alpha)
    two_secondaries = True
elif(Jy[0] < 0 and Jy[1] > 0):
    G_upper = lambda alpha: Jx[1] * np.cos(alpha) + Jy[1] * np.sin(alpha)
    G_lower = lambda alpha: Jx[0] * np.cos(alpha) + Jy[2] * np.sin(alpha)
    two_secondaries = True


if(two_secondaries):
    ''' calculating G for all of the angles between -90 and 90 degrees'''
    alphas = np.arange(-90, 90, 0.01) * np.pi /180.0
    G_upper_secondary_crack = G_upper(alphas)
    G_lower_secondary_crack = G_lower(alphas)

    """ now that youve calculated G for all these angles, find the max. If the max out of all of the angles is greater than Gc, then the crack will branch at those angles. """
    max_upper_G = G_upper_secondary_crack.max()
    max_lower_G = G_lower_secondary_crack.max()

    if(max_upper_G > Gc and max_lower_G > Gc):
        upper_angle = alphas[np.where(G_upper_secondary_crack == max_upper_G)[0]] * 180.0 / np.pi
        lower_angle = -alphas[np.where(G_lower_secondary_crack == max_lower_G)[0]] * 180.0 / np.pi
else:
    upper_angle = 2 * np.arctan(1/4*(KI / KII) - np.sign(KII)*np.sqrt(8 + (KI/KII)**2))
    lower_angle = 0

print(upper_angle)
print(lower_angle)



