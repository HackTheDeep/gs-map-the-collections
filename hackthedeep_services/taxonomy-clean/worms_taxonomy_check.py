# importing the requests library
import requests
import sys

def make_request_to_worms_multiple(scientificnames):
	url = "http://www.marinespecies.org/rest/AphiaRecordsByMatchNames"

	params = {'scientificnames[]':scientificnames, 'marine_only':'true'}

	try:
		r = requests.get(url = url, params = params)
		r.raise_for_status()
	except requests.exceptions.HTTPError as err:
		return {'error': 'Error in request'}

	if (r.status_code == 204):
		return {'error': 'None Found for species names'}

	data = r.json()
	return data

def make_request_to_worms(scientificname):
	url = "http://www.marinespecies.org/rest/AphiaRecordsByMatchNames"

	params = {'scientificnames[]':scientificname, 'marine_only':'true'}

	try:
		r = requests.get(url = url, params = params)
		r.raise_for_status()
	except requests.exceptions.HTTPError as err:
		return {'error': 'Error in request'}

	if (r.status_code == 204):
		return {'error': 'None Found for species name' + scientificname}

	data = r.json()
	if (len(data) == 1):
		return data[0]

	return {'error': 'None Found for species name' + scientificname}

def check_taxonomy_name_single(family, genus, species, authority, taxonomy_info):
	taxonomy_corrected = {}
	if (taxonomy_info['family'].lower() != family.lower()):
		taxonomy_corrected['family'] = taxonomy_info['family']
	if (taxonomy_info['genus'].lower() != genus.lower()):
		taxonomy_corrected['genus'] = taxonomy_info['genus']

	species_name = taxonomy_info['scientificname'].strip().upper();
	species_name = species_name.replace(taxonomy_info['genus'].upper(), '').strip()

	if (species_name != species.upper()):
		taxonomy_corrected['species'] = species_name.lower()

	if (taxonomy_info['valid_authority'] == ''):
		authority_name = ''
	else:
		authority_name = taxonomy_info['valid_authority'].split(',')[0][1:]
	
	authority_name_lower = authority_name.lower()
	if (authority.lower().strip() != authority_name.lower().strip()):
		taxonomy_corrected['author_name'] = authority_name

	return taxonomy_corrected

def get_taxonomy_for_single_species(family, genus, species, authority):
	scientificname = get_scientific_name(genus, species)
	response = make_request_to_worms(scientificname)
	return get_taxonomy_for_species(family, genus, species, authority, response)

def get_taxonomy_for_species(family, genus, species, authority, response):
	if (len(response) == 0):
		return response
	if (len(response) == 1 and 'error' in response):
		return response
	if (len(response) == 1):
		return check_taxonomy_name_single(family, genus, species, authority, response[0])
	else:
		return {'error': 'Obtained more than one result for species name'}


def get_scientific_name(genus, species):
	return genus + ' ' +  species

def handle_taxonomy_list(taxonomy_info, taxonomy_result):
	i = 0
	reponses = []
	for i in range(len(taxonomy_result)):
		#handle null case
		response = get_taxonomy_for_species(taxonomy_info[i][0], 
			taxonomy_info[i][1], taxonomy_info[i][2], taxonomy_info[i][3], taxonomy_result[i])
		i = i + 1
		reponses.append(response)
	return reponses

def get_taxonomy_for_list(taxonomy_info):
	scientificnames = []
	#Get all scientific names
	for x in taxonomy_info:
		scientificnames.append(get_scientific_name(x[1], x[2]))

	result = make_request_to_worms_multiple(scientificnames)
	return handle_taxonomy_list(taxonomy_info, result)