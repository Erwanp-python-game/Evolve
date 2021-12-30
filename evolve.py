import pygame# python 3.7.1, pygame 1.9.4 #evolve1.0
from math import *
import numpy as np
from pygame.locals import *
from random import *
import pickle
import pandas as pd
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
import matplotlib.pyplot as plt
import os
def pol(y):
	x=[0.1,0.5,1.1]
	y
	poly=np.polyfit(x,y,7)
	return poly
gnouf=[uniform(-0.4,0.4),uniform(-0.8,0.8),uniform(-0.4,0.4)]
def f(x,poly,b):
	a=0
	for i in range(0,7):
		a=a+poly[i]*(x**(7-i))-0.5*x*b
	return a
	
musicplayed=1	
def readlatin():
	datafile = open('latin.txt')
	lines = datafile.readlines()
	x=[]
	
	for i,j in enumerate(lines):
		x.append(lines[i].split())
	a=x[0]
	table=np.full((26,26),0)
	
	for i in a:
		for j in range(0,len(i)-1):
			if ord(i[j])-97>-1 and ord(i[j+1])-97>-1:
				table[ord(i[j])-97][ord(i[j+1])-97]=table[ord(i[j])-97][ord(i[j+1])-97]+1
	
	table3=np.full((26,26),0)
	
	for i in a:
		for j in range(0,len(i)-2):
			if ord(i[j])-97>-1 and ord(i[j+2])-97>-1:
				table3[ord(i[j])-97][ord(i[j+2])-97]=table[ord(i[j])-97][ord(i[j+2])-97]+1
	
	u=0
	table2=np.full((26,1),0)
	for i in a:
		if ord(i[0])-97>-1:
			table2[ord(i[0])-97][0]=table2[ord(i[0])-97][0]+1
	
	L2=[]
	for i in range(0,26):
		L2.append(table2[i][0])
	
	
	population=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	L=[]
	a=choices(population,weights=L2,k=1)
	mot=a[0]
	for m in range(0,6+randint(-2,1)):
		L=[]
		for i in range(0,26):
			L.append(table[ord(mot[-1])-97][i]*table3[ord(mot[max(-2,0-len(mot))])-97][i])
		K=choices(population, weights=L, k=1)
		a=K
		mot=mot+a[0]
	if mot[0:2]!='nd' and mot[0:2]!='nt' and mot[0]!=mot[1] and (mot[-1]!=mot[-2] or mot[-2]=='i') and ('zz' in mot)==False and mot[-2:len(mot)]!='tr' and mot[-2:len(mot)]!='qu':	
		return mot
	else:
		return 0



BIGSCORE=0
zoom=1
yD=0
xD=0
seed=0
taillemot=0.1
Xl=[]
Yl=[]
listnom=['monEspece']
xs=randint(0,139)
ys=randint(0,69)
machsupL=['machsuplez','taureau','smilcroco','elan','col','rhino','tetedetruc','cake','koi','espad','hippo','machsupsouris.sc1']
machinfL=['machinf','defense','machoi','bouchequipend','oinj','pelikanlol']
nageoireL=['nageoire','nageoirebelle','tenta']
jambeL=['grossepatte','jambe1','jambeinv','jnage']
piedL=['piedpalmé','panar','pieh']
vertebreL=['gros','pointe','vertebre','vertebreT','poil','vert','vertpic','pico']
textL=['wood','swirl','leo','lezar','crac']
queueL=['queue','queuebal']
brasL=['bras','bras2doigts']
#décaler la machoire vers l'avant lorsque croco+yeux aussi
dicoMaS={}
dicoMaS['plain']=['machsuplez','taureau','smilcroco','elan','col','rhino','tetedetruc','cake','koi','hippo']#mettre les montagnes
dicoMaS['plai2']=['machsuplez','taureau','smilcroco','elan','col','rhino','tetedetruc','cake','koi']
dicoMaS['foret']=['machsuplez','taureau','smilcroco','elan','col','rhino','tetedetruc','cake','koi','hippo','machsupsouris.sc1']
dicoMaS['svane']=['machsuplez','taureau','smilcroco','col','rhino','tetedetruc','cake','koi','hippo','machsupsouris.sc1']
dicoMaS['jungl']=['machsuplez','taureau','smilcroco','col','rhino','tetedetruc','cake','koi','hippo','machsupsouris.sc1']
dicoMaS['deser']=['machsuplez','taureau','smilcroco','col','rhino','tetedetruc','cake','koi','machsupsouris.sc1']
dicoMaS['stepe']=['machsuplez','taureau','elan','col','rhino','tetedetruc','cake','koi']
dicoMaS['forbo']=['machsuplez','taureau','elan','col','rhino','tetedetruc','cake','koi']
dicoMaS['tunda']=['machsuplez','taureau','elan','col','rhino','tetedetruc','cake','koi']
dicoMaS['glace']=['machsuplez','smilcroco','col','tetedetruc','cake','koi','espad']
dicoMaS['cotes']=['machsuplez','smilcroco','col','tetedetruc','cake','koi','espad','hippo']
dicoMaS['mangr']=['machsuplez','smilcroco','col','tetedetruc','cake','koi','espad','hippo']
dicoMaS['water']=['machsuplez','smilcroco','col','tetedetruc','cake','koi','espad','hippo']
dicoMaS['coldw']=['machsuplez','smilcroco','col','tetedetruc','cake','koi','espad','hippo']
dicoMaS['tropw']=['machsuplez','smilcroco','col','tetedetruc','cake','koi','espad','hippo']
dicoMaS['coldm']=['machsuplez','taureau','elan','col','rhino','tetedetruc','cake','koi']
dicoMaS['monts']=['machsuplez','taureau','smilcroco','elan','col','rhino','tetedetruc','cake','koi','hippo']
dicoMaS['hotmt']=['machsuplez','taureau','smilcroco','col','rhino','tetedetruc','cake','koi','hippo','machsupsouris.sc1']
dicoMaS['volca']=['machsuplez','taureau','elan','col','rhino','tetedetruc','cake','koi']
dicoMaS['crate']=['machsuplez','taureau','elan','col','rhino','tetedetruc','cake','koi']
dicoMaS['meteo']=['machsuplez','taureau','elan','col','rhino','tetedetruc','cake','koi']
dicoMaS['magma']=['machsuplez','taureau','elan','col','rhino','tetedetruc','cake','koi']

dicoMai={}
dicoMai['plain']=['machinf','defense','machoi','bouchequipend','oinj']
dicoMai['plai2']=['machinf','defense','machoi','bouchequipend','oinj']
dicoMai['foret']=['machinf','defense','machoi','bouchequipend','oinj']
dicoMai['svane']=['machinf','defense','machoi','bouchequipend','oinj']
dicoMai['jungl']=['machinf','defense','machoi','bouchequipend','oinj','pelikanlol']
dicoMai['deser']=['machinf','defense','machoi','bouchequipend','oinj']
dicoMai['stepe']=['machinf','defense','machoi','bouchequipend','oinj']
dicoMai['forbo']=['machinf','defense','machoi','bouchequipend','oinj']
dicoMai['tunda']=['machinf','defense','machoi','bouchequipend','oinj']
dicoMai['glace']=['machinf','machoi','oinj','pelikanlol']
dicoMai['cotes']=['machinf','machoi','oinj','pelikanlol']
dicoMai['mangr']=['machinf','machoi','oinj','pelikanlol']
dicoMai['water']=['machinf','machoi','oinj']
dicoMai['coldw']=['machinf','machoi','oinj']
dicoMai['tropw']=['machinf','machoi','oinj']
dicoMai['monts']=['machinf','defense','machoi','bouchequipend','oinj']
dicoMai['hotmt']=['machinf','defense','machoi','bouchequipend','oinj']
dicoMai['coldm']=['machinf','defense','machoi','bouchequipend','oinj']
dicoMai['volca']=['machinf','defense','machoi','bouchequipend','oinj']
dicoMai['meteo']=['machinf','defense','machoi','bouchequipend','oinj']
dicoMai['crate']=['machinf','defense','machoi','bouchequipend','oinj']
dicoMai['magma']=['machinf','defense','machoi','bouchequipend','oinj']

dicoQ={}
dicoQ['plain']=['queue']
dicoQ['plai2']=['queue']
dicoQ['foret']=['queue']
dicoQ['svane']=['queue']
dicoQ['jungl']=['queue']
dicoQ['deser']=['queue']
dicoQ['stepe']=['queue']
dicoQ['forbo']=['queue']
dicoQ['tunda']=['queue']
dicoQ['glace']=['queue','queuebal']
dicoQ['cotes']=['queue','queuebal']
dicoQ['mangr']=['queue','queuebal']
dicoQ['water']=['queue','queuebal']
dicoQ['tropw']=['queue','queuebal']
dicoQ['coldw']=['queue','queuebal']
dicoQ['coldm']=['queue']
dicoQ['hotmt']=['queue']
dicoQ['monts']=['queue']
dicoQ['meteo']=['queue']
dicoQ['volca']=['queue']
dicoQ['crate']=['queue']
dicoQ['magma']=['queue']

dicoJ={}
dicoJ['plain']=['grossepatte','jambe1','jambeinv']
dicoJ['plai2']=['grossepatte','jambe1','jambeinv']
dicoJ['foret']=['grossepatte','jambe1','jambeinv']
dicoJ['svane']=['grossepatte','jambe1','jambeinv']
dicoJ['jungl']=['grossepatte','jambe1','jambeinv']
dicoJ['deser']=['grossepatte','jambe1','jambeinv']
dicoJ['stepe']=['grossepatte','jambe1','jambeinv']
dicoJ['forbo']=['grossepatte','jambe1','jambeinv']
dicoJ['tunda']=['grossepatte','jambe1','jambeinv']
dicoJ['glace']=['jnage']
dicoJ['cotes']=['jnage']
dicoJ['mangr']=['jnage']
dicoJ['water']=['jnage']
dicoJ['coldw']=['jnage']
dicoJ['tropw']=['jnage']
dicoJ['monts']=['grossepatte','jambe1','jambeinv']
dicoJ['coldm']=['grossepatte','jambe1','jambeinv']
dicoJ['hotmt']=['grossepatte','jambe1','jambeinv']
dicoJ['meteo']=['grossepatte','jambe1','jambeinv']
dicoJ['magma']=['grossepatte','jambe1','jambeinv']
dicoJ['volca']=['grossepatte','jambe1','jambeinv']
dicoJ['crate']=['grossepatte','jambe1','jambeinv']

dicop={}
dicop['plain']=['panar','pieh']
dicop['plai2']=['panar','pieh']
dicop['foret']=['panar','pieh']
dicop['svane']=['panar','pieh']
dicop['jungl']=['panar','pieh']
dicop['deser']=['panar','pieh']
dicop['stepe']=['panar','pieh']
dicop['forbo']=['panar','pieh']
dicop['tunda']=['panar','pieh']
dicop['glace']=['piedpalmé','pieh']
dicop['cotes']=['piedpalmé','pieh']
dicop['mangr']=['piedpalmé','pieh']
dicop['water']=['piedpalmé','pieh']
dicop['coldw']=['piedpalmé','pieh']
dicop['tropw']=['piedpalmé','pieh']
dicop['monts']=['panar','pieh']
dicop['coldm']=['panar','pieh']
dicop['hotmt']=['panar','pieh']
dicop['meteo']=['panar','pieh']
dicop['crate']=['panar','pieh']
dicop['volca']=['panar','pieh']
dicop['magma']=['panar','pieh']

dicob={}
dicob['plain']=['bras','bras2doigts']
dicob['plai2']=['bras','bras2doigts']
dicob['foret']=['bras','bras2doigts']
dicob['svane']=['bras','bras2doigts']
dicob['jungl']=['bras','bras2doigts']
dicob['deser']=['bras','bras2doigts']
dicob['stepe']=['bras','bras2doigts']
dicob['forbo']=['bras','bras2doigts']
dicob['tunda']=['bras','bras2doigts']
dicob['glace']=['bras','bras2doigts']
dicob['cotes']=['bras','bras2doigts']
dicob['mangr']=['bras','bras2doigts']
dicob['water']=['bras','bras2doigts']
dicob['coldw']=['bras','bras2doigts']
dicob['tropw']=['bras','bras2doigts']
dicob['coldm']=['bras','bras2doigts']
dicob['hotmt']=['bras','bras2doigts']
dicob['monts']=['bras','bras2doigts']
dicob['meteo']=['bras','bras2doigts']
dicob['volca']=['bras','bras2doigts']
dicob['crate']=['bras','bras2doigts']
dicob['magma']=['bras','bras2doigts']

dicov={}
dicov['plain']=['gros','pointe','vertebre','vertebreT','vert','vertpic','pico']
dicov['plai2']=['gros','pointe','vertebre','vertebreT','vert','vertpic','pico']
dicov['foret']=['gros','pointe','vertebre','vertebreT','vert','vertpic','pico']
dicov['svane']=['gros','pointe','vertebre','vertebreT','vert','vertpic','pico']
dicov['jungl']=['gros','pointe','vertebre','vertebreT','vert','vertpic','pico']
dicov['deser']=['gros','pointe','vertebre','vertebreT','vert','vertpic','pico']
dicov['stepe']=['gros','pointe','vertebre','vertebreT','poil','vert']
dicov['forbo']=['gros','pointe','vertebre','vertebreT','poil','vert']
dicov['tunda']=['gros','pointe','vertebre','vertebreT','poil','vert']
dicov['glace']=['gros','pointe','vertebre','vertebreT','poil','vert']
dicov['cotes']=['gros','pointe','vertebre','vertebreT','vert','vertpic','pico']
dicov['mangr']=['gros','pointe','vertebre','vertebreT','vert','vertpic','pico']
dicov['water']=['gros','pointe','vertebre','vertebreT','vert','vertpic','pico']
dicov['coldw']=['gros','pointe','vertebre','vertebreT','vert','vertpic','pico']
dicov['tropw']=['gros','pointe','vertebre','vertebreT','vert','vertpic','pico']
dicov['coldm']=['gros','pointe','vertebre','vertebreT','poil','vert']
dicov['monts']=['gros','pointe','vertebre','vertebreT','poil','vert']
dicov['hotmt']=['gros','pointe','vertebre','vertebreT','vert','vertpic','pico']
dicov['meteo']=['gros','pointe','vertebre','vertebreT','vert','vertpic','pico']
dicov['magma']=['gros','pointe','vertebre','vertebreT','vert','vertpic','pico']
dicov['volca']=['gros','pointe','vertebre','vertebreT','vert','vertpic','pico']
dicov['crate']=['gros','pointe','vertebre','vertebreT','vert','vertpic','pico']

especes=pd.DataFrame([[100.0,xs,ys,0.0,0.0,0.0,'You']],index = ['monEspece'],columns = ['pop','X','Y','densitepoils','sec','respire','nom'])
listC=['monEspece']
RandomEspece=pd.DataFrame([[0.8+0.4*random(),0.8+0.4*random(),0.8+0.4*random(),0.8+0.4*random(),0.8+0.4*random(),randint(7,12),pol(gnouf),[],randint(0,3),0.0,0.0,0.0,choice(machsupL),choice(machinfL),choice(vertebreL),choice(nageoireL),choice(jambeL),choice(piedL),'queue',choice(brasL),0.0,(random(),random(),random()),(random(),random(),random()),min(max(np.random.normal(0.9,0.2),0.2),1.2),choice(textL),gnouf,0.0,[0.0],'no',(255,255,255),[0],0,10**5,'monEspece',random()+0.5,2]],
index = ['monEspece'],
columns = ['j0','j1','t0','t1','t2','vertebre','colonne','seed','motif','tete','nageoire','jambe','machsupTYPE','machinfTYPE','vertebreTYPE','nageoireTYPE','jambeTYPE','piedTYPE','queueTYPE','brasTYPE','Colormer','acol1','acol2','taille','texture','gnouf','bras','Tmu','mere','colortree','score','child','deadT','nominem','taillemotif','nbjambe'])

lf=[]
for i in range(0,RandomEspece.at['monEspece','vertebre']*2):
	lf.append(randint(0,1000))
RandomEspece.at['monEspece','seed']=lf

biomes=pd.DataFrame([
[20,50,500,1],
[-8,40,500,1],
[35,50,500,1],
[-17,40,500,1],
[20,20,500,1],
[14,100,500,1],
[14,70,500,1],
[35,20,500,1],
[20,100,500,1],
[20,100,500,1],
[5,20,500,1],
[20,20,500,1],
[-3,20,500,1],
[35,80,500,1],
[20,80,500,1],
[-8,20,500,1],
[-8,80,500,1],
[200,0,0,0],
[200,0,0,0],
[200,0,0,0],
[200,0,0,0],
[-17,40,500,1],
[-8,70,500,1],
[24,70,500,1],],index = 
['plain','tunda','svane','glace','plai2','cotes','water','deser','lac','mangr','monts','hotmt','coldm','jungl','foret','stepe','forbo','volca','magma','meteo','crate','glacC','coldw','tropw'],columns=['temperature','humidite','rssources maximales','renouvellement des ressources'])

caracterebiome=pd.DataFrame([
[1,1,2.5,(0.46,0.3,0.15),(0.56,0.3,0.15)],
[2,1,2.5,(1,1,1),(0.5,0.4,0.2)],
[0,1,2.5,(0.93,0.77,0.26),(0.96,0.65,0.26)],
[2,1,1,(1,1,1),(1,1,1)],
[1,2,2.5,(0.46,0.3,0.15),(0.56,0.3,0.15)],
[1,1,1,(1,1,1),(0.45,0.5,0.7)],
[1,1,0,(1,1,1),(0.45,0.5,0.7)],
[0,2,2.5,(0.93,0.77,0.26),(0.96,0.65,0.26)],
[0,0,0,(0,0,0),(0,0,0)],
[0,1,1,(0,0.9,0),(randint(0,1),randint(0,1),randint(0,1))],
[1,1,3.5,(0,0,0),(0,0,0)],
[0,1,3.5,(0,0,0),(0,0,0)],
[2,1,3.5,(0,0,0),(0,0,0)],
[0,0,2.5,(0,0.9,0),(randint(0,1),randint(0,1),randint(0,1))],
[1,0,2.5,(0,0.9,0),(0.56,0.3,0.15)],
[2,2,2.5,(0,0.9,0),(0.8,0.5,0.2)],
[2,0,2.5,(0.8,0.5,0.2),(0.5,0.4,0.2)],
[0,0,10,(0,0,0),(0,0,0)],
[0,0,10,(0,0,0),(0,0,0)],
[0,0,10,(0,0,0),(0,0,0)],
[0,0,10,(0,0,0),(0,0,0)],
[2,1,1,(0,0,0),(0,0,0)],
[2,1,0,(1,1,1),(0.45,0.5,0.7)],
[0,1,0,(1,1,1),(0.45,0.5,0.7)]],index = [
'plain'
,'tunda'
,'svane'
,'glace'
,'plai2'
,'cotes'
,'water'
,'deser'
,'lac'
,'mangr'
,'monts'
,'hotmt'
,'coldm'
,'jungl'
,'foret'
,'stepe'
,'forbo'
,'volca'
,'magma'
,'meteo'
,'crate'
,'glacC'
,'coldw'
,'tropw'],columns = ['densitepoils','sec','respire','color1','color2'])

#bestscore=[0,0,0,0,0,0,0,0,0,0]
#bestcreat=['','','','','','','','','','']
#f2 = open("scoreliste", "wb")
#pickle.dump(bestscore, f2)
#pickle.dump(bestcreat, f2)
#f2.close()

	
ListeEre=['Cambrian','Ordovician','Silurian','Devonian','Carboniferous','Permian','Triassic','Jurassic','Cretaceous','Paleocene','Eocene','Oligocene','Miocene','Pliocene','Pleistocene','Holocene','Futur']
DateEre=[541,485,443,419,358,299,252,201,145,66,56,34,23,5,2,0,-1]

colorERE=[(18, 5, 216), (50, 174, 94), (4, 34, 141), (24, 129, 79), (233, 33, 48), (134, 168, 128), (191, 50, 79), (134, 35, 117), (192, 147, 8), (19, 89, 105), (31, 206, 121), (131, 13, 173), (140, 161, 77), (159, 108, 86), (149, 186, 56), (40, 123, 202), (192, 111, 87)]

def Grad(c,age,period):
	if period !='Futur':
		pourcent=(-age-DateEre[ListeEre.index(period)])/(DateEre[ListeEre.index(period)+1]-DateEre[ListeEre.index(period)])
		C=int(c[0]*(0.5+0.5*pourcent))
		D=int(c[1]*(0.5+0.5*pourcent))
		E=int(c[2]*(0.5+0.5*pourcent))
		
		return(C,D,E)
		
	else:
		return c

addy=0
pygame.init()
pygame.display.set_icon(pygame.image.load("small.png"))
fenetre = pygame.display.set_mode((1400,700),RESIZABLE )
pygame.display.set_caption("Evolve")
changebiome=['plain','tunda','svane','plai2','deser','jungl','foret','stepe','forbo','water','glace','glacC','cotes','coldw','tropw','mangr','hotmt','coldm','monts']
son=pygame.mixer.Sound("bling.ogg")

MAP=pygame.Surface((1400,700),pygame.SRCALPHA, 32)
MAP2sec=pygame.Surface((1400,700),pygame.SRCALPHA, 32)
PopTr=[]
Time=[]
cases=np.full((140,70),"water")
nourriture=np.full((140,70),0)
temperature=np.full((140,70),0)
temperature2=np.full((140,70),0)
humidite=np.full((140,70),0)
humidite2=np.full((140,70),0)
brdG=np.full((140,70),0)

volcanMAP=np.full((140,70),'_____')
volcan_date=randint(300,600)#max(int(np.random.normal(1000,400)),100)
meteorMAP=np.full((140,70),'_____')
meteor_date=volcan_date+200*(-1)**(randint(0,1))#max(int(np.random.normal(1000,400)),100)
tremb_date=randint(50,99)
rayon=0
rayonm=0


continentM=np.empty((140,70),dtype=object)
for i in range(0,140):
	for j in range(0,70):
		continentM[i][j]=(0,0,0)
tuto=pygame.image.load("tuto.png").convert_alpha()
tutoF=pygame.image.load("tutoF.png").convert_alpha()
legendT=pygame.image.load("legendT.png").convert_alpha()
legendH=pygame.image.load("legendH.png").convert_alpha()
legend0=pygame.image.load("legend0.png").convert_alpha()
legendtree=pygame.image.load("legendtree.png").convert_alpha()

nbgraine=0
tropw=pygame.image.load("tropicalwater.png").convert_alpha()
coldw=pygame.image.load("coldwater.png").convert_alpha()
select=pygame.image.load("select.png").convert_alpha()
desert=pygame.image.load("desert.png").convert_alpha()
water=pygame.image.load("water.png").convert_alpha()
tundra=pygame.image.load("tundra.png").convert_alpha()
jungle=pygame.image.load("jungle.png").convert_alpha()
savane=pygame.image.load("svane.png").convert_alpha()
banquise=pygame.image.load("glace.png").convert_alpha()
foret=pygame.image.load("foret.png").convert_alpha()
cotes=pygame.image.load("cotes.png").convert_alpha()
montagnes=pygame.image.load("hills.png").convert_alpha()
coldm=pygame.image.load("monts.png").convert_alpha()
hotmt=pygame.image.load("mesa.png").convert_alpha()
mangrove=pygame.image.load("mangrove.png").convert_alpha()
plaines=pygame.image.load("plaines.png").convert_alpha()
lac=pygame.image.load("lac.png").convert_alpha()
steppe=pygame.image.load("steppe.png").convert_alpha()
plaines2=pygame.image.load("plainesvraies.png").convert_alpha()
foretbo=pygame.image.load("foretboreale.png").convert_alpha()
#lavefroide=pygame.image.load("lavefroide.png").convert_alpha()
humiditymap=pygame.image.load("humidite.png").convert_alpha()
heatmap=pygame.image.load("bouton2.png").convert_alpha()
save=pygame.image.load("bouton3.png").convert_alpha()
load=pygame.image.load("bouton4.png").convert_alpha()
pano=pygame.image.load("pano.png").convert_alpha()
creature=pygame.image.load("bouton5.png").convert_alpha()
worldmap=pygame.image.load("bouton6.png").convert_alpha()
evolve=pygame.image.load("bouton7.png").convert_alpha()
closet=pygame.image.load("bouton8.png").convert_alpha()
ofroid=pygame.image.load("ofroid.png").convert_alpha()
ochaud=pygame.image.load("ochaud.png").convert_alpha()
ohumide=pygame.image.load("ohumide.png").convert_alpha()
patoune=pygame.image.load("patoune.png").convert_alpha()
osec=pygame.image.load("osec.png").convert_alpha()
boutonV=pygame.image.load("boutonV.png").convert_alpha()
boutong=pygame.image.load("boutong.png").convert_alpha()
nuage=pygame.image.load("nuage.png").convert_alpha()
splito=pygame.image.load("splito.png").convert_alpha()
splitog=pygame.image.load("splitog.png").convert_alpha()
tree=pygame.image.load("tree.png").convert_alpha()
biomeshow=pygame.image.load("biomeshow.png").convert_alpha()
alive=pygame.image.load("alive.png").convert_alpha()
extinct=pygame.image.load("extinct.png").convert_alpha()
danger=pygame.image.load("danger.png").convert_alpha()
missionscreen=pygame.image.load("boutonmission.png").convert_alpha()
boutonname=pygame.image.load("boutonname.png").convert_alpha()
scoreim=pygame.image.load("scores.png").convert_alpha()
volca=pygame.image.load("volca.png").convert_alpha()
lave=pygame.image.load("lave.png").convert_alpha()
meteo=pygame.image.load("meteo.png").convert_alpha()
crate=pygame.image.load("crate.png").convert_alpha()
no=pygame.image.load("no.png").convert_alpha()
diff=pygame.image.load("diff.png").convert_alpha()
nuage=pygame.transform.scale(nuage,(16,16))
dico={}
dico['deser']=desert#les mots de 5 lettre dans les crochets
dico['svane']=savane
dico['mangr']=mangrove
dico['water']=water
dico['glace']=banquise
dico['glacC']=banquise
dico['tunda']=tundra
dico['lac']=lac
dico['foret']=foret
dico['plain']=plaines
dico['jungl']=jungle
dico['cotes']=cotes
dico['monts']=montagnes
dico['hotmt']=hotmt
dico['coldm']=coldm
dico['stepe']=steppe
dico['plai2']=plaines2
dico['forbo']=foretbo
dico['volca']=volca
dico['magma']=lave
dico['meteo']=meteo
dico['crate']=crate
dico['tropw']=tropw
dico['coldw']=coldw
dico['no']=no
#dico['lavef']=lavefroide
listedevolcans=[]
listedemetor=[]
posMax=[]
dicoImage={}
def loadTexture(a):
    textureSurface = pygame.image.load(a+'.png')
    
    width = textureSurface.get_width()
    height = textureSurface.get_height()
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    glEnable(GL_TEXTURE_2D)
    texid = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, texid)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    return texid
    

def Backdraw():
	glBegin(GL_QUADS)
	glColor3fv((1,1,1))
	glTexCoord2f(0.0, 0.0)
	glNormal3f(0, 0, 1.0)
	glVertex3f(-10,0,0)
			
	glTexCoord2f(0, 1)
	glNormal3f(0,0,1)
	glVertex3f(-10,10,0)
			
	glTexCoord2f(1, 1.0)
	glNormal3f(0,0,1)
	glVertex3f(10,10,0)
	
	glTexCoord2f(1, 0)
	glNormal3f(0,0,1)
	glVertex3f(10,0,0)
	glEnd()


def BackdrawF():
	glBegin(GL_QUADS)
	glColor3fv((1,1,1))
	glTexCoord2f(0.0, 0.0)
	glNormal3f(0, 0, 1.0)
	glVertex3f(-5,0,0)
			
	glTexCoord2f(0, 1)
	glNormal3f(0,0,1)
	glVertex3f(-5,10,0)
			
	glTexCoord2f(1, 1.0)
	glNormal3f(0,0,1)
	glVertex3f(5,10,0)
	
	glTexCoord2f(1, 0)
	glNormal3f(0,0,1)
	glVertex3f(5,0,0)
	glEnd()

def BackdrawF2():
	glBegin(GL_QUADS)
	glColor3fv((1,1,1))
	glTexCoord2f(0.0, 0.0)
	glNormal3f(0, 0, 1.0)
	glVertex3f(-100,-100,0)
			
	glTexCoord2f(0, 1)
	glNormal3f(0,0,1)
	glVertex3f(-100,100,0)
			
	glTexCoord2f(1, 1.0)
	glNormal3f(0,0,1)
	glVertex3f(100,100,0)
	
	glTexCoord2f(1, 0)
	glNormal3f(0,0,1)
	glVertex3f(100,-100,0)
	glEnd()

