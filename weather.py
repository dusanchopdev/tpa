import requests
def weather():
    city = input("Choose your city: ")
    resp = requests.get("http://api.weatherapi.com/v1/current.json?key=dffb134aeed04fc492c182437220712&q="+city+"&aqi=no")
    resp_dict = resp.json()
    print("In",resp_dict.get('location').get('name'),"it is",resp_dict.get('current').get('temp_c'),"Celsius and",resp_dict.get('current').get('temp_f'),("Fahrenhiet"))


def done():
    print("Thank u for using TPA")
    exit()