from . import forms
from django.shortcuts import render
from django.http import HttpResponse
from collections import OrderedDict
from .models import Student
from .fusioncharts import FusionCharts

def index(request):

    # Chart data is passed to the `dataSource` parameter, as dictionary in the form of key-value pairs.
    dataSource = OrderedDict()

    # The `chartConfig` dict contains key-value pairs data for chart attribute
    chartConfig = OrderedDict()
    chartConfig["caption"] = "Students at universities"
    chartConfig["xAxisName"] = "Universities"
    chartConfig["yAxisName"] = "Students counts"
    chartConfig["theme"] = "fusion"

    # The `chartData` dict contains key-value pairs data
    chartData = OrderedDict()
    
    for student in Student.objects.all():
        chartData[student.university] = Student.objects.filter(university = student.university).count()


    dataSource["chart"] = chartConfig
    dataSource["data"] = []
    
    # Convert the data in the `chartData` array into a format that can be consumed by FusionCharts. 
    # The data for the chart should be in an array wherein each element of the array is a JSON object
    # having the `label` and `value` as keys.

    # Iterate through the data in `chartData` and insert in to the `dataSource['data']` list.
    for key, value in chartData.items():
        data = {}
        data["label"] = key
        data["value"] = value
        dataSource["data"].append(data)




    # Create an object for the column 2D chart using the FusionCharts class constructor
    # The chart data is passed to the `dataSource` parameter.
    column2D = FusionCharts("column2d", "ex1" , "600", "400", "chart-1", "json", dataSource)

    return  render(request, 'index.html', {'output' : column2D.render()})






def loginUser(request):
    form = forms.LoginForm(request.POST or None)

    context = {
        "form": form
    }

    return render(request, 'login.html', context)


def members(request):
    students = Student.objects.all()
    return render(request,'members.html',{'students':students})