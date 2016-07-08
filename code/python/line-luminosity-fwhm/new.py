#!/usr/bin/env python
import matplotlib
import pylab as plt
import numpy as np
import time

from EMGs import *
from PLOT import *



if __name__=="__main__":

	object_id='all'
	object_type='SMG'
	transition='all'
	flag_include='no'
	data = Extract_EMGs_CSV(object_id=object_id,object_type=object_type, transition=transition,flag_include='no',verbose='no')

	print data['transition']
	print data['ID']
	print data['magnification']
	print data['FWHM']
	print data['type']

	object_id='all'
	object_type='QSO'
	transition='all'
	flag_include='no'
	data = Extract_EMGs_CSV(object_id=object_id,object_type=object_type, transition=transition,flag_include='no',verbose='no')

#	print ' '
#	print ' '
#	print '================================================================================================================================='
#	print transition, object_type
#
#	data = Make_Unique_EMG_Fluxes(data,transition)
#	data = DeLense_Fluxes(data)
#
#	data['L_transition']= Get_Line_Luminosity(data['z'], data['SdV'],transition)
#	data['eL_transition']= Get_Line_Luminosity(data['z'], data['eSdV'],transition)
#
#	#remove objects with no FWHM measurements
#	indices_keep=[i for i, item in enumerate(data['FWHM']) if item != -999]
#	if indices_keep != []:
#		data=data[indices_keep]
#	#where eFWHM=-999 set to 50%
#	indices_undefined=[i for i, item in enumerate(data['eFWHM']) if item == -999]
#	if indices_undefined != []:
#		for j in indices_undefined:
#			data['eFWHM'][j]=data['FWHM'][j]*0.5
#	#where eL_transition=-999 set to 50%
#	indices_undefined=[i for i, item in enumerate(data['eL_transition']) if item == -999]
#	if indices_undefined != []:
#		for j in indices_undefined:
#			data['eL_transition'][j]=data['L_transition'][j]*0.5
#
#	List_EMGs(data)
#
#	#plot data points
#	indices_upper_limit=[i for i, item in enumerate(data['eL_transition']) if item == 99]
#	indices_err=[i for i, item in enumerate(data['eL_transition']) if item != 99]
#
#	plt.errorbar(data['L_transition'][indices_err],data['FWHM'][indices_err],xerr=data['eL_transition'][indices_err],yerr=data['eFWHM'][indices_err],fmt="none",ecolor=sym_color2)
#	plt.plot(data['L_transition'][indices_err],data['FWHM'][indices_err],linestyle='',marker='o',markersize=8,markerfacecolor=sym_color1,markeredgecolor=sym_color2)
#	#if indices_upper_limit != []:
#	#	plt.errorbar(data['L_transition'][indices_upper_limit],data['FWHM'][indices_upper_limit],xerr=data['eL_transition'][indices_upper_limit],uplims=True,fmt="none",yerr=2.E9,ecolor='DarkRed')
#	#	plt.plot(data['L_transition'][indices_upper_limit],data['FWHM'][indices_upper_limit],marker='o',markersize=8,markerfacecolor='LightPink',markeredgecolor='DarkRed')
#
#
#

