#!/usr/bin/env python
import matplotlib
import pylab as plt
import numpy as np
import time

from EMGs_project import *
from PLOT_project import *


def make_L_transition_Redshift(transition,object_type,sym_color1,sym_color2):

	print ' '
	print ' '
	print '================================================================================================================================='
	print transition, object_type

	data = Extract_EMGs_CSV(object_id='all',object_type=object_type, transition=transition,flag_include='yes',verbose='no')
	data = Make_Unique_EMG_Fluxes(data,transition)
	data = DeLense_Fluxes(data)

	data['L_transition']= Get_Line_Luminosity(data['z'], data['SdV'],transition)
	data['eL_transition']= Get_Line_Luminosity(data['z'], data['eSdV'],transition)

	#where eFWHM=-999 set to 50%
	indices_undefined=[i for i, item in enumerate(data['eFWHM']) if item == -999]
	if indices_undefined != []:
		for j in indices_undefined:
			data['eFWHM'][j]=data['FWHM'][j]*0.5
	#where eL_transition=-999 set to 50%
	indices_undefined=[i for i, item in enumerate(data['eL_transition']) if item == -999]
	if indices_undefined != []:
		for j in indices_undefined:
			data['eL_transition'][j]=data['L_transition'][j]*0.5

	List_EMGs(data)

	#plot data points
	indices_upper_limit=[i for i, item in enumerate(data['eL_transition']) if item == 99]
	indices_err=[i for i, item in enumerate(data['eL_transition']) if item != 99]

	plt.errorbar(data['z'][indices_err],data['L_transition'][indices_err],yerr=data['eL_transition'][indices_err],fmt="none",ecolor=sym_color2)
	plt.plot(data['z'][indices_err],data['L_transition'][indices_err],linestyle='',marker='o',markersize=8,markerfacecolor=sym_color1,markeredgecolor=sym_color2)
	#if indices_upper_limit != []:
	#	plt.errorbar(data['L_transition'][indices_upper_limit],data['FWHM'][indices_upper_limit],xerr=data['eL_transition'][indices_upper_limit],uplims=True,fmt="none",yerr=2.E9,ecolor='DarkRed')
	#	plt.plot(data['L_transition'][indices_upper_limit],data['FWHM'][indices_upper_limit],marker='o',markersize=8,markerfacecolor='LightPink',markeredgecolor='DarkRed')



if __name__=="__main__":
	xlim1=0.01
	xlim2=11.
	ylim1=2.0E8
	ylim2=2.0E13


	#---12CO(1-0)
	transition='12CO(1-0)'
	setup_graph(x_label=r'$z$',y_label=r'$L^{\prime}_{\rm CO}\,{\rm [K\,km\,s^{-1}\,pc^2]}$',fig_size=(8,8))
	plt.yscale('log')
	plt.xlim(xlim1,xlim2)
	plt.ylim(ylim1,ylim2)

	object_type='SMG'
	make_L_transition_Redshift(transition,object_type,'LightPink','DarkRed')
	object_type='BzK'
	make_L_transition_Redshift(transition,object_type,'LightGreen','DarkGreen')
	object_type='HzRG'
	make_L_transition_Redshift(transition,object_type,'LightBlue','DarkBlue')
	object_type='QSO'
	make_L_transition_Redshift(transition,object_type,'Grey','Black')

	plt.savefig('L_CO10_vs_z.pdf')

#	#---12CO(2-1)
	transition='12CO(2-1)'
