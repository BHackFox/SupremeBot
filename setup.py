import sys
import tarfile
import os



class SetOS:
    def Importing_From_Os(self):
        if sys.platform == "win32":
            Win()
        elif sys.platform == "linux" or sys.platform == "linux2":
            modules_imp = ["selenium","datetime","tarfile","urllib"]
            for i in modules_imp:
                try:
                    print("Importing "+i)
                    __import__(i)
                except ImportError as e:
                    print(e)
                    os.system("pip3 install "+i)


    def DriverSetter(self):
        if sys.platform == "win32":
            print("OS Detected: Windows")
            tar = tarfile.open("bin/chromedriver_win.tar.gz")
            tar.extractall()
        elif sys.platform == "linux" or sys.platform == "linux2":
            print("OS Detected: Linux")
            tar = tarfile.open("bin/chromedriver_unix.tar.gz")
            tar.extractall()
        else:
            print("Assume OS is Linux based...")
            tar = tarfile.open("bin/chromedriver_unix.tar.gz")
            tar.extractall()
