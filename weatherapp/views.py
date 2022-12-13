from django.shortcuts import render,redirect
import requests
import urllib.request  
import json
import math
from datetime import datetime


def weather(request):
    if request.method == "POST":
        city_name = request.POST['city'].lower()
        print(city_name)
        api_key = 'cf474ac8cff792b86e46c794cde2fa7e'          # openweathermap api key
        url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}"
     
        response = requests.get(url).json()
        # print("---------------- ",response)
        print("================== ",response['list'][14]['main']['humidity'])

        # d = response['list'][1]['dt_txt']
        # print(d)
        # s = d.split(' ')
        # date1 = s[1]
        # print(date1)

        weather_time =  (response['list'][0]['dt_txt']).split(" ")[1][:2]
        print("weather Time------- ",weather_time)
        current_time = datetime.now().strftime("%X")[:2]
        print("current time------ ",current_time)

        if current_time == "06" or current_time < "09":
            
            print("6 o'clock or its between 6 to 9")
        elif current_time == "09" or current_time < "12":
            newtime = "09to12"
            print("9 o'clock or its between 9 to 12")
        elif current_time =="12" or current_time < "15":
            print("12 o'clock or its between 12 to 15")
        elif current_time == "15" or current_time <= "18":
            print("15 o'clock or its between 15 to 18")
        elif current_time > "18":
            print("up to 18")
  

        context = {
            # TODAY =======================================      
            # TIME: 06:00:00
            'city_name' : response["city"]["name"], 
            'country' : response['city']['country'],
            'date' : (response['list'][0]['dt_txt'].split(" ")[0]),
            'time' : (response['list'][0]['dt_txt']).split(" ")[1],
            'temp' : math.floor(response['list'][0]['main']['temp'] -273.15),                              
            'humidity' : response['list'][0]['main']['humidity'],
            'description' : (response['list'][0]['weather'][0]['description']).capitalize(),
            'icon' : response['list'][0]['weather'][0]['icon'],
            # 'newtime' : newtime,
            
            # TIME: 09:00:00

            'date1' : (response['list'][1]['dt_txt']).split(" ")[0],
            'time1' : (response['list'][1]['dt_txt']).split(" ")[1],
            'temp1' : math.floor(response['list'][1]['main']['temp']-273.15),
            'humidity1' : response['list'][1]['main']['humidity'],
            'description1' : (response['list'][1]['weather'][0]['description']).capitalize(),
            'icon1' : response['list'][1]['weather'][0]['icon'],

            # TIME: 12:00:00

            'temp2' : math.floor(response['list'][2]['main']['temp']-273.15),
            'date2' : (response['list'][2]['dt_txt']).split(" ")[0],
            'time2' : (response['list'][2]['dt_txt']).split(" ")[1],
            'humidity2' : response['list'][2]['main']['humidity'],
            'description2' : (response['list'][2]['weather'][0]['description']).capitalize(),
            'icon2' : response['list'][2]['weather'][0]['icon'],

            # TIME: 15:00:00

            'temp3' : math.floor(response['list'][3]['main']['temp']-273.15),
            'date3' : (response['list'][3]['dt_txt']).split(" ")[0],
            'time3' : (response['list'][3]['dt_txt']).split(" ")[1],
            'humidity3' : response['list'][3]['main']['humidity'],
            'description3' : (response['list'][3]['weather'][0]['description']).capitalize(),
            'icon3' : response['list'][3]['weather'][0]['icon'],

            # TIME: 18:00:00

            'temp4' : math.floor(response['list'][4]['main']['temp']-273.15),
            'date4' : (response['list'][4]['dt_txt']).split(" ")[0],
            'time4' : (response['list'][4]['dt_txt']).split(" ")[1],
            'humidity4' : response['list'][4]['main']['humidity'],
            'description4' : (response['list'][4]['weather'][0]['description']).capitalize(),
            'icon4' : response['list'][4]['weather'][0]['icon'],
          
            # 5 days
            'date_1' : (response['list'][6]['dt_txt']).split(" ")[0],
            'time_1' : (response['list'][6]['dt_txt']).split(" ")[1],
            'temp_1' : math.floor(response['list'][6]['main']['temp']-273.15),
            'humidity_1' : response['list'][6]['main']['humidity'],
            'description_1' : (response['list'][6]['weather'][0]['description']).capitalize(),
            'icon_1' : response['list'][6]['weather'][0]['icon'],
        
            'date_2' : (response['list'][14]['dt_txt']).split(" ")[0],
            'time_2' : (response['list'][14]['dt_txt']).split(" ")[1],
            'temp_2' : math.floor(response['list'][14]['main']['temp']-273.15),
            'humidity_2' : response['list'][14]['main']['humidity'],
            'description_2' : (response['list'][14]['weather'][0]['description']).capitalize(),
            'icon_2' : response['list'][14]['weather'][0]['icon'],
   
            'temp_3' : math.floor(response['list'][22]['main']['temp']-273.15),
            'time_3' : (response['list'][22]['dt_txt']).split(" ")[1],
            'date_3' : (response['list'][22]['dt_txt']).split(" ")[0],
            'humidity_3' : response['list'][22]['main']['humidity'],
            'description_3' : (response['list'][22]['weather'][0]['description']).capitalize(),
            'icon_3' : response['list'][22]['weather'][0]['icon'],
      
            'date_4' : (response['list'][30]['dt_txt']).split(" ")[0],
            'time_4' : (response['list'][30]['dt_txt']).split(" ")[1],
            'temp_4' : math.floor(response['list'][30]['main']['temp']-273.15),
            'humidity_4' : response['list'][30]['main']['humidity'],
            'description_4' : (response['list'][30]['weather'][0]['description']).capitalize(),
            'icon_4' : response['list'][30]['weather'][0]['icon'],
          
            'date_5' : (response['list'][38]['dt_txt']).split(" ")[0],
            'time_5' : (response['list'][38]['dt_txt']).split(" ")[1],
            'temp_5' : math.floor(response['list'][38]['main']['temp']-273.15),
            'humidity_5' : response['list'][38]['main']['humidity'],
            'description_5' : (response['list'][38]['weather'][0]['description']).capitalize(),
            'icon_5' : response['list'][38]['weather'][0]['icon'],
        
        }
        # return render(request,'weather.html',context=context)
        return render(request,'weather.html',context=context)
        # return redirect('/home/')
    return render(request,'weather.html')
        # return redirect('/home/')

    




# https://source.unsplash.com/random/1620x880/?weather