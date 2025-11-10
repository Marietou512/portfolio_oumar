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
    'date_naissance': '26 mars 2004',
    
    'competences_info': {
        'Python': 'Modélisation mathématique et analyse de données (pandas, scikit-learn)',
        'R': 'En cours d\'apprentissage pour l\'analyse statistique et la data science',
        'LaTeX': 'Rédaction de documents scientifiques et rapports mathématiques',
        'C/C++': 'En cours d\'apprentissage pour l\'implémentation d\'algorithmes',
        'PL/SQL': 'Notions de base pour la gestion de bases de données',
        'Outils bureautiques': 'Bonne maîtrise de Word et Excel'
    },
    
    'competences_pro': [
        'Communication scientifique : Présentation claire de concepts lors de séminaires et projets académiques',
        'Résolution de problèmes complexes : analyse et modélisation de situations réelles',
        'Modélisation mathématique : expérience en optimisation combinatoire',
        'Recherche opérationnelle : modélisation mathématique de problèmes appliqués, résolution de PLNE avec PuLP'
    ],
    
    'langues': {
        'Français': 'Langue maternelle',
        'Arabe': 'Niveau B1',
        'Anglais': 'Intermédiaire (en progression)'
    },
    
    'formation': [
        {
            'diplome': 'Master Mathématiques Appliquées aux Données',
            'etablissement': 'Université Sorbonne Paris Nord, Villetaneuse',
            'periode': '2024 – 2026',
            'details': 'Bourse d\'excellence. Parcours axé sur l\'optimisation et la science des données, avec des compétences en modélisation de problèmes (programmation linéaire et entière), optimisation numérique et combinatoire, apprentissage statistique, deep learning, ainsi qu\'en traitement et analyse de données.'
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
            'titre': 'Optimisation d\'un planning d\'équipages',
            'periode': 'Août 2025 – Sept. 2025',
            'description': 'Conception d\'un modèle de programmation linéaire en nombres entiers (PLNE) pour optimiser l\'affectation de 10 équipages à 20 vols sur 30 jours, sous contraintes de repos et de disponibilité. Implémentation en Python (PuLP, pandas) avec génération automatique d\'un planning optimal à coût minimal, dans le cadre d\'une préparation à un stage en recherche opérationnelle chez Air France.'
        }
    ],
    
    'experiences': [
        {
            'poste': 'Travail d\'étude et de recherche (TER)',
            'entreprise': 'Laboratoire LAGA - Université Sorbonne Paris Nord',
            'periode': 'Mars 2024 – Juin 2025',
            'encadrant': 'Thanh Mai PHAM NGOC',
            'details': [
                'Codage en Python d\'une chaîne reproductible (prétraitement, simulations, figures)',
                'Implémentation et comparaison d\'estimateurs à noyau (Nadaraya-Watson) et régresseurs locaux',
                'Protocole de simulation et sélection automatique de h par validation croisée (LOO)',
                'Application sur le jeu mcycle (MASS) : code, figures et rapport LaTeX'
            ]
        },
        {
            'poste': 'Projet d\'optimisation combinatoire',
            'entreprise': 'Laboratoire LAGA - Université Sorbonne Paris Nord',
            'periode': 'Nov. 2024 – Jan. 2025',
            'encadrant': 'Emmanuel Audusse et Francis Nier',
            'details': [
                'Modélisation et résolution du problème du voyageur de commerce',
                'Développement d\'algorithmes et modélisation mathématiques',
                'Amélioration de la réduction de coût et des performances de calcul'
            ]
        },
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