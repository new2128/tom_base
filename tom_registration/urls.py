from django.conf import settings
from django.urls import path

from tom_registration.views import ApprovalRegistrationView, OpenRegistrationView, UserApprovalView

app_name = 'tom_registration'

try:
    REGISTRATION_FLOW = settings.REGISTRATION_FLOW
except:
    REGISTRATION_FLOW = settings.REGISTRATION_FLOWS.OPEN  # TODO: what if USER_SELF_REGISTRATION not in settings.py?


urlpatterns = []

if REGISTRATION_FLOW == settings.REGISTRATION_FLOWS.OPEN:
    urlpatterns += [path('register/', OpenRegistrationView.as_view(), name='register')]
elif REGISTRATION_FLOW == settings.REGISTRATION_FLOWS.APPROVAL_REQUIRED:
    urlpatterns += [path('register/', ApprovalRegistrationView.as_view(), name='register')]
    urlpatterns += [path('approve/', UserApprovalView.as_view(), name='approve')]
