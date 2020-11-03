#!/usr/bin/env python

import matplotlib
matplotlib.use('Agg')
import aplpy
import numpy as np
import aplpy.regions

def contour_make_batch():
    contour_make(30169,34.595613,-5.17483, 1.16972e-05)
    contour_make(30545,34.5997,-5.17383,2.33875e-05)
    return;

def contour_make(id,ra,dec,rms):
    f01=aplpy.FITSFigure('/Users/grudnick/Work/IRAC_clusters/Data/UDS/HST/uds_cluster_wfc3_f160w_v1.0_drz_sci.fits.fz',hdu=1)
    f01.tick_labels.set_font(size='xx-large')
    f01.axis_labels.set_font(size='xx-large')
    f01.ticks.set_color('black')
    f01.ticks.set_linewidth(2)
    #f01.ticks.set_minor_frequency(5)

    f01.show_grayscale(vmin=-0.01,vmax=0.2,invert='True')

    zoomsize = 15./3600

    f01.recenter(ra,dec,width=zoomsize,height=zoomsize)
    #f01.add_label(0.5,0.9,'ID.01',relative=True)
    f01.tick_labels.set_yformat('dd:mm:ss')
    f01.tick_labels.set_xformat('hh:mm:ss.s')

    #f01.beam.set_linestyle('dashed')
    f01.beam.set_linewidth(2)  # points

    #f01.beam.set(facecolor='red', linestyle='dashed', ...) # if you want to set multiple properties in one line
    #f01.Regions.show_regions('label.reg')

    if id==30545:
        dra1 = -1.0/3600.
        ddec1 = 1.0/3600.
        racoord1 = 34.59963
        deccoord1 = -5.1738413
        f01.show_arrows(racoord1,deccoord1,dra1, ddec1, color='red')
        dra1 = -1.0/3600.
        ddec1 = 1.2/3600.
        f01.add_label(racoord1 + dra1, deccoord1 + ddec1, "30545, z=1.624")

        dra2 = -1.0/3600.
        ddec2 = 1.0/3600.
        racoord2 = 34.599928
        deccoord2 = -5.1736636
        f01.show_arrows(racoord2,deccoord2,dra2, ddec2, color='red')
        dra2 = -1.0/3600.
        ddec2 = 1.2/3600.
        f01.add_label(racoord2 + dra2, deccoord2 + ddec2, "30577, z=1.486")

        #aell=2.1/3600.0
        #bell=0.94/3600.0
        aell=3.5/3600.0
        bell=2.0/3600.0
        paell=66.0
        f01.show_ellipses(ra,dec,aell,bell,90+paell,color="magenta", linestyle='dashed', linewidth=5)

    if id==30169:
        dra1 = -1.0/3600.
        ddec1 = 1.0/3600.
        racoord1 = 34.595629
        deccoord1 = -5.1747063
        f01.show_arrows(racoord1,deccoord1,dra1, ddec1, color = "red")
        dra1 = -1.0/3600.
        ddec1 = 1.3/3600.
        f01.add_label(racoord1 + dra1, deccoord1 + ddec1, "30169, z=1.629")

    figstr = 'fig_' + str(id) + '_co.55days.eps'
    f01.save(figstr, format = 'EPS')

    figstr = 'fig_' + str(id) + '_co.55days.png'
    f01.save(figstr)
    return;

