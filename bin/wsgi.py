#!/usr/bin/python


import sys
sys.path[0:0] = [
  '/usr/lib/python2.7/dist-packages',
  '/home/zgoldberg/workspace/Proximity/go/third-party/Django',
  '/home/zgoldberg/workspace/Proximity/go/third-party/dist-modified/url-shortener',
  '/home/zgoldberg/workspace/Proximity/go/build/eggs/djangotoolbox-0.9.2-py2.7.egg',
  '/home/zgoldberg/workspace/Proximity/go/build/eggs/django_storages-1.1.8-py2.7.egg',
  '/home/zgoldberg/workspace/Proximity/go/build/eggs/djangorecipe-1.5-py2.7.egg',
  '/home/zgoldberg/workspace/Proximity/go/build/eggs/zc.recipe.egg-2.0.0-py2.7.egg',
  '/home/zgoldberg/workspace/Proximity/go/build/eggs/zc.buildout-2.2.1-py2.7.egg',
  '/home/zgoldberg/workspace/Proximity/go/build/eggs/setuptools-5.3-py2.7.egg',
  '/home/zgoldberg/workspace/Proximity/go',
  ]

import djangorecipe.wsgi

application = djangorecipe.wsgi.main('go.settings', logfile='')
