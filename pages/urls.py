from pages import views
from django.urls import path, include
from django.contrib import admin
from .forms import Reserve_table_form

app_name = 'pages'

urlpatterns = {
    path('admin/', admin.site.urls),
    path('reserve_table', include('pages.urls', namespace='reservation')),
    path('book.html', Reserve_table_form, name='Reserve_table_form'),
}
