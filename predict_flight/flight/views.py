from django.shortcuts import render
from .models import Flight

import pandas as pd
import numpy as np
# Create your views here.






def index(request):
    return render(request, 'flight/index.html')
