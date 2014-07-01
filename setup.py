from distutils.core import setup

setup(name='go',
      version='1.0',
      description='Zach Goldberg',
      author='Zach Goldberg',
      author_email='zach@zachgoldberg.com',
      url='zachgoldberg.com',
      packages=[
          'go', ],
      package_dir={
          'go': 'go/',
      },
      install_requires=[
          'django==1.3',
          'django_debug_toolbar',
          'djangotoolbox',
          'simplejson',
      ],
      )