#	xlim1=2.0E8
#	xlim2=2.0E13
#	ylim1=1.0
#	ylim2=4000.
#
#	#---CII
#	transition='[CII]158'
#	setup_graph(x_label=r'$L^{\prime}_{\rm CII}\,{\rm [K\,km\,s^{-1}\,pc^2]}$', y_label=r'${\rm FWHM}\,{\rm [km\,s^{-1}]}$', fig_size=(8,8))
#	plt.xscale('log')
#	plt.yscale('log')
#	plt.xlim(xlim1,xlim2)
#	plt.ylim(ylim1,ylim2)
#
#	object_type='SMG'
#	make_all(transition,object_type,'LightPink','DarkRed')
#	#object_type='BzK'
#	#make_all(transition,object_type,'LightGreen','DarkGreen')
#	#object_type='HzRG'
#	#make_all(transition,object_type,'LightBlue','DarkBlue')
#	object_type='QSO'
#	make_all(transition,object_type,'Grey','Black')
#
#	plt.savefig('L_CII_vs_FWHM_CII.pdf')
#
#
#	#---12CO(1-0)
#	transition='12CO(1-0)'
#	setup_graph(x_label=r'$L^{\prime}_{\rm CO}\,{\rm [K\,km\,s^{-1}\,pc^2]}$', y_label=r'${\rm FWHM}\,{\rm [km\,s^{-1}]}$', fig_size=(8,8))
#	plt.xscale('log')
#	plt.yscale('log')
#	plt.xlim(xlim1,xlim2)
#	plt.ylim(ylim1,ylim2)
#
#	object_type='SMG'
#	make_all(transition,object_type,'LightPink','DarkRed')
#	object_type='BzK'
#	make_all(transition,object_type,'LightGreen','DarkGreen')
#	object_type='HzRG'
#	make_all(transition,object_type,'LightBlue','DarkBlue')
#	object_type='QSO'
#	make_all(transition,object_type,'Grey','Black')
#
#	plt.savefig('L_CO10_vs_FWHM_CO10.pdf')
#
#	#---12CO(2-1)
#	transition='12CO(2-1)'
#	setup_graph(x_label=r'$L^{\prime}_{\rm CO}\,{\rm [K\,km\,s^{-1}\,pc^2]}$', y_label=r'${\rm FWHM}\,{\rm [km\,s^{-1}]}$', fig_size=(8,8))
#	plt.xscale('log')
#	plt.yscale('log')
#	plt.xlim(xlim1,xlim2)
#	plt.ylim(ylim1,ylim2)
#
#	object_type='SMG'
#	make_all(transition,object_type,'LightPink','DarkRed')
#	object_type='ULIRG'
#	make_all(transition,object_type,'LightBlue','DarkBlue')
#	object_type='BzK'
#	make_all(transition,object_type,'LightGreen','DarkGreen')
#	object_type='QSO'
#	make_all(transition,object_type,'Grey','Black')
#	object_type='OFRG'
#	make_all(transition,object_type,'Black','Black')
#
#	plt.savefig('L_CO21_vs_FWHM_CO21.pdf')
#
#
#	#---12CO(3-2)
#	transition='12CO(3-2)'
#	setup_graph(x_label=r'$L^{\prime}_{\rm CO}\,{\rm [K\,km\,s^{-1}\,pc^2]}$', y_label=r'${\rm FWHM}\,{\rm [km\,s^{-1}]}$', fig_size=(8,8))
#	plt.xscale('log')
#	plt.yscale('log')
#	plt.xlim(xlim1,xlim2)
#	plt.ylim(ylim1,ylim2)
#
#	object_type='SMG'
#	make_all(transition,object_type,'LightPink','DarkRed')
#	object_type='SFG'
#	make_all(transition,object_type,'LightBlue','DarkBlue')
#	object_type='MIPS'
#	make_all(transition,object_type,'LightGrey','Black')
#	object_type='BXBM'
#	make_all(transition,object_type,'LightGreen','DarkGreen')
#	object_type='QSO'
#	make_all(transition,object_type,'Grey','Black')
#	object_type='OFRG'
#	make_all(transition,object_type,'Black','Black')
#
#	plt.savefig('L_CO32_vs_FWHM_CO32.pdf')
#
#	#---12CO(4-3)
#	transition='12CO(4-3)'
#	setup_graph(x_label=r'$L^{\prime}_{\rm CO}\,{\rm [K\,km\,s^{-1}\,pc^2]}$', y_label=r'${\rm FWHM}\,{\rm [km\,s^{-1}]}$', fig_size=(8,8))
#	plt.xscale('log')
#	plt.yscale('log')
#	plt.xlim(xlim1,xlim2)
#	plt.ylim(ylim1,ylim2)
#
#	object_type='SMG'
#	make_all(transition,object_type,'LightPink','DarkRed')
#	#object_type='SFG'
#	#make_all(transition,object_type,'LightBlue','DarkBlue')
#	#object_type='MIPS'
#	#make_all(transition,object_type,'LightGrey','DarkGrey')
#	#object_type='BXBM'
#	#make_all(transition,object_type,'LightGreen','DarkGreen')
#	object_type='QSO'
#	make_all(transition,object_type,'Grey','Black')
#	object_type='OFRG'
#	make_all(transition,object_type,'Black','Black')
#
#	plt.savefig('L_CO43_vs_FWHM_CO43.pdf')
#
#
#	#---12CO(5-4)
#	transition='12CO(5-4)'
#	setup_graph(x_label=r'$L^{\prime}_{\rm CO}\,{\rm [K\,km\,s^{-1}\,pc^2]}$', y_label=r'${\rm FWHM}\,{\rm [km\,s^{-1}]}$', fig_size=(8,8))
#	plt.xscale('log')
#	plt.yscale('log')
#	plt.xlim(xlim1,xlim2)
#	plt.ylim(ylim1,ylim2)
#
#	object_type='SMG'
#	make_all(transition,object_type,'LightPink','DarkRed')
#	object_type='QSO'
#	make_all(transition,object_type,'Grey','Black')
#
#	plt.savefig('L_CO54_vs_FWHM_CO54.pdf')
#
#
#	#---12CO(6-5)
#	transition='12CO(6-5)'
#	setup_graph(x_label=r'$L^{\prime}_{\rm CO}\,{\rm [K\,km\,s^{-1}\,pc^2]}$', y_label=r'${\rm FWHM}\,{\rm [km\,s^{-1}]}$', fig_size=(8,8))
#	plt.xscale('log')
#	plt.yscale('log')
#	plt.xlim(xlim1,xlim2)
#	plt.ylim(ylim1,ylim2)
#
#	object_type='SMG'
#	make_all(transition,object_type,'LightPink','DarkRed')
#	object_type='QSO'
#	make_all(transition,object_type,'Grey','Black')
#
#	plt.savefig('L_CO65_vs_FWHM_CO65.pdf')
#
#	#---12CO(7-6)
#	transition='12CO(7-6)'
#	setup_graph(x_label=r'$L^{\prime}_{\rm CO}\,{\rm [K\,km\,s^{-1}\,pc^2]}$', y_label=r'${\rm FWHM}\,{\rm [km\,s^{-1}]}$', fig_size=(8,8))
#	plt.xscale('log')
#	plt.yscale('log')
#	plt.xlim(xlim1,xlim2)
#	plt.ylim(ylim1,ylim2)
#
#	object_type='SMG'
#	make_all(transition,object_type,'LightPink','DarkRed')
#	object_type='QSO'
#	make_all(transition,object_type,'Grey','Black')
#
#	plt.savefig('L_CO76_vs_FWHM_CO76.pdf')
#
#	#---12CO(8-7)
#	#No sources
#
#	#---12CO(9-8)
#	transition='12CO(9-8)'
#	setup_graph(x_label=r'$L^{\prime}_{\rm CO}\,{\rm [K\,km\,s^{-1}\,pc^2]}$', y_label=r'${\rm FWHM}\,{\rm [km\,s^{-1}]}$', fig_size=(8,8))
#	plt.xscale('log')
#	plt.yscale('log')
#	plt.xlim(xlim1,xlim2)
#	plt.ylim(ylim1,ylim2)
#
#	object_type='SMG'
#	make_all(transition,object_type,'LightPink','DarkRed')
#	object_type='QSO'
#	make_all(transition,object_type,'Grey','Black')
#
#	plt.savefig('L_CO98_vs_FWHM_CO98.pdf')
#
#	#---12CO(10-9)
#	transition='12CO(10-9)'
#	setup_graph(x_label=r'$L^{\prime}_{\rm CO}\,{\rm [K\,km\,s^{-1}\,pc^2]}$', y_label=r'${\rm FWHM}\,{\rm [km\,s^{-1}]}$', fig_size=(8,8))
#	plt.xscale('log')
#	plt.yscale('log')
#	plt.xlim(xlim1,xlim2)
#	plt.ylim(ylim1,ylim2)
#
#	object_type='SMG'
#	make_all(transition,object_type,'LightPink','DarkRed')
#	object_type='QSO'
#	make_all(transition,object_type,'Grey','Black')
#
#	plt.savefig('L_CO109_vs_FWHM_CO109.pdf')
#
#
##	#---12CO(11-10)
##	#No sources
##
##	#---12CO(12-11)
##	#No sources
##
##	#---12CO(14-13)
##	transition='12CO(14-13)'
##	setup_graph(x_label=r'$L^{\prime}_{\rm CO}\,{\rm [K\,km\,s^{-1}\,pc^2]}$', y_label=r'${\rm FWHM}\,{\rm [km\,s^{-1}]}$', fig_size=(8,8))
##	plt.xscale('log')
##	plt.yscale('log')
##	plt.xlim(xlim1,xlim2)
##	plt.ylim(ylim1,ylim2)
##
##	object_type='SMG'
##	make_all(transition,object_type,'LightPink','DarkRed')
##	object_type='QSO'
##	make_all(transition,object_type,'Grey','DarkGrey')
##
##	plt.savefig('L_CO1312_vs_FWHM_CO1312.pdf')
