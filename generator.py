#!/usr/bin/python
# -*- coding: UTF-8 -*-
import identicon
img = identicon.render_identicon(20150609, 480)
#20150609 is the number to generate the Avatar.So let's change it. 
#Generated image size is 3 * 480.
img.save('MyNiece.png')
