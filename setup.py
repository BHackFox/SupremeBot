import sys
import os



class SetOS:
    def Importing_From_Os(self):
        modules_imp = ["selenium","datetime","tarfile","urllib","json"]
        for module in modules_imp:
            try:
                print("Importing "+module)
                __import__(module)
            except ImportError as e:
                print(e)
                os.system("pip3 install "+module)


    def DriverSetter(self):
        import tarfile
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
