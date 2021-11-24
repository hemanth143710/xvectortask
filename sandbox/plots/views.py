from django.db.models import query
from django.shortcuts import render, HttpResponse
from plotly.offline import plot
import plotly.graph_objects as go
from .forms import CsvModelForm
from .models import Csv
import csv


def index(request):
    # return HttpResponse("this is home page")
    x_data = [0, 1, 2, 3]
    y_data = [x**2 for x in x_data]
    plot_div = plot([go.Scatter(x=x_data, y=y_data,
                                mode='lines', name='test',
                                opacity=0.8, marker_color='green')],
                    output_type='div')

    return render(request, 'plot.html', context={'plot_div': plot_div})
    # return render(request, 'plot.html')


def about(request):
    return HttpResponse("this is about page")


def data(request):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    queryset = Csv.objects.all()
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        # obj=Csv
        obj1 = Csv.objects.all()[0]
        obj = Csv.objects.get(activated=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            d = []
            for i, row in enumerate(reader):
                if i == 0:
                    pass
                else:
                    row = " ".join(row)
                    row = row.replace(';', ' ')
                    row = row.split()
                    # print(row)
                    a = row[0]
                    b = d.append(row[1])
                    c = row[2]

                    # name=row[2].upper()
                    print(type(d))
                    # print(name)
                    # print(row)
                    # print(type(row))
            obj.activated = True
            obj.save()
            global s
        s = [float(i) for i in d]
    try:
        a = max(s)
        b = min(s)
        c = sum(s)
    except Exception as e:
        a = 0
        b = 0
        c = 0

    return render(request, 'data.html', {'form': form, 'queryset': queryset, 'a': a, 'b': b, 'c': c})


def demo_plot_view(request):

    #x_data = [0,1,2,3]
    obj1 = Csv.objects.all()[0]
    obj = Csv.objects.all()[0]
    with open(obj.file_name.path, 'r') as f:
        reader = csv.reader(f)
        d = []
        e = []
        for i, row in enumerate(reader):
            if i == 0:
                pass
            else:
                row = " ".join(row)
                row = row.replace(';', ' ')
                row = row.split()
                # print(row)
                a = row[0]
                b = d.append(row[1])
                c = e.append(row[2])

                # name=row[2].upper()
                print(type(d))
                # print(name)
                # print(row)
                # print(type(row))
        obj.activated = True
        obj.save()
        global s
        s = [float(i) for i in d]
        s = s[0:30]
        x_data = s
        g = [float(i) for i in e]
        g = g[0:30]
        y_data = g
        plot_div = plot([go.Scatter(x=x_data, y=y_data,
                                    mode='lines', name='test',
                                    opacity=0.8, marker_color='green')],
                        output_type='div')

        return render(request, 'demo-plot.html', context={'plot_div': plot_div})


def homepage(request):
    return render(request, 'homepage.html')
