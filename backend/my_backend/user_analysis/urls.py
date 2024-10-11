from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user_analysis.controller.views import UserAnalysisView

router = DefaultRouter()
router.register(r'user_analysis', UserAnalysisView, basename='user_analysis')

urlpatterns = [
    path('', include(router.urls)),
    path('create', UserAnalysisView.as_view({'post': 'createUserAnalysis'}), name='create-user-analysis'),
    path('create-question', UserAnalysisView.as_view({'post': 'createUserAnalysisQuestion'}), name='create-user-analysis-question'),
    path('create-user-analysis-selection', UserAnalysisView.as_view({'post': 'createUserAnalysisCustomSelection'}), name='create-user-ananlysis-custom-selection'),
    path('submit-answer', UserAnalysisView.as_view({'post': 'submitUserAnalysisAnswer'}), name='submit-user-analysis-answer'),
    path('list-answer', UserAnalysisView.as_view({'post': 'listUserAnalysisAnswer'}), name='list-user-analysis-answer'),
    path('list-question', UserAnalysisView.as_view({'post': 'listUserAnalysisQuestion'}), name='list-user-analysis-question'),
    path('list-selection', UserAnalysisView.as_view({'post': 'listUserAnalysisSelection'}), name='list-user-analysis-selection'),
    path('list-user-analysis', UserAnalysisView.as_view({'get': 'listUserAnalysis'}), name='list-user-analysis'),
]