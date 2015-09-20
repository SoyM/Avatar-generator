#!/usr/bin/python
# -*- coding: UTF-8 -*-
import identicon
img = identicon.render_identicon(20150609, 480)
#2015.06.09 is my niece's birthday
#Generated image size is 3 * 480.
img.save('MyNiece.png')
