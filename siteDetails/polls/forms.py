# -*- coding: utf-8 -*-
from django import forms
from .models import customer_information

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    
class CustomerForm(forms.ModelForm):
    class Meta:
        model = customer_information
        fields = ['customer_fname', 'customer_lname', 'Project_name', 'plot_no', 'total_amount']
#    customer_fname = forms.CharField(max_length=200)
#    customer_lname = forms.CharField(max_length=200)
#    Project_name = forms.CharField(max_length=200)
#    plot_no = forms.CharField(max_length=20)

class CustomerSearch(forms.Form):
        customer_fname = forms.CharField(max_length=100 , required=False)
        customer_lname = forms.CharField(max_length=100, required=False)
        Project_name = forms.CharField(max_length=100, required=False)
        plot_no = forms.CharField(max_length=20, required=False)