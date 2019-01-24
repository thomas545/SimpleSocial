from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import ListView,DetailView,UpdateView,CreateView,DeleteView,RedirectView
from .models import Group , GroupMember
# Create your views here.


class ListGroups(ListView):
    model = Group


class SingleGroup(DetailView):
    model = Group


class CreateGroup(LoginRequiredMixin,CreateView):
    model = Group
    fields = ['name', 'description']


class JoinGroup(LoginRequiredMixin,RedirectView):

    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):
        group = get_object_or_404(Group,slug=self.kwargs.get('slug'))

        try:
            GroupMember.objects.create(user=self.request.user,group=group)
        except IntegrityError:
            messages.warning(self.request , 'You already a mamber!')
        else:
            messages.warning(self.request , 'You are now a mamber!')

        return super().get(request,*args,**kwargs)


class LeaveGroup(LoginRequiredMixin,RedirectView):

    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})


    def get(self,request,*args,**kwargs):

        try:
            membership = GroupMember.objects.filter(user=self.request.user,
                                group__slug=self.kwargs.get('slug')).get()
        except GroupMember.DoesNotExist:
            messages.warning(self.request, "Sorry You Are Not in This Group")
        else:
            membership.delete()
            messages.success(self.request, "You have Left Group")

        return super().get(request,*args,**kwargs)
