
import requests
import json
import codecs
import os
import random
selected_tech_all = ["ASHP","Battery","Biomass","EAHP","GAHP","WSHP","MicroCHP","SAHP","SolarPV","SolarThermal","WindTurbine"]

regions_all = ["Eastern","EastMidlands","London","NorthEast","NorthWest","SouthEast","SouthWest","WestMidlands","YorkshireHumberside","Scotland","Wales","NorthernIreland"]



def get_contractor_details(region, tech, proxies ):

    url = "https://mcs-website-widget.solsticecloud.com//Search/Search_Installers_TypeAndLocation"

    payload = {"sourceLat":"54.559449","sourceLng":"-4.4091917","nearest":99999,"selectedTechnologies":"{}".format(tech),"selectedRegions":"{}".format(region),"sortMode":1}
    headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,es-ES;q=0.7,es;q=0.6',
    'content-type': 'application/json; charset=UTF-8',
    'origin': 'https://mcscertified.com',
    'priority': 'u=0, i',
    'referer': 'https://mcscertified.com/find-an-installer/',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
    'Cookie': 'ASLBSA=0003812ff562825e46957fe881c03609d56a14101603e1dba0feb604a3e1add5a4df; ASLBSACORS=0003812ff562825e46957fe881c03609d56a14101603e1dba0feb604a3e1add5a4df'
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(payload), proxies=proxies)
    response_json = codecs.decode(response.text, 'unicode_escape')
    return response_json
    

if __name__:
    pass