def distance_parcourue(nombre_marches, hauteur_marche):
  hauteur_marche_mètre = hauteur_marche/100
  distance = (nombre_marches * 2) * (hauteur_marche_mètre)
  distance_jour = distance * 5
  distance_semaine = distance_jour * 7
  return f"Pour {nombre_marches} marches de {hauteur_marche} cm, le gardien parcours {distance_semaine} m par semaine."
print(distance_parcourue(10, 20))