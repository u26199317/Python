import geocoder
#Escribimos IP pública
ubicacion = geocoder.ip('8.8.8.8')
#Sustituir con "me" para obtener nuestra ubicación
ubicacion = geocoder.ip("me")
print (ubicacion)
