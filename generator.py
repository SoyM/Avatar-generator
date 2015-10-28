#!/usr/bin/env python2
# -*- coding:utf-8 -*-
import identicon
def gen():
    img = identicon.render_identicon(num, picsize)
    img.save('identicon.png')
    print 'The identicon was generated.'

num = raw_input('Please enter your number.\n')
num = int(num)
picsize = raw_input('Please enter the size you want.\n')
picsize = int(picsize)
gen()