def BackdrawFrise():
	glBegin(GL_QUADS)
	glColor3fv((1,1,1))
	glTexCoord2f(0.0, 0.0)
	glNormal3f(0, 0, 1.0)
	glVertex3f(-50,0,0)
			
	glTexCoord2f(0, 1)
	glNormal3f(0,0,1)
	glVertex3f(-50,4,0)
			
	glTexCoord2f(1, 1.0)
	glNormal3f(0,0,1)
	glVertex3f(50,4,0)
	
	glTexCoord2f(1, 0)
	glNormal3f(0,0,1)
	glVertex3f(50,0,0)
	glEnd()

def read(objet):

	global machmoy
	posMax=[0,0,0,1000,1000,100]
	surfaces=[]
	verticies=[]
	normals=[]
	f = open(objet, "rb")
	g=pickle.load(f)
	while g!='fin':
		surfaces.append((g[0][0],g[1][0],g[2][0]))
		g=pickle.load(f)
	g=pickle.load(f)
	while g!='fin':
		verticies.append((g[1],g[2],g[3]))
		posMax[0]=max(posMax[0],g[1])
		posMax[1]=max(posMax[1],g[2])
		posMax[2]=max(posMax[2],g[3])
		posMax[3]=min(posMax[3],g[1])
		posMax[4]=min(posMax[4],g[2])
		posMax[5]=min(posMax[5],g[3])
		g=pickle.load(f)
	g=pickle.load(f)
	while g!='fin':
		normals.append((g[1],g[2],g[3]))
		g=pickle.load(f)
	return [ verticies,normals,surfaces,posMax]

def eyepos(verticies,posMax):
	a=randint(0,len(verticies)-1)
	while (verticies[a][0]-posMax[3])<0.55*(posMax[0]-posMax[3]) or (verticies[a][2]-posMax[5])<0.1*(posMax[2]-posMax[5]) or (verticies[a][1]-posMax[4])<0.3*(posMax[1]-posMax[4]):
		a=randint(0,len(verticies)-1)
	
	return verticies[a]

