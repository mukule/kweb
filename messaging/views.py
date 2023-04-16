from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MessageForm, ReplyForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Message
from django.views import View
from itertools import groupby
from operator import attrgetter
from django.shortcuts import get_object_or_404

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST, sender=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message sent successfully')
            return redirect('messaging:inbox')
    else:
        form = MessageForm(sender=request.user)
    return render(request, 'messaging/send_message.html', {'form': form})


class InboxView(LoginRequiredMixin, View):
    def get(self, request):
        # Get all messages for the current user
        messages = Message.objects.filter(recipient=request.user).order_by('-timestamp')
        
        # Group messages by sender and count total messages for each sender
        grouped_messages = []
        for sender, messages_iter in groupby(messages, attrgetter('sender')):
            messages_list = list(messages_iter)
            count = len(messages_list)
            grouped_messages.append({
                'sender': sender,
                'last_message': messages_list[0],
                'count': count
            })
        
        # Render the template with the grouped messages
        return render(request, 'messaging/inbox.html', {'grouped_messages': grouped_messages})
    
class MessageDetailView(LoginRequiredMixin, View):
    def get(self, request, message_id):
        message = get_object_or_404(Message, pk=message_id, recipient=request.user)
        sender = message.sender
        messages = Message.objects.filter(sender=sender, recipient=request.user) | Message.objects.filter(sender=request.user, recipient=sender)
        messages = messages.order_by('timestamp')

        reply_form = ReplyForm(initial={'recipient': sender}, sender=request.user, reply_to=message_id)

        context = {
            'sender': sender,
            'messages': messages,
            'reply_form': reply_form,
        }
        return render(request, 'messaging/message_detail.html', context)

    def post(self, request, message_id):
        message = get_object_or_404(Message, pk=message_id, recipient=request.user)
        sender = message.sender
        messages = Message.objects.filter(sender=sender, recipient=request.user) | Message.objects.filter(sender=request.user, recipient=sender)
        messages = messages.order_by('timestamp')

        reply_form = ReplyForm(request.POST, sender=request.user, reply_to=message_id)
        if reply_form.is_valid():
            reply_form.save()
            return redirect('messaging:message_detail', message_id=message_id)

        context = {
            'sender': sender,
            'messages': messages,
            'reply_form': reply_form,
        }
        return render(request, 'messaging/message_detail.html', context)
