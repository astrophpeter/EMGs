#!/usr/bin/env python
import matplotlib
import pylab as plt
import numpy as np
import time
import math 
import scipy
from scipy import stats


from EMGs import *
from PLOT import *






def pltlvfwhm(transition,object_type):
	 
        print ' '
        print ' '
        print '================================================================================================================================='
        print transition, object_type, 'un-lensed'

        dataul = Extract_EMGs_CSV(object_id='all',object_type=object_type, transition=transition,flag_include='yes',verbose='no',u='yes')
        dataul = Make_Unique_EMG_Fluxes(dataul,transition)
       

        dataul['L_transition']= Get_Line_Luminosity(dataul['z'], dataul['SdV'],transition)
        dataul['eL_transition']= Get_Line_Luminosity(dataul['z'], dataul['eSdV'],transition)
	 
        #remove objects with no FWHM measurements
        indices_keep=[i for i, item in enumerate(dataul['FWHM']) if item != -999]
        if indices_keep != []:
                dataul=dataul[indices_keep]
        #where eFWHM=-999 set to 50%
        indices_undefined=[i for i, item in enumerate(dataul['eFWHM']) if item == -999]
        if indices_undefined != []:
                for j in indices_undefined:
                        dataul['eFWHM'][j]=dataul['FWHM'][j]*0.5
        #where eL_transition=-999 set to 50%
        indices_undefined=[i for i, item in enumerate(dataul['eL_transition']) if item == -999]
        if indices_undefined != []:
                for j in indices_undefined:
                        dataul['eL_transition'][j]=dataul['L_transition'][j]*0.5
	
        List_EMGs(dataul)


        print ' '
        print ' '
        print '================================================================================================================================='
        print transition, object_type, 'lensed'

        datal = Extract_EMGs_CSV(object_id='all',object_type=object_type, transition=transition,flag_include='yes',verbose='no',u='no')
        datal = Make_Unique_EMG_Fluxes(datal,transition)
	         
 
        datal['L_transition']= Get_Line_Luminosity(datal['z'], datal['SdV'],transition)
        datal['eL_transition']= Get_Line_Luminosity(datal['z'], datal['eSdV'],transition)
 
        #remove objects with no FWHM measurements
        indices_keep=[i for i, item in enumerate(datal['FWHM']) if item != -999]
        if indices_keep != []:
                datal=datal[indices_keep]
        #where eFWHM=-999 set to 50%
        indices_undefined=[i for i, item in enumerate(datal['eFWHM']) if item == -999]
        if indices_undefined != []:
                for j in indices_undefined:
                        datal['eFWHM'][j]=datal['FWHM'][j]*0.5
        #where eL_transition=-999 set to 50%
        indices_undefined=[i for i, item in enumerate(datal['eL_transition']) if item == -999]
        if indices_undefined != []:
                for j in indices_undefined:
                        datal['eL_transition'][j]=datal['L_transition'][j]*0.5
	#remove objects with no magnification factor
        indices_keep=[i for i, item in enumerate(datal['magnification']) if item != '-999']
        if indices_keep != []:
                datal=datal[indices_keep]
	
	List_EMGs(datal)

	#set up graph
        setup_graph(y_label=r'$L^{\prime}_{\rm CO,app}\,{\rm [K\,km\,s^{-1}\,pc^2]}$', x_label=r'${\rm FWHM}\,{\rm [km\,s^{-1}]}$', fig_size=(8,8))
        plt.xscale('log')
        plt.yscale('log')
        plt.xlim(150,1500)
        plt.ylim(4000000000,1000000000000)
	plt.xticks([250,500,1000],[r'$250$',r'$500$',r'$1000$'])
	

        #plot data points for lensed data
#       indices_upper_limit=[i for i, item in enumerate(datal['eL_transition']) if item == 99]
        indices_err=[i for i, item in enumerate(datal['eL_transition']) if item != 99]
 
        plt.errorbar(datal['FWHM'][indices_err],datal['L_transition'][indices_err],xerr=datal['eFWHM'][indices_err],yerr=datal['eL_transition'][indices_err],fmt="none",ecolor='RoyalBlue')
        plt.plot(datal['FWHM'][indices_err],datal['L_transition'][indices_err],label=r'$Lensed',linestyle='',marker='^',markersize=8,markerfacecolor='RoyalBlue',markeredgecolor='RoyalBlue')
