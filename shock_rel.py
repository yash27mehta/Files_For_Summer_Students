#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 11:52:45 2019

@author: yashmehta
"""
import numpy as np
import subprocess as sp
tmp = sp.call('clear', shell=True)





#==========================================================================
# Problem specific parameters
R  = 1.0    # Universal Gas Constant
Ms = 1.67    # Shock Mach number
# Cp = 1004.64    # Specific heat
g  = 1.4        # gamma for air
#==========================================================================

#==========================================================================
# Flow field downstream of the shock (quiescent-ambient condition)
u1 = 0.0 
#p1 = 83315.0844298 
T1 = 1.0 
rho1 = 1.0
#p1 = 0.05E+06
p1 = (rho1*T1)/g
#T1 = p1/(rho1*R)
#T1 = 310.86329916
c1 = (g*p1/rho1)**0.5 
us = Ms*c1      # Shock velocity
#==========================================================================

#==========================================================================
# Flow field behind the shock (Rankine-Hugoniot relations)
p2p1 = 1 + 2*g*(Ms**2-1)/(g+1) 
rho2rho1 = (Ms**2)/(1 + (Ms**2-1)*(g-1)/(g+1)) 
T2T1 = (1 + (Ms**2-1)*2*g/(g+1))*(2 + (g-1)*Ms**2)/((g+1)*Ms**2) 
p2   = p1*p2p1 
rho2 = rho1*rho2rho1 
T2   = T1*T2T1 
M2   = ((1+.5*(g-1)*Ms**2)/(g*Ms**2-.5*(g-1)))**0.5  
c2   = (g*p2/rho2)**0.5
u2   = M2*c2 
u2   = us-u2 
# Moving normal shock!!!(changing the frame of reference)
M2   = u2/c2  
print(M2)
#==========================================================================

#==============================================================================
# Knudsen number stuff
# Kn = Ma/Re(sqrt(g*pi/2))
const_1 = (np.pi*g/2)**0.5
Kn_max = 0.009
Ma_Re_max = Kn_max/const_1 # Ma/Re max based on Kn_max

#==============================================================================
# initial conditions for the code

rho1_code = rho1/rho1
rho2_code = rho2/rho1

u1_code = u1/c1
u2_code = u2/c1

T1_code = T1/T1
T2_code = T2/T1

rho_p = 63.66197724 # kg/m^3
rho_p_code = rho_p/rho1

#===============================================================================
# Getting the particle Reynolds number based on Acoustic Reynolds number

S1 = 0.4122000e-00 ;
mu1 = ((1+S1)/((T1/T1)+S1))*(T1/T1)**(1.5) ;
mu2 = ((1+S1)/((T2/T1)+S1))*(T2/T1)**(1.5) ;

# Rep based on the conditions given by Tanner
#mu_g = (2.077E-05)
#Dp = 5E-06

#Re_min = M2/Ma_Re_max # Min Rep based on Max Kn
Rep = 200 # Particle Re (user specified)
#Rep = (rho2*Dp*u2)/mu_g
Rea_Rep = (rho1/rho2)*(c1/u2)*1*(mu2/mu1) ;
Ref_Rep = (rho1/rho2)*(u2/u2)*1*(mu2/mu1) ;
#Rea_Rep = (rho1/rho2)*(1/Ms)*1*(mu1/mu2) ;
Rea = (Rep)*Rea_Rep 
#Ref = (Rep)*Ref_Rep

# Rea_Tanner = (50/(rho2*u2))*(T2**1.5)*((1+S1)/(T2+S1))


# Dp_mu = Re_min/(rho2*u2)