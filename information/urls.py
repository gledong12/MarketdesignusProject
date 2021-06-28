from django.urls import path
from .views import (MovingCompanyInformationView,
                    CustomerInformationView,
                    ApplicationofMovingView,
                    CustomerFeedbackHistoryView)

urlpatterns = [
    path('/company', MovingCompanyInformationView.as_view()),
    path('/customer', CustomerInformationView.as_view()),
    path('/application', ApplicationofMovingView.as_view()),
    path('/feedback', CustomerFeedbackHistoryView.as_view())
]
