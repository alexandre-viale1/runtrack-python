def aliments_de_saison(type,saison):
  if type == "fruits":
    if saison == "hiver":
      print("orange, mandarine et kiwi")
    elif saison == "ete":
      print("Poire, fraise, cassis")
  elif type == "legume":
    if saison == "hiver":
      print("carotte, topinambour, endive")
    elif saison == "ete":
      print("artichaut, aubergine,navet")

aliments_de_saison("fruits","hiver")