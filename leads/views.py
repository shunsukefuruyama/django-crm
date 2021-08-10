from django.shortcuts import render, redirect
from django.http import HttpResponse
# leads.models works but .models is enough because this is already in leads folder
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm

# Looks like render's 2nd augment starts from templates folder
# but not including templates folder itself

def lead_list(request):
    leads = Lead.objects.all()
    # leads = Lead.objects.values_list()

    return render(request, 'leads/lead_list.html', {
        'leads': leads,

    })

def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    return render(request, 'leads/lead_detail.html', {
        "lead": lead,
    })

def lead_create(request):
    if request.method == "POST":
        print('Receiving a post request')
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/leads')

    else:
        form = LeadModelForm()

    return render(request, 'leads/lead_create.html', {
        "form": form,
    })

# def lead_create(request):
#     if request.method == "POST":
#         print('Receiving a post request')
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             print('Form is valid')
#             print(form.cleaned_data)
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             age = form.cleaned_data['age']
#             agent = Agent.objects.first()

#             Lead.objects.create(
#                 first_name = first_name,
#                 last_name = last_name,
#                 age = age,
#                 agent = agent,
#             )
#             print("Lead has been created.")

#             return redirect('/leads')

#     else:
#         form = LeadForm()

#     return render(request, 'leads/lead_create.html', {
#         "form": form,
#     })