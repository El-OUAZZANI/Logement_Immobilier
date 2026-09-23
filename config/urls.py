from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

admin.site.site_header = "LogementImmo"
admin.site.site_title = "LogementImmo"
admin.site.index_title = "Administration de la plateforme"


urlpatterns = [
    path("django-admin/", admin.site.urls),

    path("", include("accounts.urls")),
    path("accounts/", include("accounts.urls", namespace="accounts_prefixed")),
    path("dashboard/", include("dashboard.urls")),
    path("properties/", include("properties.urls")),
    path("visits/", include("visits.urls")),
    path("favorites/", include("favorites.urls")),
    path("logout/", LogoutView.as_view(next_page="/"), name="logout"),
    path("changer-mot-de-passe/",auth_views.PasswordChangeView.as_view(template_name="accounts/changer_mot_de_passe.html",success_url="/"),name="changer_mot_de_passe"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
