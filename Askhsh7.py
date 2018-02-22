import datetime
meresgia10xronia = [];
tday = datetime.date.today()
tdelta = datetime.timedelta(days=365)
currentyear = (tday.year)
ekastotexronia = tday
count = 0
print "Shmera exoume ",tday
# Dhmiourgw pinaka me 10 times apo to 1 mexri to 7 (1 = Deutera , 2=Trith , 3= Tetarth .. . 7= Kuriakh )
# Oi times auftes antistixoun sthn hmera ths hmeromhnias gia 1 xrono sto mellon(apo shmera), 2 xronia sto mellon , 3 xronia sto mellon ..

for x in range(0, 10):
	meresgia10xronia.insert(x,ekastotexronia.isoweekday())
	#elegxw an einai disekto to etos etsi oste na prosthesw 366 hmeres h 365 hmeres
	if (currentyear % 4) == 0:
		if (currentyear % 100) == 0:
			if (currentyear % 400) == 0:
				tdelta = datetime.timedelta(days= 365 +1)
			else:
				tdelta = datetime.timedelta(days= 365)
		else:
			tdelta = datetime.timedelta(days=365 +1)
	else:
		tdelta= datetime.timedelta(days= 365)


	currentyear += 1
	ekastotexronia += tdelta



# tora pou exw etoimo ton pinaka kanw ena count to opoio afksanete otan h 1h timh tou pinaka einai idia me mia allh timh tou pinaka

for x in range(1, 10):
	if meresgia10xronia[0] == meresgia10xronia[x] :
		count += 1

thesh = tday.day
mhnas = tday.month

print "Tha uparksoun " , count , "mera/es ta epomena 10 xronia pou tha einai oi" , thesh ,"es tou " , mhnas ,"ou mhna "