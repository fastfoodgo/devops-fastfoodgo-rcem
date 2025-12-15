Groupe :
- Ricardo Zwein
- Chems Mitta
- Elyas Meziani
- Michael Li

---

# FastFoodGo – Service de commandes

Ce projet Python a été réalisé dans le cadre du **TD – Étape 3 : DevOps & Software Engineering**.
Il illustre la mise en place d’un projet **industrialisable**, intégrant logique métier, tests unitaires, packaging Python et intégration continue.

---

## Objectifs pédagogiques

Le projet répond aux objectifs suivants  :

* Structurer un dépôt Python conforme aux bonnes pratiques
* Implémenter des fonctions métier
* Écrire des tests unitaires avec pytest
* Mettre en place le packaging Python via `pyproject.toml`
* Intégrer une CI GitHub Actions exécutant les tests
* Appliquer une gouvernance Git avec protection de la branche principale

---

## Structure du projet

```
.
├── orders_service.py        # Logique métier
├── tests/
│   ├── test_order_status.py # Tests des transitions de statut
│   └── test_order_total.py  # Tests du calcul du total
├── pyproject.toml           # Configuration du projet et dépendances
└── README.md
```

Le projet est packagé conformément aux standards Python modernes à l’aide de `pyproject.toml` .

---

## Fonctionnalités implémentées

### Validation des transitions de statut

La fonction `validate_order_status_transition` valide les changements de statut d’une commande selon un cycle de vie prédéfini.
Toute transition non autorisée ou tout statut inconnu déclenche une exception `ValueError` .

---

### Calcul du total d’une commande

La fonction `calculate_order_total` calcule le montant total d’une commande en centimes à partir :

* de la quantité de chaque article
* de son prix unitaire en centimes

Les cas limites (commande vide, quantité nulle) sont pris en compte .

---

## Tests unitaires

Les tests unitaires sont écrits avec **pytest** et couvrent :

* les transitions de statut valides et invalides
* les erreurs attendues
* les cas limites du calcul du total

Exécution des tests :

```bash
pytest
```

Les tests sont définis dans les fichiers suivants :

* `test_order_status.py` 
* `test_order_total.py` 

---

## Packaging et installation

Installation du projet en mode développement :

```bash
pip install -e ".[dev]"
```

Cette commande installe le projet ainsi que les dépendances nécessaires au développement et aux tests .

---

## Intégration continue (CI)

Une intégration continue via **GitHub Actions** est configurée pour :

* exécuter automatiquement les tests à chaque `push` et `pull_request`
* garantir que le code est fonctionnel avant toute fusion

---

## Gouvernance Git

La branche `main` est protégée conformément aux exigences du TD  :

* aucune modification directe n’est autorisée
* les contributions passent par des Pull Requests
* la CI doit être validée avant le merge
* au moins une revue est requise