from django.views.generic import ListView
from .models import CompanyDocument
from django.core.paginator import Paginator
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import StaffDocument
from .forms import StaffDocumentForm
from django.contrib import messages


class Company_doc(ListView):
    model = CompanyDocument
    template_name = 'documents/company_doc.html'
    context_object_name = 'documents'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.object_list, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        return context
  

class StaffDocumentCreateView(LoginRequiredMixin, CreateView):
    model = StaffDocument
    form_class = StaffDocumentForm
    template_name = 'documents/staff_doc_create.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Your document has been uploaded successfully!')
        return response

    def get_success_url(self):
        return reverse('documents:my_docs')
    
class MyDocuments(LoginRequiredMixin, ListView):
    model = StaffDocument
    template_name = 'documents/my_documents.html'
    context_object_name = 'documents'

    def get_queryset(self):
        return StaffDocument.objects.filter(user=self.request.user)