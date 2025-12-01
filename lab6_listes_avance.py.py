notes = [12, 9, 15, 8, 17, 13, 19, 10]
total = 0
nb_notes = 8
for note in notes:
    total += note 
moyenne = total / nb_notes
print(f"Moyenne : {moyenne:.2f}")
if not notes:
    print("Aucune note à traiter.")
    exit()
notes_bonus = [min(note + 1, 20) for note in notes]
print("Notes après bonus :", notes_bonus)
seuil = 12
notes_valides = [note for note in notes if note >= seuil]
print(f"Notes ≥ {seuil} :", notes_valides)
moyenne_initiale = sum(notes) / nb_notes
moyenne_bonus = sum(notes_bonus) / len(notes_bonus)
lignes = []
lignes.append("=== Rapport des notes ===")
lignes.append(f"Nombre d'étudiants : {nb_notes}")
lignes.append(f"Notes originales : {notes}")
lignes.append(f"Notes après bonus : {notes_bonus}")
lignes.append(f"Moyenne initiale : {moyenne_initiale:.2f}")
lignes.append(f"Moyenne après bonus : {moyenne_bonus:.2f}")
lignes.append(f"Notes ≥ {seuil} : {notes_valides} (soit {len(notes_valides)} étudiants)")
lignes.append("Détails par étudiant :")

for index, note in enumerate(notes, start=1):
    bonus = notes_bonus[index - 1]
    bonus = notes_bonus[index - 1]
rapport = "\n".join(lignes)
print(rapport)
with open("rapport_notes.txt", "w", encoding="utf-8") as f:
    f.write(rapport)