#	setup_graph(x_label=r'$z$',y_label=r'$L^{\prime}_{\rm CO}\,{\rm [K\,km\,s^{-1}\,pc^2]}$',fig_size=(8,8))
#	#plt.xscale('log')
#	plt.yscale('log')
#	plt.xlim(xlim1,xlim2)
#	plt.ylim(ylim1,ylim2)
#
#	object_type='SMG'
#	make_L_transition_Redshift(transition,object_type,'LightPink','DarkRed')
#	object_type='ULIRG'
#	make_L_transition_Redshift(transition,object_type,'LightBlue','DarkBlue')
#	object_type='BzK'
#	make_L_transition_Redshift(transition,object_type,'LightGreen','DarkGreen')
#	object_type='QSO'
#	make_L_transition_Redshift(transition,object_type,'Grey','Black')
#	object_type='OFRG'
#	make_L_transition_Redshift(transition,object_type,'Black','Black')
#
#	plt.savefig('L_CO21_vs_z.pdf')
#
#
#	#---12CO(3-2)
#	transition='12CO(3-2)'
#	setup_graph(x_label=r'$z$',y_label=r'$L^{\prime}_{\rm CO}\,{\rm [K\,km\,s^{-1}\,pc^2]}$',fig_size=(8,8))
#	#plt.xscale('log')
#	plt.yscale('log')
#	plt.xlim(xlim1,xlim2)
#	plt.ylim(ylim1,ylim2)
#
#	object_type='SMG'
#	make_L_transition_Redshift(transition,object_type,'LightPink','DarkRed')
#	object_type='SFG'
#	make_L_transition_Redshift(transition,object_type,'LightBlue','DarkBlue')
#	object_type='MIPS'
#	make_L_transition_Redshift(transition,object_type,'LightGrey','Black')
#	object_type='BXBM'
#	make_L_transition_Redshift(transition,object_type,'LightGreen','DarkGreen')
#	object_type='QSO'
#	make_L_transition_Redshift(transition,object_type,'Grey','Black')
#	object_type='OFRG'
#	make_L_transition_Redshift(transition,object_type,'Black','Black')
#
#	plt.savefig('L_CO32_vs_z.pdf')
#
#
#	#---12CO(4-3)
#	transition='12CO(4-3)'
#	setup_graph(x_label=r'$z$',y_label=r'$L^{\prime}_{\rm CO}\,{\rm [K\,km\,s^{-1}\,pc^2]}$',fig_size=(8,8))
#	#plt.xscale('log')
#	plt.yscale('log')
#	plt.xlim(xlim1,xlim2)
#	plt.ylim(ylim1,ylim2)
#
#	object_type='SMG'
#	make_L_transition_Redshift(transition,object_type,'LightPink','DarkRed')
#	object_type='QSO'
#	make_L_transition_Redshift(transition,object_type,'Grey','Black')
#	object_type='OFRG'
#	make_L_transition_Redshift(transition,object_type,'Black','Black')
#
#	plt.savefig('L_CO43_vs_z.pdf')
#
#
#	#---12CO(5-4)
#	transition='12CO(5-4)'
#	setup_graph(x_label=r'$z$',y_label=r'$L^{\prime}_{\rm CO}\,{\rm [K\,km\,s^{-1}\,pc^2]}$',fig_size=(8,8))
#	#plt.xscale('log')
#	plt.yscale('log')
#	plt.xlim(xlim1,xlim2)
#	plt.ylim(ylim1,ylim2)
#
#	object_type='SMG'
#	make_L_transition_Redshift(transition,object_type,'LightPink','DarkRed')
#	object_type='QSO'
#	make_L_transition_Redshift(transition,object_type,'Grey','Black')
#
#	plt.savefig('L_CO54_vs_z.pdf')
#
#
#	#---12CO(6-5)
#	transition='12CO(6-5)'
#	setup_graph(x_label=r'$z$',y_label=r'$L^{\prime}_{\rm CO}\,{\rm [K\,km\,s^{-1}\,pc^2]}$',fig_size=(8,8))
#	#plt.xscale('log')
#	plt.yscale('log')
#	plt.xlim(xlim1,xlim2)
#	plt.ylim(ylim1,ylim2)
#
#	object_type='SMG'
#	make_L_transition_Redshift(transition,object_type,'LightPink','DarkRed')
#	object_type='QSO'
#	make_L_transition_Redshift(transition,object_type,'Grey','Black')
#
#	plt.savefig('L_CO65_vs_z.pdf')
#
#	#---12CO(7-6)
#	transition='12CO(7-6)'
#	setup_graph(x_label=r'$z$',y_label=r'$L^{\prime}_{\rm CO}\,{\rm [K\,km\,s^{-1}\,pc^2]}$',fig_size=(8,8))
#	#plt.xscale('log')
#	plt.yscale('log')
#	plt.xlim(xlim1,xlim2)
#	plt.ylim(ylim1,ylim2)
#
#	object_type='SMG'
#	make_L_transition_Redshift(transition,object_type,'LightPink','DarkRed')
#	object_type='QSO'
#	make_L_transition_Redshift(transition,object_type,'Grey','Black')
#
#	plt.savefig('L_CO76_vs_z.pdf')
#
#	#---12CO(8-7)
#	#No sources
#
#	#---12CO(9-8)
#	transition='12CO(9-8)'
#	setup_graph(x_label=r'$z$',y_label=r'$L^{\prime}_{\rm CO}\,{\rm [K\,km\,s^{-1}\,pc^2]}$',fig_size=(8,8))
#	#plt.xscale('log')
#	plt.yscale('log')
#	plt.xlim(xlim1,xlim2)
#	plt.ylim(ylim1,ylim2)
#
#	object_type='SMG'
#	make_L_transition_Redshift(transition,object_type,'LightPink','DarkRed')
#	object_type='QSO'
#	make_L_transition_Redshift(transition,object_type,'Grey','Black')
#
#	plt.savefig('L_CO98_vs_z.pdf')
#
#	#---12CO(10-9)
#	transition='12CO(10-9)'
#	setup_graph(x_label=r'$z$',y_label=r'$L^{\prime}_{\rm CO}\,{\rm [K\,km\,s^{-1}\,pc^2]}$',fig_size=(8,8))
#	#plt.xscale('log')
#	plt.yscale('log')
#	plt.xlim(xlim1,xlim2)
#	plt.ylim(ylim1,ylim2)
#
#	object_type='SMG'
#	make_L_transition_Redshift(transition,object_type,'LightPink','DarkRed')
#	object_type='QSO'
#	make_L_transition_Redshift(transition,object_type,'Grey','Black')
#
#	plt.savefig('L_CO109_vs_z.pdf')
#
#
#	#---12CO(3-2)
#	transition='12CO(3-2)'
#	setup_graph(x_label=r'$z$',y_label=r'$L^{\prime}_{\rm CO}\,{\rm [K\,km\,s^{-1}\,pc^2]}$',fig_size=(8,8))
#	#plt.xscale('log')
#	plt.yscale('log')
#	plt.xlim(xlim1,xlim2)
#	plt.ylim(ylim1,ylim2)
#
#	object_type='SMG'
#	make_L_transition_Redshift(transition,object_type,'LightPink','DarkRed')
#	object_type='QSO'
#	make_L_transition_Redshift(transition,object_type,'Grey','Black')

	plt.savefig('L_CO109_vs_z.pdf')


