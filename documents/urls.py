from django.urls import path
from .views import Company_doc, MyDocuments, StaffDocumentCreateView


app_name = 'documents'
urlpatterns = [
    path('company_doc/', Company_doc.as_view(), name='company_doc'),
    path('my_docs/', MyDocuments.as_view(), name='my_docs'),
    path('upload/', StaffDocumentCreateView.as_view(), name='staff_doc_create'),
    # other URL patterns...
]
