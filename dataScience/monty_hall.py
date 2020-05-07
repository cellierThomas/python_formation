import numpy as np

def calc_monty_hall( nbrEssai ):
  portegagnante = np.random.randint(0,3, size=(nbrEssai)) 
  choix1 = np.random.randint(0,3, size=(nbrEssai))

  changement = (portegagnante!=choix1).astype(int)
  sanschangement = (portegagnante==choix1).astype(int)

  return changement, sanschangement
