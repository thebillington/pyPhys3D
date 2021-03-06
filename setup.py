from setuptools import setup

setup(name='pyPhys3D',
      version='0.1',
      description='A 3D python physics engine for use with pygame and pyOpenGL',
      url='http://github.com/thebillington/pyPhys3D',
      author='thebillington',
      author_email='billy.rebecchi@googlemail.com',
      license='MIT',
      packages=['pyPhys3D'],
      package_data={
		'pyPhys3D' : ["Meshes/cube.mesh"],
      },
      include_package_data=True,
      zip_safe=False)
