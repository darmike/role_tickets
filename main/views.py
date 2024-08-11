from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import GroupForm, TicketForm, UserForm
from .models import Group, Ticket, User


@login_required
def group_list(request):
    groups = Group.objects.all()
    return render(request, 'groups/groups_list.html', {'groups': groups})


@login_required
def group_create(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('group_list')
    else:
        form = GroupForm()
    return render(request, 'groups/groups_create.html', {'form': form})


@login_required
def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, 'tickets/tickets_list.html', {'tickets': tickets})


@login_required
def ticket_create(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ticket_list')
    else:
        form = TicketForm()
    return render(request, 'tickets/tickets_create.html', {'form': form})


@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'users/users_list.html', {'users': users})
