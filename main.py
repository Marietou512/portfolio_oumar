from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
# ici juste après app = FastAPI()
import os
static_path = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_path), name="static")
print("STATIC PATH =", static_path)


# Montage des fichiers statiques (créez le dossier static/ d'abord)
try:
    app.mount("/static", StaticFiles(directory="static"), name="static")

except:
    pass

# Configuration des templates
templates = Jinja2Templates(directory="templates")

PROFILE = {
    "name": "MAGASSA Oumar",
    "title": "Etudiant en M2 Data Science, Modélisation Mathématique et IA à l'Université Sorbonne Paris Nord",
    "email": "oumarmagassa75@gmail.com",
    "phone": "07 73 20 21 48",
    "location": "Villetaneuse, France",
    "github": "https://github.com/oumarmagassa",
    "linkedin": "https://www.linkedin.com/in/oumar-magassa-6597b029b",
    "description": (
        "Intéressé par la data science, l’optimisation et l’analyse de données. "
        "Expérience en analyse de données, deep learning, modélisation et optimisation combinatoire (PLNE), "
        "et mise en place de pipelines reproductibles en Python."
    ),
}

PROJECTS = [
    {
        "id": 1,
        "title": "Apprentissage Statistique(TER)",
        "description": (
            "Projet de régression non paramétrique appliqué à des données réelles issues d’un crash moto. "
            "Estimation de la relation entre le temps et l’accélération grâce à l’estimateur à noyau, sans imposer de modèle linéaire. "
            "Sélection automatique de la largeur de bande h par validation croisée leave-one-out afin de trouver le meilleur niveau de lissage. "
            "Les résultats permettent d’identifier le moment de l’impact (vers 15-20 ms), d’observer une phase de fortes vibrations puis un retour progressif vers l’équilibre. "
            "La comparaison de plusieurs noyaux montre que la performance dépend principalement du choix optimal de h plutôt que du type de noyau utilisé."
         ),

        "technologies": ["Python", "pandas", "NumPy", "scikit-learn", "Matplotlib", "LaTeX"],
        "github": "https://github.com/oumarmagassa/Statistiques/blob/main/Rapport_TER_Oumar_MAGASSA_modifi%C3%A9.pdf",  # remplace si tu as un repo dédié
        "demo": None
    },
    {
        "id": 2,
        "title": "Optimisation combinatoire – Problème du Voyageur de Commerce (TSP)",
        "description": (
                "Étude, modélisation et résolution du TSP à partir d’un cas réel en comparant plusieurs méthodes d’optimisation combinatoire. "
                "Implémentation et tests de trois approches (force brute, plus proche voisin et algorithme génétique) sur un ensemble de 10 villes réelles avec de vraies distances mesurées afin d’évaluer concrètement la performance des algorithmes. "
                "Les résultats montrent que si la force brute garantit l’optimum mais devient rapidement inutilisable lorsque le nombre de villes augmente, l’algorithme génétique permet d’obtenir une solution quasiment optimale avec un temps de calcul nettement inférieur, ce qui valide l’intérêt des heuristiques pour des problématiques industrielles réelles."
        )
,
        "technologies": ["Python", "Optimisation", "Graphes", "Heuristiques"],
        "github": "https://github.com/oumarmagassa/Optimisation/blob/main/Projet_Probl%C3%A8me_du_voyageur_de_commerce.pdf",
        "demo": None
    },
    {
        "id": 3,
        "title": "Recherche Opérationnelle – Planning d’équipages (PLNE)",
        "description": (
                "Modèle de programmation linéaire en nombres entiers pour affecter 10 équipages à 20 vols sur 30 jours "
                "sous contraintes réelles (temps de repos réglementaire, disponibilité, capacité opérationnelle). "
                "Implémentation en Python (PuLP, pandas) pour déterminer un planning faisable et à coût minimal. "
                "La solution finale obtenue correspond à l’affectation optimale, exportée en fichier CSV modifiable."
        )
,
        "technologies": ["Python", "PuLP", "pandas", "PLNE", "OR"],
        "github": "https://github.com/oumarmagassa/Recherche-Op-rationnelle/blob/main/Mini_Projet_Recherche_Op%C3%A9rationnelle.ipynb%20-%20Colab.pdf",
        "demo": None
    }
]

SKILLS = {
    "Data Science & Machine Learning": [
        "Régression non paramétrique (noyaux, Nadaraya–Watson)",
        "Apprentissage statistique (en cours de consolidation)",
        "Pipelines reproductibles (prétraitement → simulations → figures)"
    ],
    "Optimisation & Recherche Opérationnelle": [
        "PLNE (PuLP), modélisation contraintes",
        "Optimisation combinatoire (TSP, affectation)",
        "Modélisation mathématique appliquée"
    ],
    "Dev / Langages": [
        "Python : Modélisation mathématique, analyse de données, optimisation et data science (pandas, NumPy, scikit-learn, Matplotlib)",
        "R : en apprentissage pour l’analyse statistique",
        "C/C++ : en apprentissage pour l’implémentation algorithmique et la performance",
        "SQL : bases pour gestion et interrogation de données",
        "LaTeX : rédaction de documents scientifiques / rapports mathématiques"
    ],

    "Outils & Écosystème": [
        "Git/GitHub",
        "Jupyter / VS Code",
        "Word/Excel"
    ],
    "Compétences transverses": [
        "Communication scientifique (séminaires, slides, rapports)",
        "Résolution de problèmes complexes",
        "Clarté & structuration"
    ],
    "Langues": [
        "Français",
        "Anglais (intermédiaire, en progression)",
        "Arabe (B1)"
    ]
}

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "profile": PROFILE,
        "projects": PROJECTS,
        "skills": SKILLS
    }
    )    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)