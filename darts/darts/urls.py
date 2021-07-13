from django.urls import include
from django.conf.urls import url

urlpatterns = [
    url(r'^student/', include('student.urls'))
]