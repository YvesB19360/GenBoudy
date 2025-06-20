# ~/projects/django-web-app/merchex/listings/views.py

from django.http import HttpResponse
from django.shortcuts import render
from boudy.models import Famille, Cousin, Melimelo
from boudy.fonction import initialisation, age
from pathlib import Path
import os

def acceuil(request):
    familles = Famille.objects.all()
    largeur = 200
    hauteur = 400
    ancetres = ["louis", "armand", "clemence", "suzanne", "gaston"]
    return render(request, 'boudy/hello.html',
         {'familles': familles, 'largeur' : largeur, 'hauteur' : hauteur, "ancetres" : ancetres})

def famille_detail(request, id):
   
   parents = [""]*2
   gParents = [""]*4
   agParents = [""]*8
   aieulle = [""]*16
   if (id == 1) | (id == 4) | (id == 32) | (id == 3) | (id == 7): # Hugo, Yves, Gabin, Charlotte, Cheyssial S.
      baieulle1 =  [""]*16
      baieulle2 =  [""]*16
      aieux = 32
   else :
      baieulle1 =  [""]*8
      baieulle2 =  [""]*8
      aieux = 16
   
   individu = Famille.objects.get(id=id) 
   Age = age(individu.dateNaissance, "")
   if Age[0] < 5 :
      ageJour = (str(Age[0]) +" ans " + str(Age[1]) + " mois")
   else :
      ageJour = (str(Age[0]) +" ans ")
   individu.dateDeces = ageJour

   iParent = initialisation(id)[0]
   igParent = initialisation(id)[1]
   aigParent = initialisation(id)[2]
   iaieulle =  initialisation(id)[3]
   ibaieulle = initialisation(id)[4]

   if id==32 : # Gabin = Hugo
      id=1

   if id==33 : # Damien = Yoann
      id=2
   
   for i in range(iParent, iParent+2) :
      parents[i-iParent] = Famille.objects.get(id=id+i)
      if parents[i-iParent].dateDeces == " " :
         Age = age((parents[i-iParent].dateNaissance),"")
         ageJour = (str(Age[0]) +" ans")
         parents[i-iParent].dateDeces = ageJour
      else :
         Age = age(parents[i-iParent].dateNaissance, parents[i-iParent].dateDeces)
         ageJour = (str(Age[0]) +" ans")
         parents[i-iParent].dateDeces = parents[i-iParent].dateDeces + " " "à : " + ageJour
      
   if igParent > 0 :
      for i in range(igParent, igParent+4) :
         gParents[i-igParent] = Famille.objects.get(id=id+i) 
         if gParents[i-igParent].dateNaissance != " " :
            if  gParents[i-igParent].dateDeces == " " :
               Age = age((gParents[i-igParent].dateNaissance),"")
               ageJour = (str(Age[0]) +" ans")
               gParents[i-igParent].dateDeces = ageJour
            else :
               Age = age(gParents[i-igParent].dateNaissance, gParents[i-igParent].dateDeces)
               if Age[0] != "" :
                  ageJour = (str(Age[0]) +" ans")
                  gParents[i-igParent].dateDeces = gParents[i-igParent].dateDeces + " " "à : " + ageJour

   if aigParent > 0 :
      for i in range(aigParent, aigParent+8) :
         agParents[i-aigParent] = Famille.objects.get(id=id+i) 
         if agParents[i-aigParent].dateNaissance != " " :
            Age = age(agParents[i-aigParent].dateNaissance, agParents[i-aigParent].dateDeces)  
            if Age[0] != "" :
               ageJour = (str(Age[0]) +" ans")
               agParents[i-aigParent].dateDeces = agParents[i-aigParent].dateDeces + " " "à : " + ageJour

   if iaieulle > 0 :
      for i in range(iaieulle, iaieulle+16) :
         aieulle[i-iaieulle] = Famille.objects.get(id=id+i)
         if aieulle[i-iaieulle].dateNaissance != " " :  
            Age = age(aieulle[i-iaieulle].dateNaissance, aieulle[i-iaieulle].dateDeces)  
            if Age[0] != "" :
               ageJour = (str(Age[0]) +" ans")
               aieulle[i-iaieulle].dateDeces = aieulle[i-iaieulle].dateDeces + " " "à : " + ageJour

   if ibaieulle > 0 :
      j=-1
      for i in range(ibaieulle, ibaieulle+aieux, 2) :
         j=j+1
         baieulle1[i-ibaieulle-j] = Famille.objects.get(id=id+i)
         if baieulle1[i-ibaieulle-j].dateNaissance != " " :
            Age = age(baieulle1[i-ibaieulle-j].dateNaissance, baieulle1[i-ibaieulle-j].dateDeces)  
            if Age[0] != "" :
               ageJour = (str(Age[0]) +" ans")
               baieulle1[i-ibaieulle-j].dateDeces = baieulle1[i-ibaieulle-j].dateDeces + " " "à : " + ageJour
      j=0
      for i in range(ibaieulle+1, ibaieulle+aieux, 2) :
         j=j+1
         baieulle2[i-ibaieulle-j] = Famille.objects.get(id=id+i)
         if baieulle1[i-ibaieulle-j].dateNaissance != " " :
             Age = age(baieulle2[i-ibaieulle-j].dateNaissance, baieulle2[i-ibaieulle-j].dateDeces)  
             if Age[0] != "" :
               ageJour = (str(Age[0]) +" ans")
               baieulle2[i-ibaieulle-j].dateDeces = baieulle2[i-ibaieulle-j].dateDeces + " " "à : " + ageJour
         
   return render(request,
          'boudy/famille_detail.html',
         {'choix': individu, 'parents' : parents, 'gParents' : gParents, 'agParents' : agParents,
          'aieulle' : aieulle, 'baieulle1' : baieulle1, 'baieulle2' : baieulle2, 'aieux' : aieux })

def individu_detail(request, id):
   individu = Famille.objects.get(id=id)
   fichier = "/static/boudy/fiches/" + individu.nom + individu.prenom + ".png"
   fichier2 = "/static/boudy/fiches/" + individu.nom + individu.prenom + "_2.png"

   file_path = "\\boudy\\static\\boudy\\fiches\\" + individu.nom + individu.prenom + "_2.png"

   current_directory = os.getcwd()

   file_path1 = current_directory + file_path
  
   if os.path.exists(file_path1):
      
      return render(request,
         'boudy/individu_detail.html',
          {'familles': individu, 'fichier' : fichier, 'fichier2' : fichier2})

   return render(request,
         'boudy/individu_detail.html',
          {'familles': individu, 'fichier' : fichier})

def cousins(request):
    cousins = Cousin.objects.all()
    return render(request, 'boudy/cousins.html',
         {'cousins': cousins})

def cousins_details(request, id):
    cousins = Cousin.objects.get(id=id)
    print(cousins)
    fichier = "/static/boudy/fiches/cousins/" + cousins.nom + cousins.prenom + ".png"
    return render(request, 'boudy/cousins_details.html',
         {'cousins': cousins, 'fichier' : fichier})

def melimelo(request):
    melimelos = Melimelo.objects.all()
    return render(request, 'boudy/melimelo.html',
         {'melimelos': melimelos})

def melimelo_details(request, id):
    melimelos = Melimelo.objects.get(id=id)
    fichier = "/static/boudy/fiches/melimelo/" + melimelos.nom + melimelos.prenom + ".png"
    return render(request, 'boudy/melimelo_details.html',
         {'melimelos': melimelos, 'fichier' : fichier})