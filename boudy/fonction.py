from django.utils import timezone
from datetime import date, time, datetime,timedelta

def initialisation(i) :
   match i :
         case 1 | 32 : # Hugo, Gabin
            iParent = 1
            iGParent = 3
            iAGParent = 7
            iAieulle = 15    
            ibAieulle = 37      
         case 2 | 33: # Yoann, Damien
            iParent = 2
            iGParent = 6
            iAGParent = 14
            iAieulle = 36
            ibAieulle = 68
         case 3 : # Charlotte
            iParent = 3
            iGParent = 9
            iAGParent = 21
            iAieulle = 51
            ibAieulle = 115
         case 4 : # Yves
            iParent = 4
            iGParent = 12
            iAGParent = 34
            iAieulle = 66
            ibAieulle = 82 
         case 5 : #Abassia
            iParent = 5
            iGParent = 15
            iAGParent = 41
            iAieulle = 0  
            ibAieulle = 0  
         case 34 : # Julie
            iParent = 1
            iGParent = 0
            iAGParent = 0
            iAieulle = 0   
            ibAieulle = 0 
         case 6 : # Leymarie A.
            iParent = 6
            iGParent = 18
            iAGParent = 48
            iAieulle = 112   
            ibAieulle = 144 
         case 7 : # Cheyssial S.
            iParent = 7
            iGParent = 21
            iAGParent = 55
            iAieulle = 127   
            ibAieulle = 175
         case 35 : # Serge
            iParent = -1
            iGParent = 0
            iAGParent = 0
            iAieulle = 0   
            ibAieulle = 0 

   return iParent, iGParent, iAGParent, iAieulle, ibAieulle

def age (naissance, deces) :

   ans=0
   mois=0

   now = datetime.now()
   
   if (naissance != " ") & (deces == " ") :
      ans = ""
      mois = ""
      return ans, mois

   if (deces != " ") :
      if len(naissance) < 5:
         if (naissance != " ") :
            naissance = "01/01/"+naissance
            jNaissance = datetime.strptime(naissance, "%d/%m/%Y")
            deces = "01/01/"+deces
            jDeces = datetime.strptime(deces, "%d/%m/%Y")
            difference = jDeces-jNaissance
            ans = difference.days // 365.25  
            mois = 0
      else :
         if naissance != "" :
            jNaissance = datetime.strptime(naissance, "%d-%m-%Y")
            if deces != "" :
               jDeces = datetime.strptime(deces, "%d-%m-%Y")
               difference = jDeces-jNaissance
            else :
               difference = now - jNaissance
            ans = difference.days // 365.25
            reste = difference.days % 365.25
            mois = reste // 30.43
            jours = reste % 30.43
         else :
            ans = 0
            mois = 0
      
   return int(ans), int (mois)
