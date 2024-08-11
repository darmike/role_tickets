from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, authenticate
from .forms import GroupForm, TicketForm, UserForm
from .models import Group, Ticket, User
from django.contrib.auth.forms import AuthenticationForm


def register_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')  # або інший URL після реєстрації
    else:
        form = UserForm()
    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            next_url = request.POST.get('next')  # Отримання URL після входу
            if not next_url or next_url == '/login/':
                next_url = 'home'  # або інший URL за замовчуванням
            return redirect(next_url)
        else:
            return render(request, 'registration/login.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def user_is_admin(user):
    return user.role == 'Admin'


def user_is_manager(user):
    return user.role == 'Manager'


def user_is_analyst(user):
    return user.role == 'Analyst'


@login_required
def home(request):
    if request.user.role == 'Admin':
        return redirect('admin_dashboard')
    elif request.user.role == 'Manager':
        return redirect('manager_dashboard')
    elif request.user.role == 'Analyst':
        return redirect('analyst_dashboard')
    return redirect('default_dashboard')  # стандартна сторінка


@login_required
@user_passes_test(user_is_admin)
def admin_dashboard(request):
    return render(request, 'dashboard/admin_dashboard.html')


@login_required
@user_passes_test(user_is_manager)
def manager_dashboard(request):
    return render(request, 'dashboard/manager_dashboard.html')


@login_required
@user_passes_test(user_is_analyst)
def analyst_dashboard(request):
    return render(request, 'dashboard/analyst_dashboard.html')


@login_required
def default_dashboard(request):
    return render(request, 'dashboard/default_dashboard.html')


@login_required
@user_passes_test(user_is_admin)
def group_list(request):
    groups = Group.objects.all()
    return render(request, 'groups/groups_list.html', {'groups': groups})


@login_required
@user_passes_test(user_is_admin)
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
@user_passes_test(user_is_admin)
def group_detail(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    return render(request, 'groups/groups_detail.html', {'group': group})


@login_required
@user_passes_test(user_is_admin)
def group_update(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('group_detail', group_id=group.id)
    else:
        form = GroupForm(instance=group)
    return render(request, 'groups/groups_update.html', {'form': form, 'group': group})


@login_required
@user_passes_test(user_is_admin)
def group_delete(request, group_id):
    group = get_object_or_404(Group, id=group_id)
    if request.method == 'POST':
        group.delete()
        return redirect('group_list')
    return render(request, 'groups/groups_confirm_delete.html', {'group': group})


@login_required
def ticket_list(request):
    if request.user.role == 'Admin':
        tickets = Ticket.objects.all()
    else:
        tickets = Ticket.objects.filter(user=request.user)
    return render(request, 'tickets/tickets_list.html', {'tickets': tickets})


@login_required
def ticket_create(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('ticket_list')
    else:
        form = TicketForm()
    return render(request, 'tickets/tickets_create.html', {'form': form})


@login_required
def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    return render(request, 'tickets/tickets_detail.html', {'ticket': ticket})


@login_required
def ticket_update(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('ticket_detail', ticket_id=ticket.id)
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'tickets/tickets_update.html', {'form': form, 'ticket': ticket})


@login_required
def ticket_delete(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method == 'POST':
        ticket.delete()
        return redirect('ticket_list')
    return render(request, 'tickets/tickets_confirm_delete.html', {'ticket': ticket})


@login_required
@user_passes_test(user_is_admin)
def user_list(request):
    users = User.objects.all()
    return render(request, 'users/users_list.html', {'users': users})
