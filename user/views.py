
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .user import UserForm


def listusers(request):
    template = loader.get_template('userlist.html')
    return HttpResponse(template.render({}, request))


def userhome(request):
    return HttpResponse("<h1>This is list of user home page</h1>")


def additems(request):
    if request.method == "POST":
        userform_data = UserForm(request.POST)

        if userform_data.is_valid():
            Itemname = userform_data.cleaned_data["Itemname"]
            dom = userform_data.cleaned_data["dom"]
            doe = userform_data.cleaned_data["doe"]

            return render(request, 'additems_success.html', {
                'Itemname': Itemname,
                'dom': dom,
                'doe': doe
            })

    else:
        userform_data = UserForm()

    return render(request, 'additems.html', {
        'userform': userform_data
    })


def additems_success(request):
    return HttpResponse("Item added successfully!")
