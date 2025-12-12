import json
import requests
from config import API_KEY as API

cities = ["london", "Paris", "New York", "Los Angeles", "Dubai", "Tokyo", "Rome"]

ascii = r'''
 __      __               __  .__                   __________                             __   
/  \    /  \ ____ _____ _/  |_|  |__   ___________  \______   \ ____ ______   ____________/  |_ 
\   \/\/   // __ \\__  \\   __\  |  \_/ __ \_  __ \  |       _// __ \\____ \ /  _ \_  __ \   __\
 \        /\  ___/ / __ \|  | |   Y  \  ___/|  | \/  |    |   \  ___/|  |_> >  <_> )  | \/|  |  
  \__/\  /  \___  >____  /__| |___|  /\___  >__|     |____|_  /\___  >   __/ \____/|__|   |__|  
       \/       \/     \/          \/     \/                \/     \/|__|                       '''

def user_menu():
    '''
    Docstring for user_menu
    '''
    print("="*50)
    print("===What city would you like to see weather for?===")
    print("="*50)

    count = 1
    for i in cities:
        print(f"{count} {i}:")
        count += 1
    
def user_input():
    '''
    Docstring for user_input
    :returns the users choice in numerical format
    '''
    
    listLength = len(cities)
    
    flag=True
    while flag == True: 
        userChoice = input(f"Enter a number 1-{listLength}: ")
        try:
            userChoice = int(userChoice)
            if userChoice < 0 or userChoice > listLength:
                print("Type a valid number")
            else:
                print("="*14)
                print("== Accepted ==")
                print("="*14)
                return userChoice
        except ValueError:
            print("Please type a valid number")

def convert_to_city(userChoice):
    '''
    Docstring for convert_to_city
    
    :param userChoice: Users numerical choice
    :returns convertedURL: URL with relevant city inserted
    '''

    print(f"You chose {cities[userChoice-1]}")
    print("---------------------------")

    textCity = cities[userChoice-1]

    if userChoice == 3:
        textCity = "NYC"
    elif userChoice == 4:
        textCity = "LA"

    convertedURL = f"http://api.weatherapi.com/v1/current.json?key={API}&q={textCity}&aqi=no"
    
    return convertedURL

def make_request(convertedURL):
    
    headers = {"Authorization": f"Bearer {API}"}
    response = requests.get(convertedURL, headers=headers)
    response = response.text
    
    dictionary = json.loads(response)
    cleanJSON = json.dumps(dictionary, indent=4)
    cleanJSON = json.loads(cleanJSON) 
    return cleanJSON   

def clean_json(JSON):
    cleaned_data = {
        "location": {
            "name": JSON["location"]["name"],
            "country": JSON["location"]["country"],
            "localtime": JSON["location"]["localtime"]
        },

        "current": {
            "Last_updated": JSON["current"]["last_updated"], 
            "Temp (C)": JSON["current"]["temp_c"], 
            "Feelslike (C)": JSON["current"]["feelslike_c"], 
            "Condition": JSON["current"]["condition"]["text"], 
            "Icon": JSON["current"]["condition"]["icon"], 
            "Wind (kph)": JSON["current"]["wind_kph"], 
            "Wind Direction": JSON["current"]["wind_dir"], 
            "Humidity": JSON["current"]["humidity"], 
            "UV": JSON["current"]["uv"], 
            "Visibility_km": JSON["current"]["vis_km"] }
    }

    for section_name, section_data in cleaned_data.items(): 
        print(f"\n[{section_name}]") 
        for key, value in section_data.items(): 
            print(key, ":", value) 
            
    return cleaned_data
    
def main():

    print(ascii)
    user_menu()
    userChoice = user_input()
    convertedURL = convert_to_city(userChoice)
    JSON = make_request(convertedURL)
    final_json = clean_json(JSON)
    return final_json