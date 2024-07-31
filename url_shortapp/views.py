from django.http import HttpResponse
from django.shortcuts import render
from .forms import FormLinks
from .models import Links
from django.shortcuts import redirect


def home(request):
    form = FormLinks()
    status = request.GET.get("status")
    return render(request, "home.html", {"form": form, "status": status})


def validate_link(request):
    form = FormLinks(request.POST)

    short_link = form.data["short_link"]
    links = Links.objects.filter(short_link=short_link)
    if len(links) > 0:
        return redirect("/?status=1")

    if form.is_valid():
        try:
            form.save()
            return HttpResponse(
                f"Your link was successfully created and is: http://127.0.0.1:8000/{form.data['short_link']}"
            )
        except:
            return HttpResponse("Internal system error.")


def redirecion(request, link):
    links = Links.objects.filter(short_link = link)
    if len(links) == 0:
        return redirect('/')

    return redirect(links[0].redirect_link)
