from django.urls import path, include
from . import views
# from .customer import views as customer_views
# from .courier import views as courier_views

app_name = 'core'

# customer_urlpatterns = [
#     path('', customer_views.home, name="home"),

# ]

# courier_urlpatterns = [
#     path('', courier_views.home, name="home"),
    
# ]

urlpatterns = [
    path('', views.home),
    path('sign-up/', views.sign_up),
    # path('customer/', include((customer_urlpatterns, 'customer'), namespace='customer')),
    # path('courier/', include((courier_urlpatterns, 'courier'), namespace='courier')),
]
