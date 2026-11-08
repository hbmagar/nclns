# Create your views here.
from django.shortcuts import render, get_object_or_404

"""include all models here"""
from about_team_app.models import *  

def about_team(request):
    team_member_title = TeamMember_title_part.objects.all()
    admin_team_members = AdminTeamMember.objects.all()
    staff_team_members = staffTeamMember.objects.all()
    context = {
        'team_member_title': team_member_title,
        'admin_team_members': admin_team_members,
        'staff_team_members': staff_team_members,
    }
    return render(request, 'webpages/about_team.html', context)