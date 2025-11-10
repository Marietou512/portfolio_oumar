from flask import Flask, render_template

app = Flask(__name__)

# Données du portfolio basées sur le CV
data = {
    'nom': 'Oumar MAGASSA',
    'titre': 'Étudiant en Master Mathématiques Appliquées aux Données',
    'recherche': 'Stage de fin d\'année (4 à 6 mois) à partir de mars 2026 en data science, optimisation ou analyse de données',
    'email': 'oumarmagassa75@gmail.com',
    'telephone': '07 73 20 21 48',
    'localisation': '93430, Villetaneuse, France',
    'linkedin': 'linkedin.com/in/oumar-magassa-6597b029b',
    'github': 'github.com/oumarmagassa',
    
    'competences_info': {
        'Python': 'Modélisation mathématique et analyse de données (pandas, scikit-learn)',
        'R': 'En cours d\'apprentissage pour l\'analyse statistique et la data science',
        'LaTeX': 'Rédaction de documents scientifiques et rapports mathématiques',
        'C/C++': 'En cours d\'apprentissage pour l\'implémentation d\'algorithmes',
        'SQL': 'Notions de base pour la gestion de bases de données',
        'Git': 'Gestion de versions et collaboration sur projets',
        'Outils bureautiques': 'Bonne maîtrise de Word et Excel'
    },
    
    'competences_pro': [
        'Communication scientifique : Présentation claire de concepts lors de séminaires et projets académiques',
        'Résolution de problèmes complexes : analyse et modélisation de situations réelles',
        'Modélisation mathématique : expérience en optimisation combinatoire',
        'Recherche opérationnelle : modélisation mathématique de problèmes appliqués, résolution de PLNE avec PuLP'
    ],
    
    'langues': {
        'Français': '',
        'Arabe': 'Niveau B1',
        'Anglais': 'Intermédiaire (en progression)'
    },
    
    'formation': [
        {
            'diplome': 'Master Mathématiques Appliquées aux Données',
            'etablissement': 'Université Sorbonne Paris Nord, Villetaneuse',
            'periode': '2024 – 2026',
            'details': 'Parcours axé sur l\'optimisation et la science des données, avec des compétences en modélisation de problèmes (programmation linéaire et entière), optimisation numérique et combinatoire, apprentissage statistique, deep learning, ainsi qu\'en traitement et analyse de données.'
        },
        {
            'diplome': 'Licence Mathématiques Appliquées',
            'etablissement': 'Université Sorbonne Paris Nord',
            'periode': '2022 – 2024',
            'details': 'Mention Bien'
        },
        {
            'diplome': 'L1 Mathématiques',
            'etablissement': 'Université Paris 8 Saint-Denis',
            'periode': '2021 – 2022',
            'details': 'Mention Bien'
        }
    ],
    
    'projets': [
        {
            'id': 1,
            'titre': 'Apprentissage Statistique (TER)',
            'periode': 'Mars 2025 – Juin 2025',
            'lieu': 'Laboratoire LAGA - Université Sorbonne Paris Nord',
            'encadrant': 'Thanh Mai PHAM NGOC',
            'description': (
                'Projet de régression non paramétrique appliqué à des données réelles issues d\'un crash moto. '
                'Estimation de la relation entre le temps et l\'accélération grâce à l\'estimateur à noyau, sans imposer de modèle linéaire. '
                'Sélection automatique de la largeur de bande h par validation croisée leave-one-out afin de trouver le meilleur niveau de lissage. '
                'Les résultats permettent d\'identifier le moment de l\'impact (vers 15-20 ms), d\'observer une phase de fortes vibrations puis un retour progressif vers l\'équilibre. '
                'La comparaison de plusieurs noyaux montre que la performance dépend principalement du choix optimal de h plutôt que du type de noyau utilisé.'
            ),
            'technologies': ['Python', 'pandas', 'NumPy', 'scikit-learn', 'Matplotlib', 'LaTeX'],
            'github': 'https://github.com/oumarmagassa/Statistiques/blob/main/Rapport_TER_Oumar_MAGASSA_modifi%C3%A9.pdf',
            'demo': None
        },
        {
            'id': 2,
            'titre': 'Optimisation combinatoire – Problème du Voyageur de Commerce (TSP)',
            'periode': 'Nov. 2024 – Jan. 2025',
            'lieu': 'Laboratoire LAGA - Université Sorbonne Paris Nord',
            'encadrant': 'Emmanuel Audusse et Francis Nier',
            'description': (
                'Étude, modélisation et résolution du TSP à partir d\'un cas réel en comparant plusieurs méthodes d\'optimisation combinatoire. '
                'Implémentation et tests de trois approches (force brute, plus proche voisin et algorithme génétique) sur un ensemble de 10 villes réelles avec de vraies distances mesurées afin d\'évaluer concrètement la performance des algorithmes. '
                'Les résultats montrent que si la force brute garantit l\'optimum mais devient rapidement inutilisable lorsque le nombre de villes augmente, l\'algorithme génétique permet d\'obtenir une solution quasiment optimale avec un temps de calcul nettement inférieur, ce qui valide l\'intérêt des heuristiques pour des problématiques industrielles réelles.'
            ),
            'technologies': ['Python', 'Optimisation', 'Graphes', 'Heuristiques'],
            'github': 'https://github.com/oumarmagassa/Optimisation/blob/main/Projet_Probl%C3%A8me_du_voyageur_de_commerce.pdf',
            'demo': None
        },
        {
            'id': 3,
            'titre': 'Recherche Opérationnelle – Planning d\'équipages (PLNE)',
            'periode': 'Août 2025 – Sept. 2025',
            'description': (
                'Modèle de programmation linéaire en nombres entiers pour affecter 10 équipages à 20 vols sur 30 jours '
                'sous contraintes réelles (temps de repos réglementaire, disponibilité, capacité opérationnelle). '
                'Implémentation en Python (PuLP, pandas) pour déterminer un planning faisable et à coût minimal. '
                'La solution finale obtenue correspond à l\'affectation optimale, exportée en fichier CSV modifiable.'
            ),
            'technologies': ['Python', 'PuLP', 'pandas', 'PLNE', 'OR'],
            'github': 'https://github.com/oumarmagassa/Recherche-Op-rationnelle/blob/main/Mini_Projet_Recherche_Op%C3%A9rationnelle.ipynb%20-%20Colab.pdf',
            'demo': None
        }
    ],
    
    'experiences': [
          
        {
            'poste': 'Projet d\'analyse numérique',
            'entreprise': 'Laboratoire LAGA - Université Sorbonne Paris Nord',
            'periode': 'Mai 2024 – Juil. 2024',
            'encadrant': 'Emmanuel Audusse',
            'details': [
                'Application de méthodes numériques pour résoudre des équations différentielles complexes',
                'Optimisation d\'implémentations pour améliorer les performances de calcul'
            ]
        },
        {
            'poste': 'Professeur particulier',
            'entreprise': 'Acadomia',
            'periode': 'Oct. 2024 – En cours',
            'details': [
                'Soutien et enseignement en mathématiques (aide aux devoirs jusqu\'au niveau licence)',
                'Accompagnement personnalisé'
            ]
        },
        {
            'poste': 'Employé de rayon',
            'entreprise': 'Carrefour Goussainville',
            'periode': 'Juil. 2022 – Sept. 2024',
            'details': [
                'Mise en rayon, gestion des stocks et accueil client'
            ]
        }
    ],
    
    'conferences': [
        {
            'nom': 'IA & Data Science Conference',
            'lieu': 'New York City',
            'date': 'Août 2025',
            'description': 'Assistance à des présentations sur l\'IA appliquée, le machine learning, les LLMs, et les applications de l\'IA à l\'optimisation'
        }
    ]
}

@app.route('/')
def index():
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)