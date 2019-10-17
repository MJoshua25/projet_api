from django.shortcuts import render, redirect
from django_seed import Seed
from random import randint
from .models import *

# Create your views here.
def fake_mois(request):
    mois = ['Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre','Octobre','Novembre','Décembre',]
    seeder = Seed.seeder()
    seeder.add_entity(Mois, 11, {
        'titre':lambda x: mois[randint(0,len(mois)-1)],
    })
    inserted_pks = seeder.execute()
    return redirect('../api/Mois/')