def objdraw(dos,ventre,col1,col2,verticies,normals,surfaces):# ventre 1=>jambe 2 couleur h_b      dos 1=> vertebre 2 couleur h_b
	glBegin(GL_TRIANGLES)
	for i_surface, surface in enumerate(surfaces):
		x = 0
		#
		
		for vertex in surface:
			x+=1
			glColor3fv(col1)
			if verticies[vertex-1][1]>0.5 and dos==2:
				glColor3fv(col2)
			if verticies[vertex-1][1]<-1.5 and ventre==1:
				glColor3fv(col2)
			
			if ((verticies[vertex-1][1]-verticies[seed%len(verticies)][1])**2+(verticies[vertex-1][2]-verticies[seed%len(verticies)][2])**2+(verticies[vertex-1][0]-verticies[seed%len(verticies)][0])**2)**0.5<0.4*taillemot and dos==1:
				glColor3fv(col2)
			if ((verticies[vertex-1][1]-verticies[(seed+len(verticies)//2)%len(verticies)][1])**2+(verticies[vertex-1][2]-verticies[(seed+len(verticies)//2)%len(verticies)][2])**2+(verticies[vertex-1][0]-verticies[(seed+len(verticies)//2)%len(verticies)][0])**2)**0.5<0.4*taillemot and dos==1:
				glColor3fv(col2)
			
			if abs(verticies[vertex-1][2]-verticies[seed%len(verticies)][2])<0.15*taillemot and dos==3:
				glColor3fv(col2)
				
			if verticies[vertex-1][2]>-0.2 and dos==-1:
				glColor3fv((1,1,1))
				if verticies[vertex-1][2]>-0.04:
					glColor3fv((0,0,0))
			if x==1:
				glTexCoord2f(0.0, 0.0)
			if x==2:
				glTexCoord2f(0, 1.0)
			if x==3:
				glTexCoord2f(1, 00)
			if x==4:
				glTexCoord2f(1, 1.0)
			
			glNormal3fv(normals[vertex-1])
			glVertex3fv(verticies[vertex-1])
	glEnd()

class graine(pygame.sprite.Sprite):
	
	def __init__(self,i,j,V,taille,C):
		global cases,nbgraine,listedevolcans
		pygame.sprite.Sprite.__init__(self)
		self.pos=[i,j]
		self.Type='?'
		self.vie=V
		self.T=taille
		self.color=C
			
	def update(self):
		
		global cases,nbgraine,startsize
		
		
		if self.pos[1]<=69 and self.pos[1]>=0:
			
			cases[self.pos[0]%140][self.pos[1]]='plain'
			continentM[self.pos[0]%140][self.pos[1]]=self.color
			if (self.pos[1]<62+randint(-2,2) and self.pos[1]>58+randint(-2,2)) or (self.pos[1]<12+randint(-2,2) and self.pos[1]>8+randint(-2,2)):
				cases[self.pos[0]%140][self.pos[1]]='stepe'
			if (self.pos[1]<58+randint(-2,2) and self.pos[1]>52+randint(-2,2)) or (self.pos[1]<18+randint(-2,2) and self.pos[1]>12+randint(-2,2)):
				cases[self.pos[0]%140][self.pos[1]]='plai2'
			if randint(0,1000)==0:
				cases[self.pos[0]%140][self.pos[1]]='volca'
				
				
			if self.pos[1]<60+randint(-2,2) and self.pos[1]>10+randint(-2,2) :
				if randint(0,50)==0:
					cases[self.pos[0]%140][self.pos[1]]='deser'
				score=0
				if cases[self.pos[0]%140][(self.pos[1]-1)%70]=='deser':
					score=score+1.8
				if cases[self.pos[0]%140][(self.pos[1]+1)%70]=='deser':
					score=score+1.8
				if cases[(self.pos[0]-1)%140][self.pos[1]]=='deser':
					score=score+1.8
				if cases[(self.pos[0]+1)%140][self.pos[1]]=='deser':
					score=score+1.8
				if randint(0,floor(score*1.7))>0:
					cases[self.pos[0]%140][self.pos[1]]='deser'
					
					
			
			
			R=randint(0,startsize-self.vie)
			if R<self.T and self.vie>0 and (cases[(self.pos[0]+1)%140][self.pos[1]]=='water' or randint(0,200)==0):
				Graine((self.pos[0]+1)%140,self.pos[1],self.vie-1,self.T,self.color)
				
			R=randint(0,startsize-self.vie)
			if R<self.T and self.vie>0 and (cases[(self.pos[0]-1)%140][self.pos[1]]=='water' or randint(0,200)==0):
				Graine((self.pos[0]-1)%140,self.pos[1],self.vie-1,self.T,self.color)
				
			R=randint(0,startsize-self.vie)
			if R<self.T and self.vie>0 and (cases[self.pos[0]%140][(self.pos[1]+1)%70]=='water' or randint(0,200)==0):
				Graine(self.pos[0]%140,(self.pos[1]+1)%70,self.vie-1,self.T,self.color)
				
			R=randint(0,startsize-self.vie)
			if R<self.T and self.vie>0 and (cases[self.pos[0]%140][(self.pos[1]-1)%70]=='water' or randint(0,200)==0):
				Graine(self.pos[0]%140,(self.pos[1]-1)%70,self.vie-1,self.T,self.color)
			if (self.pos[1]==67 or self.pos[1]==1)and randint(0,2)==0:
				cases[self.pos[0]%140][self.pos[1]]='water'
				continentM[self.pos[0]%140][self.pos[1]]=(0,0,0)
				
		nbgraine=nbgraine-1
		self.kill()
curseur=0
font = pygame.font.Font('freesansbold.ttf', 25)
def choosegame():
	listdir3=os.listdir('svg/')
	listdir2=[]
	for i in listdir3:
		if i[len(i)-4:]!='.png':
			listdir2.append(i)
	for i in range(0,min(len(listdir2),6)):
			T=listdir2[(i+curseur)%len(listdir2)]
			text = font.render(T, True, (0,0,0))
			textRect = text.get_rect()
			textRect.center = (700+addy, 225+i*50)
			fenetre.blit(text,textRect)
	return listdir2



def Graine(i,j,V,taille,C):
	global continents,nbgraine
	continents.add(graine(i,j,V,taille,C))
	nbgraine=nbgraine+1

# mettre si partie créée
partie_créée=1
menu_start=0
chargeur=0
playlist=[]
playlist.append('1.ogg')
playlist.append('2.ogg')
playlist.append('3.ogg')
pygame.mixer.music.set_endevent ( pygame.USEREVENT )
pygame.mixer.music.load(choice(playlist))
pygame.mixer.music.play()
CURSE=2
while menu_start==0:
	pygame.display.flip()
	mous=pygame.mouse.get_pos()
	fenetre.blit(pano,(0,0))
	fenetre.blit(load,(25,115))
	fenetre.blit(evolve,(25,15))
	fenetre.blit(pygame.image.load("fond.png"),(350,0))
	fenetre.blit(pygame.image.load("newgame.png"),(25,215))
	fenetre.blit(scoreim,(25,315))
	fenetre.blit(diff,(25,415))
	for event in pygame.event.get():
		clic=pygame.mouse.get_pressed()
		KEY=pygame.key.get_pressed()
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.USEREVENT:# each while loop
			pygame.mixer.music.load(choice(playlist))
			if musicplayed==1:
				pygame.mixer.music.play()
	for i in range(0,4):
		fenetre.blit(pygame.image.load("cliceur.png"),(225,500+i*36))
		if abs(mous[0]-225-13)<13:
			if abs(mous[1]-(500+i*36+13))<13:
				pygame.mouse.set_cursor(*pygame.cursors.diamond)
				if clic[0]==1:
					CURSE=i
	if CURSE!=10:
		fenetre.blit(pygame.image.load("cliceurok.png"),(225,500+CURSE*36))
	if abs(mous[0]-175)<150:
		if abs(mous[1]-(315+40))<40:
			pygame.mouse.set_cursor(*pygame.cursors.diamond)
			if clic[0]==1:
				fenetre.blit(pygame.image.load("bestscoremenu.png"),(350+(1050-300)//2,100))
				file1 = open("scoreliste", "rb")
				bestscore=pickle.load(file1)
				bestcreat=pickle.load(file1)
				file1.close()
				for i in range(0,10):
					text = font.render(str(bestscore[9-i])+'  '+str(bestcreat[9-i]), True, (0,0,0))
					textRect = text.get_rect()
					textRect.center = (150+350+(1050-300)//2,200+30*i)
					fenetre.blit(text,textRect)
					
				while KEY[K_RETURN]==0 and KEY[K_ESCAPE]==0:
					mous=pygame.mouse.get_pos()
					clic=pygame.mouse.get_pressed()
					for event in pygame.event.get():
						KEY=pygame.key.get_pressed()
					pygame.display.flip()
	
	if abs(mous[0]-175)<150:
		if abs(mous[1]-(115+40))<40:
			pygame.mouse.set_cursor(*pygame.cursors.diamond)
			if clic[0]==1:
				loadingscreen=pygame.image.load("menuloadgame.png")
				
				pygame.key.set_repeat()
				while KEY[K_RETURN]==0 and KEY[K_ESCAPE]==0:
					mous=pygame.mouse.get_pos()
					clic=pygame.mouse.get_pressed()
					for event in pygame.event.get():
						KEY=pygame.key.get_pressed()
						if event.type==KEYDOWN:
							if KEY[K_DOWN]:
								curseur=(curseur+1)
							if KEY[K_UP]:
								curseur=(curseur-1)
						if event.type==MOUSEBUTTONUP:
							if event.button==5:
								curseur=(curseur+1)
							if event.button==4:
								curseur=(curseur-1)
							if abs(mous[0]-(500+(1050-300)//2))<150 and abs(mous[1]-(225+50+125))<125:#
								if event.button==1:
									ululu=(mous[1]-(225+25))//50
									curseur=curseur+ululu+1
						if event.type == pygame.USEREVENT:# each while loop
							pygame.mixer.music.load(choice(playlist))
							if musicplayed==1:
								pygame.mixer.music.play()
					KEY=pygame.key.get_pressed()
					fenetre.blit(loadingscreen,(350+(1050-300)//2,100))
					fenetre.blit(pygame.image.load("valideur.png"),(240+350+(1050-300)//2,110+100))
					fenetre.blit(pygame.image.load("closeur.png"),(270+350+(1050-300)//2,100))
					addy=175
					L0=choosegame()
					pygame.display.flip()
					if KEY[K_RETURN]==1:
						chargeur=L0[(curseur)%len(L0)]
						menu_start=1
						partie_créée=0
						addy=0
						fenetre.blit(pygame.image.load("loadcircle.png"),(350+(1050-300)//2,330))
						pygame.display.flip()
					if abs(mous[1]-650)<50:
						if abs(mous[0]-(500+(1050-300)//2))<150:
							if clic[0]==1:
								blug=0
								while blug==0:
									for event in pygame.event.get():
										KEY=pygame.key.get_pressed()
									KEY=pygame.key.get_pressed()
									mous=pygame.mouse.get_pos()
									clic=pygame.mouse.get_pressed()
									deleteur=pygame.image.load("deleteur.png")	
									fenetre.blit(deleteur,(400+(1050-300)//2,250))
									pygame.display.flip()
									if abs(mous[1]-350)<40:
										if abs(mous[0]-(-50+500+(1050-300)//2))<40:
											if clic[0]==1:
												blug=1
												L_file=os.listdir('svg/')
												for qua in L_file:
													if qua[0:len(L0[(curseur)%len(L0)])]==L0[(curseur)%len(L0)]:
														os.remove('svg/'+qua)
										if abs(mous[0]-(50+500+(1050-300)//2))<40:
											if clic[0]==1:
												blug=1
					if abs(mous[1]-115)<15:
						if abs(mous[0]-(285+350+(1050-300)//2))<15:
							if clic[0]==1:
								break
								
					if abs(mous[1]-225)<15:
						if abs(mous[0]-(255+350+(1050-300)//2))<15:
							if clic[0]==1:			
								chargeur=L0[(curseur)%len(L0)]
								menu_start=1
								partie_créée=0
								addy=0
								fenetre.blit(pygame.image.load("loadcircle.png"),(350+(1050-300)//2,330))
								pygame.display.flip()
								break
								
						
	if abs(mous[0]-175)<150:
		if abs(mous[1]-(215+40))<40:
			pygame.mouse.set_cursor(*pygame.cursors.diamond)
			if clic[0]==1:
				menu_start=1
				partie_créée=1
				fenetre.blit(pygame.image.load("build.png"),(350+(1050-300)//2,330))
				pygame.display.flip()
		

q=0
pointF=[randint(0,140),randint(0,70),randint(-180,180),randint(1,2)]
pointC=[randint(0,140),randint(0,70),randint(-180,180),randint(1,2)]
pointS=[randint(0,140),randint(0,70),randint(-180,180),randint(1,2)]
pointH=[randint(0,140),randint(0,70),randint(-180,180),randint(1,2)]
addTemp=0
dicoContinent={}
dicocosXcon={}
dicosinXcon={}
dicocosYcon={}
dicosinYcon={}
dicoNcon={}
def angle_f(x1,y1,x2,y2):
	if x2!=x1:
		a=np.arctan((y2-y1)/(x2-x1))
	else:
		a=0
	if x2<x1:
		a=a+1*pi
	return a
if partie_créée==1:
	continents=pygame.sprite.LayeredUpdates()
	startsize=20
	for i in range(0,randint(7,12)):
		taille=randint(5,7)
		Graine(randint(0,140),randint(0,70),startsize,taille,(randint(0,255),randint(0,255),randint(0,255)))
	for i in range(0,randint(20,30)):
		taille=randint(1,3)
		Graine(randint(0,140),randint(0,70),startsize,taille,(randint(0,255),randint(0,255),randint(0,255)))
	
	finished=0
	
	while finished==0:
		continents.update()
		
		#print(nbgraine)
		if nbgraine==0:
			finished=1
	
	for i in range(0,140):
		for j in range(0,70):
			
			if cases[i][j]!='water' and cases[i][j]!='glace':
				MAP.blit(dico[cases[i][j]],(i*10-1,j*10-1))
				if j<8:
					MAP.blit(tundra,(i*10-1,j*10-1))
					cases[i][j]='tunda'
				if j==8:
					if randint(0,1)==1:
						MAP.blit(tundra,(i*10-1,j*10-1))
						cases[i][j]='tunda'
					
				
				if 69-j<8:
					MAP.blit(tundra,(i*10-1,j*10-1))
					cases[i][j]='tunda'
				if 69-j==8 and randint(0,1)==1:
					MAP.blit(tundra,(i*10-1,j*10-1))
					cases[i][j]='tunda'
				
			if cases[i][j]=='water':
				MAP.blit(water,(i*10-1,j*10-1))
				if i<138 and j<68 and i>0 and j>0:
					if cases[i][j+1]!='water' and cases[i+1][j]!='water' and cases[i-1][j]!='water' and cases[i][j-1]!='water':
						MAP.blit(cotes,(i*10-1,j*10-1))
						cases[i][j]='cotes'

			# if j==0 and randint(0,2)==1:
				# MAP.blit(banquise,(i*10-1,j*10-1))
				# cases[i][j]='glace'
			# if j<=3 and cases[i][j-1]=='glace'and randint(0,1)==1:# ici à changer
				# MAP.blit(banquise,(i*10-1,j*10-1))
				# cases[i][j]='glace'
			

			# if j==0 and randint(0,2)==1:
				# MAP.blit(banquise,(i*10-1,700-(j*10-1)))
				# cases[i][69-j]='glace'
			# if j<=3 and j>0 and cases[i][69-(j-1)]=='glace'and randint(0,1)==1:
				# MAP.blit(banquise,(i*10-1,700-(j*10-1)))
				# cases[i][69-j]='glace'
			
	for i in range(0,140):
		for j in range(0,70):
			if cases[i][j]!='water' and j<=69  and j>=0:
				# if (cases[i][max(j-1,0)]not in ['water','glace','cotes','glacC'] or cases[i][min(j+1,69)]not in ['water','glace','cotes','glacC'] or cases[(i+1)%140][j]not in ['water','glace','cotes','glacC'] or cases[(i-1)%140][j]not in ['water','glace','cotes','glacC']) and cases[i][j]=='glace':
					# MAP.blit(banquise,(i*10-1,j*10-1))
					# cases[i][j]='glacC'
				
				if (cases[i][max(j-1,0)]=='water' or cases[i][min(j+1,69)]=='water' or cases[(i+1)%140][j]=='water' or cases[(i-1)%140][j]=='water') and cases[i][j]!='glace':
					MAP.blit(cotes,(i*10-1,j*10-1))
					cases[i][j]='cotes'
					if randint(0,8)==0 and j<50 and j>20:
						MAP.blit(mangrove,(i*10-1,j*10-1))
						cases[i][j]='mangr'
				if ((cases[i][max(j-1,0)]!='deser' and cases[i][max(j-1,0)]!='svane') or (cases[i][min(j+1,69)]!='deser'and cases[i][min(j+1,69)]!='svane') or (cases[(i+1)%140][j]!='deser'and cases[(i+1)%140][j]!='svane') or (cases[(i-1)%140][j]!='deser'and cases[(i-1)%140][j]!='svane')) and cases[i][j]=='deser':
					MAP.blit(savane,(i*10-1,j*10-1))
					cases[i][j]='svane'
				if cases[i][j] in ['plain','svane','tunda']:
					if j<60+randint(-2,2) and j>10+randint(-2,2) :
						score=0
						if cases[i][max(j-1,0)]=='foret':
							score=score+1
						if cases[i][min(j+1,69)]=='foret':
							score=score+1
						if cases[(i-1)%140][j]=='foret':
							score=score+1
						if cases[(i+1)%140][j]=='foret':
							score=score+1
						if randint(0,4-score)<1:
							cases[i][j]='foret'
							MAP.blit(foret,(i*10-1,j*10-1))
							if (j<62 and j>58) or (j<12 and j>8):
								cases[i][j]='forbo'
								MAP.blit(foretbo,(i*10-1,j*10-1))
					if j<40+randint(-2,2) and j>30+randint(-2,2) :
						score=0
						if cases[i][max(j-1,0)]=='jungl':
							score=score+1
						if cases[i][min(j+1,69)]=='jungl':
							score=score+1
						if cases[(i-1)%140][j]=='jungl':
							score=score+1
						if cases[(i+1)%140][j]=='jungl':
							score=score+1
						if randint(0,4-score)<2:
							cases[i][j]='jungl'
							MAP.blit(jungle,(i*10-1,j*10-1))
				if cases[i][j] in ['tunda','stepe','forbo']:
					
						score=0
						if cases[i][max(j-1,0)]=='forbo':
							score=score+1
						if cases[i][min(j+1,69)]=='forbo':
							score=score+1
						if cases[(i-1)%140][j]=='forbo':
							score=score+1
						if cases[(i+1)%140][j]=='forbo':
							score=score+1
						if randint(0,4-score)<2:
							cases[i][j]='forbo'
							MAP.blit(foretbo,(i*10-1,j*10-1))
						score=0
						if cases[i][max(j-1,0)]=='stepe':
							score=score+1
						if cases[i][min(j+1,69)]=='stepe':
							score=score+1
						if cases[(i-1)%140][j]=='stepe':
							score=score+1
						if cases[(i+1)%140][j]=='stepe':
							score=score+1
						if randint(0,4-score)<1:
							cases[i][j]='stepe'
							MAP.blit(steppe,(i*10-1,j*10-1))
			if (cases[i][j]=='water' or cases[i][j]=='cotes') and j!=69:
					Cont=(0,0,0)
					score=0
					if cases[i][max(j-1,0)]=='mangr':
						score=score+3
						if continentM[i][max(j-1,0)]!=(0,0,0):
							Cont=continentM[i][max(j-1,0)]
					if cases[i][min(j+1,69)]=='mangr':
						score=score+3
						if continentM[i][min(j+1,69)]!=(0,0,0):
							Cont=continentM[i][min(j+1,69)]
					if cases[(i-1)%140][j]=='mangr':
						score=score+3
						if continentM[(i-1)%140][j]!=(0,0,0):
							Cont=continentM[(i-1)%140][j]
					if cases[(i+1)%140][j]=='mangr':
						score=score+3
						if continentM[(i+1)%140][j]!=(0,0,0):
							Cont=continentM[(i+1)%140][j]
					if cases[i][max(j-1,0)]=='cotes':
						score=score+1
						if continentM[i][max(j-1,0)]!=(0,0,0):
							Cont=continentM[i][max(j-1,0)]
					if cases[i][min(j+1,69)]=='cotes':
						score=score+1
						if continentM[i][max(j-1,0)]!=(0,0,0):
							Cont=continentM[i][max(j-1,0)]
					if cases[(i-1)%140][j]=='cotes':
						score=score+1
						if continentM[(i-1)%140][j]!=(0,0,0):
							Cont=continentM[(i-1)%140][j]
					if cases[(i+1)%140][j]=='cotes':
						score=score+1
						if continentM[(i+1)%140][j]!=(0,0,0):
							Cont=continentM[(i+1)%140][j]
					if cases[i][max(j-1,0)]=='svane':
						score=score+3
						if continentM[i][max(j-1,0)]!=(0,0,0):
							Cont=continentM[i][max(j-1,0)]
					if cases[i][min(j+1,69)]=='svane':
						score=score+3
						if continentM[i][min(j+1,69)]!=(0,0,0):
							Cont=continentM[i][min(j+1,69)]
					if cases[(i-1)%140][j]=='svane':
						score=score+3
						if continentM[(i-1)%140][j]!=(0,0,0):
							Cont=continentM[(i-1)%140][j]
					if cases[(i+1)%140][j]=='svane':
						score=score+3
						if continentM[(i+1)%140][j]!=(0,0,0):
							Cont=continentM[(i+1)%140][j]
					if randint(0,score)>2:
						cases[i][j]='mangr'
						MAP.blit(mangrove,(i*10-1,j*10-1))
						continentM[i][j]=Cont
					
						
	x=randint(0,139)
	y=randint(0,69)
	
	for i in range(0,140):
		for j in range (0,70):
			if continentM[i][j]!=(0,0,0):
				co=continentM[i][j]
				scoreM=0
				ok=0
				
				for k in [0,1,-1]:
					for l in [0,1,-1]:
						if continentM[(i+k)%140][(j+l)%70]!=co and continentM[(i+k)%140][(j+l)%70]!=(0,0,0):
							ok=1
						if cases[(i+k)%140][(j+l)%70]=='monts':
							scoreM=scoreM+1
				if randint(0,scoreM+4)>3 and ok==1:
					if cases[i][j]=='svane' or cases[i][j]=='jungl' or cases[i][j]=='deser':
						cases[i][j]='hotmt'
					else:
						if cases[i][j]=='glace' or cases[i][j]=='stepe' or cases[i][j]=='tunda':
							cases[i][j]='coldm'
						else:
							cases[i][j]='monts'
	
	
	liste=['a','e','i','u','o','y','a','e','i','u','o','ou','ai','ei','ui']
	liste2=['b','c','d','f','g','h','j','k','l','m','n','p','qu','r','s','t','v','w','x','z','b','c','d','f','g','j','k','l','m','n','p','r','s','t','v']
	if randint(0,2)==1:
		nom=choice(liste2)[0].upper()
	else:
		nom=choice(liste)[0].upper()
		nom=nom+choice(liste2)
	liste2.append('ss')
	liste2.append('tt')
	liste2.append('ll')
	for i in range(0,randint(1,3)):
		nom=nom+choice(liste)
		nom=nom+choice(liste2)
	if randint(0,1)==1:
		nom=nom+choice(liste)
	
	pygame.display.set_caption("Evolve in "+nom)
	q=0
	J=np.random.normal(0,5)+7
	K=np.random.normal(0,5)
	dicoContinent={}
	dicocosXcon={}
	dicosinXcon={}
	dicocosYcon={}
	dicosinYcon={}
	dicoNcon={}
	for i in range(0,140):
		for j in range(0,70):
			
			sco1=0
			for f1 in [1,0,-1]:
				for g1 in [1,0,-1]:
					if continentM[(i+f1)%140][(j+g1)%70]!=continentM[i][j] and abs(f1)+abs(g1)==1:
						sco1=sco1+1
			if sco1==4:
				continentM[i][j]=continentM[(i+1)%140][(j+1)%70]
					
	for i in range(0,140):
		for j in range (0,70):
			nourriture[i][j]=biomes.loc[cases[i][j]]['rssources maximales']
			humidite[i][j]=biomes.loc[cases[i][j]]['humidite']+randint(-10,10)+J
			temperature[i][j]=biomes.loc[cases[i][j]]['temperature']+randint(-2,2)+K
			if cases[i][j]=='water' or cases[i][j]=='cotes':
				temperature[i][j]=biomes.loc[cases[i][j]]['temperature']-floor(1.2*abs(34.5-j))+randint(-1,1)+8*1.2
			if cases[i][j]=='glace':
				temperature[i][j]=biomes.loc[cases[i][j]]['temperature']-floor(0.3*abs(35-j))+randint(2,4)-100
			if (continentM[i][j] in dicoContinent.keys())==False:
				liste=['a','e','i','u','o','y','a','e','i','u','o','ou','ai','ei','ui']
				liste2=['b','c','d','f','g','h','j','k','l','m','n','p','qu','r','s','t','v','w','x','z','b','c','d','f','g','j','k','l','m','n','p','r','s','t','v']
				if randint(0,2)==1:
					nomc=choice(liste2)[0].upper()
				else:
					nomc=choice(liste)[0].upper()
					nomc=nomc+choice(liste2)
				liste2.append('ss')
				liste2.append('tt')
				liste2.append('ll')
				for g in range(0,randint(1,3)):
					nomc=nomc+choice(liste)
					nomc=nomc+choice(liste2)
				if randint(0,1)==1:
					nomc=nomc+choice(liste)
				
				if continentM[i][j]!=(0,0,0):
					dicoContinent[continentM[i][j]]=nomc
					dicocosXcon[continentM[i][j]]=cos(2*pi*i/140)
					dicosinXcon[continentM[i][j]]=sin(2*pi*i/140)
					dicocosYcon[continentM[i][j]]=cos(2*pi*j/70)
					dicosinYcon[continentM[i][j]]=sin(2*pi*j/70)
					dicoNcon[continentM[i][j]]=1
			else:
				if continentM[i][j]!=(0,0,0):
					dicocosXcon[continentM[i][j]]=dicocosXcon[continentM[i][j]]+cos(2*pi*i/140)
					dicosinXcon[continentM[i][j]]=dicosinXcon[continentM[i][j]]+sin(2*pi*i/140)
					dicocosYcon[continentM[i][j]]=dicocosYcon[continentM[i][j]]+cos(2*pi*j/70)
					dicosinYcon[continentM[i][j]]=dicosinYcon[continentM[i][j]]+sin(2*pi*j/70)
					dicoNcon[continentM[i][j]]=dicoNcon[continentM[i][j]]+1
			
	pointF=[randint(0,140),randint(0,70),randint(-180,180),randint(1,2)]
	pointC=[randint(0,140),randint(0,70),randint(-180,180),randint(1,2)]
	pointS=[randint(0,140),randint(0,70),randint(-180,180),randint(1,2)]
	pointH=[randint(0,140),randint(0,70),randint(-180,180),randint(1,2)]
	temperature3=temperature.copy()
	for i in range(0,140):
		for j in range (0,70):
			if cases[i][j] in ['plain','tunda','svane','plai2','deser','jungl','foret','stepe','forbo']:
				Tt=0
				st=0
				if cases[(i+1)%140][j] in ['plain','tunda','svane','plai2','deser','jungl','foret','stepe','forbo']:
					Tt=Tt+1
					st=st+temperature[(i+1)%140][j]
				if cases[(i-1)%140][j] in ['plain','tunda','svane','plai2','deser','jungl','foret','stepe','forbo']:
					Tt=Tt+1
					st=st+temperature[(i-1)%140][j]
				if cases[i][(j+1)%70] in ['plain','tunda','svane','plai2','deser','jungl','foret','stepe','forbo']:
					Tt=Tt+1
					st=st+temperature[i][(j+1)%70]
				if cases[i][(j-1)%70] in ['plain','tunda','svane','plai2','deser','jungl','foret','stepe','forbo']:
					Tt=Tt+1
					st=st+temperature[i][(j-1)%70]
				if Tt!=0: 
					temperature3[i][j]=0.5*temperature[i][j]+0.5*st/Tt
	temperature=temperature3	
	for k_k in range(0,randint(4,8)):
		xk=randint(0,139)
		yk=randint(0,69)
		while cases[xk][yk]!='water':
			xk=randint(0,139)
			yk=randint(0,69)
		listedevolcans.append([xk,yk])
		cases[xk][yk]='volca'
		temperature[xk][yk]=biomes.loc['volca']['temperature']
	
# jusque là pour la creation d'un monde
dicoXcon={}
dicoYcon={}
dicoVcon={}
for i in dicoContinent.keys():
	dicoXcon[i]=int(140*(angle_f(0,0,dicocosXcon[i]/dicoNcon[i],dicosinXcon[i]/dicoNcon[i])%(2*pi))/(2*pi))
	dicoYcon[i]=int(70*(angle_f(0,0,dicocosYcon[i]/dicoNcon[i],dicosinYcon[i]/dicoNcon[i])%(2*pi))/(2*pi))
	vcx=randint(-1,1)
	vcy=randint(-1,1)
	while abs(vcx)+abs(vcy)==0:
		vcx=randint(-1,1)
		vcy=randint(-1,1)
		
	dicoVcon[i]=(vcx,vcy)
	

def changecondition(i,j):
	global humidite2, temperature2, cases
	if cases[i][j]=='water' :
		if temperature2[i][j]<-12:
			cases[i][j]='glace'
		if temperature2[i][j]<0 and temperature2[i][j]>=-12:
			cases[i][j]='coldw'
		if temperature2[i][j]>18:
			cases[i][j]='tropw'
			
	else:
		
		if cases[i][j]=='glace':
			if temperature2[i][j]>=-12 and temperature2[i][j]<0:
				cases[i][j]='coldw'
			if temperature2[i][j]>=-12 and temperature2[i][j]>0:
				cases[i][j]='water'
		
		else:
			if cases[i][j]!='glacC' and cases[i][j]!='cotes' and cases[i][j]!='coldw' and cases[i][j]!='tropw' and cases[i][j]!='mangr' and cases[i][j]!='hotmt' and cases[i][j]!='coldm' and cases[i][j]!='monts':
				if temperature2[i][j]<5:
					if humidite2[i][j]<35:
						cases[i][j]='stepe'
					if humidite2[i][j]>65:
						cases[i][j]='forbo'
					if humidite2[i][j]<=65 and humidite2[i][j]>=35:
						cases[i][j]='tunda'
				if temperature2[i][j]>28:
					if humidite2[i][j]<35:
						cases[i][j]='deser'
					if humidite2[i][j]>65:
						cases[i][j]='jungle'
					if humidite2[i][j]<=65 and humidite2[i][j]>=35:
						cases[i][j]='svane'
				if temperature2[i][j]<=28 and temperature2[i][j]>=5:
					if humidite2[i][j]<35:
						cases[i][j]='plai2'
					if humidite2[i][j]>65:
						cases[i][j]='foret'
					if humidite2[i][j]<=65 and humidite2[i][j]>=35:
						cases[i][j]='plain'
	if cases[i][j]=='cotes' :
		if temperature2[i][j]<-6:
			cases[i][j]='glacC'
		if temperature2[i][j]>18:
			cases[i][j]='mangr'
	if cases[i][j]=='glacC':
		if temperature2[i][j]>=-6:
			cases[i][j]='cotes'
	if cases[i][j]=='coldw' :
		if temperature2[i][j]<-12:
			cases[i][j]='glace'
		if temperature2[i][j]>0:
			cases[i][j]='water'
	if cases[i][j]=='tropw' :
		if temperature2[i][j]<18:
			cases[i][j]='water'
	if cases[i][j]=='mangr' :
		if temperature2[i][j]<18:
			cases[i][j]='cotes'
	if cases[i][j]=='monts' :
		if temperature2[i][j]>15:
			cases[i][j]='hotmt'
		if temperature2[i][j]<0:
			cases[i][j]='coldm'
	if cases[i][j]=='coldm' :
		if temperature2[i][j]>0:
			cases[i][j]='monts'
	if cases[i][j]=='hotmt' :
		if temperature2[i][j]<15:
			cases[i][j]='monts'
ageglaciaire=0
AG=1
RG=1
def mixImage(im1,im2,t):
	immixed=pygame.Surface((12,12),pygame.SRCALPHA, 32)
	for i in range(0,12):
		for j in range(0,12):
			c1=im1.get_at((i,j))
			c2=im2.get_at((i,j))
			C=[0,0,0,0]
			for g in range(0,4):
				C[g]=t*c2[g]+(1-t)*c1[g]
			immixed.set_at((i,j),tuple(C))
	return immixed
	
def whiteflash(t):
	flash=pygame.Surface((700,700),pygame.SRCALPHA, 32)
	color=int(min(255*exp(-log(t)**2)/t,255))
	flash.fill((255,255,255,color))
	return flash

def changecondvolcan(case,T,H):
	if T<5:
		if H<35:
			case_return='stepe'
		if H>65:
			case_return='forbo'
		if H<=65 and H>=35:
			case_return='tunda'
	if T>28:
		if H<35:
			case_return='deser'
		if H>65:
			case_return='jungle'
		if H<=65 and H>=35:
			case_return='svane'
	if T<=28 and T>=5:
		if H<35:
			case_return='plai2'
		if H>65:
			case_return='foret'
		if H<=65 and H>=35:
			case_return='plain'
	return case_return


def changecondmeteor(case,T):
	case2=case
	if case in ['water','coldw','tropw','glace'] :
		if T<-12:
			case2='glace'
		if T<0 and T>-12:
			case2='coldw'
		if T<18 and T>0:
			case2='water'	
		if T>18:
			case2='tropw'
	if case in ['cotes','mangr','glacC'] :
		if T<-6:
			case2='glacC'
		if T>18:
			case2='mangr'
		if T<18 and T>-6:
			case2='cotes'
	return case2

def chute_meteor(x,y):
	global cases,rayonm,meteorMAP
	if tour==meteor_date:
		rayonm=max(int(np.random.normal(4,1)),3)
		for i in range(0,2*rayonm+1):
			for j in range(0,2*rayonm+1):
				meteorMAP[(i-rayonm+x)%140][min(max(j-rayonm+y,0),69)]='water'
				if cases[(i-rayonm+x)%140][min(max(j-rayonm+y,0),69)]=='meteo':
					meteorMAP[(i-rayonm+x)%140][min(max(j-rayonm+y,0),69)]='monts'
					
	for i in range(0,2*rayonm+1):
		for j in range(0,2*rayonm+1):
			dx=i-rayonm
			dy=j-rayonm
			if -0.5+random()+(dx**2+dy**2)**0.5<=min(rayonm,tour-meteor_date) and (dx**2+dy**2)!=0 :
				if (tour-meteor_date)<rayonm+1:
					cases[(i-rayonm+x)%140][min(max(j-rayonm+y,0),69)]='crate'
					temperature[(i-rayonm+x)%140][min(max(j-rayonm+y,0),69)]=biomes.loc['crate']['temperature']
			if cases[(i-rayonm+x)%140][min(max(j-rayonm+y,0),69)]=='crate':
				if (tour-meteor_date)==rayonm+1 and ((cases[(i-rayonm+x+1)%140][min(max(j-rayonm+y,0),69)]not in ['crate','meteo']) or (cases[(i-rayonm+x-1)%140][min(max(j-rayonm+y,0),69)]not in ['crate','meteo'])or (cases[(i-rayonm+x)%140][min(max(j-rayonm+y+1,0),69)]not in ['crate','meteo'])or (cases[(i-rayonm+x)%140][min(max(j-rayonm+y-1,0),69)]not in ['crate','meteo'])):
					meteorMAP[(i-rayonm+x)%140][min(max(j-rayonm+y,0),69)]='cotes'
				else:
					continentM[(i-rayonm+x)%140][min(max(j-rayonm+y,0),69)]=(0,0,0)
					
	if tour==meteor_date+rayonm+1:
		for i in range(0,2*rayonm+1):
			for j in range(0,2*rayonm+1):
				T=biomes.loc[meteorMAP[(i-rayonm+x)%140][min(max(j-rayonm+y,0),69)]]['temperature']-floor(1*abs(35-min(max(j-rayonm+y,0),69)))+randint(-1,1)+8
				meteorMAP[(i-rayonm+x)%140][min(max(j-rayonm+y,0),69)]=changecondmeteor(meteorMAP[(i-rayonm+x)%140][min(max(j-rayonm+y,0),69)],T)
				
	if tour>meteor_date+rayonm and tour<meteor_date+20:
		for i in range(0,2*rayonm+1):
			for j in range(0,2*rayonm+1):
				if cases[(i-rayonm+x)%140][min(max(j-rayonm+y,0),69)]=='crate' :
					I=(i-rayonm+x)%140
					J=min(max(j-rayonm+y,0),69)
					d1=min(abs(pointS[0]-I),140-abs(pointS[0]-I))
					d2=pointS[1]-J
					d3=min(abs(pointH[0]-I),140-abs(pointH[0]-I))
					d4=pointH[1]-J
					HH=biomes.loc[meteorMAP[(i-rayonm+x)%140][min(max(j-rayonm+y,0),69)]]['humidite']
					humcase=HH-20*exp(-(((d1)**2)+((d2)**2))/(2*100))+20*exp(-(((d3)**2)+((d4)**2))/(2*36))
					
					d1=min(abs(pointF[0]-I),140-abs(pointF[0]-I))
					d2=pointF[1]-J
					d3=min(abs(pointC[0]-I),140-abs(pointC[0]-I))
					d4=pointC[1]-J
					if meteorMAP[(i-rayonm+x)%140][min(max(j-rayonm+y,0),69)] in ['cotes','glace','mangr','glacC','water','coldw','tropw','glace']:
						TT=biomes.loc['water']['temperature']
						tempcase=TT-AG*15*exp(-(((d1)**2)+((d2)**2))/(2*100))+RG*15*exp(-(((d3)**2)+((d4)**2))/(2*36))+addTemp
						tempcase=tempcase-floor(1*abs(35-min(max(j-rayonm+y,0),69)))+8
						meteorMAP[(i-rayonm+x)%140][min(max(j-rayonm+y,0),69)]=changecondmeteor(meteorMAP[(i-rayonm+x)%140][min(max(j-rayonm+y,0),69)],tempcase)
					
	if tour==meteor_date+20:
		for i in range(0,2*rayonm+1):
			for j in range(0,2*rayonm+1):
				if cases[(i-rayonm+x)%140][min(max(j-rayonm+y,0),69)]=='crate' or cases[(i-rayonm+x)%140][min(max(j-rayonm+y,0),69)]=='meteo':
					cases[(i-rayonm+x)%140][min(max(j-rayonm+y,0),69)]=meteorMAP[(i-rayonm+x)%140][min(max(j-rayonm+y,0),69)]
					temperature[(i-rayonm+x)%140][min(max(j-rayonm+y,0),69)]=biomes.loc['water']['temperature']-floor(1*abs(35-min(max(j-rayonm+y,0),69)))+8
					

def erupt_volcan(x,y):
	global cases,rayon,volcanMAP,temperature
	if tour==volcan_date:
		rayon=max(int(np.random.normal(4,1)),3)
		for i in range(0,2*rayon+1):
			for j in range(0,2*rayon+1):
				volcanMAP[(i-rayon+x)%140][min(max(j-rayon+y,0),69)]='plain'
	for i in range(0,2*rayon+1):
		for j in range(0,2*rayon+1):
			dx=i-rayon
			dy=j-rayon
			if -0.5+random()+(dx**2+dy**2)**0.5<=min(rayon,tour-volcan_date) and (dx**2+dy**2)!=0 :
				if (tour-volcan_date)<rayon+1:
					cases[(i-rayon+x)%140][min(max(j-rayon+y,0),69)]='magma'
					temperature[(i-rayon+x)%140][min(max(j-rayon+y,0),69)]=biomes.loc['magma']['temperature']
					if continentM[x][y]!=(0,0,0):
						if continentM[(i-rayon+x)%140][min(max(j-rayon+y,0),69)]==(0,0,0):
							continentM[(i-rayon+x)%140][min(max(j-rayon+y,0),69)]=continentM[x][y]
						
							
						
			if cases[(i-rayon+x)%140][min(max(j-rayon+y,0),69)]=='magma':
				if (tour-volcan_date)==rayon+1 and ((cases[(i-rayon+x+1)%140][min(max(j-rayon+y,0),69)] in ['water','coldw','tropw','glace']) or (cases[(i-rayon+x-1)%140][min(max(j-rayon+y,0),69)]in ['water','coldw','tropw','glace'])or (cases[(i-rayon+x)%140][min(max(j-rayon+y+1,0),69)] in ['water','coldw','tropw','glace'])or (cases[(i-rayon+x)%140][min(max(j-rayon+y-1,0),69)] in ['water','coldw','tropw','glace'])):
					volcanMAP[(i-rayon+x)%140][min(max(j-rayon+y,0),69)]='cotes'	
					
	if tour==volcan_date+rayon+1:
		
		for j in range(0,2*rayon+1):# roll les volcans
			Komp=1
			meant=0    
			meanhum=0
			for g in range(0,139):
				if cases[g][min(max(j-rayon+y,0),69)] not in ['monts','coldm','hotmt','water','coldw','tropw','glace','crate','meteo','volca','magma','cotes','mangr']:
					Komp=Komp+1
					meant=meant+temperature[g][min(max(j-rayon+y,0),69)]
					meanhum=meanhum+humidite[g][min(max(j-rayon+y,0),69)]
			meant=meant/Komp
			meanhum=meanhum/Komp
			for i in range(0,2*rayon+1):
				if cases[(i-rayon+x)%140][min(max(j-rayon+y,0),69)]=='magma' and volcanMAP[(i-rayon+x)%140][min(max(j-rayon+y,0),69)]!='cotes':
					humcase=meanhum+randint(-10,10)
					tempcase=meant+randint(-5,5)
					temperature[(i-rayon+x)%140][min(max(j-rayon+y,0),69)]=tempcase
					humidite[(i-rayon+x)%140][min(max(j-rayon+y,0),69)]=humcase
					volcanMAP[(i-rayon+x)%140][min(max(j-rayon+y,0),69)]=changecondvolcan(volcanMAP[(i-rayon+x)%140][min(max(j-rayon+y,0),69)],tempcase,humcase)
				if cases[(i-rayon+x)%140][min(max(j-rayon+y,0),69)]=='magma' and volcanMAP[(i-rayon+x)%140][min(max(j-rayon+y,0),69)]=='cotes':
					tempcase=biomes.loc['cotes']['temperature']-floor(1*abs(35-min(max(j-rayon+y,0),69)))+randint(-1,1)+8
					volcanMAP[(i-rayon+x)%140][min(max(j-rayon+y,0),69)]=changecondmeteor(volcanMAP[(i-rayon+x)%140][min(max(j-rayon+y,0),69)],tempcase)
					
					
	if tour>volcan_date+rayon and tour<volcan_date+20:
		for i in range(0,2*rayon+1):
			for j in range(0,2*rayon+1):
				if cases[(i-rayon+x)%140][min(max(j-rayon+y,0),69)]=='magma' :
					I=(i-rayon+x)%140
					J=min(max(j-rayon+y,0),69)
					d1=min(abs(pointS[0]-I),140-abs(pointS[0]-I))
					d2=pointS[1]-J
					d3=min(abs(pointH[0]-I),140-abs(pointH[0]-I))
					d4=pointH[1]-J
					HH=humidite[I][J]#biomes.loc[volcanMAP[(i-rayon+x)%140][min(max(j-rayon+y,0),69)]]['humidite']
					humcase=HH-20*exp(-(((d1)**2)+((d2)**2))/(2*100))+20*exp(-(((d3)**2)+((d4)**2))/(2*36))
					
					d1=min(abs(pointF[0]-I),140-abs(pointF[0]-I))
					d2=pointF[1]-J
					d3=min(abs(pointC[0]-I),140-abs(pointC[0]-I))
					d4=pointC[1]-J
					TT=temperature[I][J]#biomes.loc[volcanMAP[(i-rayon+x)%140][min(max(j-rayon+y,0),69)]]['temperature']
					tempcase=TT-AG*15*exp(-(((d1)**2)+((d2)**2))/(2*100))+RG*15*exp(-(((d3)**2)+((d4)**2))/(2*36))+addTemp
					if volcanMAP[(i-rayon+x)%140][min(max(j-rayon+y,0),69)]not in ['cotes','glace','mangr','glacC']:
						volcanMAP[(i-rayon+x)%140][min(max(j-rayon+y,0),69)]=changecondvolcan(volcanMAP[(i-rayon+x)%140][min(max(j-rayon+y,0),69)],tempcase,humcase)
					if volcanMAP[(i-rayon+x)%140][min(max(j-rayon+y,0),69)] in ['cotes','glace','mangr','glacC']:
						TT=biomes.loc['cotes']['temperature']
						tempcase=TT-AG*15*exp(-(((d1)**2)+((d2)**2))/(2*100))+RG*15*exp(-(((d3)**2)+((d4)**2))/(2*36))+addTemp
						tempcase=tempcase-floor(1*abs(35-min(max(j-rayon+y,0),69)))+8
						volcanMAP[(i-rayon+x)%140][min(max(j-rayon+y,0),69)]=changecondmeteor(volcanMAP[(i-rayon+x)%140][min(max(j-rayon+y,0),69)],tempcase)
						
		
					
	if tour==volcan_date+20:
		for j in range(0,2*rayon+1):
			for i in range(0,2*rayon+1):
				if cases[(i-rayon+x)%140][min(max(j-rayon+y,0),69)]=='magma':
					cases[(i-rayon+x)%140][min(max(j-rayon+y,0),69)]=volcanMAP[(i-rayon+x)%140][min(max(j-rayon+y,0),69)]
					if cases[(i-rayon+x)%140][min(max(j-rayon+y,0),69)]in ['cotes','glace','mangr','glacC']:
						temperature[(i-rayon+x)%140][min(max(j-rayon+y,0),69)]=biomes.loc['cotes']['temperature']-floor(1*abs(35-min(max(j-rayon+y,0),69)))+randint(-1,1)+8
						humidite[(i-rayon+x)%140][min(max(j-rayon+y,0),69)]=biomes.loc[cases[(i-rayon+x)%140][min(max(j-rayon+y,0),69)]]['humidite']


def moveCont(col,V):
	global continentM,humidite,temperature,cases,dicoXcon,dicoVcon,especes,xs,ys,dicocosXcon,dicosinXcon,dicosinYcon,dicocosXcon,dicoNcon
	moveurC=np.empty((140,70),dtype=object)
	for i in range(0,140):
		for j in range(0,70):
			moveurC[i][j]=(0,0,0)
	moveurH=np.full((140,70),0)
	moveurT=np.full((140,70),0)
	moveurbiomes=np.full((140,70),'aaaaa')
	copy_cont=continentM.copy()
	JM=0
	Jm=69
	for j in range(0,70):
		for i in range(0,140):
			if col==copy_cont[i][j] :
				JM=max(JM,j)
				Jm=min(Jm,j)
				if cases[i][j]!='volca':
					moveurC[i][j]=continentM[i][j]
					moveurH[i][j]=humidite[i][j]
					moveurT[i][j]=temperature[i][j]
					moveurbiomes[i][j]=cases[i][j]
					continentM[i][j]=(0,0,0)
					humidite[i][j]=100
					temperature[i][j]=biomes.loc['water']['temperature']-floor(1*abs(35-min(max(j,0),69)))+randint(-1,1)+8
					cases[i][j]='water'
				else:
					moveurC[i][j]=continentM[i][j]
					moveurH[i][j]=humidite[i][j]
					moveurT[i][j]=temperature[i][j]
					if randint(0,2)==0:
						moveurbiomes[i][j]='monts'
						continentM[i][j]=(0,0,0)
						humidite[i][j]=100
						temperature[i][j]=biomes.loc['monts']['temperature']
					else:
						moveurbiomes[i][j]='plain'
						continentM[i][j]=(0,0,0)
						humidite[i][j]=50
						temperature[i][j]=biomes.loc['plain']['temperature']
	if Jm<=1 and V[1]==-1:
		dicoVcon[col]=(dicoVcon[col][0],1)
	if JM>=68 and V[1]==1:
		dicoVcon[col]=(dicoVcon[col][0],-1)
				
	moveurC=np.roll(moveurC,V[0],axis=0)
	moveurH=np.roll(moveurH,V[0],axis=0)
	moveurT=np.roll(moveurT,V[0],axis=0)
	moveurbiomes=np.roll(moveurbiomes,V[0],axis=0)
	moveurC=np.roll(moveurC,V[1],axis=1)
	moveurH=np.roll(moveurH,V[1],axis=1)
	moveurT=np.roll(moveurT,V[1],axis=1)
	moveurbiomes=np.roll(moveurbiomes,V[1],axis=1)
	
	for j in especes.iterrows():
		if continentM[especes.at[j[0],'X']][especes.at[j[0],'Y']]==col or moveurC[especes.at[j[0],'X']][especes.at[j[0],'Y']]==col:
			especes.at[j[0],'X']=(especes.at[j[0],'X']+V[0])%140
			especes.at[j[0],'Y']=(especes.at[j[0],'Y']+V[1])%70
			if j[0]=='monEspece':
				xs=(xs+V[0])%140	
				ys=(ys+V[1])%70		
			
	for j in range(0,70):
		meant=LISTEmeant[j]
		meanhum=LISTEmeanhum[j]
		Komp=0
		meanTC=0
		for g in range(0,140):
			if col==moveurC[g][j] and moveurbiomes[g][j]not in ['monts','coldm','hotmt','water','coldw','tropw','glace','crate','meteo','volca','magma','cotes','mangr','glacC']:
				Komp=Komp+1
				meanTC=meanTC+moveurT[g][j]
		if Komp!=0:
			meanTC=meanTC/Komp
				
		for i in range(0,140):
			if col==moveurC[i][j]:
				if moveurbiomes[i][j] not in ['monts','coldm','hotmt','water','coldw','tropw','glace','crate','meteo','volca','magma','cotes','mangr','glacC']:
					humidite[i][j]=moveurH[i][j]
					temperature[i][j]=moveurT[i][j]+(LISTEmeant[j]-LISTEmeant[(j-V[1])%70])
					
				if cases[i][j]!='volca':
					cases[i][j]=moveurbiomes[i][j]
				
				if cases[i][j]=='monts' and continentM[i][j]!=(0,0,0) and randint(0,4)==0:
					cases[i][j]='mangr'
				if cases[i][j]!='volca' and continentM[i][j]!=(0,0,0) and randint(0,4)==0:
					cases[i][j]='monts'
				
				
				if cases[i][j] in ['mangr','glacC','cotes'] and continentM[i][j]!=(0,0,0):
					cases[i][j]='plain'
					temperature[i][j]=meant+randint(-1,1)
					humidite[i][j]=meanhum+randint(-5,5)
					if randint(0,4)==0:
						cases[i][j]='monts'
						temperature[i][j]=temperature[i][j]-15
				
	for i in range(0,140):
		for j in range(0,70):
			if col==moveurC[i][j]:
				continentM[i][j]=moveurC[i][j]
	for i in range(0,140):
		for j in range(0,70):
			if cases[i][j] not in ['volca','mangr','glacC','cotes','water','coldw','tropw','glace'] :
				for f in [1,0,-1]:
					for g in [1,0,-1]:
						if cases[(i+f)%140][(j+g)%70] in ['water','coldw','tropw','glace'] and abs(f)+abs(g)==1:
							cases[(i+f)%140][(j+g)%70]='cotes'
							temperature[(i+f)%140][(j+g)%70]=biomes.loc['cotes']['temperature']-floor(1*abs(35-min(max(j,0),69)))+randint(-1,1)+8
							continentM[(i+f)%140][(j+g)%70]=continentM[i][j]
	for i in dicoContinent.keys():
		dicocosXcon[i]=0
		dicosinXcon[i]=0
		dicocosYcon[i]=0
		dicosinYcon[i]=0
		dicoNcon[i]=0
		
	for i in range(0,140):
		for j in range(0,70):
			if continentM[i][j]!=(0,0,0):
				dicocosXcon[continentM[i][j]]=dicocosXcon[continentM[i][j]]+cos(2*pi*i/140)
				dicosinXcon[continentM[i][j]]=dicosinXcon[continentM[i][j]]+sin(2*pi*i/140)
				dicocosYcon[continentM[i][j]]=dicocosYcon[continentM[i][j]]+cos(2*pi*j/70)
				dicosinYcon[continentM[i][j]]=dicosinYcon[continentM[i][j]]+sin(2*pi*j/70)
				dicoNcon[continentM[i][j]]=dicoNcon[continentM[i][j]]+1
	for i in dicoContinent.keys():
		if dicoNcon[i]!=0:
			dicoXcon[i]=int(140*(angle_f(0,0,dicocosXcon[i]/dicoNcon[i],dicosinXcon[i]/dicoNcon[i])%(2*pi))/(2*pi))
			dicoYcon[i]=int(70*(angle_f(0,0,dicocosYcon[i]/dicoNcon[i],dicosinYcon[i]/dicoNcon[i])%(2*pi))/(2*pi))
				
	# rebondir les uns sur les autres pas trop
	# svg vitesse cont date mvt et meanhum et meant
		
def createMAP():
	global MAP,listedevolcans,temperature2,temperature,humidite,humidite2,cases
	listedevolcans=[]
	listedemeteor=[]
	for i in range(0,140):
		for j in range(0,70):
			d1=min(abs(pointF[0]-i),140-abs(pointF[0]-i))
			d2=pointF[1]-j
			d3=min(abs(pointC[0]-i),140-abs(pointC[0]-i))
			d4=pointC[1]-j
			temperature2[i][j]=temperature[i][j]-AG*15*exp(-(((d1)**2)+((d2)**2))/(2*100))+RG*15*exp(-(((d3)**2)+((d4)**2))/(2*36))+addTemp
			d1=min(abs(pointS[0]-i),140-abs(pointS[0]-i))
			d2=pointS[1]-j
			d3=min(abs(pointH[0]-i),140-abs(pointH[0]-i))
			d4=pointH[1]-j
			humidite2[i][j]=humidite[i][j]-20*exp(-(((d1)**2)+((d2)**2))/(2*100))+20*exp(-(((d3)**2)+((d4)**2))/(2*36))
			
			if nourriture[i][j]<500:
				nourriture[i][j]=min(500,nourriture[i][j]+5)
			
			if cases[i][j]in changebiome:
				changecondition(i,j)
			
			
			MAP.blit(dico[cases[i][j]],(i*10-1,j*10-1))
			
			if cases[i][j]=='crate' or cases[i][j]=='meteo':
				if (tour-meteor_date)>=rayonm+1 and (tour-meteor_date)<=20:
					if meteorMAP[i][j]!='_____':
						Image1=mixImage(dico[cases[i][j]],dico[meteorMAP[i][j]],max((tour-meteor_date-5)/15,0))
						MAP.blit(Image1,(i*10-1,j*10-1))
			if cases[i][j]=='magma':
				if (tour-volcan_date)>=rayonm+1 and (tour-volcan_date)<=20:
					if volcanMAP[i][j]!='_____':
						Image1=mixImage(dico[cases[i][j]],dico[volcanMAP[i][j]],max((tour-volcan_date-5)/15,0))
						MAP.blit(Image1,(i*10-1,j*10-1))
			
			if abs(i-xs)%139<2 and abs(j-ys)<2:
				brdG[i][j]=1
			for h1 in range(0,len(Xl)):
				if abs(i-Xl[h1])%139<1 and abs(j-Yl[h1])<1:
					brdG[i][j]=1
				if showworld==1:
					MAP.blit(US2,(Xl[h1]*10+2,Yl[h1]*10+2))
			if cases[i][j]=='volca':
				listedevolcans.append([i,j])# modifier qd roll
			if cases[i][j]=='meteo':
				listedemetor.append([i,j])
			if showtemp==1:
				a=temperature2[i][j]+20
				b=min(a*4,255)
				if b<0:
					b=0
				c=max(255-a*3,0)
				if c>255:
					c=255
				point.fill((b,0,c))
				MAP.blit(point,(i*10,j*10))
				if i==floor(pointC[0]) and j==floor(pointC[1]):
					marker2.fill((0,0,0))
					marker.fill((255,0,0))
				if i==floor(pointF[0]) and j==floor(pointF[1]):
					marker2.fill((0,0,0))
					marker.fill((0,0,255))
			if showhum==1:
				a=humidite2[i][j]*0.2
				
				b=min(floor((a**2)),255)
				if b<0:
					b=0
				c=max(floor(255-(a**2))-20,0)
				if c>255:
					c=255
				point.fill((c,b,c))
				MAP.blit(point,(i*10,j*10))
			if showCont==1:
				if continentM[i][j]!=(0,0,0):
					point.fill(continentM[i][j])
				else:
					point.fill((0,10,100))
				MAP.blit(point,(i*10,j*10))
	if showCont==1:
		font = pygame.font.Font('freesansbold.ttf', 14)
		for i in dicoContinent.keys():
			if i[0]+i[1]+i[2]<255*1.5:
				text = font.render(dicoContinent[i], True, (255,255,255))
			else:
				text = font.render(dicoContinent[i], True, (0,0,0))
			textRect = text.get_rect()
			if dicoNcon[i]!=0:
				textRect.center = (10*dicoXcon[i], 10*dicoYcon[i])
				MAP.blit(text,textRect)
		font = pygame.font.Font('freesansbold.ttf', 25)
	for i in range(0,140):
		for j in range(0,70):
			if brdG[i][j]==0:
				MAP.blit(nuage,(i*10-4,j*10-4))
				
	font = pygame.font.Font('freesansbold.ttf', 14)
	if mission_en_cours.type_ret()==2 and showCont==1:
		i=mission_en_cours.col_ret()
		if i[0]+i[1]+i[2]<255*1.5:
			text = font.render(dicoContinent[i], True, (255,255,255))
		else:
			text = font.render(dicoContinent[i], True, (0,0,0))
		textRect = text.get_rect()
		if dicoNcon[i]!=0:
			textRect.center = (10*dicoXcon[i], 10*dicoYcon[i])
			MAP.blit(text,textRect)
		font = pygame.font.Font('freesansbold.ttf', 25)
			
	if showtemp==1:
		MAP.blit(ofroid,(floor(pointF[0])*10,floor(pointF[1])*10))
		MAP.blit(ochaud,(floor(pointC[0])*10,floor(pointC[1])*10))
	if showhum==1:
		MAP.blit(ohumide,(floor(pointH[0])*10,floor(pointH[1])*10))
		MAP.blit(osec,(floor(pointS[0])*10,floor(pointS[1])*10))

pT=0
Tm=0
Hm=0
if partie_créée==1:
	for i in range(0,140):
		for j in range(0,70):
			if cases[i][j] in ['water','cotes','glace','glacC','mangr','coldw','tropw']:
				pT=pT+1
			Tm=temperature[i][j]+Tm
			Hm=humidite[i][j]+Hm
	print(pT/(14*7),Tm/(140*70)+10, Hm/(140*70))

def worldparam():
	pT=0
	Tm=0
	Hm=0
	for i in range(0,140):
		for j in range(0,70):
			if cases[i][j] not in ['water','cotes','glace','glacC','mangr','coldw','tropw']:
				pT=pT+1
			Tm=temperature2[i][j]+Tm
			Hm=humidite2[i][j]+Hm
	return (pT/(14*7),Tm/(140*70)+10, Hm/(140*70))
	

point=pygame.Surface((10,10),pygame.SRCALPHA, 32)
marker2=pygame.Surface((12,12),pygame.SRCALPHA, 32)
marker=pygame.Surface((10,10),pygame.SRCALPHA, 32)
vue=pygame.Surface((70,70),pygame.SRCALPHA, 32)
tuto_step=0

tutotext=['Welcome in Evolve, the goal of this game is to make your group of creatures survive and evolve in a constantly changing world. First you can name your creature. Evolve is a turn based game, each turn is a step in the time where your group of creatures and its environment may change, you thus have to carefully guide your group to adapted biomes. Click on next.',
'To survive you must keep your population high enough at each turn. Your population naturally grows if the case on which you move contains enough food and that you are well adapted to this environment. By moving your mouse above cases adjacent to your creature you can see if the population will grow. The case is highlighted in green if the population will rise and red else. Click on next.'
,'As you are not adapted to any biome for now the adjacent cases are orange or red, do not worry, your creature will adapt to this sea biome quickly. Please click on an adjacent case to go to the next turn, you cannot stay on the same case two turns in a row. You can see that new cases have been revealed when you moved, exploration of the world is also important in Evolve. Click on next.'
]

def Tutoriel(t_step):
	fenetre.blit(tuto,(350,400))
	line=tutotext[t_step].split()
	x=0
	y=0
	font = pygame.font.Font('freesansbold.ttf', 18)
	for j,i in enumerate(line):
		text = font.render(i, True, (0,0,0))
		fenetre.blit(text,(x+350+45,y+400+90))
		x=x+text.get_width()
		x=x+8
		t=font.render(line[(j+1)%len(line)], True, (0,0,0))
		if x+t.get_width()>600:
			x=0
			y=y+20
	if t_step==1:
		fenetre.blit(pygame.transform.flip(tutoF,1,0),(950,150))


def menu():
	fenetre.blit(pano,(0,0))
	fenetre.blit(pano,(1050,0))
	fenetre.blit(evolve,(25,15))
	fenetre.blit(save,(25,115))
	fenetre.blit(load,(25,215))
	fenetre.blit(worldmap,(25,315))
	fenetre.blit(heatmap,(25,415))
	fenetre.blit(humiditymap,(25,515))
	fenetre.blit(boutong,(25,615))
	fenetre.blit(boutonV,(1075,115))
	fenetre.blit(creature,(1075,15))
	fenetre.blit(tree,(1075,315))
	if musicplayed==1:
		fenetre.blit(pygame.image.load('sono.png'),(1030,0))
	else:
		fenetre.blit(pygame.image.load('sonox.png'),(1030,0))
	if especes.at['monEspece','pop']<700:
		fenetre.blit(splitog,(1075,215))
	else:
		fenetre.blit(splito,(1075,215))
	text = font.render('population : '+str(especes.at['monEspece','pop']), True, (0,0,0))
	textRect = text.get_rect()
	textRect.center = (1225, 155)
	fenetre.blit(text,textRect)
	if tuto_step<len(tutotext):
		Tutoriel(tuto_step)

def selector(x,y,specie):
	BIO=caracterebiome.loc[cases[x][y]]
	Manip=especes.loc[specie]
	compt=-1
	desadapt=0
	for k in Manip:
		compt=compt+1
		if compt>2 and compt<6:
			desadapt=desadapt+abs(k-BIO[compt-3])
	
	niam2=(nourriture[x][y]-max(0,especes.at[specie,'pop']-500))/5000
	
	return -1*(5*niam2-desadapt)
machD=0
machDz=0
def Desadapteur(biome,specie):
	BIO=caracterebiome.loc[biome]
	Manip=especes.loc[specie]
	compt=-1
	desadapt=0
	for k in Manip:
		compt=compt+1
		if compt>2 and compt<6:
			desadapt=desadapt+abs(k-BIO[compt-3])
	
	
	
	return desadapt




def changecolor(x,c,mask):
	u=[]
	for i in range(0,3):
		u.append(c[i]*(1-0.45*x)+mask[i]*0.45*x)
	return (u[0],u[1],u[2])

C1=RandomEspece.loc['monEspece']['acol1']
C2=RandomEspece.loc['monEspece']['acol2']



def showAnim(angle,ex,posMax,posMaxV,posMaxJ,specie):
	global seed,taillemot
	seed=RandomEspece.at[specie,'seed'][0]
	taillemot=RandomEspece.at[specie,'taillemotif']
	dos=RandomEspece.at[specie,'motif']
	C1,C2=RandomEspece.loc[specie]['acol1'],RandomEspece.loc[specie]['acol2']
	vertebreNB=RandomEspece.loc[specie]['vertebre']+floor((2-especes.loc[specie]['densitepoils'])*3)
	loadTexture(RandomEspece.loc[specie]['texture'])
	glLoadIdentity()
	lJ=1+(especes.loc[specie]['sec']-1)/3
	glTranslatef(0.0, especes.loc[specie]['sec']/3, -13)
	glTranslatef(0.0, 0, -13)
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)
	glEnable(GL_COLOR_MATERIAL)
	if angle!=-90:
		glPushMatrix()
		glTranslatef(-28,10, -20)
		loadTexture('exiteur')
		Backdraw()
		glPopMatrix()
		
		if specie=='monEspece':
			glPushMatrix()
			glTranslatef(0,-25, -35)
			loadTexture('frise2')
			BackdrawFrise()
			glPopMatrix()
		
		glPushMatrix()
		glTranslatef(-28,-16, -20)
		loadTexture('tailleecran')
		Backdraw()
		glPopMatrix()
		
		glPushMatrix()
		glTranslatef(-28,-5, -20)
		loadTexture('fleched')
		BackdrawF()
		glPopMatrix()
		
		glPushMatrix()
		glTranslatef(28,-5, -20)
		loadTexture('flecheg')
		BackdrawF()
		glPopMatrix()
		
		glPushMatrix()
		glTranslatef(28,5, -20)
		loadTexture('T')
		BackdrawF()
		glPopMatrix()
		
		glPushMatrix()
		glTranslatef(0,90, -250)
		loadTexture('nom')
		BackdrawF2()
		glPopMatrix()
	
		glPushMatrix()
		glTranslatef(28,8, -20)
		if especes.loc[specie]['pop']>100:
			loadTexture('alive')
		if especes.loc[specie]['pop']<1:
			loadTexture('extinct')
		if especes.loc[specie]['pop']<=100 and especes.loc[specie]['pop']>=1:
			loadTexture('danger')
		BackdrawF()
		glPopMatrix()
	
	
	glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE )
	
	
	
	b_=RandomEspece.loc[specie]['bras']# a mettre dans showfilm
	
	
	
	glTranslatef(0.0, 1.0*b_, +13)
	glRotatef(angle, 0, 1, 0)
				
	glTranslatef(0.0, 0.0, 2)
	t1=RandomEspece.loc[specie]['t1']
	t0=RandomEspece.loc[specie]['t0']
	t2=RandomEspece.loc[specie]['t2']
	
	j1=RandomEspece.loc[specie]['j1']
	j0=RandomEspece.loc[specie]['j0']

	gr=0
	if RandomEspece.loc[specie]['tete']>0:
		glPushMatrix()
		sc=(2.5-RandomEspece.loc[specie]['tete'])/2.5
		glScale(sc*t0,sc*t1,sc*t2)
		ut=Bv[3]
		glTranslatef(0.0, 0.0-0.5*(ut[1]+ut[4]), 0.2)
		loadTexture(RandomEspece.loc[specie]['texture'])	
		objdraw(0,0,C1,C2,Bv[0],Bv[1],Bv[2])
		glPopMatrix()
		glPushMatrix()
		sc=RandomEspece.loc[specie]['tete']/2.5
		glScale(sc*t0,sc*t1,sc*t2)
		ut=Ms[3]
		glTranslatef(0.0, 0.0-0.5*(ut[1]+ut[4])+0.35+machD, 0.5-0.5*(ut[2]+ut[5])+machDz)
		loadTexture(RandomEspece.loc[specie]['texture'])
		gr=-0.5*(ut[1]+ut[4])+0.4*(ut[1]-ut[4])
		objdraw(0,0,C1,C2,Ms[0],Ms[1],Ms[2])
		glPopMatrix()
		glPushMatrix()
	else:
		glPushMatrix()
		glTranslatef(0.0, 0.0, 0.2)
		loadTexture(RandomEspece.loc[specie]['texture'])
				
		objdraw(0,0,C1,C2,Bv[0],Bv[1],Bv[2])
		glPopMatrix()
		glPushMatrix()
	sc=RandomEspece.loc[specie]['tete']/2.5
	glScale(sc*t0,sc*t1,sc*t2)
	glTranslatef(0.0, 0.0, 0.5)
	loadTexture('eyewhite')
	ut=E[3]
	glTranslatef(-ut[3]+ex[0]*0.9-(posMax[0]+posMax[3])*0.5,ex[1]-0.5*(ut[1]+ut[4])-(posMax[1]+posMax[4])*0.5-gr+machD,machDz+ex[2]-0.5*(ut[2]+ut[5])-(posMax[2]+posMax[5])*0.5)
	objdraw(-1,0,C1,C2,E[0],E[1],E[2])
	glPopMatrix()
	glPushMatrix()
	sc=RandomEspece.loc[specie]['tete']/2.5
	glScale(sc*t0,sc*t1,sc*t2)
	ut=E[3]
	glTranslatef(0.0, 0.0, 0.5)
	glTranslatef(-ut[0]-ex[0]*0.9+(posMax[0]+posMax[3])*0.5,ex[1]-0.5*(ut[1]+ut[4])-(posMax[1]+posMax[4])*0.5-gr+machD,machDz+ex[2]-0.5*(ut[2]+ut[5])-(posMax[2]+posMax[5])*0.5)
	objdraw(-1,0,C1,C2,E[0],E[1],E[2])
	glPopMatrix()
	
	if RandomEspece.loc[specie]['tete']>0:
		glPushMatrix()
		loadTexture(RandomEspece.loc[specie]['texture'])
		sc=RandomEspece.loc[specie]['tete']/2.5
		glScale(sc*t0,sc*t1,sc*t2)
		ut=Mi[3]
		glTranslatef(0.0-0.5*(ut[0]+ut[3]), 0.0-0.5*(ut[1]+ut[4])-0.35-machDi, 0.5-0.5*(ut[2]+ut[5]))
		objdraw(0,0,C1,C2,Mi[0],Mi[1],Mi[2])
		glTranslatef(0, 0,-0.3)
		glPopMatrix()
	
	loadTexture(RandomEspece.loc[specie]['texture'])
	fr=max(especes.loc[specie]['densitepoils']/1.5,1)
	
	for i in range(0,vertebreNB):
		seed=RandomEspece.at[specie,'seed'][(i+1)%len(RandomEspece.at[specie,'seed'])]
		glTranslatef(0.0, 0, -0.4*1)
		
		glTranslatef(0.0, f(i/vertebreNB,RandomEspece.loc[specie]['colonne'],b_),0)
		glPushMatrix()
		glScale(exp(-(abs(i-vertebreNB*0.4)**2)/(vertebreNB*0.7)**2)*fr,exp(-(abs(i-vertebreNB*0.4)**2)/(vertebreNB*0.7)**2)*fr,1)
		ang=angle_f(0,f(i/vertebreNB,RandomEspece.loc[specie]['colonne'],b_),0.4,f((i+1)/vertebreNB,RandomEspece.loc[specie]['colonne'],b_))
		glRotatef(180*ang/pi, 1, 0, 0)
		if i!=vertebreNB-1 :
			objdraw(dos,0,C1,C2,Ve[0],Ve[1],Ve[2])
		if i==vertebreNB-1:
			glScale(1,1,exp(-(abs(i-vertebreNB*0.4)**2)/(vertebreNB*0.7)**2)*fr)
			objdraw(dos,0,C1,C2,Qu[0],Qu[1],Qu[2])
		if i==floor((vertebreNB-(2-especes.loc[specie]['densitepoils'])*3)/3) and RandomEspece.loc[specie]['bras']==1:
			glRotatef(-180*ang/pi, 1, 0, 0)
			objdraw(dos,0,C1,C2,Br[0],Br[1],Br[2])
		glPopMatrix()
		glScale(exp(-(abs(i-vertebreNB*0.4)**2)/(vertebreNB*0.7)**2),1,1)
		
		
		if i==floor(2*vertebreNB/3) or i==floor(vertebreNB/3):
			
			glPushMatrix()
			
			glTranslatef(1.0, 0.0, 0)
			sc=RandomEspece.loc[specie]['nageoire']/2.5
			glScale(sc,sc,sc)
			glRotatef(30, 1, -1, 1)
			loadTexture(RandomEspece.loc[specie]['texture'])
			objdraw(0,0,C1,C2,Na[0],Na[1],Na[2])
			glPopMatrix()
			glPushMatrix()
			
			glTranslatef(-1, 0.0, 0)
			sc=RandomEspece.loc[specie]['nageoire']/2.5
			glScale(sc,sc,sc)
			glRotatef(-30, -1, -1, 1)
			loadTexture(RandomEspece.loc[specie]['texture'])
			objdraw(0,0,C1,C2,Na[0],Na[1],Na[2])
			glPopMatrix()
			
			loadTexture(RandomEspece.loc[specie]['texture'])
		listejambe=[]
		nbjambe=RandomEspece.loc[specie]['nbjambe']
		for k in range(0,nbjambe):
			listejambe.append(floor((k+1)*(vertebreNB-(2-especes.loc[specie]['densitepoils'])*3)/(nbjambe+1)))
		
		if i in listejambe:
			if i==listejambe[0]:
				sc=RandomEspece.loc[specie]['jambe']
				L=(posMaxJ[1]-posMaxJ[4])*sc*lJ*j1
				x1=f(i/vertebreNB,RandomEspece.loc[specie]['colonne'],b_)
				U=1
				if b_==1:
					U=0
			if i==listejambe[1]:
				x2=f(i/vertebreNB,RandomEspece.loc[specie]['colonne'],b_)
				dx=x1-x2
				
				U=max((L-dx)/L,0)
				if b_==1:
					U=1
			if nbjambe>2:
				if i==listejambe[2]:
					x3=f(i/vertebreNB,RandomEspece.loc[specie]['colonne'],b_)
					dx=x1-x3
					
					U=max((L-dx)/L,0)
					if b_==1:
						U=max((L-(x2-x3))/L,0)
			
			if RandomEspece.loc[specie]['jambe']>0:
				glPushMatrix()
				glTranslatef(1.0, 0, 0)
				glScale(j0,j1,j0)
				loadTexture(RandomEspece.loc[specie]['texture'])
				sc=RandomEspece.loc[specie]['jambe']
				glScale(0.5+sc*0.5*lJ,lJ*sc*U,0.5+sc*0.5*lJ)
				glTranslatef(0,-posMaxJ[1], 0)
				objdraw(0,1,C1,C2,Ja[0],Ja[1],Ja[2])
				objdraw(0,1,C1,C2,Pp[0],Pp[1],Pp[2])
				glPopMatrix()
				glPushMatrix()
				glTranslatef(-1, 0, 0)
				loadTexture(RandomEspece.loc[specie]['texture'])
				glScale(j0,j1,j0)
				sc=RandomEspece.loc[specie]['jambe']
				glScale(0.5+sc*0.5*lJ,sc*U*lJ,0.5+sc*0.5*lJ)
				glTranslatef(0,-posMaxJ[1],0)
				objdraw(0,1,C1,C2,Ja[0],Ja[1],Ja[2])
				objdraw(0,1,C1,C2,Pp[0],Pp[1],Pp[2])
				
				glPopMatrix()
			
			loadTexture(RandomEspece.loc[specie]['texture'])
		glScale(exp((abs(i-vertebreNB*0.4)**2)/(vertebreNB*0.7)**2),1,1)
		glTranslatef(0.0, -f(i/vertebreNB,RandomEspece.loc[specie]['colonne'],b_),0)
	
	
	
	glDisable(GL_LIGHT0)
	glDisable(GL_LIGHTING)
	glDisable(GL_COLOR_MATERIAL)

def update_frise():
	#glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glClear(GL_DEPTH_BUFFER_BIT)
	glLoadIdentity()
	glTranslatef(0.0, 0, -26)
	glTranslatef(0,-25, -35)
	loadTexture('frise2')
	BackdrawFrise()

def clear_buf():
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

	
def showFILM(angle,ex,posMax,posMaxV,posMaxJ,specie):
	global seed,taillemot
	seed=svgmuteur2.at[specie,'seed'][0]
	taillemot=svgmuteur2.at[specie,'taillemotif']
	dos=svgmuteur2.at[specie,'motif']
	C1,C2=svgmuteur2.loc[specie]['acol1'],svgmuteur2.loc[specie]['acol2']
	vertebreNB=svgmuteur2.loc[specie]['vertebre']+floor((2-svgmuteur1.loc[specie]['densitepoils'])*3)
	loadTexture(svgmuteur2.loc[specie]['texture'])
	glLoadIdentity()
	lJ=1+(svgmuteur1.loc[specie]['sec']-1)/3
	
	glTranslatef(0.0, 0, -26)
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	glEnable(GL_LIGHTING)
	glEnable(GL_LIGHT0)
	glEnable(GL_COLOR_MATERIAL)
	
	if angle!=-90:
		glPushMatrix()
		glTranslatef(-28,10, -20)
		loadTexture('exiteur')
		Backdraw()
		glPopMatrix()
		
		glPushMatrix()
		glTranslatef(0,-25, -35)
		loadTexture('frise2')
		BackdrawFrise()
		glPopMatrix()
		
		glPushMatrix()
		glTranslatef(-28,-16, -20)
		loadTexture('tailleecran')
		Backdraw()
		glPopMatrix()
		
		glPushMatrix()
		glTranslatef(-28,-5, -20)
		loadTexture('fleched')
		BackdrawF()
		glPopMatrix()
		
		glPushMatrix()
		glTranslatef(28,-5, -20)
		loadTexture('flecheg')
		BackdrawF()
		glPopMatrix()
		
		glPushMatrix()
		glTranslatef(28,5, -20)
		loadTexture('T')
		BackdrawF()
		glPopMatrix()
		
		glPushMatrix()
		glTranslatef(0,90, -250)
		loadTexture('nom')
		BackdrawF2()
		glPopMatrix()
	
		glPushMatrix()
		glTranslatef(28,8, -20)
		if svgmuteur1.loc[specie]['pop']>100:
			loadTexture('alive')
		if svgmuteur1.loc[specie]['pop']<1:
			loadTexture('extinct')
		if svgmuteur1.loc[specie]['pop']<=100 and svgmuteur1.loc[specie]['pop']>=1:
			loadTexture('danger')
		BackdrawF()
		glPopMatrix()
	glTranslatef(0.0, svgmuteur1.loc[specie]['sec']/3, 0)
	glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE )
	b_=svgmuteur2.loc[specie]['bras']
	glTranslatef(0.0, 1.0*b_, +13)
	glRotatef(angle, 0, 1, 0)
				
	glTranslatef(0.0, 0.0, 2)
	t1=svgmuteur2.loc[specie]['t1']
	t0=svgmuteur2.loc[specie]['t0']
	t2=svgmuteur2.loc[specie]['t2']
	
	j1=svgmuteur2.loc[specie]['j1']
	j0=svgmuteur2.loc[specie]['j0']
	
	gr=0
	if svgmuteur2.loc[specie]['tete']>0:
		glPushMatrix()
		sc=(2.5-svgmuteur2.loc[specie]['tete'])/2.5
		glScale(sc*t0,sc*t1,sc*t2)
		ut=Bv[3]
		glTranslatef(0.0, 0.0-0.5*(ut[1]+ut[4]), 0.2)
		loadTexture(svgmuteur2.loc[specie]['texture'])	
		objdraw(0,0,C1,C2,Bv[0],Bv[1],Bv[2])
		glPopMatrix()
		glPushMatrix()
		sc=svgmuteur2.loc[specie]['tete']/2.5
		glScale(sc*t0,sc*t1,sc*t2)
		ut=Ms[3]
		glTranslatef(0.0, 0.0-0.5*(ut[1]+ut[4])+0.35+machD, 0.5-0.5*(ut[2]+ut[5])+machDz)
		loadTexture(svgmuteur2.loc[specie]['texture'])
		gr=-0.5*(ut[1]+ut[4])+0.4*(ut[1]-ut[4])
		objdraw(0,0,C1,C2,Ms[0],Ms[1],Ms[2])
		glPopMatrix()
		glPushMatrix()
	else:
		glPushMatrix()
		glTranslatef(0.0, 0.0, 0.2)
		loadTexture(svgmuteur2.loc[specie]['texture'])
				
		objdraw(0,0,C1,C2,Bv[0],Bv[1],Bv[2])
		glPopMatrix()
		glPushMatrix()
	sc=svgmuteur2.loc[specie]['tete']/2.5
	glScale(sc*t0,sc*t1,sc*t2)
	glTranslatef(0.0, 0.0, 0.5)
	loadTexture('eyewhite')
	ut=E[3]
	glTranslatef(-ut[3]+ex[0]*0.9-(posMax[0]+posMax[3])*0.5,ex[1]-0.5*(ut[1]+ut[4])-(posMax[1]+posMax[4])*0.5-gr+machD,machDz+ex[2]-0.5*(ut[2]+ut[5])-(posMax[2]+posMax[5])*0.5)
	objdraw(-1,0,C1,C2,E[0],E[1],E[2])
	glPopMatrix()
	glPushMatrix()
	sc=svgmuteur2.loc[specie]['tete']/2.5
	glScale(sc*t0,sc*t1,sc*t2)
	ut=E[3]
	glTranslatef(0.0, 0.0, 0.5)
	glTranslatef(-ut[0]-ex[0]*0.9+(posMax[0]+posMax[3])*0.5,ex[1]-0.5*(ut[1]+ut[4])-(posMax[1]+posMax[4])*0.5-gr+machD,machDz+ex[2]-0.5*(ut[2]+ut[5])-(posMax[2]+posMax[5])*0.5)
	objdraw(-1,0,C1,C2,E[0],E[1],E[2])
	glPopMatrix()
	
	if svgmuteur2.loc[specie]['tete']>0:
		glPushMatrix()
		loadTexture(svgmuteur2.loc[specie]['texture'])
		sc=svgmuteur2.loc[specie]['tete']/2.5
		glScale(sc*t0,sc*t1,sc*t2)
		ut=Mi[3]
		glTranslatef(0.0-0.5*(ut[0]+ut[3]), 0.0-0.5*(ut[1]+ut[4])-0.35-machDi, 0.5-0.5*(ut[2]+ut[5]))
		objdraw(0,0,C1,C2,Mi[0],Mi[1],Mi[2])
		glTranslatef(0, 0,-0.3)
		glPopMatrix()
	
	loadTexture(svgmuteur2.loc[specie]['texture'])
	fr=max(svgmuteur1.loc[specie]['densitepoils']/1.5,1)
	
	for i in range(0,vertebreNB):
		seed=svgmuteur2.at[specie,'seed'][(i+1)%len(svgmuteur2.at[specie,'seed'])]
		glTranslatef(0.0, 0, -0.4*1)
		
		glTranslatef(0.0, f(i/vertebreNB,svgmuteur2.loc[specie]['colonne'],b_),0)
		glPushMatrix()
		glScale(exp(-(abs(i-vertebreNB*0.4)**2)/(vertebreNB*0.7)**2)*fr,exp(-(abs(i-vertebreNB*0.4)**2)/(vertebreNB*0.7)**2)*fr,1)
		ang=angle_f(0,f(i/vertebreNB,svgmuteur2.loc[specie]['colonne'],b_),0.4,f((i+1)/vertebreNB,svgmuteur2.loc[specie]['colonne'],b_))
		glRotatef(180*ang/pi, 1, 0, 0)
		if i!=vertebreNB-1 :
			objdraw(dos,0,C1,C2,Ve[0],Ve[1],Ve[2])
		if i==vertebreNB-1:
			glScale(1,1,exp(-(abs(i-vertebreNB*0.4)**2)/(vertebreNB*0.7)**2)*fr)
			objdraw(dos,0,C1,C2,Qu[0],Qu[1],Qu[2])
		if i==floor((vertebreNB-(2-svgmuteur1.loc[specie]['densitepoils'])*3)/3) and svgmuteur2.loc[specie]['bras']==1:
			glRotatef(-180*ang/pi, 1, 0, 0)
			objdraw(dos,0,C1,C2,Br[0],Br[1],Br[2])
		glPopMatrix()
		glScale(exp(-(abs(i-vertebreNB*0.4)**2)/(vertebreNB*0.7)**2),1,1)
		
		
		if i==floor(2*vertebreNB/3) or i==floor(vertebreNB/3):
			
			glPushMatrix()
			
			glTranslatef(1.0, 0.0, 0)
			sc=svgmuteur2.loc[specie]['nageoire']/2.5
			glScale(sc,sc,sc)
			glRotatef(30, 1, -1, 1)
			loadTexture(svgmuteur2.loc[specie]['texture'])
			objdraw(0,0,C1,C2,Na[0],Na[1],Na[2])
			glPopMatrix()
			glPushMatrix()
			
			glTranslatef(-1, 0.0, 0)
			sc=svgmuteur2.loc[specie]['nageoire']/2.5
			glScale(sc,sc,sc)
			glRotatef(-30, -1, -1, 1)
			loadTexture(svgmuteur2.loc[specie]['texture'])
			objdraw(0,0,C1,C2,Na[0],Na[1],Na[2])
			glPopMatrix()
			
			loadTexture(svgmuteur2.loc[specie]['texture'])
		listejambe=[]
		nbjambe=svgmuteur2.loc[specie]['nbjambe']
		for k in range(0,nbjambe):
			listejambe.append(floor((k+1)*(vertebreNB-(2-svgmuteur1.loc[specie]['densitepoils'])*3)/(nbjambe+1)))
		
		if i in listejambe:
			if i==listejambe[0]:
				sc=svgmuteur2.loc[specie]['jambe']
				L=(posMaxJ[1]-posMaxJ[4])*sc*lJ*j1
				x1=f(i/vertebreNB,svgmuteur2.loc[specie]['colonne'],b_)
				U=1
				if b_==1:
					U=0
			if i==listejambe[1]:
				x2=f(i/vertebreNB,svgmuteur2.loc[specie]['colonne'],b_)
				dx=x1-x2
				
				U=max((L-dx)/L,0)
				if b_==1:
					U=1
			if nbjambe>2:
				if i==listejambe[2]:
					x3=f(i/vertebreNB,svgmuteur2.loc[specie]['colonne'],b_)
					dx=x1-x3
					
					U=max((L-dx)/L,0)
					if b_==1:
						U=max((L-(x2-x3))/L,0)
			
			if svgmuteur2.loc[specie]['jambe']>0:
				glPushMatrix()
				glTranslatef(1.0, 0, 0)
				glScale(j0,j1,j0)
				loadTexture(svgmuteur2.loc[specie]['texture'])
				sc=svgmuteur2.loc[specie]['jambe']
				glScale(0.5+sc*0.5*lJ,lJ*sc*U,0.5+sc*0.5*lJ)
				glTranslatef(0,-posMaxJ[1], 0)
				objdraw(0,1,C1,C2,Ja[0],Ja[1],Ja[2])
				objdraw(0,1,C1,C2,Pp[0],Pp[1],Pp[2])
				glPopMatrix()
				glPushMatrix()
				glTranslatef(-1, 0, 0)
				loadTexture(svgmuteur2.loc[specie]['texture'])
				glScale(j0,j1,j0)
				sc=svgmuteur2.loc[specie]['jambe']
				glScale(0.5+sc*0.5*lJ,sc*U*lJ,0.5+sc*0.5*lJ)
				glTranslatef(0,-posMaxJ[1],0)
				objdraw(0,1,C1,C2,Ja[0],Ja[1],Ja[2])
				objdraw(0,1,C1,C2,Pp[0],Pp[1],Pp[2])
				
				glPopMatrix()
			
			loadTexture(svgmuteur2.loc[specie]['texture'])
		glScale(exp((abs(i-vertebreNB*0.4)**2)/(vertebreNB*0.7)**2),1,1)
		glTranslatef(0.0, -f(i/vertebreNB,svgmuteur2.loc[specie]['colonne'],b_),0)
	
	
	
	glDisable(GL_LIGHT0)
	glDisable(GL_LIGHTING)
	glDisable(GL_COLOR_MATERIAL)	


	
def split(n,Spece,Nb):
	global especes,RandomEspece,showcreature,bypass,alivecreature,listC,listnom
	k=especes.iloc[[Nb]]
	k.index=['Espece'+str(n)]
	alivecreature=alivecreature+1
	k.at['Espece'+str(n),'nom']='Espece'+str(n)
	if Spece=='monEspece':
		k.at['Espece'+str(n),'pop']=(k.at['Espece'+str(n),'pop']-100)
		especes.at[Spece,'pop']=100
	else:
		k.at['Espece'+str(n),'pop']=(k.at['Espece'+str(n),'pop']-200)
		especes.at[Spece,'pop']=200
	l=RandomEspece.iloc[[Nb]]
	l.index=['Espece'+str(n)]
	especes=pd.concat([especes,k])
	RandomEspece=pd.concat([RandomEspece,l])
	RandomEspece.at['Espece'+str(n),'mere']=Spece
	RandomEspece.at[Spece,'child']=RandomEspece.at[Spece,'child']+1
	RandomEspece.at['Espece'+str(n),'score']=RandomEspece.at['Espece'+str(n),'score'].copy()
	RandomEspece.at['Espece'+str(n),'score'].append(RandomEspece.at[Spece,'child'])
	RandomEspece.at['Espece'+str(n),'child']=0
	Lk=[]
	
		
	if len(RandomEspece.at['Espece'+str(n),'score'])==2:
		RandomEspece.at['Espece'+str(n),'colortree']=(randint(0,255),randint(0,255),randint(0,255))
		if RandomEspece.at['Espece'+str(n),'colortree']==(100,100,100) or RandomEspece.at['Espece'+str(n),'colortree']==(0,0,255) or RandomEspece.at['Espece'+str(n),'colortree']==(255,255,255):
			RandomEspece.at['Espece'+str(n),'colortree']=(255,255,0)
	#dicoImage['Espece'+str(n)]=pygame.image.load("patoune2.png")
	Xl2.append(especes.at[Spece,'X'])
	Yl2.append(especes.at[Spece,'Y'])
	if Spece=='monEspece':
		dicoImage['Espece'+str(n)]=pygame.image.load("patoune2.png")
		showcreature=1
		bypass='Espece'+str(n)
	else:
		dicoImage['Espece'+str(n)]=pygame.image.load("patouneq.png")
	
	nominem=0
	if len(RandomEspece.at['Espece'+str(n),'score'])==2:
		while nominem==0:
			nominem=readlatin()
	else:
		nominem=RandomEspece.at['Espece'+str(n),'nominem'].split()[0]
	nominem2=0
	while nominem2==0:
		nominem2=readlatin()
	RandomEspece.at['Espece'+str(n),'nominem']=nominem[0].upper()+nominem[1:]+' '+nominem2
	lf=[]
	for i in range(0,RandomEspece.at['Espece'+str(n),'vertebre']*2):
		lf.append(randint(0,1000))
	RandomEspece.at['Espece'+str(n),'seed']=lf
	
	listC.append(k.at['Espece'+str(n),'nom'])
	listnom.append(RandomEspece.at['Espece'+str(n),'nominem'])
	listnom2=sorted(listnom,key=str.lower)
	listC2=listC.copy()
	for i in range(0,len(listnom)):
		listC[i]=listC2[listnom.index(listnom2[i])]
	listnom=listnom2.copy()
	return


dicoNbio={}
dicoNbio['plain']=['plain','forest','savannah','tundra','coast','mountain']
dicoNbio['plai2']=['grassland','steppe','desert']
dicoNbio['foret']=['grassland','jungle','boreal forest']
dicoNbio['svane']=['desert','jungle','grassland','mangrove','hot mountain']
dicoNbio['jungl']=['forest','savannah']
dicoNbio['deser']=['plain','savannah']
dicoNbio['stepe']=['tundra','plain']
dicoNbio['forbo']=['forest','tundra']
dicoNbio['tunda']=['grassland','boreal forest','steppe','ice','cold mountain']
dicoNbio['glace']=['tundra','coast','polar sea']
dicoNbio['cotes']=['sea','grassland','mangrove','ice']
dicoNbio['mangr']=['savannah','coast','tropical sea']
dicoNbio['water']=['coast','polar sea','tropical sea']
dicoNbio['monts']=['grassland','hot mountain','cold mountain']
dicoNbio['hotmt']=['savannah','mountain']
dicoNbio['coldm']=['tundra','mountain']
dicoNbio['lac']=['no']
dicoNbio['volca']=['no']
dicoNbio['meteo']=['no']
dicoNbio['crate']=['meteor']
dicoNbio['magma']=['volcano']
dicoNbio['glacC']=['tundra','coast','polar sea']
dicoNbio['coldw']=['sea','ice']
dicoNbio['tropw']=['sea','mangrove']

dicoNbio1={}
dicoNbio1['plain']=['plai2','foret','svane','tunda','cotes','monts']
dicoNbio1['plai2']=['plain','stepe','deser']
dicoNbio1['foret']=['plain','jungl','forbo']
dicoNbio1['svane']=['deser','jungl','plain','mangr','hotmt']
dicoNbio1['jungl']=['foret','svane']
dicoNbio1['deser']=['plai2','svane']
dicoNbio1['stepe']=['tunda','plai2']
dicoNbio1['forbo']=['foret','tunda']
dicoNbio1['tunda']=['plain','forbo','stepe','glace','coldm']
dicoNbio1['glace']=['tunda','cotes','coldw']
dicoNbio1['cotes']=['water','plain','mangr','glace']
dicoNbio1['mangr']=['svane','cotes','tropw']
dicoNbio1['water']=['cotes','coldw','tropw']
dicoNbio1['monts']=['plain','hotmt','coldm']
dicoNbio1['hotmt']=['svane','monts']
dicoNbio1['coldm']=['tunda','monts']
dicoNbio1['lac']=['tunda']
dicoNbio1['volca']=['no']
dicoNbio1['meteo']=['no']
dicoNbio1['crate']=['meteo']
dicoNbio1['magma']=['volca']
dicoNbio1['glacC']=['tunda','cotes','coldw']
dicoNbio1['coldw']=['water','glace']
dicoNbio1['tropw']=['water','mangr']

dicoNbi={}
dicoNbi['plain']='grassland'
dicoNbi['plai2']='plain'
dicoNbi['foret']='forest'
dicoNbi['svane']='savannah'
dicoNbi['jungl']='jungle'
dicoNbi['deser']='desert'
dicoNbi['stepe']='steppe'
dicoNbi['forbo']='boreal forest'
dicoNbi['tunda']='tundra'
dicoNbi['glace']='ice'
dicoNbi['cotes']='coast'
dicoNbi['mangr']='mangrove'
dicoNbi['water']='sea'
dicoNbi['monts']='mountain'
dicoNbi['coldm']='cold mountain'
dicoNbi['hotmt']='hot mountain'
dicoNbi['lac']='lake'
dicoNbi['volca']='volcano'
dicoNbi['meteo']='meteor'
dicoNbi['crate']='crater'
dicoNbi['magma']='lava'
dicoNbi['glacC']='ice'
dicoNbi['coldw']='polar sea'
dicoNbi['tropw']='tropical sea'

def biomemontre(biome):
	global biomeshow
	biomeshow=pygame.image.load("biomeshow.png").convert_alpha()
	font = pygame.font.Font('freesansbold.ttf', 16)
	text = font.render(dicoNbi[biome], True, (0,0,0,100))
	textRect = text.get_rect()
	textRect=(textRect[0]+20,14+textRect[1])
	biomeshow.blit(text,textRect)
	font = pygame.font.Font('freesansbold.ttf', 12)
	text = font.render('nearest biomes', True, (0,0,0,100))
	textRect = text.get_rect()
	textRect=(textRect[0]+20,32+textRect[1])
	biomeshow.blit(text,textRect)
	for k,j in enumerate(dicoNbio[biome]):
		text = font.render('- '+j, True, (0,0,0,100))
		textRect = text.get_rect()
		textRect=(textRect[0]+20,50+textRect[1]+k*18)
		biomeshow.blit(text,textRect)
		biomeshow.blit(dico[dicoNbio1[biome][k]],(100,50+k*18))
	font = pygame.font.Font('freesansbold.ttf', 25)
	return



BIGSCORE2=0
US=pygame.Surface((4,4),pygame.SRCALPHA, 32)
US.fill((255,0,0))

US2=pygame.Surface((4,4),pygame.SRCALPHA, 32)
US2.fill((255,0,255))

noir=pygame.Surface((700,700),pygame.SRCALPHA, 32)
noir.fill((0,0,0))
yeuxP=0
menu()
StockaddT=0
ageglaciaire=0
rechauffement=0
tour=0
cycle=0
pause1=randint(80,120)
Dageglaciaire=randint(80,120)
pause2=randint(80,120)
Drechauff=randint(80,120)
cycle=pause1+pause2+Dageglaciaire+Drechauff
showworld=0
action=0
showhum=0
showtemp=0
showcreature=0
showCont=0
vertebreNB=10
Ns=0

def chooseCreature():
	
	for i in range(0,min(len(listC),6)):
			T=RandomEspece.at[listC[(i+curseur)%len(listC)],'nominem']
			text = font.render(T, True, (0,0,0))
			textRect = text.get_rect()
			textRect.center = (700, 225+i*50)
			fenetre.blit(text,textRect)
	return


	
def choosesave(lettre,ululu,alt):
	global T0
	listdir3=os.listdir('svg/')
	listdir2=[]
	for i in listdir3:
		if i[len(i)-4:]!='.png':
			listdir2.append(i)
	if ululu!='a' and ululu<len(listdir2):
		T0=listdir2[(ululu+curseur)%len(listdir2)]
	if lettre==-1:
		T0=T0[:-1]
	if lettre!=-1 and lettre!=0:
		T0=T0+lettre
	
	text = font.render(T0, True, (0,0,0))
	textRect = text.get_rect()
	if alt==-1:
		text = font.render(T0+'_', True, (0,0,0))
	textRect.center = (700, 225)
	fenetre.blit(text,textRect)
	for i in range(0,min(len(listdir2),5)):
			T=listdir2[(i+curseur)%len(listdir2)]
			
			text = font.render(T, True, (0,0,0))
			textRect = text.get_rect()
			textRect.center = (700, 225+i*50+50)
			fenetre.blit(text,textRect)
	return listdir2

def imageCreature():
	global Ms,E,Mi,Ve,Na,Ja,Pp,vignette,yeuxP,ex,Bv,dicoImage,Qu,Br

	frame2=pygame.Surface((200,200),pygame.SRCALPHA, 32)
	txt = font.render('monEspece', True, (255,255,255))
	frame2.blit(txt,(0,0))
	pygame.image.save(frame2,"nom.png")
	
	glMatrixMode(GL_PROJECTION)
	gluPerspective(45, display[0] / display[1], 0.1, 50.0)
	glMatrixMode(GL_MODELVIEW)
	glLight(GL_LIGHT0, GL_POSITION,  (5, 5, 5, 1)) # point light from the left, top, front
	glLightfv(GL_LIGHT0, GL_AMBIENT, (0, 0, 0, 1))
	glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))
	glTranslatef(0.0, 0.0, -13)
	glEnable(GL_DEPTH_TEST)
	
	angle=30
	Bv=read('bouchever')
	Br=read('bras')
	Ms=read('machsuplez')
	E=read('eye')
	Mi=read('machinf')
	Ve=read('vertebre')
	Na=read('nageoire')
	Ja=read('jambe1')
	Pp=read('piedpalmé')
	Qu=read('queue')
	if yeuxP==0:
		ex=eyepos(Ms[0],Ms[3])
		yeuxP=1
	
	
		
	angle=(angle+5)%360
	
	showAnim(angle,ex,Ms[3],Ve[3],Ja[3],'monEspece')
	

	image1=pygame.Surface((1400,700),pygame.SRCALPHA, 32)
	image1.fill((0,0,0))
	screen_size=[1400,700]
	r = glReadPixels(0,0,1400,1400,   GL_RGB,GL_FLOAT)
	op=r[0]
	op=op[0]
	for i in range(0,700):
		for j in range(0,1400):
			
			a=r[i]
			b=a[j]
			if b[0]!=0 or b[1]!=0 or b[1]!=0:
				image1.set_at((j,700-i),pygame.Color(floor(b[0]*255),floor(b[1]*255),floor(b[2]*255)))
	
	
	pygame.image.save(image1,"creature1.png")
	
	frame=pygame.Surface((425,425),pygame.SRCALPHA, 32)
	image = pygame.image.load("creature1.png")
	frame.blit(image,(-495,-180))
	frame=pygame.transform.scale(frame,(50,50))
	vignette = pygame.image.load("patoune2.png")
	vignette.blit(frame,(25,25))
	dicoImage['monEspece']=vignette
	
	

def mutation(niv,spece):
	global especes,RandomEspece,listeyear
	if niv==0:
		Ran=randint(0,9)
		
		if Ran==0:
			RandomEspece.at[spece,'taille']=max(min(RandomEspece.at[spece,'taille']*0.8+np.random.lognormal(0,2.5)*0.2,2*RandomEspece.at[spece,'taille']),0.5*RandomEspece.at[spece,'taille'])
		if Ran==1:
			RandomEspece.at[spece,'j0']=max(min(RandomEspece.at[spece,'j0']+(random()-0.5)*0.4,2),0.5)
		if Ran==2:
			RandomEspece.at[spece,'j1']=max(min(RandomEspece.at[spece,'j1']+(random()-0.5)*0.4,2),0.5)
		if Ran==3:
			RandomEspece.at[spece,'t0']=max(min(RandomEspece.at[spece,'t0']+(random()-0.5)*0.4,2),0.5)
		if Ran==4:
			RandomEspece.at[spece,'t1']=max(min(RandomEspece.at[spece,'t1']+(random()-0.5)*0.4,2),0.5)
		if Ran==5:
			RandomEspece.at[spece,'t2']=max(min(RandomEspece.at[spece,'t2']+(random()-0.5)*0.4,2),0.5)
		if Ran==6:
			RandomEspece.at[spece,'vertebre']=max(min(RandomEspece.at[spece,'vertebre']+randint(-2,2),20),5)
		if Ran==7:
			listM=[]
			grouf=RandomEspece.at[spece,'gnouf']
			for i in range(0,3):
				listM.append(max(min(grouf[i]+(random()-0.5)*0.75,0.8),-0.8))
			RandomEspece.at[spece,'gnouf']=listM
			RandomEspece.at[spece,'colonne']=pol(listM)
		
		if Ran==8:
			listM=[]
			grouf=RandomEspece.at[spece,'acol1']# avant color1
			for i in range(0,3):
				listM.append(max(min(grouf[i]+(random()-0.5)*0.2,1),0))
			RandomEspece.at[spece,'acol1']=tuple(listM)
			listM=[]
			grouf=RandomEspece.at[spece,'acol2']
			for i in range(0,3):
				listM.append(max(min(grouf[i]+(random()-0.5)*0.2,1),0))
			RandomEspece.at[spece,'acol2']=tuple(listM)
		if Ran==9:
			if randint(0,2)==0:
				RandomEspece.at[spece,'motif']=randint(0,3)
		
	if niv==1:
		Ran=choice([0,1,2,3,4,5,6,8])
		bio=cases[especes.at[spece,'X']][especes.at[spece,'Y']]
		if bio=='glacC':
			bio='glace'
		if Ran==0:
			L=dicoMaS[bio]
			RandomEspece.at[spece,'machsupTYPE']=choice(L)
		if Ran==1:
			L=dicoMai[bio]
			RandomEspece.at[spece,'machinfTYPE']=choice(L)
		if Ran==2:
			L=dicoQ[bio]
			que=choice(L)
			RandomEspece.at[spece,'queueTYPE']=que
		if Ran==3:
			L=dicoJ[bio]
			RandomEspece.at[spece,'jambeTYPE']=choice(L)
		if Ran==4:
			L=dicop[bio]
			RandomEspece.at[spece,'piedTYPE']=choice(L)
		if Ran==5:
			L=dicov[bio]
			RandomEspece.at[spece,'vertebreTYPE']=choice(L)
		if Ran==6:
			L=textL
			RandomEspece.at[spece,'texture']=choice(L)
		if Ran==7:
			L=nageoireL
			RandomEspece.at[spece,'nageoireTYPE']=choice(L)
		if Ran==8:
			L=dicob[bio]
			RandomEspece.at[spece,'brasTYPE']=choice(L)
	
		





def saveim(r,Espe):
	global dicoImage,bypass
	image1=pygame.Surface((1400,700),pygame.SRCALPHA, 32)
	image1.fill((0,0,0,0))
	image1=pygame.image.frombuffer(r,(1400,1400),'RGB')
	image1=pygame.transform.flip(image1,0,1)
	image1=pygame.transform.scale(image1,(140,140))
	
	pygame.image.save(image1,"creature1.png")
	frame=pygame.Surface((42,42),pygame.SRCALPHA, 32)
	image = pygame.image.load("creature1.png")
	frame.blit(image1,(-49,-18-70))
	frame=pygame.transform.scale(frame,(50,50))
	vignette = pygame.image.load("patoune2.png")
	vignette.blit(frame,(25,25))
	dicoImage[Espe]=vignette
	bypass=0
	return

def saveim2(r):
	image1=pygame.Surface((140,70),pygame.SRCALPHA, 32)
	image1.fill((0,0,0,0))
	screen_size=[1400,700]
	op=r[0]
	op=op[0]
	lmin=140
	lmax=0
	hmin=140
	hmax=0
	for i in range(0,70):
		for j in range(0,140):
			
			a=r[i*10]
			b=a[j*10]
			
			if b[0]!=0 or b[1]!=0 or b[1]!=0:
				c=(floor(b[0]*255)+floor(b[1]*255)+floor(b[2]*255))//3
				image1.set_at((j,70-i),pygame.Color(c,c,c))
				lmin=min(lmin,j)
				lmax=max(lmax,j)
				hmin=min(hmin,i)
				hmax=max(hmax,i)
	
	return image1,hmax-hmin,lmax-lmin,lmin,lmax,hmin,hmax

def saveim3(r):
	image1=pygame.Surface((1400,700),pygame.SRCALPHA, 32)
	image1.fill((0,0,0,0))
	#op=r[0]
	#op=op[0]
	image1=pygame.image.frombuffer(r,(1400,1400),'RGB')
	return image1
	
def ditsanceBiome(x,y,biome_given,adap):
	Dmin=1000
	if adap==0:
		g=10
	if biome_given=='cotes':
		g=10
	for i in range(0,140):
		for j in range(0,70):
			if cases[i][j]==biome_given:
				w=0
				for k in [+1,-1,0,-2,2]:
					for l in [+1,-1,0,-2,2]:
						if cases[(i+k)%140][(j+l)%70]==biome_given:
							w=w+2-abs(l)+2-abs(k)
				if w>g:
					dx=min(abs(x-i),140-abs(x-i))
					dy=abs(y-j)
					D=(dx**2+dy**2)**0.5
					Dmin=min(Dmin,D)
	return Dmin
			
	
class mission(pygame.sprite.Sprite):
	def __init__(self,Type):
		pygame.sprite.Sprite.__init__(self)
		global brdG
		if Type==0:
			self.name='split your group'
			#self.nbtour=70
			self.win=max(70-especes.at['monEspece','pop']//10,10)
			self.text='you must adapt yourself to a biome and reach a population of 700 to split your group. Reward '+str(int(self.win*(1.25-CURSE*0.25)))+' turns'
			self.type_=0
			self.split=0
		if Type==1:
			self.name='adapt to the biome'
			#self.nbtour=30
			if numero_mission!=2:
				self.win=301
				c=0
				while self.win>300+c or self.win<60:
					self.bio=choice(['coldm','hotmt','monts','tropw','coldw','plain','tunda','svane','glace','plai2','cotes','water','deser','mangr','jungl','foret','stepe','forbo'])
					self.win=int(ditsanceBiome(xs,ys,self.bio,0)**2+5)
					c=c+1
			else:
				self.bio='cotes'
				self.win=int(ditsanceBiome(xs,ys,self.bio,0)**2+5)
			self.win=self.win//2
			self.text='you must go to the biome: '+dicoNbi[self.bio]+'. Reward '+str(int(self.win*(1.25-CURSE*0.25)))+' turns'
			self.type_=1
			self.adapt=0
		if Type==2:
			self.name='continent'
			self.col=(0,0,0)
			self.win=0
			self.x_choosed=(xs+randint(-30,30))%140
			self.y_choosed=(ys+randint(-30,30))%70
			while self.col==(0,0,0) or self.win<30 or  continentM[self.x_choosed][self.y_choosed]==continentM[xs][ys] or self.win>200 or dicoNcon[continentM[self.x_choosed][self.y_choosed]]==0:
				self.x_choosed=(xs+randint(-30,30))%140
				self.y_choosed=(ys+randint(-30,30))%70
				dx=min(abs(self.x_choosed-xs),140-abs(self.x_choosed-xs))
				dy=abs(self.y_choosed-ys)
				self.win=2*int((dx**2+dy**2)**0.5)+5
				if continentM[self.x_choosed][self.y_choosed]!=(0,0,0):
					self.text='you must go to the continent:     '+str(dicoContinent[continentM[self.x_choosed][self.y_choosed]])+'. Reward '+str(int(self.win*(1.25-CURSE*0.25)))+' turns'
				self.type_=2
				self.col=continentM[self.x_choosed][self.y_choosed]
		if Type==3:
			self.type_=3
			self.bio=choice(dicoNbio1[cases[xs][ys]])
			self.win=int(20*Desadapteur(self.bio,'monEspece'))
			self.text='you must adapt yourself to the biome: '+dicoNbi[self.bio]+'. Reward '+str(int(self.win*(1.25-CURSE*0.25)))+' turns'
			
	def show1(self):
		global fenetre,point
		fenetre.blit(missionscreen,(1075,415))
		line=self.text.split()
		x=30
		y=30
		font = pygame.font.Font('freesansbold.ttf', 18)
		for j,i in enumerate(line):
			
			text = font.render(i, True, (0,0,0))
			fenetre.blit(text,(x+1075,y+455))
			x=x+text.get_width()
			x=x+8
			if self.type_==2 and i=='continent:':
				point.fill(continentM[self.x_choosed][self.y_choosed])
				fenetre.blit(point,(1075+x-5,455+y+5))
				x=x+5
			t=font.render(line[(j+1)%len(line)], True, (0,0,0))
			if x+t.get_width()>270:
				x=30
				y=y+20
		text = font.render('clic to discard mission '+str(-int(self.win*(1.25-CURSE*0.25))//2)+' turns', True, (255,0,0))
		fenetre.blit(text,(1080,650))
		fenetre.blit(pygame.image.load("closeur.png"),(1370,670))	
			
	def check_complete(self):
		#self.nbtour=self.nbtour-1
		#if self.nbtour==-1:
			#return 'stop'
		if self.type_==0:
			return self.split
		if self.type_==1 :
			a=cases[xs][ys]==self.bio
			if self.bio=='glace' and cases[xs][ys]=='glacC':
				a=True
			return a
		if self.type_==2 :
			if continentM[self.x_choosed][self.y_choosed]==continentM[xs][ys]:
				return True
		if self.type_==3:
			if Desadapteur(cases[xs][ys],'monEspece')<0.1 and cases[xs][ys]==self.bio:
				return True
	def validate(self,num):
		if self.type_==0 and num==0:
			self.split=1
			
	def time(self):
		return self.win*(1.25-CURSE*0.25)
	def type_ret(self):
		return self.type_
	def col_ret(self):
		return self.col
	def roll_me(self,x):
		if self.type_==2:
			self.x_choosed=(self.x_choosed+x)%140


	
#print(Desadapteur(cases[xs][ys],'monEspece'))
	

bypass=0
vignette = pygame.image.load("patoune2.png")
display = (1400, 700)
pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL )
imageCreature()
pygame.display.set_mode((1400,700),RESIZABLE )
menu()
showtree=0
alivecreature=1
TIME=500+(1-CURSE)*150+1
mission_en_cours=mission(0)
numero_mission=1
createMAP()
brdG=np.full((140,70),0)
while cases[xs][ys]!='water' or temperature2[xs][ys]>18 or temperature2[xs][ys]<0:
	xs=randint(0,139)
	ys=randint(0,69)

especes.at['monEspece','X']=xs
especes.at['monEspece','Y']=ys
svgmuteur1=especes.iloc[[0]]
svgmuteur2=RandomEspece.iloc[[0]]
svgmuteur1.index=[str(0)]
svgmuteur2.index=[str(0)]
listeyear=[0]
def savefilm(t):
	global svgmuteur1,svgmuteur2
	k=especes.iloc[[0]]
	l=RandomEspece.iloc[[0]]
	k.index=[str(t)]
	l.index=[str(t)]
	
	svgmuteur1=pd.concat([svgmuteur1,k])
	svgmuteur2=pd.concat([svgmuteur2,l])
namechoosed=0
def sauvegarde(name):
	
	f = open("svg/"+name, "wb")
	pickle.dump(Ns, f)
	pickle.dump(RandomEspece, f)
	pickle.dump(StockaddT, f)
	pickle.dump(TIME, f)
	pickle.dump(Tm, f)
	pickle.dump(Hm, f)
	pickle.dump(ageglaciaire, f)
	pickle.dump(tour, f)
	pickle.dump(cycle, f)
	pickle.dump(Dageglaciaire, f)
	pickle.dump(Drechauff, f)
	pickle.dump(alivecreature, f)
	pickle.dump(brdG, f)
	pickle.dump(cases, f)
	pickle.dump(continentM, f)
	#pickle.dump(dicoImage, f) # sauver toutes les images avec le nom associé du dictionnaire
	pickle.dump(especes, f)
	pickle.dump(humidite, f)
	pickle.dump(humidite2, f)
	pickle.dump(temperature, f)
	pickle.dump(temperature2, f)
	pickle.dump(listedevolcans, f)
	pickle.dump(machD, f)
	pickle.dump(machDz, f)
	pickle.dump(mission_en_cours, f)
	pickle.dump(nom, f)
	pickle.dump(nourriture, f)
	pickle.dump(numero_mission, f)
	pickle.dump(pT, f)
	pickle.dump(pause1, f)
	pickle.dump(pause2, f)
	pickle.dump(pointC, f)
	pickle.dump(pointF, f)
	pickle.dump(pointH, f)
	pickle.dump(pointS, f)
	pickle.dump(rechauffement, f)
	pickle.dump(xs, f)
	pickle.dump(ys, f)
	pickle.dump(yeuxP, f)
	pickle.dump(listC, f)
	pickle.dump(listnom, f)
	pickle.dump(listeyear, f)
	pickle.dump(svgmuteur1, f)
	pickle.dump(svgmuteur2, f)
	pickle.dump(dicoContinent, f)
	pickle.dump(dicoXcon, f)
	pickle.dump(dicoYcon, f)
	pickle.dump(dicoNcon, f)
	for filename_,im in dicoImage.items():
		pygame.image.save(im,"svg/"+name+filename_+".png")
	pickle.dump(volcanMAP, f)
	pickle.dump(volcan_date, f)
	pickle.dump(rayon, f)
	pickle.dump(xv_, f)
	pickle.dump(yv_, f)
	pickle.dump(meteorMAP, f)
	pickle.dump(meteor_date, f)
	pickle.dump(rayonm, f)
	pickle.dump(x_, f)
	pickle.dump(y_, f)
	pickle.dump(flash, f)
	pickle.dump(flash1, f)
	pickle.dump(dicoVcon, f)
	pickle.dump(LISTEmeanhum, f)
	pickle.dump(LISTEmeant, f)
	pickle.dump(tremb_date, f)
	pickle.dump(xmov, f)
	pickle.dump(ymov, f)
	pickle.dump(CURSE, f)
	pickle.dump(BIGSCORE, f)
	pickle.dump(ex, f)
	pickle.dump(tuto_step, f)
	f.close()
	return
def chargement(name):
	global tuto_step,ex,BIGSCORE,CURSE,xmov,ymov,flash1,dicoVcon,LISTEmeanhum,LISTEmeant,tremb_date, volcanMAP,meteorMAP,volcan_date,meteor_date,rayon,rayonm,xv_,yv_,x_,y_,flash, dicoContinent,dicoNcon,dicoXcon,dicoYcon,nomL,listnom,listeyear,svgmuteur1,svgmuteur2,zoom,yD,xD,Xl,Yl,listC,Ns,RandomEspece,StockaddT,TIME,Tm,Hm,ageglaciaire,tour,cycle,Dageglaciaire,Drechauff,alivecreature,brdG,cases,continentM,dicoImage,especes,humidite,humidite2,temperature,temperature2,listedevolcans,machD,machDz,mission_en_cours,nom,nourriture,numero_mission,pT,pause1,pause2,pointC,pointF,pointH,pointS,rechauffement,xs,ys,yeuxP
	zoom=1
	yD=0
	xD=0
	f = open("svg/"+name, "rb")
	Ns=pickle.load(f)
	RandomEspece=pickle.load(f)
	StockaddT=pickle.load(f)
	TIME=pickle.load(f)
	Tm=pickle.load(f)
	Hm=pickle.load(f)
	ageglaciaire=pickle.load(f)
	tour=pickle.load(f)
	cycle=pickle.load(f)
	Dageglaciaire=pickle.load(f)
	Drechauff=pickle.load(f)
	alivecreature=pickle.load(f)
	brdG=pickle.load(f)
	cases=pickle.load(f)
	continentM=pickle.load(f)
	#dicoImage=pickle.load(f)
	especes=pickle.load(f)
	humidite=pickle.load(f)
	humidite2=pickle.load(f)
	temperature=pickle.load(f)
	temperature2=pickle.load(f)
	listedevolcans=pickle.load(f)
	machD=pickle.load(f)
	machDz=pickle.load(f)
	mission_en_cours=pickle.load(f)
	nom=pickle.load(f)
	nourriture=pickle.load(f)
	numero_mission=pickle.load(f)
	pT=pickle.load(f)
	pause1=pickle.load(f)
	pause2=pickle.load(f)
	pointC=pickle.load(f)
	pointF=pickle.load(f)
	pointH=pickle.load(f)
	pointS=pickle.load(f)
	rechauffement=pickle.load(f)
	xs=pickle.load(f)
	ys=pickle.load(f)
	yeuxP=pickle.load(f)
	listC=pickle.load(f)
	listnom=pickle.load(f)
	listeyear=pickle.load(f)
	svgmuteur1=pickle.load(f)
	svgmuteur2=pickle.load(f)
	dicoContinent=pickle.load(f)
	dicoXcon=pickle.load(f)
	dicoYcon=pickle.load(f)
	dicoNcon=pickle.load(f)
	volcanMAP=pickle.load(f)
	volcan_date=pickle.load(f)
	rayon=pickle.load(f)
	xv_=pickle.load(f)
	yv_=pickle.load(f)
	meteorMAP=pickle.load(f)
	meteor_date=pickle.load(f)
	rayonm=pickle.load(f)
	x_=pickle.load(f)
	y_=pickle.load(f)
	flash=pickle.load(f)
	flash1=pickle.load(f)
	dicoVcon=pickle.load(f)
	LISTEmeanhum=pickle.load(f)
	LISTEmeant=pickle.load(f)
	tremb_date=pickle.load(f)
	xmov=pickle.load(f)
	ymov=pickle.load(f)
	CURSE=pickle.load(f)
	BIGSCORE=pickle.load(f)
	ex=pickle.load(f)
	tuto_step=pickle.load(f)
	pygame.display.set_caption("Evolve in "+nom)
	Xl=[]
	Yl=[]
	nomL=[]
	ldir=os.listdir('svg/')
	dicoImage={}
	for i in range(0,len(ldir)):
		
		if ldir[i][0:len(name)]==name and ldir[i]!=name:
			
			dicoImage[ldir[i][len(name):len(ldir[i])-4]]=pygame.image.load('svg/'+ldir[i])
	f.close()

text_addt=' '
numbers=[0,1,2,3]
poids=[1,3,3,3]
flash=0
xv_=0
yv_=0
x_=0
y_=0


xmov=0
ymov=0
LISTEmeant=[]
LISTEmeanhum=[]
for j in range(0,70):
	Komp=1
	meant=0    
	meanhum=0
	for g in range(0,139):
		if cases[g][min(max(j,0),69)] not in ['monts','coldm','hotmt','water','coldw','tropw','glace','crate','meteo','volca','magma','cotes','mangr','glacC']:
			Komp=Komp+1
			meant=meant+temperature[g][min(max(j,0),69)]
			meanhum=meanhum+humidite[g][min(max(j,0),69)]
	meant=meant/Komp
	meanhum=meanhum/Komp
	if j<5 or j>64 and meant==0:
		meant=-15
	LISTEmeanhum.append(meanhum)
	if j==0:
		LISTEmeant.append(meant)
	if j<35 and j>0:
		LISTEmeant.append(max(meant,LISTEmeant[-1]))
	if j>34:
		LISTEmeant.append(min(meant,LISTEmeant[-1]))
		



Ltemp=[]
Lhum=[]
for j in range(0,70):
	Ltemp.append(LISTEmeant[(j-1)%70]*0.3+LISTEmeant[(j+1)%70]*0.3+LISTEmeant[j]*0.4)
	Lhum.append(LISTEmeanhum[(j-1)%70]*0.3+LISTEmeanhum[(j+1)%70]*0.3+LISTEmeanhum[j]*0.4)
flash1=0
LISTEmeant=Ltemp
LISTEmeanhum=Lhum
#plt.plot(np.linspace(0,69,70),LISTEmeant)
#plt.show()
while q==0:
	
	if tour>=volcan_date and tour<=volcan_date+20:
		if tour==volcan_date:
			xy=choice(listedevolcans)
			xv_=xy[0]
			yv_=xy[1]
		erupt_volcan(xv_,yv_)
		if continentM[xv_][yv_]==(0,0,0):
			cv=(randint(0,255),randint(0,255),randint(0,255))
			dicoXcon[cv]=xv_
			dicoYcon[cv]=yv_
			dicoNcon[cv]=1
			dicoVcon[cv]=(randint(-1,1),randint(-1,1))
			liste=['a','e','i','u','o','y','a','e','i','u','o','ou','ai','ei','ui']
			liste2=['b','c','d','f','g','h','j','k','l','m','n','p','qu','r','s','t','v','w','x','z','b','c','d','f','g','j','k','l','m','n','p','r','s','t','v']
			if randint(0,2)==1:
				nomc=choice(liste2)[0].upper()
			else:
				nomc=choice(liste)[0].upper()
				nomc=nomc+choice(liste2)
			liste2.append('ss')
			liste2.append('tt')
			liste2.append('ll')
			for g in range(0,randint(1,3)):
				nomc=nomc+choice(liste)
				nomc=nomc+choice(liste2)
			if randint(0,1)==1:
				nomc=nomc+choice(liste)
			dicoContinent[cv]=nomc
			continentM[xv_][yv_]=cv
			
		if tour==volcan_date+20:
			volcan_date=volcan_date+20+randint(300,700)
			if (volcan_date-meteor_date)<40:
				volcan_date=volcan_date+80
			flash=0
			
	if tour>=meteor_date and tour<=meteor_date+20:
		if tour==meteor_date:
			
			x_=(xs+randint(10,119))%140
			y_=randint(0,69)
			cases[x_][y_]='meteo'
			temperature[x_][y_]=200
		chute_meteor(x_,y_)
		if tour==meteor_date+20:
			meteor_date=meteor_date+20+randint(300,700)
			if (volcan_date-meteor_date)<40:
				meteor_date=meteor_date+80
			flash=0
	if tour==tremb_date-1:
		flash1=0
		xmov=randint(0,139)
		ymov=randint(0,69)
		while continentM[xmov][ymov]==(0,0,0):
			xmov=randint(0,139)
			ymov=randint(0,69)
	if tour==tremb_date:
		moveCont(continentM[xmov][ymov],dicoVcon[continentM[xmov][ymov]])
		tremb_date=tremb_date+randint(100,200)
		while tremb_date-meteor_date<21 or tremb_date-volcan_date<21:
			tremb_date=tremb_date+30
	
	if chargeur!=0:
		chargement(chargeur)
		chargeur=0
	action=0
	if tour%cycle==pause1:
		StockaddT=randint(-13,-8)
		addTemp=0
	if tour%cycle<Dageglaciaire+pause1 and tour%cycle>pause1:
		ageglaciaire=1
		AG=1
		if tour%cycle>Dageglaciaire+pause1+StockaddT:
			addTemp=addTemp+1
		if tour%cycle>pause1 and tour%cycle<pause1-StockaddT:
			addTemp=addTemp-1
	
	if tour%cycle==pause1+Dageglaciaire+pause2:
		StockaddT=randint(8,13)
		addTemp=0
		RG=1
	if tour%cycle<Dageglaciaire+pause1+Drechauff+pause2 and tour%cycle>pause1+Dageglaciaire+pause2:
		rechauffement=1
		if tour%cycle>Dageglaciaire+pause1+pause2 and tour%cycle<Dageglaciaire+pause1+pause2+StockaddT:
			addTemp=addTemp+1
		if tour%cycle>Dageglaciaire+pause1+pause2+Drechauff-StockaddT :
			addTemp=addTemp-1
	
	if tour%cycle<pause1 or (tour%cycle<pause1+Dageglaciaire+pause2 and tour%cycle>pause1+Dageglaciaire):
		addTemp=0
		ageglaciaire=0
		rechauffement=0
		AG=1
		RG=1
	if tour==0:
		while KEY[K_RETURN]==0:
			for event in pygame.event.get():
				KEY=pygame.key.get_pressed()
			fenetre.blit(pygame.image.load('flug.png'),(350,0))
			fenetre.blit(pygame.image.load('boutonpresent.png'),(550,300))
			pygame.display.flip()
		pygame.time.wait(100)
	print(tour)
	tour=tour+1
	if especes.at['monEspece','pop']<=0:
		fenetre.blit(pygame.image.load('boutondead.png'),(550,300))
		if tour<=5000:
			txt = font.render(RandomEspece.at['monEspece','nominem'], True, (0,0,0))
			ltxt=txt.get_width()//2
			fenetre.blit(txt,(700-ltxt,360))
			pygame.display.flip()
			BIGSCORE=((np.sum(brdG)//500)+BIGSCORE+tour//10)*CURSE
			if CURSE!=0:
				txt = font.render('score: '+str(BIGSCORE), True, (0,0,0))
				ltxt=txt.get_width()//2
				fenetre.blit(txt,(700-ltxt,420))
				file1 = open("scoreliste", "rb")
				bestscore=pickle.load(file1)
				bestcreat=pickle.load(file1)
				bestscore.append(BIGSCORE)
				bestcreat.append(RandomEspece.at['monEspece','nominem'])
				bestcreat=[x for _,x in sorted(zip(bestscore,bestcreat))]
				bestscore=sorted(bestscore)
				bestscore=bestscore[1:]
				bestcreat=bestcreat[1:]
				file1.close()
				f2 = open("scoreliste", "wb")
				pickle.dump(bestscore, f2)
				pickle.dump(bestcreat, f2)
				f2.close()
		while q==0:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					q=1
					pygame.quit()
					sys.exit()
	if TIME<=0:
		especes.at['monEspece','pop']=especes.at['monEspece','pop']*(1-0.90-random()*0.09)
		TIME=500+(1-CURSE)*150+1			
		
	TIME=TIME-1
	Time.append(tour)
	PopTr.append(especes.at['monEspece','pop']*1000)
	
	if tour%20==19:
		savefilm(tour)
		listeyear.append(tour)
		sauvegarde('autosave')
	
	if mission_en_cours.check_complete()==1 and CURSE!=0:
		numero_mission=numero_mission+1
		TIME=TIME+mission_en_cours.time()
		son.play()
		text_addt='+'+str(mission_en_cours.time())
		pygame.display.flip()
		BIGSCORE=BIGSCORE+1
		if numero_mission>2:
			mission_en_cours=mission(choices(numbers,poids,k=1)[0])
		if numero_mission==2:
			mission_en_cours=mission(1)
	
	
	createMAP()
	especes.at['monEspece','X']=xs
	especes.at['monEspece','Y']=ys
	
	Xl=[]
	Yl=[]
	nomL=[]
	Xl2=[]
	Yl2=[]
	comptour=-1
	for j in especes.iterrows():
		comptour=comptour+1
		if especes.at[j[0],'pop']>0:
			xs1=especes.at[j[0],'X']
			ys1=especes.at[j[0],'Y']
			BIO=caracterebiome.loc[cases[xs1][ys1]]
			if randint(0,6)==0 and especes.at[j[0],'pop']>0:
				mutation(0,j[0])
			if randint(0,75)==0 and especes.at[j[0],'pop']>0:
				mutation(1,j[0])
			if randint(0,1000)==0 and especes.at[j[0],'pop']>0:
				RandomEspece.at[j[0],'bras']=(RandomEspece.at[j[0],'bras']+1)%2
				if cases[xs1][ys1] in ['glacC','glace','water','cotes','coldw','tropw','mangr']:
					RandomEspece.at[j[0],'bras']=0
			if randint(0,1000)==0 and especes.at[j[0],'pop']>0 :
				if RandomEspece.at[j[0],'vertebre']>8 and randint(1,2)==1:
					RandomEspece.at[j[0],'nbjambe']=3
				else:
					RandomEspece.at[j[0],'nbjambe']=2
			if randint(0,40+Ns*2)==0 and especes.at[j[0],'pop']>300 and j[0]!='monEspece':
				if cases[xs1][ys1]=='water' :
					if randint(0,1)==0:
						Ns=Ns+1
						split(Ns,j[0],comptour)
						#RandomEspece.at['Espece'+str(Ns),'distmu']=[0.0]
						RandomEspece.at['Espece'+str(Ns),'Tmu']=[tour]
				else:
					if randint(0,1)==0:
						Ns=Ns+1
						split(Ns,j[0],comptour)
						#RandomEspece.at['Espece'+str(Ns),'distmu']=[0.0]
						RandomEspece.at['Espece'+str(Ns),'Tmu']=[tour]
			
			if randint(0,max(50*alivecreature,1000))<alivecreature and j[0]!='monEspece' and  (cases[xs1][ys1]=='water' or  cases[xs1][ys1]=='glace')==True:
				especes.at[j[0],'pop']=floor(especes.at[j[0],'pop']*0.05)
				
				if especes.at[j[0],'pop']<1:
					RandomEspece.at[j[0],'deadT']=tour
					alivecreature=alivecreature-1
			
			Manip=especes.loc[j[0]]
			compt=-1
			desadapt=0
			for k in Manip:
				compt=compt+1
				if compt>2 and compt<6:
					desadapt=desadapt+abs(k-BIO[compt-3])
					if abs(k-BIO[compt-3])>0.01:
						if k>BIO[compt-3]:
							especes.at[j[0],caracterebiome.columns[compt-3]]=k-0.1
						if k<BIO[compt-3]:
							especes.at[j[0],caracterebiome.columns[compt-3]]=k+0.1
			niam=(nourriture[xs1][ys1]-max(0,especes.at[j[0],'pop']-500))/5000
			nourriture[xs1][ys1]=max(nourriture[xs1][ys1]-especes.at[j[0],'pop'],0)
			if especes.at[j[0],'pop']!=0 and int(especes.at[j[0],'pop']*(1+niam-desadapt/5))<1:
				RandomEspece.at[j[0],'deadT']=tour
				alivecreature=alivecreature-1
			especes.at[j[0],'pop']=int(especes.at[j[0],'pop']*(1+niam-desadapt/5))
			RandomEspece.at[j[0],'tete']=max(RandomEspece.at[j[0],'tete'],especes.at[j[0],'respire'])
			if tour-RandomEspece.at[j[0],'Tmu'][0]>50:
				RandomEspece.at[j[0],'tete']=max(RandomEspece.at[j[0],'tete'],min(2.5*(tour-RandomEspece.at[j[0],'Tmu'][0]-50)/50,2.5))
			
			if RandomEspece.at[j[0],'nageoire']<2.5-especes.at[j[0],'respire']:
				RandomEspece.at[j[0],'nageoire']=RandomEspece.at[j[0],'nageoire']+0.1
			if RandomEspece.at[j[0],'nageoire']>2.5-especes.at[j[0],'respire']:
				RandomEspece.at[j[0],'nageoire']=max(RandomEspece.at[j[0],'nageoire']-0.1,0)
			
			
			RandomEspece.at[j[0],'jambe']=min(especes.at[j[0],'respire']/2.5,1)
			#lC1=[RandomEspece.loc[j[0]]['acol1']]
			#lC2=[RandomEspece.loc[j[0]]['acol2']]
			#for i in ['plain','tunda','svane','glace','plai2','cotes','water','deser','mangr','jungl','foret','stepe','forbo']:
			
				#if max(1-Desadapteur(i,j[0])/2,0)>0.5:
					#lC1.append(changecolor(max(1-Desadapteur(i,j[0]),0),RandomEspece.loc[j[0]]['color1'],caracterebiome.loc[i]['color1']))
					#lC2.append(changecolor(max(1-Desadapteur(i,j[0]),0),RandomEspece.loc[j[0]]['color2'],caracterebiome.loc[i]['color2']))
					#lC1.append(changecolor(max(1-Desadapteur(i,j[0]),0),RandomEspece.loc[j[0]]['color1'],caracterebiome.loc[i]['color1']))
					#lC2.append(changecolor(max(1-Desadapteur(i,j[0]),0),RandomEspece.loc[j[0]]['color2'],caracterebiome.loc[i]['color2']))
			#c1=0
			#c2=0
			#c3=0
			#for i in lC1:
				#c1=i[0]+c1
				#c2=i[1]+c2
				#c3=i[2]+c3
			#C1=RandomEspece.at[j[0],'acol1']
			#RandomEspece.at[j[0],'acol1']=(0.5*(c1/len(lC1)+C1[0]),0.5*(c1/len(lC1)+C1[1]),0.5*(c3/len(lC1)+C1[2]))
			
			#c1=0
			#c2=0
			#c3=0
			#for i in lC2:
				#c1=i[0]+c1
				#c2=i[1]+c2
				#c3=i[2]+c3
			#C2=RandomEspece.at[j[0],'acol2']
			#RandomEspece.at[j[0],'acol2']=(0.5*(c1/len(lC2)+C2[0]),0.5*(c2/len(lC2)+C2[1]),0.5*(c3/len(lC2)+C2[2]))
		if j[0]!='monEspece':
			MAP.blit(US2,(xs1*10+2,ys1*10+2))
			Xl2.append(especes.at[j[0],'X'])
			Yl2.append(especes.at[j[0],'Y'])
			if especes.at[j[0],'pop']>0:
				pax=0
				pay=0
				choox=1000
				add1=0
				add2=0
				for u1 in [1,-1,0]:
					for u2 in [1,-1,0]:
						if u1!=0 or u2!=0:
							ps=0
							if (ys1!=69 or u2!=+1)==True and (ys1!=0 or u2!=-1)==True:
								ps=selector((xs1+u1)%140,(ys1+u2)%70,j[0])#teleporte sud nord
							if cases[(xs1+u1)%140][(ys1+u2)%70]=='cotes' and  (cases[xs1][ys1]=='water' or cases[xs1][ys1]=='cotes')==True and especes.at[j[0],'pop']>100:
								add1=0.5+np.random.normal(1,0.6)
							else:
								add1=0
							if cases[(xs1+u1)%140][(ys1+u2)%70]=='plain' and  (cases[xs1][ys1]=='cotes' or cases[xs1][ys1]=='plain')==True and especes.at[j[0],'pop']>200 and especes.at[j[0],'respire']<2.2:
								add2=2+np.random.normal(1,0.6)
							else:
								add2=0
							if choox+np.random.normal(0,0.6+0.2*alivecreature/(20+RandomEspece.at['monEspece','child']))+add1+add2>ps:
								pax=u1
								pay=u2
								choox=ps
				if especes.at[j[0],'Y']==0 and pay==-1:
					pay=1
				if especes.at[j[0],'Y']==69 and pay==1:
					pay=-1
				especes.at[j[0],'X']=(especes.at[j[0],'X']+pax)%140
				especes.at[j[0],'Y']=(especes.at[j[0],'Y']+pay)%70
			if especes.at[j[0],'pop']>0:
				Xl.append(especes.at[j[0],'X'])
				Yl.append(especes.at[j[0],'Y'])
				nomL.append(j[0])
	chargeur=0
	while action==0:
		fenetre.blit(noir,(350,0))
		KEY=pygame.key.get_pressed()
		if KEY[K_SPACE]==1:
			action=1
		#if KEY[K_0]==1:
			#print('save')
			#sauvegarde('1')
		#if KEY[K_9]==1:
			#chargeur=1
			#action=1
			##chargement('1')
			#print('load')
		
		clic=pygame.mouse.get_pressed()# mettre while nothing done
		mous=pygame.mouse.get_pos()
		if abs(mous[0]-1225)<150:
			if abs(mous[1]-(255))<40:
				pygame.mouse.set_cursor(*pygame.cursors.diamond)
				if clic[0]==1 and especes.at['monEspece','pop']>700:
					Ns=Ns+1
					split(Ns,'monEspece',0)
					mission_en_cours.validate(0)
					#RandomEspece.at['Espece'+str(Ns),'distmu']=[0.0]
					RandomEspece.at['Espece'+str(Ns),'Tmu']=[tour]
		
		
		vue=pygame.Surface((70,70),pygame.SRCALPHA, 32)
		MAP.blit(US,(xs*10+2,ys*10+2))
		vue.blit(MAP,(-xs*10+1+30,-ys*10+1+30))
		if xs>134:
			vue.blit(MAP,(-xs*10+1+30+1400,-ys*10+1+30))
		if xs<5:
			vue.blit(MAP,(-xs*10+1+30-1400,-ys*10+1+30))
		vue=pygame.transform.scale(vue,(70*10,70*10))
		
		
		ugh=-1
		for j in especes.iterrows():
			if j[0]!='monEspece':
				ugh=ugh+1
				
				xs1=Xl2[ugh]
				ys1=Yl2[ugh]
				
				op1,op2=np.sign(xs-xs1)*min(abs(xs-xs1),140-abs(xs-xs1)),np.sign(ys-ys1)*min(abs(ys-ys1),140-abs(ys-ys1))#pb avec le bord en x
				if abs(op1)<4 and abs(op2)<4 and especes.at[j[0],'pop']>0:
					vue.blit(dicoImage[j[0]],(650-100*op1-350,300-100*op2))
					if abs(mous[0]-(700-100*op1))<50:
						if abs(mous[1]-(350-100*op2))<50:
							if j[0]!='monEspece':
								text = font.render(RandomEspece.at[j[0],'nominem'], True, (255,255,255))
								vue.blit(text,(mous[0]+50-350,mous[1]-50))
							
		vue.blit(dicoImage['monEspece'],(300,300))
		fenetre.blit(vue,(350,0))
		pygame.draw.line(fenetre, (0,0,0),(350,0),(350,700),10)
		pygame.draw.line(fenetre, (0,0,0),(1050,0),(1050,700),10)
		
		if (tour==volcan_date+1 or tour==meteor_date+1) and flash==0:
			son1=pygame.mixer.Sound("erupteur.ogg")
			son1.play()
			pygame.time.wait(100)
			for w in range(1,200):
				fenetre.blit(vue,(350+(randint(-2,2)+cos(w/10))*abs(4-w/50),0))
				fenetre.blit(whiteflash(w/10),(350,0))
				pygame.draw.line(fenetre, (0,0,0),(350,0),(350,700),10)
				pygame.draw.line(fenetre, (0,0,0),(1050,0),(1050,700),10)	
				pygame.time.wait(40)
				pygame.display.flip()
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
					
			flash=1
		if (tour==tremb_date) and flash1==0:
			son1=pygame.mixer.Sound("gronde.ogg")
			dx=xs-xmov
			dy=ys-ymov
			son1.play()
			for w in range(1,25):
				fenetre.blit(vue,(350+((randint(-2,2)+cos(w/10))*abs(2-2*w/25))*min(100/(dx**2+dy**2)**0.5,2),0))
				pygame.draw.line(fenetre, (0,0,0),(350,0),(350,700),10)
				pygame.draw.line(fenetre, (0,0,0),(1050,0),(1050,700),10)	
				pygame.time.wait(40)
				pygame.display.flip()
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
					
			flash1=1
		clic=pygame.mouse.get_pressed()# mettre while nothing done
		mous=pygame.mouse.get_pos()
		if showworld==0 and (showtree==0 and showcreature==0):
			if (abs(mous[0]-700)<150 and abs(mous[1]-350)<150) or (abs(mous[1]-350)<150 and abs(mous[0]-700)<150):
				if ys+(mous[1]//100)-3>-1 and ys+(mous[1]//100)-3<70:
					xq=xs
					yq=ys
					if mous[0]<650:
						xq=(xs-1)%140
						
					if mous[0]>750:
						xq=(xs+1)%140
						
					if mous[1]<300 and ys>0:
						yq=ys-1
						
					if mous[1]>400 and ys<69:
						yq=ys+1
					drr=selector(xq,yq,'monEspece')
					if drr<0:
						select.fill((max(floor(255*(drr+0.5)/0.5),0),255,0), special_flags=pygame.BLEND_RGBA_MULT)
						
					else:
						select.fill((255,max(floor(255*(-drr+2.5)/2.5),0),0), special_flags=pygame.BLEND_RGBA_MULT)
						
					fenetre.blit(select,((((mous[0]-50)//100)*100)+50,((mous[1]//100)*100)))
					biomemontre(cases[xq][yq])
					fenetre.blit(biomeshow,(mous[0],mous[1]))
					select=pygame.image.load("select.png").convert_alpha()
				if clic[0]==1:
					if mous[0]<650:
						xs=(xs-1)%140
						action=1
					if mous[0]>750:
						xs=(xs+1)%140
						action=1
					if mous[1]<300 and ys>0:
						ys=ys-1
						action=1
					if mous[1]>400 and ys<69:
						ys=ys+1
						action=1
					
			if abs(mous[0]-1225)>150 or  abs(mous[1]-(255))>40:
				pygame.mouse.set_cursor(*pygame.cursors.arrow)	
			if abs(mous[0]-1385)<15:
				if abs(mous[1]-685)<15:
					pygame.mouse.set_cursor(*pygame.cursors.diamond)
					if clic[0]==1:
						numero_mission=numero_mission+1
						TIME=TIME-mission_en_cours.time()//2
						text_addt='-'+str(mission_en_cours.time()//2)
						pygame.display.flip()
						mission_en_cours=mission(choices(numbers,poids,k=1)[0])
						pygame.time.wait(100)
			
			if abs(mous[0]-175)<150:
				if abs(mous[1]-(315+40))<40:
					pygame.mouse.set_cursor(*pygame.cursors.diamond)
					if clic[0]==1:
						showworld=1
						MAP2sec=MAP.copy()
						createMAP()
			if abs(mous[0]-175)<150:
				if abs(mous[1]-(115+40))<40:
					pygame.mouse.set_cursor(*pygame.cursors.diamond)
					if clic[0]==1:
						loadingscreen=pygame.image.load("menusavegame.png")
						T0='default'
						pygame.key.set_repeat()
						com=0
						alt=1
						while KEY[K_RETURN]==0 and KEY[K_ESCAPE]==0:
							lettre=0
							com=(com+1)%1000
							for event in pygame.event.get():
								if event.type==MOUSEBUTTONUP:
									if event.button==5:
										curseur=(curseur+1)
									if event.button==4:
										curseur=(curseur-1)
								if event.type == KEYDOWN:
								
									if event.unicode!="\x08" and event.key!=13:
										lettre=event.unicode
									if event.unicode=="\x08" or event.unicode=="":
										lettre=-1
								if event.type == pygame.USEREVENT:# each while loop
									pygame.mixer.music.load(choice(playlist))
									if musicplayed==1:
										pygame.mixer.music.play()
							KEY=pygame.key.get_pressed()
							mous=pygame.mouse.get_pos()
							clic=pygame.mouse.get_pressed()
							fenetre.blit(loadingscreen,(700-300//2,100))
							fenetre.blit(pygame.image.load("valideur.png"),(240+700-300//2,110+100))
							fenetre.blit(pygame.image.load("closeur.png"),(270+700-300//2,100))
							#(700, 225+i*50+50)
							ululu='a'
							if abs(mous[0]-700)<150 and abs(mous[1]-(225+50+125))<125:
								pygame.mouse.set_cursor(*pygame.cursors.tri_left)
								if clic[0]==1:
									ululu=(mous[1]-(225+25))//50
							else:
								pygame.mouse.set_cursor(*pygame.cursors.diamond)
							if com%150==0:
								alt=-alt
							L0=choosesave(lettre,ululu,alt)
							pygame.display.flip()
							if KEY[K_RETURN]==1:
								sauvegarde(T0)
							if abs(mous[1]-115)<15:
								if abs(mous[0]-(285+700-300//2))<15:
									if clic[0]==1:
										break
							if abs(mous[1]-225)<15:
								if abs(mous[0]-(255+700-300//2))<15:
									if clic[0]==1:			
										sauvegarde(T0)
										break
								
			if abs(mous[0]-175)<150:
				if abs(mous[1]-(215+40))<40:
					pygame.mouse.set_cursor(*pygame.cursors.diamond)
					if clic[0]==1:
						loadingscreen=pygame.image.load("menuloadgame.png")
						
						pygame.key.set_repeat()
						while KEY[K_RETURN]==0 and KEY[K_ESCAPE]==0:
							mous=pygame.mouse.get_pos()
							clic=pygame.mouse.get_pressed()
							for event in pygame.event.get():
								KEY=pygame.key.get_pressed()
								if event.type==KEYDOWN:
									if KEY[K_DOWN]:
										curseur=(curseur+1)
									if KEY[K_UP]:
										curseur=(curseur-1)
								if event.type==MOUSEBUTTONUP:
									if event.button==5:
										curseur=(curseur+1)
									if event.button==4:
										curseur=(curseur-1)
									if abs(mous[0]-700)<150 and abs(mous[1]-(225+50+125))<125:#
										
										if event.button==1:
											ululu=(mous[1]-(225+25))//50
											curseur=curseur+ululu+1

								if event.type == pygame.USEREVENT:# each while loop
									pygame.mixer.music.load(choice(playlist))
									if musicplayed==1:
										pygame.mixer.music.play()
								
							KEY=pygame.key.get_pressed()
							fenetre.blit(loadingscreen,(700-300//2,100))
							fenetre.blit(pygame.image.load("valideur.png"),(240+700-300//2,110+100))
							fenetre.blit(pygame.image.load("closeur.png"),(270+700-300//2,100))
							L0=choosegame()
							
									
							
							pygame.display.flip()
							if KEY[K_RETURN]==1:
								chargeur=L0[(curseur)%len(L0)]
								action=1
								fenetre.blit(pygame.image.load("loadcircle.png"),(700-300//2,330))
								pygame.display.flip()
							if abs(mous[1]-650)<50:
								if abs(mous[0]-700)<150:
									if clic[0]==1:
										blug=0
										
										while blug==0:
											for event in pygame.event.get():
												KEY=pygame.key.get_pressed()
											KEY=pygame.key.get_pressed()
											mous=pygame.mouse.get_pos()
											clic=pygame.mouse.get_pressed()
											deleteur=pygame.image.load("deleteur.png")	
											fenetre.blit(deleteur,(600,250))
											pygame.display.flip()
											if abs(mous[1]-350)<40:
												if abs(mous[0]-650)<40:
													if clic[0]==1:
														blug=1
														L_file=os.listdir('svg/')
														for qua in L_file:
															if qua[0:len(L0[(curseur)%len(L0)])]==L0[(curseur)%len(L0)]:
																os.remove('svg/'+qua)
												if abs(mous[0]-750)<40:
													if clic[0]==1:
														blug=1
							if abs(mous[1]-115)<15:
								if abs(mous[0]-(285+700-300//2))<15:
									if clic[0]==1:
										break
							if abs(mous[1]-225)<15:
								if abs(mous[0]-(255+700-300//2))<15:
									if clic[0]==1:			
										chargeur=L0[(curseur)%len(L0)]
										action=1
										fenetre.blit(pygame.image.load("loadcircle.png"),(700-300//2,330))
										pygame.display.flip()
										break
			if abs(mous[0]-1040)<10:
				if abs(mous[1]-(10))<10:
					pygame.mouse.set_cursor(*pygame.cursors.diamond)
					if clic[0]==1:
						musicplayed=-musicplayed
						if musicplayed==-1:
							pygame.mixer.music.pause()
						else:
							pygame.mixer.music.unpause()
						pygame.time.wait(100)
			if abs(mous[0]-175)<150:
				if abs(mous[1]-(515+40))<40:
					pygame.mouse.set_cursor(*pygame.cursors.diamond)
					if clic[0]==1:
						showworld=1
						MAP2sec=MAP.copy()
						showhum=1
						createMAP()
			if abs(mous[0]-175)<150:
				if abs(mous[1]-(415+40))<40:
					pygame.mouse.set_cursor(*pygame.cursors.diamond)
					if clic[0]==1:
						showworld=1
						MAP2sec=MAP.copy()
						showtemp=1
						createMAP()
			if abs(mous[0]-175)<150:
				if abs(mous[1]-(615+40))<40:
					pygame.mouse.set_cursor(*pygame.cursors.diamond)
					if clic[0]==1:
						showCont=1
						showworld=1
						MAP2sec=MAP.copy()
						createMAP()
			if abs(mous[0]-1225)<150:
				if abs(mous[1]-(155))<40:
					pygame.mouse.set_cursor(*pygame.cursors.diamond)
					if clic[0]==1:
						plt.title('Demography')
						plt.xlabel('time in 100 000 years')
						plt.ylabel('population in individues')
						plt.plot(Time,PopTr)
						plt.show()
			if abs(mous[0]-1225)<150:
				if abs(mous[1]-(55))<40:
					pygame.mouse.set_cursor(*pygame.cursors.diamond)
					if clic[0]==1:
						showcreature=1
			if abs(mous[0]-1225)<150:
				if abs(mous[1]-(355))<40:
					pygame.mouse.set_cursor(*pygame.cursors.diamond)
					if clic[0]==1:
						showtree=1
			
			if tuto_step<len(tutotext):
				if abs(mous[0]-615-350)<75:
					if abs(mous[1]-435)<15:
						pygame.mouse.set_cursor(*pygame.cursors.diamond)
						if clic[0]==1:
							tuto_step=len(tutotext)
				if abs(mous[0]-615-350)<75:
					if abs(mous[1]-665)<15:
						pygame.mouse.set_cursor(*pygame.cursors.diamond)
						if clic[0]==1:
							tuto_step+=1
							pygame.time.wait(300)
				if abs(mous[0]-85-350)<75:
					if abs(mous[1]-665)<15:
						pygame.mouse.set_cursor(*pygame.cursors.diamond)
						if clic[0]==1:
							tuto_step=max(tuto_step-1,0)
							pygame.time.wait(300)
			
		
		if showcreature==1:
			im=pygame.image.load("frise.png")
			font = pygame.font.Font('freesansbold.ttf', 18)
			ref=max(len(listeyear)-10,0)
			for k in range(0,min(10,len(listeyear))):
				x=int(k*1400/(10))
				age=(listeyear[ref+k]*541/5000)-541
				period=ListeEre[-1]
				for fg in DateEre:
					if age<-fg:
						period=ListeEre[DateEre.index(fg)-1]
						break
				pygame.draw.rect(im,Grad(colorERE[ListeEre.index(period)],age,period),(x,50,int(1400/(10)),50))
				pygame.draw.line(im,(255,0,0),(x,50),(x,100),2)
				txt = font.render(period, True, (255,255,255))
				im.blit(txt,(x,80))
			pygame.image.save(im,"frise2.png")	
			
			if bypass==0:
				curseur=0
				Espe=listC[curseur%len(listC)]
				chargescreen=pygame.image.load("menuload.png")
				fenetre.blit(chargescreen,(700-300//2,100))
				pygame.key.set_repeat()
				while KEY[K_RETURN]==0 and KEY[K_ESCAPE]==0:
					mous=pygame.mouse.get_pos()
					clic=pygame.mouse.get_pressed()		
					KEY=pygame.key.get_pressed()
					for event in pygame.event.get():
						KEY=pygame.key.get_pressed()
						if event.type==KEYDOWN:
							if KEY[K_UP]==1:
								curseur=(curseur-1)
							if KEY[K_DOWN]==1:
								curseur=(curseur+1)
						if event.type==MOUSEBUTTONUP:
							if event.button==5:
								curseur=(curseur+1)
								Espe=listC[curseur%len(listC)]
							if event.button==4:
								curseur=(curseur-1)
								Espe=listC[curseur%len(listC)]
							if abs(mous[0]-700)<150 and abs(mous[1]-(225+50+125))<125:#
								if event.button==1:
									ululu=(mous[1]-(225+25))//50
									curseur=curseur+ululu+1
									Espe=listC[curseur%len(listC)]
						if event.type == pygame.USEREVENT:# each while loop
							pygame.mixer.music.load(choice(playlist))
							if musicplayed==1:
								pygame.mixer.music.play()
					fenetre.blit(chargescreen,(700-300//2,100))
					fenetre.blit(pygame.image.load("valideur.png"),(240+700-300//2,110+100))
					fenetre.blit(pygame.image.load("closeur.png"),(270+700-300//2,100))
					chooseCreature()
					if KEY[K_ESCAPE]==1:
						showcreature=0
						font = pygame.font.Font('freesansbold.ttf', 25)
					
						
					if abs(mous[1]-115)<15:
						if abs(mous[0]-(285+700-300//2))<15:
							if clic[0]==1:
								showcreature=0
								font = pygame.font.Font('freesansbold.ttf', 25)
								break
					if abs(mous[1]-225)<15:
						if abs(mous[0]-(255+700-300//2))<15:
							if clic[0]==1:			
										
								break
					pygame.display.flip()
		
			
			else:
				Espe=bypass
			frame2=pygame.image.load("vide.png")
			
			txt = font.render(RandomEspece.at[Espe,'nominem'], True, (255,255,255))
			ltxt=(200-txt.get_width())//2
			frame2.blit(txt,(ltxt,100))
			pygame.image.save(frame2,"nom.png")
			display = (1400, 700)
			fenetre =pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL )
			
			
			
			
			glMatrixMode(GL_PROJECTION)
			gluPerspective(45, display[0] / display[1], 0.1, 500.0)
			glMatrixMode(GL_MODELVIEW)
			glLight(GL_LIGHT0, GL_POSITION,  (5, 5, 5, 1)) # point light from the left, top, front
			glLightfv(GL_LIGHT0, GL_AMBIENT, (0, 0, 0, 1))
			glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))
			glTranslatef(0.0, 0.0, -13)
			glEnable(GL_DEPTH_TEST)
			Bv=read('bouchever')
			
			Ms=read(RandomEspece.at[Espe,'machsupTYPE'])
			E=read('eye')
			Mi=read(RandomEspece.at[Espe,'machinfTYPE'])
			machD=0
			machDi=0
			machDz=0
			if RandomEspece.at[Espe,'machsupTYPE']=='smilcroco':
				machD=-0.35
				machDz=0.3
			if RandomEspece.at[Espe,'machsupTYPE']=='espad':
				machD=-0.25
			if RandomEspece.at[Espe,'machsupTYPE']=='cake':
				machD=-0.25
			if RandomEspece.at[Espe,'machsupTYPE']=='machsupsouris.sc1':
				machD=-0.25
			if RandomEspece.at[Espe,'machinfTYPE']=='pelikanlol':
				machDi=+0.25
			Ve=read(RandomEspece.at[Espe,'vertebreTYPE'])
			Na=read(RandomEspece.at[Espe,'nageoireTYPE'])
			Br=read(RandomEspece.at[Espe,'brasTYPE'])
			Ja=read(RandomEspece.at[Espe,'jambeTYPE'])
			Pp=read(RandomEspece.at[Espe,'piedTYPE'])
			Qu=read(RandomEspece.at[Espe,'queueTYPE'])
			angle=30
			recreate=0
			if yeuxP==0:
				ex=eyepos(Ms[0],Ms[3])
				yeuxP=1
			if showcreature==1:
				showAnim(-90,ex,Ms[3],Ve[3],Ja[3],Espe)# ici mettre 90
				
				r2 = glReadPixels(0,0,1400,1400,   GL_RGB,GL_FLOAT)
				
				profile=saveim2(r2)
				#
				decal=0
				xmou=700
				angle1=0
				
				frame2=pygame.image.load("taillecomp.png")
				hum=pygame.image.load("human.png")
				ty=RandomEspece.loc[Espe]['taille']*profile[1]/20
				tx=RandomEspece.loc[Espe]['taille']*profile[2]/20
				profpic=profile[0]
				tsc=min(1,16/ty)
				profilew=profile[1]
				if tx>ty:
					tsc=min(1,24/tx)
					ty=tx
					profilew=profile[2]
				hum=pygame.transform.scale(hum,(int(80*tsc),int(150*tsc)))
				t_x=(1.8/int(150*tsc))*int((ty*profile[1]*10)/profilew)
				t_y=(1.8/int(150*tsc))*int((ty*profile[2]*10)/profilew)
				ty=min(16,ty)
				profpic=pygame.transform.scale(profpic,(int((ty*1400)/profilew),int((ty*700)/profilew)))
				frame2.blit(hum,(30+80-int(40*tsc)-40,200-10-int(150*tsc)))
				lmin=profile[3]
				lmax=profile[4]
				hmin=profile[5]
				hmax=profile[6]
				pygame.draw.line(frame2,(255,255,255),(150,180),(150,180-int((ty*profile[1]*10)/profilew)),4)
				pygame.draw.line(frame2,(255,255,255),(147,180),(155,180),4)
				pygame.draw.line(frame2,(255,255,255),(147,180-int((ty*profile[1]*10)/profilew)),(155,180-int((ty*profile[1]*10)/profilew)),4)
				pygame.draw.line(frame2,(255,255,255),(160,187),(160,195),4)
				pygame.draw.line(frame2,(255,255,255),(160+int((ty*profile[2]*10)/profilew),187),(160+int((ty*profile[2]*10)/profilew),195),4)
				pygame.draw.line(frame2,(255,255,255),(160,190),(160+int((ty*profile[2]*10)/profilew),190),4)
				frame2.blit(profpic,(160-int((ty*lmin*10)/profilew),180-int((ty*700)/profilew)+int((ty*hmin*10)/profilew)))
				poid=str(round(t_x*t_y*30,2))
				txt = font.render(str(round(t_x,2))+'m x '+str(round(t_y,2))+'m'+' '+poid+'kg'+' biome '+dicoNbi[cases[especes.loc[Espe]['X']][especes.loc[Espe]['Y']]], True, (255,255,255))
				frame2.blit(txt,(10,10))
				
				pygame.image.save(frame2,"tailleecran.png")
				
				showAnim(angle,ex,Ms[3],Ve[3],Ja[3],Espe)
				r = glReadPixels(0,0,1400,1400,   GL_RGB,GL_UNSIGNED_BYTE)
				pygame.display.flip()
				saveim(r,Espe)
			scrollf=0
			change=0
			
			while showcreature==1:
				
				#angle=(angle+5)%360
				#print(angle)
				
				
				for event in pygame.event.get():
					KEY=pygame.key.get_pressed()
					mous2=pygame.mouse.get_pos()
					clic2=pygame.mouse.get_pressed()
					if event.type == pygame.QUIT:
						pygame.quit()
						sys.exit()
					if event.type == pygame.USEREVENT:# each while loop
						pygame.mixer.music.load(choice(playlist))
						if musicplayed==1:
							pygame.mixer.music.play()
					if event.type==MOUSEBUTTONUP:
							if event.button==5:
								if scrollf<len(listeyear)-10:
									scrollf=scrollf+1
									change=1
							if event.button==4:
								if scrollf>0:
									scrollf=scrollf-1
									change=1
				
				if clic2[0]==1 and mous2[1]<669:
					if decal==0:
						decal=1
						xmou=mous2[0]
					else:
						angle1=120*(mous2[0]-xmou)/700
						showAnim(angle+angle1,ex,Ms[3],Ve[3],Ja[3],Espe)
						pygame.display.flip()
				if clic2[0]==0 and angle1!=0 and mous2[1]<669:
					decal=0
					angle=angle1+angle
					angle1=0
				
				if change==1 and Espe=='monEspece':
					im=pygame.image.load("frise.png")
					font = pygame.font.Font('freesansbold.ttf', 18)
					ref=min(max(len(listeyear)-scrollf-10,0),max(len(listeyear)-10,0))
					for k in range(0,min(10,len(listeyear))):
						x=int(k*1400/(10))
						
						age=(listeyear[ref+k]*541/5000)-541
						period=ListeEre[-1]
						for fg in DateEre:
							if age<-fg:
								period=ListeEre[DateEre.index(fg)-1]
								break
						pygame.draw.rect(im,Grad(colorERE[ListeEre.index(period)],age,period),(x,50,int(1400/(10)),50))
						pygame.draw.line(im,(255,0,0),(x,50),(x,100),2)
						txt = font.render(period, True, (255,255,255))
						im.blit(txt,(x,80))
					pygame.image.save(im,"frise2.png")
					
					clear_buf()
					pygame.display.flip()
					update_frise()
					pygame.display.flip()
					
					change=0
					
					
				
				if abs(mous2[0]-696)<693 and abs(mous2[1]-682)<13 and clic2[0]==1 and Espe=='monEspece':
					
					
					#i=int((len(listeyear)+1)*mous2[0]/1400)
					i0=int((10)*mous2[0]/1400)
					if i0<min(10,len(listeyear)):
						im=pygame.image.load("frise.png")
						ref=max(len(listeyear)-10-scrollf,0)
						for k in range(0,min(10,len(listeyear))):
							x=int(k*1400/(10))
							age=(listeyear[ref+k]*541/5000)-541
							period=ListeEre[-1]
							for fg in DateEre:
								if age<-fg:
									period=ListeEre[DateEre.index(fg)-1]
									break
							pygame.draw.rect(im,Grad(colorERE[ListeEre.index(period)],age,period),(x,50,int(1400/(10)),50))
							pygame.draw.line(im,(255,0,0),(x,50),(x,100),2)
							txt = font.render(period, True, (255,255,255))
							im.blit(txt,(x,80))
						x=int((i0)*1400/(10))
						pygame.draw.rect(im,(155,209,136,44),(x,50,int(1400/(10)),50))
						i=i0+ref
						age=(listeyear[i]*541/5000)-541
						period=ListeEre[-1]
						for fg in DateEre:
							if age<-fg:
								period=ListeEre[DateEre.index(fg)-1]
								break
						txt = font.render(period, True, (255,0,255))
						im.blit(txt,(x,80))
						pygame.image.save(im,"frise2.png")	
						Bv=read('bouchever')
						Ms=read(svgmuteur2.at[str(listeyear[i]),'machsupTYPE'])
						E=read('eye')
						Mi=read(svgmuteur2.at[str(listeyear[i]),'machinfTYPE'])
						machD=0
						machDi=0
						machDz=0
						if svgmuteur2.at[str(listeyear[i]),'machsupTYPE']=='cake':
							machD=-0.25
						if svgmuteur2.at[str(listeyear[i]),'machsupTYPE']=='smilcroco':
							machD=-0.35
							machDz=0.3
						if svgmuteur2.at[str(listeyear[i]),'machsupTYPE']=='espad':
							machD=-0.25
						if svgmuteur2.at[str(listeyear[i]),'machsupTYPE']=='machsupsouris.sc1':
							machD=-0.25
						if svgmuteur2.at[str(listeyear[i]),'machinfTYPE']=='pelikanlol':
							machDi=+0.25
						Ve=read(svgmuteur2.at[str(listeyear[i]),'vertebreTYPE'])
						Na=read(svgmuteur2.at[str(listeyear[i]),'nageoireTYPE'])
						Br=read(svgmuteur2.at[str(listeyear[i]),'brasTYPE'])
						Ja=read(svgmuteur2.at[str(listeyear[i]),'jambeTYPE'])
						Pp=read(svgmuteur2.at[str(listeyear[i]),'piedTYPE'])
						Qu=read(svgmuteur2.at[str(listeyear[i]),'queueTYPE'])
						showFILM(-90,ex,Ms[3],Ve[3],Ja[3],str(listeyear[i]))
						r2 = glReadPixels(0,0,1400,1400,   GL_RGB,GL_FLOAT)#
						profile=saveim2(r2)
						frame2=pygame.image.load("taillecomp.png")
						hum=pygame.image.load("human.png")
						ty=svgmuteur2.loc[str(listeyear[i])]['taille']*profile[1]/20
						tx=svgmuteur2.loc[str(listeyear[i])]['taille']*profile[2]/20
						profpic=profile[0]
						tsc=min(1,16/ty)
						profilew=profile[1]
						if tx>ty:
							tsc=min(1,24/tx)
							ty=tx
							profilew=profile[2]
						hum=pygame.transform.scale(hum,(int(80*tsc),int(150*tsc)))
						t_x=(1.8/int(150*tsc))*int((ty*profile[1]*10)/profilew)
						t_y=(1.8/int(150*tsc))*int((ty*profile[2]*10)/profilew)
						ty=min(16,ty)
						profpic=pygame.transform.scale(profpic,(int((ty*1400)/profilew),int((ty*700)/profilew)))
						frame2.blit(hum,(30+80-int(40*tsc)-40,200-10-int(150*tsc)))
						lmin=profile[3]
						lmax=profile[4]
						hmin=profile[5]
						hmax=profile[6]
						pygame.draw.line(frame2,(255,255,255),(150,180),(150,180-int((ty*profile[1]*10)/profilew)),4)
						pygame.draw.line(frame2,(255,255,255),(147,180),(155,180),4)
						pygame.draw.line(frame2,(255,255,255),(147,180-int((ty*profile[1]*10)/profilew)),(155,180-int((ty*profile[1]*10)/profilew)),4)
						pygame.draw.line(frame2,(255,255,255),(160,187),(160,195),4)
						pygame.draw.line(frame2,(255,255,255),(160+int((ty*profile[2]*10)/profilew),187),(160+int((ty*profile[2]*10)/profilew),195),4)
						pygame.draw.line(frame2,(255,255,255),(160,190),(160+int((ty*profile[2]*10)/profilew),190),4)
						frame2.blit(profpic,(160-int((ty*lmin*10)/profilew),180-int((ty*700)/profilew)+int((ty*hmin*10)/profilew)))
						poid=str(round(t_x*t_y*30,2))
						txt = font.render(str(round(t_x,2))+'m x '+str(round(t_y,2))+'m'+' '+poid+'kg'+' biome '+dicoNbi[cases[svgmuteur1.loc[str(listeyear[i])]['X']][svgmuteur1.loc[str(listeyear[i])]['Y']]], True, (255,255,255))
						frame2.blit(txt,(10,10))
				
						pygame.image.save(frame2,"tailleecran.png")#
						showFILM(30,ex,Ms[3],Ve[3],Ja[3],str(listeyear[i]))
						pygame.display.flip()
					else:
						scrollf=0
						im=pygame.image.load("frise.png")
						font = pygame.font.Font('freesansbold.ttf', 18)
						ref=max(len(listeyear)-10,0)
						for k in range(0,min(10,len(listeyear))):
							x=int(k*1400/(10))
							age=(listeyear[ref+k]*541/5000)-541
							period=ListeEre[-1]
							for fg in DateEre:
								if age<-fg:
									period=ListeEre[DateEre.index(fg)-1]
									break
							pygame.draw.rect(im,Grad(colorERE[ListeEre.index(period)],age,period),(x,50,int(1400/(10)),50))
							pygame.draw.line(im,(255,0,0),(x,50),(x,100),2)
							txt = font.render(period, True, (255,255,255))
							im.blit(txt,(x,80))
						pygame.image.save(im,"frise2.png")	
						Bv=read('bouchever')
						Ms=read(RandomEspece.at[Espe,'machsupTYPE'])
						E=read('eye')
						Mi=read(RandomEspece.at[Espe,'machinfTYPE'])
						machD=0
						machDz=0
						machDi=0
						if RandomEspece.at[Espe,'machsupTYPE']=='cake':
							machD=-0.25
						if RandomEspece.at[Espe,'machsupTYPE']=='smilcroco':
							machD=-0.35
							machDz=0.3
						if RandomEspece.at[Espe,'machsupTYPE']=='espad':
							machD=-0.25
						if RandomEspece.at[Espe,'machsupTYPE']=='machsupsouris.sc1':
							machD=-0.25
						if RandomEspece.at[Espe,'machinfTYPE']=='pelikanlol':
							machDi=+0.25
						Ve=read(RandomEspece.at[Espe,'vertebreTYPE'])
						Na=read(RandomEspece.at[Espe,'nageoireTYPE'])
						Br=read(RandomEspece.at[Espe,'brasTYPE'])
						Ja=read(RandomEspece.at[Espe,'jambeTYPE'])
						Pp=read(RandomEspece.at[Espe,'piedTYPE'])
						Qu=read(RandomEspece.at[Espe,'queueTYPE'])
						showAnim(-90,ex,Ms[3],Ve[3],Ja[3],Espe)
						r2 = glReadPixels(0,0,1400,1400,   GL_RGB,GL_FLOAT)
						profile=saveim2(r2)
						frame2=pygame.image.load("taillecomp.png")
						hum=pygame.image.load("human.png")
						ty=RandomEspece.loc[Espe]['taille']*profile[1]/20
						tx=RandomEspece.loc[Espe]['taille']*profile[2]/20
						profpic=profile[0]
						tsc=min(1,16/ty)
						profilew=profile[1]
						if tx>ty:
							tsc=min(1,24/tx)
							ty=tx
							profilew=profile[2]
						hum=pygame.transform.scale(hum,(int(80*tsc),int(150*tsc)))
						t_x=(1.8/int(150*tsc))*int((ty*profile[1]*10)/profilew)
						t_y=(1.8/int(150*tsc))*int((ty*profile[2]*10)/profilew)
						ty=min(16,ty)
						profpic=pygame.transform.scale(profpic,(int((ty*1400)/profilew),int((ty*700)/profilew)))
						frame2.blit(hum,(30+80-int(40*tsc)-40,200-10-int(150*tsc)))
						lmin=profile[3]
						lmax=profile[4]
						hmin=profile[5]
						hmax=profile[6]
						pygame.draw.line(frame2,(255,255,255),(150,180),(150,180-int((ty*profile[1]*10)/profilew)),4)
						pygame.draw.line(frame2,(255,255,255),(147,180),(155,180),4)
						pygame.draw.line(frame2,(255,255,255),(147,180-int((ty*profile[1]*10)/profilew)),(155,180-int((ty*profile[1]*10)/profilew)),4)
						pygame.draw.line(frame2,(255,255,255),(160,187),(160,195),4)
						pygame.draw.line(frame2,(255,255,255),(160+int((ty*profile[2]*10)/profilew),187),(160+int((ty*profile[2]*10)/profilew),195),4)
						pygame.draw.line(frame2,(255,255,255),(160,190),(160+int((ty*profile[2]*10)/profilew),190),4)
						frame2.blit(profpic,(160-int((ty*lmin*10)/profilew),180-int((ty*700)/profilew)+int((ty*hmin*10)/profilew)))
						poid=str(round(t_x*t_y*30,2))
						txt = font.render(str(round(t_x,2))+'m x '+str(round(t_y,2))+'m'+' '+poid+'kg'+' biome '+dicoNbi[cases[especes.loc[Espe]['X']][especes.loc[Espe]['Y']]], True, (255,255,255))
						frame2.blit(txt,(10,10))
						
						pygame.image.save(frame2,"tailleecran.png")
						showAnim(angle+angle1,ex,Ms[3],Ve[3],Ja[3],Espe)
						pygame.display.flip()
				
				if KEY[K_ESCAPE]==1 or (clic2[0]==1 and mous2[0]<368 and mous2[1]<159):
					showcreature=0
					showworld=0
					font = pygame.font.Font('freesansbold.ttf', 25)
					recreate=1
				if KEY[K_t]==1 or (clic2[0]==1 and abs(mous2[0]-1200)<100 and abs(mous2[1]-165)<75):
					showcreature=0
					font = pygame.font.Font('freesansbold.ttf', 25)
					showtree=1
					recreate=1
				if KEY[K_RIGHT]==1:
					curseur=(curseur+1)
					Espe=listC[curseur%len(listC)]
					frame2=pygame.image.load("vide.png")
					txt = font.render(RandomEspece.at[Espe,'nominem'], True, (255,255,255))
					ltxt=(200-txt.get_width())//2
					frame2.blit(txt,(ltxt,100))
					pygame.image.save(frame2,"nom.png")
					Bv=read('bouchever')
					
					Ms=read(RandomEspece.at[Espe,'machsupTYPE'])
					E=read('eye')
					Mi=read(RandomEspece.at[Espe,'machinfTYPE'])
					machD=0
					machDz=0
					machDi=0
					if RandomEspece.at[Espe,'machsupTYPE']=='cake':
						machD=-0.25
					if RandomEspece.at[Espe,'machsupTYPE']=='smilcroco':
						machD=-0.35
						machDz=0.3
					if RandomEspece.at[Espe,'machsupTYPE']=='espad':
						machD=-0.25
					if RandomEspece.at[Espe,'machsupTYPE']=='machsupsouris.sc1':
						machD=-0.25
					if RandomEspece.at[Espe,'machinfTYPE']=='pelikanlol':
						machDi=+0.25
					Ve=read(RandomEspece.at[Espe,'vertebreTYPE'])
					Br=read(RandomEspece.at[Espe,'brasTYPE'])
					Na=read(RandomEspece.at[Espe,'nageoireTYPE'])
					Ja=read(RandomEspece.at[Espe,'jambeTYPE'])
					Pp=read(RandomEspece.at[Espe,'piedTYPE'])
					Qu=read(RandomEspece.at[Espe,'queueTYPE'])
					showAnim(-90,ex,Ms[3],Ve[3],Ja[3],Espe)# ici mettre 90
					r2 = glReadPixels(0,0,1400,1400,   GL_RGB,GL_FLOAT)
					profile=saveim2(r2)
					frame2=pygame.image.load("taillecomp.png")
					hum=pygame.image.load("human.png")
					ty=RandomEspece.loc[Espe]['taille']*profile[1]/20
					tx=RandomEspece.loc[Espe]['taille']*profile[2]/20
					profpic=profile[0]
					tsc=min(1,16/ty)
					profilew=profile[1]
					if tx>ty:
						tsc=min(1,24/tx)
						ty=tx
						profilew=profile[2]
					hum=pygame.transform.scale(hum,(int(80*tsc),int(150*tsc)))
					t_x=(1.8/int(150*tsc))*int((ty*profile[1]*10)/profilew)
					t_y=(1.8/int(150*tsc))*int((ty*profile[2]*10)/profilew)
					ty=min(16,ty)
					profpic=pygame.transform.scale(profpic,(int((ty*1400)/profilew),int((ty*700)/profilew)))
					frame2.blit(hum,(30+80-int(40*tsc)-40,200-10-int(150*tsc)))
					lmin=profile[3]
					lmax=profile[4]
					hmin=profile[5]
					hmax=profile[6]
					pygame.draw.line(frame2,(255,255,255),(150,180),(150,180-int((ty*profile[1]*10)/profilew)),4)
					pygame.draw.line(frame2,(255,255,255),(147,180),(155,180),4)
					pygame.draw.line(frame2,(255,255,255),(147,180-int((ty*profile[1]*10)/profilew)),(155,180-int((ty*profile[1]*10)/profilew)),4)
					pygame.draw.line(frame2,(255,255,255),(160,187),(160,195),4)
					pygame.draw.line(frame2,(255,255,255),(160+int((ty*profile[2]*10)/profilew),187),(160+int((ty*profile[2]*10)/profilew),195),4)
					pygame.draw.line(frame2,(255,255,255),(160,190),(160+int((ty*profile[2]*10)/profilew),190),4)
					frame2.blit(profpic,(160-int((ty*lmin*10)/profilew),180-int((ty*700)/profilew)+int((ty*hmin*10)/profilew)))
					poid=str(round(t_x*t_y*30,2))
					txt = font.render(str(round(t_x,2))+'m x '+str(round(t_y,2))+'m'+' '+poid+'kg'+' biome '+dicoNbi[cases[especes.loc[Espe]['X']][especes.loc[Espe]['Y']]], True, (255,255,255))
					frame2.blit(txt,(10,10))
					pygame.image.save(frame2,"tailleecran.png")
					
					angle=30
					recreate=0
					showAnim(angle,ex,Ms[3],Ve[3],Ja[3],Espe)
					r = glReadPixels(0,0,1400,1400,   GL_RGB,GL_UNSIGNED_BYTE)
					pygame.display.flip()
					saveim(r,Espe)
				if KEY[K_LEFT]==1:
					curseur=(curseur-1)
					Espe=listC[curseur%len(listC)]
					frame2=pygame.image.load("vide.png")
					txt = font.render(RandomEspece.at[Espe,'nominem'], True, (255,255,255))
					ltxt=(200-txt.get_width())//2
					frame2.blit(txt,(ltxt,100))
					pygame.image.save(frame2,"nom.png")
					Bv=read('bouchever')
					
					Ms=read(RandomEspece.at[Espe,'machsupTYPE'])
					E=read('eye')
					Mi=read(RandomEspece.at[Espe,'machinfTYPE'])
					machD=0
					machDz=0
					machDi=0
					
					if RandomEspece.at[Espe,'machsupTYPE']=='cake':
						machD=-0.25
					if RandomEspece.at[Espe,'machsupTYPE']=='smilcroco':
						machD=-0.35
						machDz=0.3
					if RandomEspece.at[Espe,'machsupTYPE']=='espad':
						machD=-0.25
					if RandomEspece.at[Espe,'machsupTYPE']=='machsupsouris.sc1':
						machD=-0.25
					if RandomEspece.at[Espe,'machinfTYPE']=='pelikanlol':
						machDi=+0.25
					Ve=read(RandomEspece.at[Espe,'vertebreTYPE'])
					Br=read(RandomEspece.at[Espe,'brasTYPE'])
					Na=read(RandomEspece.at[Espe,'nageoireTYPE'])
					Ja=read(RandomEspece.at[Espe,'jambeTYPE'])
					Pp=read(RandomEspece.at[Espe,'piedTYPE'])
					Qu=read(RandomEspece.at[Espe,'queueTYPE'])
					showAnim(-90,ex,Ms[3],Ve[3],Ja[3],Espe)# ici mettre 90
					r2 = glReadPixels(0,0,1400,1400,   GL_RGB,GL_FLOAT)
					profile=saveim2(r2)
					frame2=pygame.image.load("taillecomp.png")
					hum=pygame.image.load("human.png")
					ty=RandomEspece.loc[Espe]['taille']*profile[1]/20
					tx=RandomEspece.loc[Espe]['taille']*profile[2]/20
					profpic=profile[0]
					tsc=min(1,16/ty)
					profilew=profile[1]
					if tx>ty:
						tsc=min(1,24/tx)
						ty=tx
						profilew=profile[2]
					hum=pygame.transform.scale(hum,(int(80*tsc),int(150*tsc)))
					t_x=(1.8/int(150*tsc))*int((ty*profile[1]*10)/profilew)
					t_y=(1.8/int(150*tsc))*int((ty*profile[2]*10)/profilew)
					ty=min(16,ty)
					profpic=pygame.transform.scale(profpic,(int((ty*1400)/profilew),int((ty*700)/profilew)))
					frame2.blit(hum,(30+80-int(40*tsc)-40,200-10-int(150*tsc)))
					lmin=profile[3]
					lmax=profile[4]
					hmin=profile[5]
					hmax=profile[6]
					pygame.draw.line(frame2,(255,255,255),(150,180),(150,180-int((ty*profile[1]*10)/profilew)),4)
					pygame.draw.line(frame2,(255,255,255),(147,180),(155,180),4)
					pygame.draw.line(frame2,(255,255,255),(147,180-int((ty*profile[1]*10)/profilew)),(155,180-int((ty*profile[1]*10)/profilew)),4)
					pygame.draw.line(frame2,(255,255,255),(160,187),(160,195),4)
					pygame.draw.line(frame2,(255,255,255),(160+int((ty*profile[2]*10)/profilew),187),(160+int((ty*profile[2]*10)/profilew),195),4)
					pygame.draw.line(frame2,(255,255,255),(160,190),(160+int((ty*profile[2]*10)/profilew),190),4)
					frame2.blit(profpic,(160-int((ty*lmin*10)/profilew),180-int((ty*700)/profilew)+int((ty*hmin*10)/profilew)))
					poid=str(round(t_x*t_y*30,2))
					txt = font.render(str(round(t_x,2))+'m x '+str(round(t_y,2))+'m'+' '+poid+'kg'+' biome '+dicoNbi[cases[especes.loc[Espe]['X']][especes.loc[Espe]['Y']]], True, (255,255,255))
					frame2.blit(txt,(10,10))
					pygame.image.save(frame2,"tailleecran.png")
					
					
					
					angle=30
					recreate=0
					showAnim(angle,ex,Ms[3],Ve[3],Ja[3],Espe)
					r = glReadPixels(0,0,1400,1400,   GL_RGB,GL_UNSIGNED_BYTE)
					pygame.display.flip()
					saveim(r,Espe)
					
				
			
			
			fenetre = pygame.display.set_mode((1400,700),RESIZABLE )
			menu()
			if CURSE!=0:
				mission_en_cours.show1()
		if showtree==1:
			stopp=0
			mous2=pygame.mouse.get_pos()
			clic2=pygame.mouse.get_pressed()
			#zoom=1
			#yD=0
			#xD=0
			pygame.key.set_repeat(1)
			while stopp==0:
				pygame.time.wait(20)
				#evotree(1,0,0)
				fenetre.fill((0,0,0))
				pygame.draw.line(fenetre,(0,0,255),(0,0),(1399,0),1)
				pygame.draw.line(fenetre,(0,0,255),(0,699),(1399,699),1)
				pygame.draw.line(fenetre,(0,0,255),(0,0),(0,699),1)
				pygame.draw.line(fenetre,(0,0,255),(1399,0),(1399,699),1)
				
				for uf in DateEre:
					if tour>int((-uf+541)*5000/541):
						ageT=int((-uf+541)*5000/541)
						pygame.draw.line(fenetre,(100,100,100),(int(zoom*ageT*0.5-xD),0),(int(zoom*ageT*0.5-xD),700),int(zoom)+1)
						
				
				lenghtM=0
				for j in especes.iterrows():
					lenghtM=max(len(RandomEspece.at[j[0],'score']),lenghtM)
				scoreL=[]
				nameL=[]
				numberL=[]
				fullscore=[]
				for j in especes.iterrows():
					som=0
					for i in range(0,len(RandomEspece.at[j[0],'score'])):
						som=som+(100-RandomEspece.at[j[0],'score'][i])*(100)**(lenghtM-i)
					scoreL.append(som)
					nameL.append(j[0])
					fullscore.append(RandomEspece.at[j[0],'score'])
					if RandomEspece.at[j[0],'score']!=[0]:
						numberL.append(RandomEspece.at[j[0],'score'][1])
					else:
						numberL.append(0)
				Z = [x for _,x in sorted(zip(scoreL,nameL))]
				Z2 = [x for _,x in sorted(zip(scoreL,numberL))]
				Z3 = [x for _,x in sorted(zip(scoreL,fullscore))]
				
				
				Ld=0
				LL=[0,0]
				for k,i in enumerate(Z):
					Ti=RandomEspece.at[i,'Tmu']
					knop=(-1)**Z2[k]
					
					gn=Z3[k]
					
					if k!=0:
						LL[(1+knop)//2]=LL[(1+knop)//2]+10
					Ld=LL[int((1+knop)/2)]
					colo=RandomEspece.at[i,'colortree']
					pygame.draw.line(fenetre,colo,(int(zoom*Ti[0]*0.5-xD),int(zoom*Ld*knop-yD+350)),(int(zoom*min(tour*0.5,RandomEspece.at[i,'deadT']*0.5)-xD),int(zoom*Ld*knop-yD+350)),int(zoom)+1)
					imageEs=pygame.transform.scale(dicoImage[i],(int(zoom*6),int(zoom*6)))
					fenetre.blit(imageEs,(int(zoom*min(tour*0.5,RandomEspece.at[i,'deadT']*0.5)-xD+zoom),int(zoom*Ld*knop-yD+350-3*zoom)))
					if min(tour*0.5,RandomEspece.at[i,'deadT']*0.5)==RandomEspece.at[i,'deadT']*0.5:
						pygame.draw.line(fenetre,(255,0,0),(int(zoom*min(tour*0.5,RandomEspece.at[i,'deadT']*0.5)-xD-zoom*5+7*zoom),int(zoom*Ld*knop-yD+350+zoom*5)),(int(5+zoom*min(tour*0.5,RandomEspece.at[i,'deadT']*0.5)-xD+7*zoom),int(zoom*Ld*knop-yD+350-zoom*5)),int(zoom)+1)
						pygame.draw.line(fenetre,(255,0,0),(int(zoom*min(tour*0.5,RandomEspece.at[i,'deadT']*0.5)-xD-zoom*5+7*zoom),int(zoom*Ld*knop-yD+350-zoom*5)),(int(5+zoom*min(tour*0.5,RandomEspece.at[i,'deadT']*0.5)-xD+7*zoom),int(zoom*5+zoom*Ld*knop-yD+350)),int(zoom)+1)
					uK=zoom*5
					if k!=0:
						Xi=min(max(int(zoom*Ti[0]*0.5-xD),0),1399)
						Yi=min(max(int(zoom*Ld*knop-yD-uK*knop-zoom*5*knop+350),0),699)
						while fenetre.get_at((Xi,Yi))==(0,0,0,255):#attention à sortir de l'image
							pygame.draw.line(fenetre,colo,(int(zoom*Ti[0]*0.5-xD),int(zoom*Ld*knop-yD+350)),(int(zoom*Ti[0]*0.5-xD),int(zoom*Ld*knop-yD-uK*knop+350)),int(zoom)+1)
							uK=uK+zoom*5
							if uK>10000*zoom:
								break
							Xi=min(max(int(zoom*Ti[0]*0.5-xD),0),1399)
							Yi=min(max(int(zoom*Ld*knop-yD-uK*knop-zoom*5*knop+350),0),699)
							
						pygame.draw.line(fenetre,colo,(int(zoom*Ti[0]*0.5-xD),int(zoom*Ld*knop-yD+350)),(int(zoom*Ti[0]*0.5-xD),int(zoom*Ld*knop-yD-uK*knop-zoom*5*knop+350)),int(zoom)+1)
					
					
					
					#Ld=Ld+10
				font = pygame.font.Font('freesansbold.ttf', int(14*zoom)+1)
				for uf in DateEre:
					if tour>int((-uf+541)*5000/541):
						ageT=int((-uf+541)*5000/541)
						periodtxt=ListeEre[DateEre.index(uf)]
						txt = font.render(periodtxt, True, (100,100,100))
						fenetre.blit(txt,(int(zoom*(ageT+5)*0.5-xD),int(-zoom*(50+Ld+20*(DateEre.index(uf)%4))-yD+350)))
				font = pygame.font.Font('freesansbold.ttf', 25)	
					
				for event in pygame.event.get():
					mous2=pygame.mouse.get_pos()
					clic2=pygame.mouse.get_pressed()
					#(int(zoom*min(tour*0.5,RandomEspece.at[i,'deadT']*0.5)-xD+zoom),int(zoom*Ld*knop-yD+350-3*zoom))
					if event.type == pygame.USEREVENT:# each while loop
						pygame.mixer.music.load(choice(playlist))
						if musicplayed==1:
							pygame.mixer.music.play()
					if event.type==MOUSEBUTTONUP:
							if event.button==4:
								zoom=zoom*2
								xD=xD*2+700+(mous2[0]-700)
								yD=yD*2+(mous2[1]-350)
							if event.button==5:
								zoom=zoom/2
								xD=int((xD-700-(mous2[0]-700))/2)
								yD=int((yD-(mous2[1]-350))/2)
								
					KEY=pygame.key.get_pressed()
					if KEY[K_RIGHT]==1:
						xD=xD+10
					if KEY[K_LEFT]==1:
						xD=xD-10
					if KEY[K_UP]==1:
						yD=yD-10
					if KEY[K_DOWN]==1:
						yD=yD+10
					if KEY[K_ESCAPE]==1:
						stopp=1
						showworld=0
						zoom=1
						yD=0
						xD=0
				Ld=0
				LL=[0,0]
				for k,i in enumerate(Z):
					knop=(-1)**Z2[k]
					if k!=0:
						LL[(1+knop)//2]=LL[(1+knop)//2]+10
					Ld=LL[int((1+knop)/2)]
					if abs(mous2[0]-int(zoom*min(tour*0.5,RandomEspece.at[i,'deadT']*0.5)-xD+zoom+int(zoom*3)))<int(zoom*3) and abs(mous2[1]-int(zoom*Ld*knop-yD+350-3*zoom)-int(zoom*3))<int(zoom*3):
						
						text = font.render(RandomEspece.at[i,'nominem'], True, (255,255,255))
						fenetre.blit(text,(mous2[0]+50,mous2[1]))
						if clic2[0]==1:
							bypass=i
							showcreature=1
							stopp=1
							curseur=listC.index(i)
						
				if abs(mous2[0]-700)>650:
					xD=xD+10*np.sign(mous2[0]-700)
				if abs(mous2[1]-350)>300:
					yD=yD+10*np.sign(mous2[1]-350)
					
				if abs(mous2[0]-60)<60:
					if abs(mous2[1]-(20))<20:
						if clic2[0]==1:
							stopp=1
							showworld=0
				
				fenetre.blit(closet,(0,0))
				fenetre.blit(legendtree,(1200,600))
				pygame.display.flip()
			showtree=0
			pygame.key.set_repeat()
		if showworld==1:
			fenetre.blit(MAP,(0,0))
			fenetre.blit(closet,(0,0))
			wrld=worldparam()
			if showhum==1:
				font = pygame.font.Font('freesansbold.ttf', 14)
				text=font.render('global humidity : '+str(round(wrld[2],2)), True, (255,255,255))
				fenetre.blit(text,(1200,20))
				font = pygame.font.Font('freesansbold.ttf', 25)
				fenetre.blit(legendH,(1200,600))
			if showtemp==1:
				font = pygame.font.Font('freesansbold.ttf', 14)
				text=font.render('global temperature : '+str(round(wrld[1],2)), True, (255,255,255))
				fenetre.blit(text,(1200,20))
				font = pygame.font.Font('freesansbold.ttf', 25)
				fenetre.blit(legendT,(1200,600))
				
			if showhum==0 and showtemp==0 and showCont==0:
				font = pygame.font.Font('freesansbold.ttf', 14)
				text=font.render('land percentage : '+str(round(wrld[0],2)), True, (0,0,0))
				fenetre.blit(text,(1200,20))
				font = pygame.font.Font('freesansbold.ttf', 25)
				fenetre.blit(legend0,(1200,600))
			for ki in range(0,len(Xl)):
				if abs(mous[0]-Xl[ki]*10+2)<10 and abs(mous[1]-Yl[ki]*10+2)<10:
					font = pygame.font.Font('freesansbold.ttf', 14)
					text = font.render(RandomEspece.at[nomL[ki],'nominem'], True, (255,255,255))
					fenetre.blit(text,(mous[0],mous[1]))
					font = pygame.font.Font('freesansbold.ttf', 25)
					
			
			for event in pygame.event.get():
				KEY=pygame.key.get_pressed()
				if event.type == pygame.USEREVENT:# each while loop
					pygame.mixer.music.load(choice(playlist))
					if musicplayed==1:
						pygame.mixer.music.play()
				
			if KEY[K_ESCAPE]==1:
				showworld=0
				showhum=0
				showtemp=0
				MAP=MAP2sec.copy()
				showCont=0
				createMAP()
				menu()
				if CURSE!=0:
					mission_en_cours.show1()
			if abs(mous[0]-60)<60:
				if abs(mous[1]-(20))<20:
					if clic[0]==1:
						showworld=0
						showhum=0
						showtemp=0
						showCont=0
						MAP=MAP2sec.copy()
						createMAP()
						menu()
						if CURSE!=0:
							mission_en_cours.show1()
		#pygame.time.wait(15)
		if action==1:
			testou=pygame.mouse.get_pressed()
			Cp=0
			while testou[0]==1 and Cp<10:
				pygame.time.wait(20)
				for event in pygame.event.get():
					testou=pygame.mouse.get_pressed()
					if event.type == pygame.USEREVENT:# each while loop
						pygame.mixer.music.load(choice(playlist))
						if musicplayed==1:
							pygame.mixer.music.play()
				Cp=Cp+1
				
				
		#apres pour action
		if randint(0,10)==0 and len(listedevolcans)!=0:
			X=choice(listedevolcans)
			#cases[(X[0]+randint(-1,1))%140][(X[1]+randint(-1,1))%140]='lave'
			cases[X[0]][X[1]]='volca'
		if KEY[K_RIGHT]==1 and showworld==1:
			cases=np.roll(cases,-1,axis=0)#roll secheresse
			temperature=np.roll(temperature,-1,axis=0)
			humidite=np.roll(humidite,-1,axis=0)
			nourriture=np.roll(nourriture,-1,axis=0)
			brdG=np.roll(brdG,-1,axis=0)
			continentM=np.roll(continentM,-1,axis=0)
			volcanMAP=np.roll(volcanMAP,-1,axis=0)
			meteorMAP=np.roll(meteorMAP,-1,axis=0)
			pointF[0]=(pointF[0]-1)%140
			pointC[0]=(pointC[0]-1)%140
			pointS[0]=(pointS[0]-1)%140
			pointH[0]=(pointH[0]-1)%140
			for k in range(0,len(Xl)):
				Xl[k]=(Xl[k]-1)%140
			xs=(xs-1)%140
			x_=(x_-1)%140
			xv_=(xv_-1)%140
			for i in dicoContinent.keys():
				dicoXcon[i]=(dicoXcon[i]-1)%140
			mission_en_cours.roll_me(-1)
			createMAP()
		if KEY[K_LEFT]==1 and showworld==1:
			cases=np.roll(cases,1,axis=0)
			temperature=np.roll(temperature,1,axis=0)
			humidite=np.roll(humidite,1,axis=0)
			nourriture=np.roll(nourriture,1,axis=0)
			brdG=np.roll(brdG,1,axis=0)
			continentM=np.roll(continentM,1,axis=0)
			volcanMAP=np.roll(volcanMAP,1,axis=0)
			meteorMAP=np.roll(meteorMAP,1,axis=0)
			pointF[0]=(pointF[0]+1)%140
			pointC[0]=(pointC[0]+1)%140
			pointS[0]=(pointS[0]+1)%140
			pointH[0]=(pointH[0]+1)%140
			for k in range(0,len(Xl)):
				Xl[k]=(Xl[k]+1)%140
			xs=(xs+1)%140
			x_=(x_+1)%140
			xv_=(xv_+1)%140
			for i in dicoContinent.keys():
				dicoXcon[i]=(dicoXcon[i]+1)%140
			mission_en_cours.roll_me(1)
			createMAP()
		
		for event in pygame.event.get():
			if event.type == QUIT:
				q=1
				action=1
			if event.type == pygame.USEREVENT:# each while loop
				pygame.mixer.music.load(choice(playlist))
				if musicplayed==1:
					pygame.mixer.music.play()
		if showworld==0 and showcreature!=1 and showtree!=1:# see showworld
			menu()
			if CURSE!=0:
				text=font.render('turns before massive extinction: '+str(TIME), True, (max(min(255-(TIME-(500+(1-CURSE)*150)),255),0),max(min(255+(TIME-(500+(1-CURSE)*150)),255),0),0))
				fenetre.blit(text,(360,50))
				text.get_width()
				if text_addt[0]=='-':
					coloR=(255,0,0)
				else:
					coloR=(0,255,0)
					
				t_t=font.render(text_addt, True, coloR)
				fenetre.blit(t_t,(text.get_width()+370,50))
				mission_en_cours.show1()
			age=(tour*541/5000)-541
			period=ListeEre[-1]
			for fg in DateEre:
				if age<-fg:
					period=ListeEre[DateEre.index(fg)-1]
					break
			text=font.render('turn '+str(tour)+'   '+str(round(age,2))+' Ma, period: '+period, True, (255,255,255))
			fenetre.blit(text,(360,20))
			if tour==5000 and BIGSCORE2==0:
				fenetre.blit(pygame.image.load('boutonfutur.png'),(550,300))
				BIGSCORE2=((np.sum(brdG)//500)+BIGSCORE+tour//10)*CURSE+1
				if CURSE!=0:
					txt = font.render('score: '+str(BIGSCORE2), True, (0,0,0))
					ltxt=txt.get_width()//2
					fenetre.blit(txt,(700-ltxt,450))
					file1 = open("scoreliste", "rb")
					bestscore=pickle.load(file1)
					bestcreat=pickle.load(file1)
					bestscore.append(BIGSCORE2)
					bestcreat.append(RandomEspece.at['monEspece','nominem'])
					bestcreat=[x for _,x in sorted(zip(bestscore,bestcreat))]
					bestscore=sorted(bestscore)
					bestscore=bestscore[1:]
					bestcreat=bestcreat[1:]
					file1.close()
					f2 = open("scoreliste", "wb")
					pickle.dump(bestscore, f2)
					pickle.dump(bestcreat, f2)
					f2.close()
				while KEY[K_RETURN]==0:
					for event in pygame.event.get():
						KEY=pygame.key.get_pressed()
					fenetre.blit(pygame.image.load('flug1.png'),(350,0))
					fenetre.blit(pygame.image.load('boutonfutur.png'),(550,300))
					fenetre.blit(txt,(700-ltxt,450))
					pygame.display.flip()
				pygame.time.wait(100)
				CURSE=0
				

				
		pygame.display.flip()
		
		if tour==1 and namechoosed==0:
			com=0
			T0='my creature'
			alt=1
			while namechoosed==0 :
				lettre=0
				com=(com+1)%1000
				if com%300==0:
					alt=-alt
				for event in pygame.event.get():
					KEY=pygame.key.get_pressed()
					if KEY[K_RETURN]==1:
						namechoosed=1
					if event.type==MOUSEBUTTONUP:
						if event.button==5:
							curseur=(curseur+1)
						if event.button==4:
							curseur=(curseur-1)
					if event.type == KEYDOWN:
					
						if event.unicode!="\x08" and event.key!=13:
							lettre=event.unicode
						if event.unicode=="\x08" or event.unicode=="":
							lettre=-1
					if event.type == pygame.USEREVENT:# each while loop
						pygame.mixer.music.load(choice(playlist))
						if musicplayed==1:
							pygame.mixer.music.play()
				KEY=pygame.key.get_pressed()
				
				
				
				if lettre==-1:
					T0=T0[:-1]
				if lettre!=-1 and lettre!=0:
					T0=T0+lettre
			
				text = font.render(T0, True, (0,0,0))
				textRect = text.get_rect()
				if alt==-1:
					text = font.render(T0+'_', True, (0,0,0))
				textRect.center = (700, 350)
				fenetre.blit(boutonname,(550,250))
				fenetre.blit(text,textRect)
				pygame.display.flip()
			RandomEspece.at['monEspece','nominem']=T0
			listnom[0]=T0
			namechoosed=1
		#pygame.time.wait(10)
	text_addt=' '
	if pointF[1]>60:
		pointF[2]=+abs(pointF[2])
	if pointF[1]<10:
		pointF[2]=-abs(pointF[2])
	
	pointF[0]=(pointF[0]+0.3*pointF[3]*cos(pointF[2]*pi/180.0))%140
	pointF[1]=pointF[1]-0.3*pointF[3]*sin(pointF[2]*pi/180.0)
	
	if pointC[1]>60:
		pointC[2]=+abs(pointC[2])
	if pointC[1]<10:
		pointC[2]=-abs(pointC[2])
	
	pointC[0]=(pointC[0]+0.3*pointC[3]*cos(pointC[2]*pi/180.0))%140
	pointC[1]=pointC[1]-0.3*pointC[3]*sin(pointC[2]*pi/180.0)
	
	if pointS[1]>60:
		pointS[2]=+abs(pointS[2])
	if pointS[1]<10:
		pointS[2]=-abs(pointS[2])
	
	pointS[0]=(pointS[0]+0.3*pointS[3]*cos(pointS[2]*pi/180.0))%140
	pointS[1]=pointS[1]-0.3*pointS[3]*sin(pointS[2]*pi/180.0)
	
	if pointH[1]>60:
		pointH[2]=+abs(pointH[2])
	if pointH[1]<10:
		pointH[2]=-abs(pointH[2])
	
	pointH[0]=(pointH[0]+0.3*pointH[3]*cos(pointH[2]*pi/180.0))%140
	pointH[1]=pointH[1]-0.3*pointH[3]*sin(pointH[2]*pi/180.0)

	
