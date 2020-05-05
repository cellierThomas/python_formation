# -*- coding: Latin-1 -*-
import os

from package.fonctions import table
table(5) # Appel de la fonction table

# Ou ...
import package.fonctions
package.fonctions.table(10)  # Appel de la fonction table

os.system("pause")