#        plt.legend(bbox_to_anchor=(0.90, 0.85),bbox_transform=plt.gcf().transFigure)
        


        #plot data points for un-lensed data
        indices_upper_limit=[i for i, item in enumerate(dataul['eL_transition']) if item == 99]
        indices_err=[i for i, item in enumerate(dataul['eL_transition']) if item != 999]
 
        plt.errorbar(dataul['FWHM'][indices_err],dataul['L_transition'][indices_err],xerr=dataul['eFWHM'][indices_err],yerr=dataul['eL_transition'][indices_err],fmt="none",ecolor='Crimson')
	plt.plot(dataul['FWHM'][indices_err],dataul['L_transition'][indices_err],label=r'$Unlensed$',linestyle='',marker='o',markersize=8,markerfacecolor='Crimson',markeredgecolor='Crimson')
#        plt.legend(bbox_to_anchor=(0.90, 0.35),bbox_transform=plt.gcf().transFigure)	
	
#    	if indices_upper_limit != []:
#		plt.errorbar(dataul['L_transition'][indices_upper_limit],dataul['FWHM'][indices_upper_limit],xerr=dataul['eL_transition'][indices_upper_limit],uplims=True,fmt="none",yerr=2.E9,ecolor='Crimson')
#	plt.plot(dataul['L_transition'][indices_upper_limit],dataul['FWHM'][indices_upper_limit],marker='o',markersize=8,markerfacecolor='Crimson',markeredgecolor='Crimson')


        #plot power-law fit for ul-lensed data      
	m, b = np.polyfit(np.log10(dataul['FWHM']),np.log10(dataul['L_transition']),1)
        x = np.arange(0, 4000., 1)
        plt.plot(x, (10**b)*(x**m),linestyle='-',color='Crimson',linewidth=2.0)
############################################################################################################################################
        slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(np.log10(dataul['FWHM']),np.log10(dataul['L_transition']))      
	print '====='
	print slope,intercept,r_value,p_value, std_err
	print '====='
	print m , b
############################################################################################################################################ 
	#plot power-law fit from Harris et al (2012)
#        plt.plot(x,(10**6.03)*(x**1.7), linestyle='dashed',color='Black')
	plt.savefig('J:3-2')

	#derive magnification for lensed data
	magfloat = [float(i) for i in datal['magnification']]
	magderive = (datal['L_transition'])/((10**b)*(datal['FWHM']**m))
	fracmagerr = ((m*datal['eFWHM']/datal['FWHM'])**2+(datal['eL_transition']/datal['L_transition'])**2)**0.5
	magfrac=(magderive-magfloat)/(magfloat)
	

	
	

	
	#plot mag-mag relations
	setup_graph(x_label=r'$\mu_{l}$', y_label=r'$\mu_{r}$', fig_size=(8,8))
	plt.xlim(0,35)
	plt.ylim(0,35)
	xdat=np.arange(0,40,1)
	plt.plot(xdat,xdat,label='direct correspondance',linestyle='dashed',color='black')
	plt.plot(magfloat,magderive,linestyle='', marker='s',markerfacecolor='Green',markeredgecolor='Green')
  	plt.errorbar(magfloat,magderive,xerr=0,yerr=fracmagerr*magderive,fmt="none",ecolor='Green')	
	plt.show()

	#plot mag deviation from literature 
	setup_graph(x_label=r'$\mu_{l}$', y_label=r'$(\mu_{r}-\mu_{l})/\mu_{l}$', fig_size=(8,8))
	plt.xlim(0,35)
	plt.ylim(-1.5,11)
	plt.plot(magfloat,(magderive-magfloat)/magfloat,linestyle='',marker='s',markerfacecolor='DarkRed',markeredgecolor='DarkRed')
	plt.errorbar(magfloat,(magderive-magfloat)/magfloat,xerr=0,yerr=fracmagerr*(magderive-magfloat)/magfloat,fmt="none",ecolor='DarkRed')
	plt.plot(xdat,xdat*0,linestyle='dashed',color='black')
  	plt.show()
#	err=fracmagerr*magderive
	print m 
 	print datal['reference']

pltlvfwhm('12CO(3-2)','SMG')
	 


