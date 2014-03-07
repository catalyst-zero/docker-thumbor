# -*- coding: utf-8 -*-
# vi:si:et:sw=4:sts=4:ts=4

##
## Copyright (C) 2013 - George Y. Kussumoto <georgeyk.dev@gmail.com>
##
## This program is free software; you can redistribute it and/or
## modify it under the terms of the GNU Lesser General Public License
## as published by the Free Software Foundation; either version 2
## of the License, or (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU Lesser General Public License for more details.
##
## You should have received a copy of the GNU Lesser General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., or visit: http://www.gnu.org/.
##
##

import urlparse

from libthumbor import CryptoURL


SECRET_KEY = 'MY_SECURE_KEY'
THUMBOR_SERVER = 'http://127.0.0.1:8888'

# upload & get the thumbnail url

crypto = CryptoURL(key=SECRET_KEY)
image_url = crypto.generate(width=150, height=150,
    image_url='29.media.tumblr.com/tumblr_lltzgnHi5F1qzib3wo1_400.jpg')
print urlparse.urljoin(THUMBOR_SERVER, image_url)
