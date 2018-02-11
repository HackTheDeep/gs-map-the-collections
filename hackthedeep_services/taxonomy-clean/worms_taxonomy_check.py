# importing the requests library
import requests
import sys

def make_request_to_worms(scientificname):
	url = "http://www.marinespecies.org/rest/AphiaRecordsByMatchNames"
	names = [scientificname]

	params = {'scientificnames[]':names, 'marine_only':'true'}

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

	authority_name = taxonomy_info['valid_authority'].split(',')[0][1:]
	authority_name_lower = authority_name.lower()
	if (authority.lower().strip() != authority_name_lower.strip()):
		taxonomy_corrected['author_name'] = authority_name

	return taxonomy_corrected

def get_taxonomy_for_species(family, genus, species, authority):
	scientificname = genus + ' ' +  species	
	response = make_request_to_worms(scientificname)
	if (len(response) == 0):
		return response
	if (len(response) == 1 and 'error' in response):
		return response
	if (len(response) == 1):
		return check_taxonomy_name_single(family, genus, species, authority, response[0])
	else:
		return {'error': 'Obtained more than one result for species name: ' + scientificname}