# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 12:56:07 2018

@author: sandb
"""
def steamgif_crop(filename):
    from imgpy import Img
    with Img(fp=filename) as im:
        x = im.width
        y = im.height
        while (x-12)%(4) != 0:
            x = x-1
        #number 1 crop
        im.crop(box=(0, 0,(x-12)/4 , y))
        im.save(fp='1.gif')
    #    #number 2 crop
    with Img(fp=filename) as im2:
        im2.crop(box=((x-12)/4+4, 0, (x-12)/2+4, y))
        im2.save(fp='2.gif')
    #    #number 3 crop
    with Img(fp=filename) as im3:
        im3.crop(box=((x-12)/2+8, 0, (x-12)/4*3+8, y))
        im3.save(fp='3.gif')
        #number 4 crop
    with Img(fp=filename) as im4:
        im4.crop(box=((x-12)/4*3+12, 0, x, y))
        im4.save(fp='4.gif')
    return
