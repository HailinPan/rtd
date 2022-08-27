import setuptools

setuptools.setup(
    name="rtdpy",
    version="1.0",
    author="Hailin Pan",
    author_email="hailinpan1988@163.com",
    description="Test",
    url="https://github.com/HailinPan/rtd",
    packages=setuptools.find_packages(),
    install_requires=["numpy==1.20.0"],
    python_requires='>=3.8',
)
