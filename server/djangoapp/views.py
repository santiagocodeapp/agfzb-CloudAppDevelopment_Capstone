# from django.shortcuts import render
# from django.http import HttpResponseRedirect, HttpResponse
# from django.contrib.auth.models import User
# from django.shortcuts import get_object_or_404, render, redirect
# # from .models import related models
# # from .restapis import related methods
# from django.contrib.auth import login, logout, authenticate
# from django.contrib import messages
# from datetime import datetime
# import logging
# import json
# from django.db import IntegrityError
# from django.urls import reverse


# # Get an instance of a logger
# logger = logging.getLogger(__name__)


# # Create your views here.


# # Create an `about` view to render a static about page
# def about(request):
#     return render(request, 'djangoapp/about.html')


# # Create a `contact` view to return a static contact page
# def contact(request):
#     return render(request, 'djangoapp/contact.html')

# # Create a `login_request` view to handle sign in request
# def login_request(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         if not username and not password:
#             return render(request, "djangoapp/index.html", {
#                 "message": "Please enter Username and/or Password."
#             })
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('djangoapp:index')
#         else:
#             return render(request, "djangoapp/index.html", {
#                 "message": "Invalid username and/or password."
#             })

# # Create a `logout_request` view to handle sign out request
# def logout_request(request):
#     logout(request)
#     return redirect('djangoapp:index')

# # Create a `registration_request` view to handle sign up request
# def registration_request(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         first_name = request.POST['first-name']
#         last_name = request.POST['last-name']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
        
#         if password1 != password2:
#             return render(request, 'djangoapp/registration.html',{
#                 'message': 'Passwords must match.'
#             })
#         try:   
#             user = User.objects.create_user(username, '' ,password1, first_name=first_name, last_name=last_name)
#             user.save()
#         except IntegrityError:
#              return render(request, "djangoapp/registration.html", {
#                 "message": "Username already taken."
#             })
#         login(request, user)
#         return HttpResponseRedirect(reverse("djangoapp:index"))
#     else:
#         return render(request, 'djangoapp/registration.html')

# # Update the `get_dealerships` view to render the index page with a list of dealerships
# def get_dealerships(request):
#     context = {}
#     if request.method == "GET":
#         return render(request, 'djangoapp/index.html', context)


# # Create a `get_dealer_details` view to render the reviews of a dealer
# # def get_dealer_details(request, dealer_id):
# # ...

# # Create a `add_review` view to submit a review
# # def add_review(request, dealer_id):
# # ...




from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Players, Report, User, Positions, IMG_Teams
from django.views.decorators.csrf import csrf_exempt


# Index View that will return all the teams storage in the DB


def index(request):
    if request.user.is_authenticated:
        teams = IMG_Teams.objects.all()
        is_user = True
        return render(request, 'djangoapp/index.html', {
            "is_user": is_user,
            "teams": teams
        })
    else:
        return HttpResponseRedirect(reverse("login"))


# Log In User into Website
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "djangoapp/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "djangoapp/login.html")


# Log Out user from Website
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        first = request.POST["first"]
        last = request.POST["last"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "djangoapp/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password, first_name=first, last_name=last)
            user.save()
        except IntegrityError:
            return render(request, "MyReport/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "djangoapp/register.html")


# Here we can send and save the new reports on each players
@login_required
def send_report(request):

    if request.method != "POST":
        return JsonResponse({"error": "POST request required."}, status=400)

    defense = request.POST['defense']
    hitting = request.POST['hitting']
    pitching = request.POST['pitching']
    character_work_ethic = request.POST['character-work-ethic']
    first = request.POST['first']
    last = request.POST['last']
    x = request.POST['team']

    player = Players.objects.get(first=first, last=last)

    report = Report(CoachName=str(request.user), Player=player, Defense=defense, Hitting=hitting, Pitching=pitching, Character_Work_Ethic=character_work_ethic)
    report.save()

    return team(request, f"{x}")


# This function look up for the players into specific team and render a new html with the results if any
@login_required
def team(request, team):
    players = Players.objects.filter(team=team)
    is_user = True
    return render(request, 'djangoapp/team.html', {
        "team": team,
        "players": players,
        "is_user": is_user
    })


# This Function will allow Coaches to add new player to a Team.
@login_required
def add_player(request):
    if request.method == "POST":

        team = request.POST['exampleDataList']
        first_name = request.POST['create-first']
        last_name = request.POST['create-last']
        position = request.POST['create-position']

        player = Players(team=team, first=first_name, last=last_name, player_positions=position)
        player.save()

        teams = IMG_Teams.objects.all()
        is_user = True
        
        return render(request, 'djangoapp/index.html', {
            "is_user": is_user,
            "teams": teams,
            "message": "message",
        })


# This Function will allow coaches to create new teams. 
@login_required
def add_team(request):

    if request.method == "POST":

        team = request.POST['new-team']

        new_team = IMG_Teams(team = team)
        new_team.save()

        teams = IMG_Teams.objects.all()
        is_user = True

        return render(request, 'djangoapp/index.html', {
            "is_user": is_user,
            "teams": teams,
            "message1": "message",
        })