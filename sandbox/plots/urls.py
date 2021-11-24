from _plotly_utils.exceptions import PlotlyEmptyDataError
from django.urls import path
from .views import demo_plot_view
#from .views import views
from .views import index
from .views import data
from .views import plot
from .views import homepage


urlpatterns = [
    path('demo-plot/', index),

    path("", homepage),
    path("data", data),
    path("plot", demo_plot_view),
    path("homepage", homepage),

]
