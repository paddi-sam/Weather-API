Where you see "API" is where you put your API key you get from weatherapi.com, this is fed into the APIKEY constant in config.py

Change 12/12/25:
-Added more relevant details to the cleaned dictionary that goes off of the API response
-Outputs into a textual summary broken down into location and current info
-Added graphical_ouput.py which outputs a bar chart for relevant info (subject to change because I dont like it right now)
-Made a config file where you put your API key to make it easier than going into the script to change it


Change(s) for 13/12/2025
-Add error catching for if api is empty so it doesnt spew out long error message