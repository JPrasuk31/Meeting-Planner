from django.shortcuts import render, get_object_or_404,redirect
from .models import Meeting,Room
from django.forms import modelform_factory

def meeting_detail(request, id):
    meeting = get_object_or_404(Meeting, pk = id)
    return render(request,"meetings/meeting_detail.html", {"meeting": meeting})

def room_list(request):
    return render(request, "meetings/room_list.html", {"rooms": Room.objects.all()})

MeetingForm = modelform_factory(Meeting, exclude=[])

def new(request):
    if request.method == "POST":
        # Form has submitted process data
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})

