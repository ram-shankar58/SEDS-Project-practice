import spiceypy
import datetime as dt
import math
#import spiceypy

#Finding today date
today = dt.datetime.today
#Kernals are where the actual planetary/spacecraft flight data are stored, not in libraries.
'''Both ESA and NASA-jpl have these informations. We can import from their websites.
Now loading spice kernals for data for planets: '''

#Accessing the downlaoded kernel

spiceypy.furnsh('../otherfiles/kernels/lsk/naif0012.tls')
spiceypy.furnsh('../otherkernels/spk/de432s.bsp')

#help(spiceypy.furnsh)

#converting into string
td = dt.datetime.today()
tdstr = td.strftime('%Y-%m-%dT00:00:00')

#Computing ephermis time:
ephtime = spiceypy.utc2et(tdstr)

#Computing the state vector of the Earth w.r.t. the Sun

earthstate, earthsunlighttime = spiceypy.spkgeo(targ=399,
                                                et=et_today_midnight,
                                                ref='ECLIPJ2000',
                                                obs=10)
# The state vector is 6 dimensional: x,y,z in km and the corresponding velocities in km/s

#earthstate is the state vector of earth with respect to sun today.

#Computing the distance(in km)

earth_distance = math.sqrt(earthstate[0]**2.0 \
                             + earthstate[1]**2.0 \
                             + earthstate[2]**2.0)
#Converting km into AU

earthdistanceAU = spiceypy.convrt(earth_distance, 'km', 'AU')
#This gives the distance of earth in AU



