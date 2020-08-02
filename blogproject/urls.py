from django.contrib import admin
from django.urls import include, path # include는 url 관리 할때 추가!
import blogapp.views
import portfolioapp.views
# media 사용을 위해 아래 두개 import 해야하는건 외우셈
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blogapp.views.home, name="home"),
    path('blog/', include('blogapp.urls')),
    path('portfolio/',portfolioapp.views.portfolio, name="portfolio"),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
