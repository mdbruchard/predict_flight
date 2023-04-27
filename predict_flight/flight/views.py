from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse


from .models import Flight
from .logic import dataset_cleaner

import pandas as pd
import numpy as np
import pickle
# Create your views here.

def remove_symbol(time):
    if 'h' in time:
        time = time.split('h')
        return int(time[0])
    else:
        return 0
    
def remove_symbol_2(time):
    if 'm' in time:
        tempo = time.split()
        time = tempo[-1].strip('m').strip()
        return int(time)
    else:
        return 0

def index(request):
   
        # If request method is POST
        if request.method == 'POST':

                # Save request POST
                airline = request.POST['airline']
                depature = request.POST['depature']
                destination = request.POST['destination']
                source = request.POST['source']

                # Filter the airline if is request POST
                if airline:
                        flights = Flight.objects.filter(
                                airline=airline,
                                date_of_journey=depature,
                                destination=destination,
                                source=source
                        )
                        return render(request, 'flight/flights.html', {
                                'flights': flights
                        })
                else:
                        flights = Flight.objects.filter(
                                date_of_journey=depature,
                                destination=destination,
                                source=source
                        )
                        return render(request, 'flight/flights.html', {
                                'flights': flights
                        })
              
                        
        return render(request, 'flight/index.html')

def get_flight(request):
        flights = Flight.objects.all()
        return render(request, 'flight/flights.html', {
                'flights':flights
        })



def flight(request, flight_id):

        # Get the flight reqeusted
        flight_id = Flight.objects.get(pk=flight_id)

        # Get the flights in models database
        flight = Flight.objects.all()

        # Turn them into dataframe
        data = pd.DataFrame(flight.values())

        # Clean and preprocess the dataset
        data = dataset_cleaner(data)
        print('Dataset loaded!')

        
        # Rename the columns exacly hte way is was fitted
        data.rename(columns={
        'airline_Air Asia': 'Airline_Air Asia', 'airline_Air India':'Airline_Air India', 
        'airline_GoAir':'Airline_GoAir',
       'airline_IndiGo': 'Airline_IndiGo', 'airline_Jet Airways': 'Airline_Jet Airways', 
       'airline_Jet Airways Business': 'Airline_Jet Airways Business',
       'airline_Multiple carriers': 'Airline_Multiple carriers',
       'airline_Multiple carriers Premium economy': 'Airline_Multiple carriers Premium economy', 
       'airline_SpiceJet': 'Airline_SpiceJet','airline_Vistara': 'Airline_Vistara', 
       'airline_Vistara Premium economy': 'Airline_Vistara Premium economy', 
       'source_Banglore':'Source_Banglore','source_Chennai':'Source_Chennai', 
       'source_Delhi': 'Source_Delhi', 'source_Kolkata':'Source_Kolkata', 
       'source_Mumbai': 'Source_Mumbai','destination_Banglore':'Destination_Banglore', 
       'destination_Cochin': 'Destination_Cochin', 'destination_Delhi':'Destination_Delhi',
       'destination_Hyderabad':'Destination_Hyderabad', 'destination_Kolkata':'Destination_Kolkata',
       'destination_New Delhi':'Destination_New Delhi'
         }, inplace=True)
        

        # Set fitted column missing in the dataset
        data['Airline_Trujet'] = 0.0

        # Order the columns in the same order durind the model fitting 
        data = data[['Total_Stops', 'Journey_day', 'Journey_month', 'Dep_hour', 'Dep_minute',
       'Arrival_hour', 'Arrival_minute', 'Duration_hour', 'Duration_minute',
       'Airline_Air Asia', 'Airline_Air India', 'Airline_GoAir',
       'Airline_IndiGo', 'Airline_Jet Airways', 'Airline_Jet Airways Business',
       'Airline_Multiple carriers',
       'Airline_Multiple carriers Premium economy', 'Airline_SpiceJet',
       'Airline_Trujet', 'Airline_Vistara', 'Airline_Vistara Premium economy',
       'Source_Banglore', 'Source_Chennai', 'Source_Delhi', 'Source_Kolkata',
       'Source_Mumbai', 'Destination_Banglore', 'Destination_Cochin',
       'Destination_Delhi', 'Destination_Hyderabad', 'Destination_Kolkata',
       'Destination_New Delhi']]

        # Load the model
        with open('data/model2.pkl', 'rb') as file:
              model = pickle.load(file)

        # Filter the flight 
        X = data.iloc[[flight_id.id - 1]]

        # Predicting price flight and returning to the info html
        price = model.predict(X)

        return render(request, 'flight/info.html', {
                'flight': flight_id,
                'price': round(price[0], 2)
        })
    


