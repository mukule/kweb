from django.shortcuts import render
from .forms import MessageForm
from users.models import CustomUser

def send_message(request):
    sender = request.user
    users = CustomUser.objects.exclude(pk=sender.pk)
    form = MessageForm(sender=sender, data=request.POST or None, files=request.FILES or None)
    if form.is_valid():
        form.save()
        # Do something, such as redirect to a success page
    return render(request, "my_template.html", {"users": users, "form": form})