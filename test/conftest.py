# importing the needed modules
import pytest
from typing import List
from typing import Dict

# adding some fixtures to be able to use them later in testing
# fixtures help us avoid repetition while keeping things clearer


# this is the arrange part
# creating a fixtures of kwargs that can be used
@pytest.fixture
def fake_kwargs() -> Dict:
    """This returns kwargs to be used in testing"""
    return {
        'classe_consommation_energie': 'A',
        'classe_estimation_ges': 'B',
        'consommation_energie': '0-500',
        'nom_methode_dpe': '3CL'
    }


# this is arrange part of the test
# creating a fake kwargs where there is no results
@pytest.fixture
def fake_kwargs_nothing_found() -> Dict:
    """This returns a kwargs that are not found in the dataset to be used in the testing """
    return {
        'classe_consommation_energie': 'A',
        'classe_estimation_ges': 'B',
        'consommation_energie': '0-1',
        'nom_methode_dpe': '3CL'
    }


# this is the arrange part
# creating a fixtures of kwargs that can be used
@pytest.fixture
def fake_kwargs_habitation() -> Dict:
    """This returns kwargs to be used in testing"""
    return {
        'secteur_activite': 'Maison Individuelle',
        'surface_habitable': '110-150',
        'annee_construction': 2006.0
    }


# creating a fixture to see if inventory works well
@pytest.fixture
def fake_kwargs_inventory() -> Dict:
    """this return a dictionary for inventory count query"""
    return {'classe_consommation_energie': 'A', 'classe_estimation_ges': 'A', 'annee_construction': 2006.0}


# creating a fixtures to replace a fake query_list
@pytest.fixture
def fake_query_list() -> List[Dict]:
    """This function return a list of Dictionary where"""
    return [
        {'consommations_energie.classe_consommation_energie': 'A'},
        {'emissions_ges.classe_estimation_ges': 'B'},
        {'$and': [
                    {'consommations_energie.consommation_energie': {'$gt': 0}},
                    {'consommations_energie.consommation_energie': {'$lt': 500}}
                 ]
         },
        {'methodologie.nom_methode_dpe': '3CL'}
    ]


# creating a fixtures to replace a fake results for search_all_dpe
@pytest.fixture
def expected_results_search_all_dpe() -> List:
    """this is function returns the expected results to get for a certain kwargs for the search_all_dpe function"""
    return ["{\"numero_dpe\": \"1401N1001678F\", \"identification\": {\"id\": 1446898, \"usr_diagnostiqueur_id\": 6931, \"usr_logiciel_id\": 7, \"tr001_modele_dpe_id\": 11}, \"methodologie\": {\"nom_methode_dpe\": \"3CL\", \"version_methode_dpe\": \"Version 1.3\", \"nom_methode_etude_thermique\": NaN, \"version_methode_etude_thermique\": NaN}, \"date\": {\"date_visite_diagnostiqueur\": \"2014-10-09\", \"date_etablissement_dpe\": \"2014-10-09\", \"date_arrete_tarifs_energies\": \"2011-08-15\", \"date_reception_dpe\": \"2014-10-17 16:33:26\"}, \"commentaire\": {\"commentaires_ameliorations_recommandations\": NaN, \"explication_personnalisee\": NaN}, \"consommations_energie\": {\"consommation_energie\": 50.62, \"classe_consommation_energie\": \"A\"}, \"emissions_ges\": {\"estimation_ges\": 6.87, \"classe_estimation_ges\": \"B\"}, \"quartier\": {\"tv016_departement_id\": 1, \"commune\": \"VILLARS LES DOMBES\", \"arrondissement\": \"-\", \"type_voie\": NaN, \"nom_rue\": \"Lotissement la Mantoli\\u00e8res n\\u00b035\", \"numero_rue\": \"Lotissement la Mantoli\\u00e8res n\\u00b035\", \"code_postal\": 1330.0, \"code_insee_commune\": \"63000\", \"code_insee_commune_actualise\": \"63000\"}, \"batiment\": {\"tr002_type_batiment_id\": 1, \"secteur_activite\": NaN, \"annee_construction\": 2014, \"batiment\": NaN, \"escalier\": NaN, \"numero_lot\": NaN, \"surface_commerciale_contractuelle\": NaN, \"portee_dpe_batiment\": 1.0, \"partie_batiment\": NaN, \"shon\": 0.0, \"surface_utile\": 0.0, \"surface_thermique_parties_communes\": 0.0, \"en_souterrain\": 0.0, \"en_surface\": 1.0, \"nombre_niveaux\": 1.0, \"nombre_circulations_verticales\": 0.0, \"nombre_boutiques\": 0.0, \"surface_baies_orientees_nord\": 8.37, \"surface_baies_orientees_est_ouest\": 0.57, \"surface_baies_orientees_sud\": 5.94, \"surface_planchers_hauts_deperditifs\": 100.61, \"surface_planchers_bas_deperditifs\": 100.61, \"surface_parois_verticales_opaques_deperditives\": 99.19, \"etat_avancement\": 1, \"organisme_certificateur\": \"Organisme certificateur\", \"adresse_organisme_certificateur\": \"  -  \", \"dpe_vierge\": 0.0, \"est_efface\": 0}, \"maison\": {\"surface_habitable\": 98.29, \"surface_thermique_lot\": 98.29, \"etage\": NaN, \"porte\": NaN, \"presence_verriere\": 0.0, \"surface_verriere\": 0.0, \"type_vitrage_verriere\": NaN, \"nombre_entrees_avec_sas\": 0.0, \"nombre_entrees_sans_sas\": 0.0}}","{\"numero_dpe\": \"1501N1001406V\", \"identification\": {\"id\": 2204127, \"usr_diagnostiqueur_id\": 6931, \"usr_logiciel_id\": 7, \"tr001_modele_dpe_id\": 11}, \"methodologie\": {\"nom_methode_dpe\": \"3CL\", \"version_methode_dpe\": \"Version 1.3\", \"nom_methode_etude_thermique\": NaN, \"version_methode_etude_thermique\": NaN}, \"date\": {\"date_visite_diagnostiqueur\": \"2015-06-08\", \"date_etablissement_dpe\": \"2015-06-08\", \"date_arrete_tarifs_energies\": \"2011-08-15\", \"date_reception_dpe\": \"2015-06-08 18:25:55\"}, \"commentaire\": {\"commentaires_ameliorations_recommandations\": NaN, \"explication_personnalisee\": NaN}, \"consommations_energie\": {\"consommation_energie\": 49.29, \"classe_consommation_energie\": \"A\"}, \"emissions_ges\": {\"estimation_ges\": 6.37, \"classe_estimation_ges\": \"B\"}, \"quartier\": {\"tv016_departement_id\": 1, \"commune\": \"SAINT JEAN LE VIEUX\", \"arrondissement\": \"-\", \"type_voie\": NaN, \"nom_rue\": \"LE CLOS DISSIER LOT 17\", \"numero_rue\": \"LE CLOS DISSIER LOT 17\", \"code_postal\": \"01640\", \"code_insee_commune\": \"63000\", \"code_insee_commune_actualise\": \"63000\"}, \"batiment\": {\"tr002_type_batiment_id\": 1, \"secteur_activite\": NaN, \"annee_construction\": 2014, \"batiment\": NaN, \"escalier\": NaN, \"numero_lot\": NaN, \"surface_commerciale_contractuelle\": NaN, \"portee_dpe_batiment\": 1.0, \"partie_batiment\": NaN, \"shon\": 0.0, \"surface_utile\": 0.0, \"surface_thermique_parties_communes\": 0.0, \"en_souterrain\": 0.0, \"en_surface\": 1.0, \"nombre_niveaux\": 2.0, \"nombre_circulations_verticales\": 0.0, \"nombre_boutiques\": 0.0, \"surface_baies_orientees_nord\": 0.93, \"surface_baies_orientees_est_ouest\": 14.97, \"surface_baies_orientees_sud\": 4.98, \"surface_planchers_hauts_deperditifs\": 64.12, \"surface_planchers_bas_deperditifs\": 64.12, \"surface_parois_verticales_opaques_deperditives\": 141.52, \"etat_avancement\": 1, \"organisme_certificateur\": \"Organisme certificateur\", \"adresse_organisme_certificateur\": \"  -  \", \"dpe_vierge\": 0.0, \"est_efface\": 0}, \"maison\": {\"surface_habitable\": 120.32, \"surface_thermique_lot\": 120.32, \"etage\": NaN, \"porte\": NaN, \"presence_verriere\": 0.0, \"surface_verriere\": 0.0, \"type_vitrage_verriere\": NaN, \"nombre_entrees_avec_sas\": 0.0, \"nombre_entrees_sans_sas\": 0.0}}","{\"numero_dpe\": \"1501N1001585D\", \"identification\": {\"id\": 2282624, \"usr_diagnostiqueur_id\": 6931, \"usr_logiciel_id\": 7, \"tr001_modele_dpe_id\": 11}, \"methodologie\": {\"nom_methode_dpe\": \"3CL\", \"version_methode_dpe\": \"Version 1.3\", \"nom_methode_etude_thermique\": NaN, \"version_methode_etude_thermique\": NaN}, \"date\": {\"date_visite_diagnostiqueur\": \"2015-06-22\", \"date_etablissement_dpe\": \"2015-06-22\", \"date_arrete_tarifs_energies\": \"2011-08-15\", \"date_reception_dpe\": \"2015-06-26 10:16:41\"}, \"commentaire\": {\"commentaires_ameliorations_recommandations\": NaN, \"explication_personnalisee\": NaN}, \"consommations_energie\": {\"consommation_energie\": 44.64, \"classe_consommation_energie\": \"A\"}, \"emissions_ges\": {\"estimation_ges\": 8.29, \"classe_estimation_ges\": \"B\"}, \"quartier\": {\"tv016_departement_id\": 1, \"commune\": \"VILLARS-LES-DOMBES\", \"arrondissement\": \"-\", \"type_voie\": NaN, \"nom_rue\": \"LOT 10, Lotissement ''LA MANTOLIERE''\", \"numero_rue\": \"LOT 10, Lotissement ''LA MANTOLIERE''\", \"code_postal\": \"01330\", \"code_insee_commune\": \"63000\", \"code_insee_commune_actualise\": \"63000\"}, \"batiment\": {\"tr002_type_batiment_id\": 1, \"secteur_activite\": NaN, \"annee_construction\": 2013, \"batiment\": NaN, \"escalier\": NaN, \"numero_lot\": NaN, \"surface_commerciale_contractuelle\": NaN, \"portee_dpe_batiment\": 1.0, \"partie_batiment\": NaN, \"shon\": 0.0, \"surface_utile\": 0.0, \"surface_thermique_parties_communes\": 0.0, \"en_souterrain\": 0.0, \"en_surface\": 1.0, \"nombre_niveaux\": 2.0, \"nombre_circulations_verticales\": 0.0, \"nombre_boutiques\": 0.0, \"surface_baies_orientees_nord\": 7.73, \"surface_baies_orientees_est_ouest\": 10.38, \"surface_baies_orientees_sud\": 14.85, \"surface_planchers_hauts_deperditifs\": 102.88, \"surface_planchers_bas_deperditifs\": 104.23, \"surface_parois_verticales_opaques_deperditives\": 161.61, \"etat_avancement\": 1, \"organisme_certificateur\": \"Organisme certificateur\", \"adresse_organisme_certificateur\": \"  -  \", \"dpe_vierge\": 0.0, \"est_efface\": 0}, \"maison\": {\"surface_habitable\": 166.44, \"surface_thermique_lot\": 166.44, \"etage\": NaN, \"porte\": NaN, \"presence_verriere\": 0.0, \"surface_verriere\": 0.0, \"type_vitrage_verriere\": NaN, \"nombre_entrees_avec_sas\": 0.0, \"nombre_entrees_sans_sas\": 0.0}}"]


# creating a fixture to send ID to the function
@pytest.fixture
def fake_id() -> str:
    """this function returns a fake temporary ID to do some testing"""
    return '1301V1000003T'


# creating a fixture to replace a fake results for search_all_dpe_by_id
@pytest.fixture
def expected_results_search_all_dpe_by_id() -> str:
    """This is function returns the expected results to get for a certain ID"""
    return "{\"numero_dpe\": \"1301V1000003T\", \"identification\": {\"id\": 178, \"usr_diagnostiqueur_id\": 6991, \"usr_logiciel_id\": 3, \"tr001_modele_dpe_id\": 1}, \"methodologie\": {\"nom_methode_dpe\": \"3CL\", \"version_methode_dpe\": \"3CL-DPE, version 1.3\", \"nom_methode_etude_thermique\": NaN, \"version_methode_etude_thermique\": NaN}, \"date\": {\"date_visite_diagnostiqueur\": \"2013-04-10\", \"date_etablissement_dpe\": \"2013-04-12\", \"date_arrete_tarifs_energies\": \"2011-09-15\", \"date_reception_dpe\": \"2013-04-11 04:00:00\"}, \"commentaire\": {\"commentaires_ameliorations_recommandations\": NaN, \"explication_personnalisee\": NaN}, \"consommations_energie\": {\"consommation_energie\": 132.0, \"classe_consommation_energie\": \"C\"}, \"emissions_ges\": {\"estimation_ges\": 29.0, \"classe_estimation_ges\": \"D\"}, \"quartier\": {\"tv016_departement_id\": 1, \"commune\": \"SAINT-MARTIN-DU-FR\\u00caNE\", \"arrondissement\": NaN, \"type_voie\": NaN, \"nom_rue\": \"3, Impasse du Tilleul\", \"numero_rue\": NaN, \"code_postal\": \"01430\", \"code_insee_commune\": \"01430\", \"code_insee_commune_actualise\": \"01430\"}, \"batiment\": {\"tr002_type_batiment_id\": 1, \"secteur_activite\": \"Maison Individuelle\", \"annee_construction\": 5200, \"batiment\": NaN, \"escalier\": NaN, \"numero_lot\": NaN, \"surface_commerciale_contractuelle\": NaN, \"portee_dpe_batiment\": 2.0, \"partie_batiment\": NaN, \"shon\": 190.0, \"surface_utile\": 0.0, \"surface_thermique_parties_communes\": 0.0, \"en_souterrain\": 0.0, \"en_surface\": 0.0, \"nombre_niveaux\": 2.0, \"nombre_circulations_verticales\": 0.0, \"nombre_boutiques\": 0.0, \"surface_baies_orientees_nord\": 0.0, \"surface_baies_orientees_est_ouest\": 0.0, \"surface_baies_orientees_sud\": 0.0, \"surface_planchers_hauts_deperditifs\": 0.0, \"surface_planchers_bas_deperditifs\": 0.0, \"surface_parois_verticales_opaques_deperditives\": 0.0, \"etat_avancement\": 1, \"organisme_certificateur\": \"DEKRA\", \"adresse_organisme_certificateur\": \"3/5 avenue Garlande 92220 BAGNEUX (d\\u00e9tail sur www.cofrac.fr programme n\\u00b04-4-11)\", \"dpe_vierge\": 0.0, \"est_efface\": 0}, \"maison\": {\"surface_habitable\": 190.0, \"surface_thermique_lot\": 190.0, \"etage\": NaN, \"porte\": NaN, \"presence_verriere\": 0.0, \"surface_verriere\": 0.0, \"type_vitrage_verriere\": NaN, \"nombre_entrees_avec_sas\": 0.0, \"nombre_entrees_sans_sas\": 0.0}}"


# creating a fixture for search_all_habitation expected results for a certain kwargs
@pytest.fixture
def expected_results_search_all_habitation() -> List:
    return  ["{\"maison\": {\"surface_habitable\": 123.0, \"surface_thermique_lot\": 123.0, \"etage\": NaN, \"porte\": NaN, \"presence_verriere\": 0.0, \"surface_verriere\": 0.0, \"type_vitrage_verriere\": NaN, \"nombre_entrees_avec_sas\": 0.0, \"nombre_entrees_sans_sas\": 0.0}, \"quartier\": {\"tv016_departement_id\": 1, \"commune\": \"CESSY\", \"arrondissement\": NaN, \"type_voie\": NaN, \"nom_rue\": \"916 rue du Jura\", \"numero_rue\": NaN, \"code_postal\": \"01170\", \"code_insee_commune\": \"01170\", \"code_insee_commune_actualise\": \"01170\"}, \"batiment\": {\"tr002_type_batiment_id\": 1, \"secteur_activite\": \"Maison Individuelle\", \"annee_construction\": 2006, \"batiment\": NaN, \"escalier\": NaN, \"numero_lot\": \"Non communiqu\\u00e9\", \"surface_commerciale_contractuelle\": \"100\", \"portee_dpe_batiment\": 2.0, \"partie_batiment\": NaN, \"shon\": 123.0, \"surface_utile\": 100.0, \"surface_thermique_parties_communes\": 0.0, \"en_souterrain\": 0.0, \"en_surface\": 0.0, \"nombre_niveaux\": 2.0, \"nombre_circulations_verticales\": 0.0, \"nombre_boutiques\": 0.0, \"surface_baies_orientees_nord\": 0.0, \"surface_baies_orientees_est_ouest\": 0.0, \"surface_baies_orientees_sud\": 0.0, \"surface_planchers_hauts_deperditifs\": 0.0, \"surface_planchers_bas_deperditifs\": 0.0, \"surface_parois_verticales_opaques_deperditives\": 0.0, \"etat_avancement\": 1, \"organisme_certificateur\": \"V\\u00e9ritas\", \"adresse_organisme_certificateur\": \"Le Guillaumet 92046 PARIS LA DEFENSE CEDEX (d\\u00e9tail sur www.cofrac.fr programme n\\u00b04-4-11)\", \"dpe_vierge\": 0.0, \"est_efface\": 0}}"]


# creating a fixture to replace a fake results for search_habitation_dpe_by_id
@pytest.fixture
def expected_results_search_habitation_dpe_by_id() -> str:
    """This is function returns the expected results to get for a certain ID"""
    return "{\"maison\": {\"surface_habitable\": 190.0, \"surface_thermique_lot\": 190.0, \"etage\": NaN, \"porte\": NaN, \"presence_verriere\": 0.0, \"surface_verriere\": 0.0, \"type_vitrage_verriere\": NaN, \"nombre_entrees_avec_sas\": 0.0, \"nombre_entrees_sans_sas\": 0.0}, \"quartier\": {\"tv016_departement_id\": 1, \"commune\": \"SAINT-MARTIN-DU-FR\\u00caNE\", \"arrondissement\": NaN, \"type_voie\": NaN, \"nom_rue\": \"3, Impasse du Tilleul\", \"numero_rue\": NaN, \"code_postal\": \"01430\", \"code_insee_commune\": \"01430\", \"code_insee_commune_actualise\": \"01430\"}, \"batiment\": {\"tr002_type_batiment_id\": 1, \"secteur_activite\": \"Maison Individuelle\", \"annee_construction\": 5200, \"batiment\": NaN, \"escalier\": NaN, \"numero_lot\": NaN, \"surface_commerciale_contractuelle\": NaN, \"portee_dpe_batiment\": 2.0, \"partie_batiment\": NaN, \"shon\": 190.0, \"surface_utile\": 0.0, \"surface_thermique_parties_communes\": 0.0, \"en_souterrain\": 0.0, \"en_surface\": 0.0, \"nombre_niveaux\": 2.0, \"nombre_circulations_verticales\": 0.0, \"nombre_boutiques\": 0.0, \"surface_baies_orientees_nord\": 0.0, \"surface_baies_orientees_est_ouest\": 0.0, \"surface_baies_orientees_sud\": 0.0, \"surface_planchers_hauts_deperditifs\": 0.0, \"surface_planchers_bas_deperditifs\": 0.0, \"surface_parois_verticales_opaques_deperditives\": 0.0, \"etat_avancement\": 1, \"organisme_certificateur\": \"DEKRA\", \"adresse_organisme_certificateur\": \"3/5 avenue Garlande 92220 BAGNEUX (d\\u00e9tail sur www.cofrac.fr programme n\\u00b04-4-11)\", \"dpe_vierge\": 0.0, \"est_efface\": 0}}"
