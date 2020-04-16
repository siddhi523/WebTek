from django.urls import path,include
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'WebTek.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url('admin/', include(admin.site.urls)),
    path('admin/', admin.site.urls),
    #url(r'^student/', include('student.urls')),
    path('student/', include('student.urls')),
    path('',include('student.urls'))


]
