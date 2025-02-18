# CyberHiveIDS
1. Introduction

Cette documentation décrit le processus de mise en place d’un Système de Détection d’Intrusions (IDS) hybride sur Azure Machine Learning (Azure ML). L’IDS utilise un modèle supervisé (RandomForest) pour détecter les attaques connues et un modèle non supervisé (IsolationForest) pour repérer les anomalies et les attaques inconnues.

L'objectif est d'automatiser l’entraînement du modèle via un pipeline Azure ML, d'assurer son déploiement et d’intégrer le modèle dans un environnement cloud sécurisé.



2. Architecture de la Solution

La solution repose sur plusieurs étapes clés :

Création de l’environnement Azure ML
Enregistrement des composants du pipeline
Définition et exécution du pipeline de traitement et d'entraînement
Enregistrement des modèles IDS
Déploiement du modèle pour une utilisation en production



3. Étape 1 : Configuration de l’Environnement

3.1. Prérequis

Avant de commencer, assurez-vous d’avoir :

Un compte Azure avec un abonnement actif.
Un Azure Machine Learning Workspace.
Un groupe de ressources disponible.
Un Azure Blob Storage pour stocker les données.
Un Compute Cluster pour l'entraînement des modèles.

3.2. Création de l’Environnement Azure ML

L’environnement Azure ML est configuré avec Python 3.8, scikit-learn, pandas, numpy et une image Docker officielle Azure ML. Cet environnement garantit une compatibilité avec les composants et les pipelines.



4. Étape 2 : Enregistrement des Composants

Les composants sont des briques logiques du pipeline Azure ML, comprenant :

Un composant de prétraitement pour nettoyer et normaliser les données.
Un composant d’entraînement pour entraîner le modèle IDS hybride.

Chaque composant est défini et enregistré dans Azure ML afin d’être réutilisé dans plusieurs exécutions du pipeline.



5. Étape 3 : Mise en Place du Pipeline

Le pipeline Azure ML est conçu pour exécuter les étapes suivantes de manière automatisée :

Chargement des données IDS depuis Azure Blob Storage.
Prétraitement des données :

Suppression des colonnes inutiles.
Encodage des variables catégorielles.
Normalisation des données numériques.
Entraînement du modèle IDS hybride :

RandomForest pour détecter les intrusions connues.
IsolationForest pour détecter les anomalies et attaques inconnues.
Sauvegarde des modèles IDS sur Azure ML pour une utilisation future.



6. Étape 4 : Exécution et Suivi du Pipeline

Une fois le pipeline défini, il est exécuté automatiquement sur un compute cluster d’Azure ML.
L’exécution peut être suivie en temps réel depuis Azure ML Studio, sous la section Expériences > Hybrid-IDS-Training.



7. Étape 5 : Enregistrement et Déploiement du Modèle

7.1. Enregistrement du Modèle IDS

Une fois l'entraînement terminé, les modèles IDS sont enregistrés dans Azure ML pour être réutilisés ou déployés.

7.2. Déploiement en API REST (optionnel)

Le modèle peut être exposé sous forme d’API REST pour être utilisé dans un environnement de production.
Cette API permet à des systèmes externes d’envoyer des données réseau et de recevoir une prédiction indiquant si l’activité détectée est normale ou suspecte.



8. Résumé des Problèmes et Solutions

Problème rencontré

Solution mise en place

Docker image requise pour l’environnement

Ajout d’une image officielle Azure ML pour l’environnement

Erreur de référence des sorties (${{outputs.preprocessed_data}})

Utilisation de la nouvelle syntaxe ${{parent.jobs.preprocess.outputs.preprocessed_data}}

Erreur sur les sorties du pipeline (${{outputs.model}})

Utilisation de la nouvelle syntaxe ${{parent.outputs.model}}

Absence du groupe de ressources dans Azure ML

Ajout explicite du groupe de ressources dans chaque commande CLI



9. Conclusion

Cette solution permet d’entraîner et de déployer un IDS hybride sur Azure ML de manière automatisée. Le pipeline peut être exécuté régulièrement pour adapter le modèle aux nouvelles menaces.

Prochaines étapes possibles :

Connecter le modèle IDS à un SIEM (ex: Azure Sentinel) pour une détection en temps réel.
Optimiser les hyperparamètres du modèle via un pipeline d’expérimentation.
Déployer une API REST pour une intégration facile avec d’autres systèmes.

💡 Cette solution fournit une base évolutive pour améliorer la sécurité réseau avec du Machine Learning dans le cloud ! 🚀
