from setuptools import setup, find_packages

version = '0.1'

setup(name='collective.ruleactions.pythonscript',
      version=version,
      description="",
      long_description="""\
""",
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Florian Schulze',
      author_email='florian.schulze@gmx.net',
      url='http://svn.plone.org/svn/collective/collective.ruleactions.pythonscript',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective.ruleactions'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )