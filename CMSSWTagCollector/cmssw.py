from flask import Flask
app = Flask(__name__)

import json, sys, urllib2
import subprocess
sys.path.insert(0, './cms-bot')
from categories import *


@app.route("/<CMSSW_VERSION>")
def return_json(CMSSW_VERSION):
	
	def GetResponsibles(cat):
		res = []
		for i in Data['CMSSW_L2']:
			if cat in Data['CMSSW_L2'][i]: res.append(i)
		return res
	
 	test = subprocess.call(['./check_repository.sh'], shell=True)
	Data = {}
	Data['CMSSW_VERSION']    = 'CMSSW_7_0_0' # default cmssw version
	Data['CMSSW_VERSION'] = CMSSW_VERSION
	Data['DOC_URL']          = 'https://cmssdt.cern.ch/SDT/doxygen/%s/doc/html/' % Data['CMSSW_VERSION']
	Data['GITHUB_URL']       = 'https://github.com/cms-sw/cmssw/tree/%s' % Data['CMSSW_VERSION']
	Data['CMSSW_MAP']        = {'analysis':'Analysis', 'alca':'Calibration and Alignment', 'daq':'DAQ', 'core' : 'Core',
		                    'dqm':'DQM', 'db':'Database', 'docs':'Documentation', 'fastsim':'Fast Simulation',
		                    'simulation':'Full Simulation', 'generators':'Generators', 'geometry':'Geometry',
		                    'hlt':'HLT', 'l1':'L1', 'operations':'Operations', 'reconstruction':'Reconstruction',
		                    'visualization':'Visualization'}
	Data['CMSSW_L1']         = CMSSW_L1 
	Data['CMSSW_L2']         = CMSSW_L2
	Data['CMSSW_CATEGORIES'] = CMSSW_CATEGORIES
	Data['CMSSW_CATEGORIES_URL'] = 'https://raw.github.com/cms-sw/cms-bot/master/categories.py'
	Data['TWIKI_PAGES']      = {'Analysis':'https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideCrab',
		                    'Calibration and Alignment':'https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideCalAli',
		                    'Core':'https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFrameWork',
		                    'DAQ':'https://twiki.cern.ch/twiki/bin/view/CMS/TriDASWikiHome',
		                    'DQM':'https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideDQM',
		                    'Database':'https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideCondDB',
		                    'Documentation':'https://twiki.cern.ch/twiki/bin/view/CMS/SWGuide',
		                    'Fast Simulation':'https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideFastSimulation',
		                    'Full Simulation':'https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideSimulation',
		                    'Generators':'https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideEventGeneration',
		                    'Geometry':'https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideDetectorDescription',
		                    'HLT':'https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideHighLevelTrigger',
		                    'L1':'https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideL1Trigger',
		                    'Reconstruction':'https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideReco',
		                    'Visualization':'https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideVisualization'}
	Data['PERSON_MAP']       = {'Analysis' : {
		                        'Gena Kukartsev'           : 'gennadiy.kukartsev@cern.ch',
		                        'Roger Wolf'               : 'Roger.Wolf@cern.ch',
		                        'Volker Adler'             : 'volker.adler@cern.ch'},
		                    'Calibration and Alignment'    : {
		                        'Andreas Pfeiffer'         : 'andreas.pfeiffer@cern.ch',
		                        'Roberto Castello'         : 'Roberto.Castello@cern.ch',
		                        'Gianluca Cerminara'       : 'gianluca.cerminara@cern.ch',
		                        'Marco De Mattia'          : 'Marco.De.Mattia@cern.ch',
		                        'Andreas Mussgiller'       : 'andreas.mussgiller@cern.ch',
		                        'Rainer Mankel'            : 'Rainer.Mankel@cern.ch'},
		                    'Core' : {
		                        'Christopher Jones'        : 'cdj@fnal.gov',
		                        'Peter Elmer'              : 'Peter.Elmer@cern.ch',
		                        'Giulio Eulisse'           : 'Giulio.Eulisse@cern.ch',
		                        'Elizabeth Sexton-Kennedy' : 'sexton@fnal.gov'},
		                    'DAQ' : {
		                        'Emilio Meschi'            : 'Emilio.Meschi@cern.ch',
		                        'Remi Mommsen'             : 'remigius.mommsen@cern.ch'},
		                    'DQM' : {
		                        'Federico De Guio'         : 'federico.de.guio@cern.ch',
		                        'Suchandra Dutta'          : 'Suchandra.Dutta@cern.ch',
		                        'Elias Ron Alvarez'        : 'elias.ron@cern.ch',
		                        'Fawad Saeed'              : 'fsaeed@cern.ch',
		                        'Muhammad Imran'           : 'muhammad.imran@cern.ch',
		                        'Muhammad Atif Shad Rao'   : 'mrao@cern.ch',
		                        'Marco Rovere'             : 'marco.rovere@cern.ch',
		                        'Adeel-ur-Rehman Zafar'    : 'zafar@mail.cern.ch'},
		                    'Database' : {
		                        'Andreas Pfeiffer'         : 'andreas.pfeiffer@cern.ch',
		                        'Frank Glege'              : 'Frank.Glege@cern.ch',
		                        'Giacomo Govi'             : 'giacomo.govi@cern.ch'},
		                    'Documentation' : {
		                        'Sudhir Malik'             : 'Sudhir.Malik@cern.ch',
		                        'Ali Mehmet Altundag'      : 'ali.mehmet.altundag@cern.ch'},
		                    'Fast Simulation' : {
		                        'Andrea Perrotta'          : 'aperrott@cern.ch',
		                        'Andrea Giammanco'         : 'andrea.giammanco@cern.ch',
		                        'Martin Grunewald'         : 'Martin.Grunewald@cern.ch',
		                        'Mike Hildreth'            : 'mikeh@omega.hep.nd.edu',
		                        'Vladimir Ivanchenko'      : 'Vladimir.Ivantchenko@cern.ch'},
		                    'Full Simulation' : {
		                        'Vladimir Ivantchenko'     : 'civanch@cern.ch',
		                        'Andrea Giammanco'         : 'andrea.giammanco@cern.ch',
		                        'Mike Hildreth'            : 'mikeh@omega.hep.nd.edu',
		                        'Sunanda Banerjee'         : 'Sunanda.banerjee@cern.ch'},
		                    'Generators' : {
		                        'Fabio Cossutti'           : 'fabio.cossutti@ts.infn.it',
		                        'Piergiulio Lenzi'         : 'piergiulio.lenzi@cern.ch',
		                        'Martijn Gosselink'        : 'martijn.gosselink@cern.ch',
		                        'Sanjay Padhi'             : 'Sanjay.Padhi@cern.ch',
		                        'Vitaliano Ciulli'         : 'vitaliano.ciulli@cern.ch'},
		                    'Geometry' : {
		                        'Christopher Jones'        : 'cdj@fnal.gov',
		                        'Mike Hildreth'            : 'mikeh@omega.hep.nd.edu',
		                        'Sunanda Banerjee'         : 'Sunanda.banerjee@cern.ch',
		                        'Ianna Osborne'            : 'Ianna.Osborne@cern.ch'},
		                    'HLT' : {
		                        'Andrea Perrotta'          : 'aperrott@cern.ch',
		                        'Andrea Bocci'             : 'andrea.bocci@cern.ch',
		                        'Martin Grunewald'         : 'Martin.Grunewald@cern.ch'},
		                    'L1' : {
		                        'Vasile Mihai Ghete'       : 'Vasile.Mihai.Ghete@cern.ch',
		                        'Arno Heister'             : 'Arno.Heister@cern.ch',
		                        'Homer Wolfe'              : 'hwolfe@fnal.gov'},
		                    'Operations' : {
		                        'Salavat Abdoulline'       : 'Salavat.Abdoulline@cern.ch',
		                        'Andrea Perrotta'          : 'aperrott@cern.ch',
		                        'David Lange'              : 'David.Lange@cern.ch',
		                        'Fabio Cossutti'           : 'fabio.cossutti@ts.infn.it',
		                        'Fabian Stoeckli'          : 'fabian.stoeckli@cern.ch',
		                        'Elizabeth Sexton-Kennedy' : 'sexton@fnal.gov',
		                        'Mike Hildreth'            : 'mikeh@omega.hep.nd.edu',
		                        'Maurizio Pierini'         : 'maurizio.pierini@cern.ch',
		                        'Francesco Santanastasio'  : 'francesco.santanastasio@cern.ch',
		                        'Salvatore Rappoccio'      : 'rappoccio@gmail.com',
		                        'Sunanda Banerjee'         : 'Sunanda.banerjee@cern.ch',
		                        'Jean-Roch Vlimant'        : 'jean-roch.vlimant@cern.ch'},
		                    'Reconstruction' : {
		                        'David Lange'              : 'David.Lange@cern.ch',
		                        'Slava Krutelyov'          : 'slava77@cern.ch',
		                        'Thomas Speer'             : 'Thomas.Speer@cern.ch',
		                        'Jean-Roch Vlimant'        : 'jean-roch.vlimant@cern.ch'},
		                    'Visualization' : {
		                        'Christopher Jones'        : 'cdj@fnal.gov',
		                        'Dmytro Kovalskyi'         : 'dmytro.kovalskyi@cern.ch',
		                        'Giulio Eulisse'           : 'Giulio.Eulisse@cern.ch',
		                        'Matevz Tadel'             : 'matevz.tadel@cern.ch'}
		                   }
	Data['CONTACTS']         = {}
	for i in Data['CMSSW_MAP']:
	    Data['CONTACTS'][Data['CMSSW_MAP'][i]] = GetResponsibles(i)
	Data['GITHUB_PAGES']     = {}
	for i in Data['CMSSW_L2']:
	    Data['GITHUB_PAGES'][i] = 'https://github.com/%s' % i
	for i in Data['CMSSW_L1']:
	    Data['GITHUB_PAGES'][i] = 'https://github.com/%s' % i
	# reorganize CMSSW_CATEGORIES
	for domain in Data['CMSSW_CATEGORIES']:
	    if not domain in Data['CMSSW_MAP'] or not domain in Data['CMSSW_CATEGORIES']: continue
	    Data['CMSSW_CATEGORIES'][Data['CMSSW_MAP'][domain]] = Data['CMSSW_CATEGORIES'][domain]
	    del Data['CMSSW_CATEGORIES'][domain]

	tmp = {}
	for domain in Data['CMSSW_CATEGORIES']:
	    tmp[domain] = {}
	    for i in Data['CMSSW_CATEGORIES'][domain]:
		level = i.split('/')
		if not len(level) == 2: continue
		if not level[0] in tmp[domain]: tmp[domain][level[0]] = {}
		tmp[domain][level[0]][level[1]] = {}

	Data['CMSSW_CATEGORIES'] = tmp

	return json.dumps(Data, indent = 2)

if __name__ == "__main__":
    app.run()
