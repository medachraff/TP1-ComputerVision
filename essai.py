from PyQt6 import QtWidgets # Import des widgets PyQt5
import sys # Import du module système
# Création de l'objet application
app = QtWidgets.QApplication(sys.argv)
# Création de la fenêtre principale
first_window = QtWidgets.QWidget()
# Définition de la taille de la fenêtre
first_window.resize(400, 300)
# Définition du titre de la fenêtre


first_window.setWindowTitle("Premier programme PyQt")
# Affichage de la fenêtre
first_window.show()
# Exécution de l'application
sys.exit(app.exec())