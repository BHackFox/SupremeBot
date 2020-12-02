import setup
import sys


def install():
    settings = setup.SetOS()
    settings.Importing_From_Os()
    settings.DriverSetter()



if __name__ == "__main__":
    install()
