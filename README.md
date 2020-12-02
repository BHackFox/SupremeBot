# SupremeBot

SupremeBot only works in python 3.4+

USAGE:  
   Run install.py to install and setup all modules that are needed for the program to work.
        
   Run SupremeBot.py to start the program.
        
   Add the information manually by editing the data /data.JSON file or answer the the questions of the program.
   
   Informations:
                {"name":"Your Name",
                 "email":"your@email.com",
                 "phone":"1234567890",
                 "size":"Medium",
                 "addr1":"First route",
                 "addr2":"Second route",
                 "addr3":"Third route",
                 "zip":"00111",
                 "city":"Rome",
                 "country":"IT",
                 "cardtype":"Mastercard",
                 "cardnumber":"1234567890123456",
                 "cardexpmonth":"07",
                 "cardexpyear":"37",
                 "cardcode":"444"}
  
 
 
SupremeBot search for changes in the supreme shop page by sending 6 requests every second and saving the responses in the data/old.txt and data/new.txt files
To speed up the opening of chromedriver the selenium.Chrome() function is initialized before the one for checking the shop page change.
