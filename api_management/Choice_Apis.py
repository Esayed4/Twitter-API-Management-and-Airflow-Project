import pandas as pd
import numpy as np
from datetime import datetime

Number_Of_Wanted_Tweets=100


#-------
def choice_Apis(Number_Of_Required_Requstes, API_file, APIs_Will_Be_Used,total_requests_we_take):
    for API in API_file.to_dict('records'):  # Convert to list of dictionaries
        if Number_Of_Required_Requstes <= 0:
            break
        
        total_requests_we_take_per_API = 0
        
        if API['Avilabe_requests_per_month'] > 0:
            if API['Avilabe_requests_per_month'] >= Number_Of_Required_Requstes:
                API['Avilabe_requests_per_month'] -= Number_Of_Required_Requstes
                total_requests_we_take_per_API = Number_Of_Required_Requstes
                Number_Of_Required_Requstes = 0
            else:
                total_requests_we_take_per_API = API['Avilabe_requests_per_month']
                API['Avilabe_requests_per_month'] = 0
                Number_Of_Required_Requstes -= total_requests_we_take_per_API
            
            APIs_Will_Be_Used.append({
                "url": API['url'],
                "x-rapidapi-key": API['x-rapidapi-key'],
                "x-rapidapi-host": API['x-rapidapi-host'],
                "total_requests_we_take_per_API": total_requests_we_take_per_API
            })
        
        total_requests_we_take += total_requests_we_take_per_API
    return total_requests_we_take

#--------
API_file = pd.read_json("API_file.json")

Constrains = pd.read_json("Constrains.json")



Number_Of_Required_Requstes = np.ceil(Number_Of_Wanted_Tweets/ Constrains['limit'])
Number_Of_Required_Requstes=Number_Of_Required_Requstes[0]
print(f"Number of requests = {Number_Of_Required_Requstes}")

APIs_Will_Be_Used = []
total_requests_we_take=0




total_requests_we_take = choice_Apis(Number_Of_Required_Requstes, API_file, APIs_Will_Be_Used,total_requests_we_take)

start_date = datetime.strptime(Constrains['start_date'][0], "%Y-%m-%d").date()
end_date = datetime.strptime(Constrains['end_date'][0], "%Y-%m-%d").date()
number_of_days = (end_date - start_date).days

print("number_of_days",number_of_days)
if(total_requests_we_take):
    intervals_days_from_request_to_other= np.floor(number_of_days/total_requests_we_take)
else : 
    intervals_days_from_request_to_other=0
Number_of_requests_per_day= np.floor(total_requests_we_take/number_of_days)

Number_of_reminder_requests=int(total_requests_we_take)% number_of_days




print(f"Number of Avilable requests = {total_requests_we_take}")

for Api in APIs_Will_Be_Used:
    print(Api)





print("intervals_days_from_request_to_other : ",intervals_days_from_request_to_other)
print("Number_of_requests_per_day : ",Number_of_requests_per_day)
print("Number_of_reminder_requests : ",Number_of_reminder_requests)





