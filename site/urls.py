from django.conf.urls import url, include
from django.contrib import admin
import main.urls

urlpatterns = [
    url(r'', include(main.urls)),
    url(r'^admin/', admin.site.urls),
]
