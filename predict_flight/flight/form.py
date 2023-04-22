from django import forms

class BookFlight(forms.Form):
    CHOICES_SOURCE = [
        ('Cities',(
        ('Banglore', 'banglore'),
        ('Chennai', 'chennai'),
        ('Delhi', 'delhi'),
        ('Kolkata', 'kolkata'),
        ('Mumbai', 'mumbai')
        ))
    ]

    CHOICES_DESTINATION = [
        ('Cities', (
        ('Banglore', 'banglore'),
        ('Cochin', 'cochin'),
        ('Delhi', 'delhi'),
        ('Kolkata', 'kolkata'),
        ('New Delhi', 'new delhi'),
        ('Hyderbad', 'hyderbad')
        ))
    ]
    airline = forms.CharField(max_length=36, required=False, label='Airline')
    flight_date = forms.DateField(label='Depature Date')
    source = forms.ChoiceField(required=True, label='From', choices=CHOICES_SOURCE)
    destination = forms.ChoiceField(required=True, label='To', choices=CHOICES_DESTINATION)
    dep_time
    
