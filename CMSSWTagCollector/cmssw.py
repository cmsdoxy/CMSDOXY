import json, sys, urllib2

Data = {}

Data['CMSSW_VERSION']    = 'CMSSW_7_0_0' # default cmssw version
if len(sys.argv) > 1: Data['CMSSW_VERSION'] = sys.argv[1]
Data['DOC_URL']          = 'https://cmssdt.cern.ch/SDT/doxygen/%s/doc/html/' % Data['CMSSW_VERSION']
Data['GITHUB_URL']       = 'https://github.com/cms-sw/cmssw/tree/%s' % Data['CMSSW_VERSION']

CategoriesSource         = urllib2.urlopen('https://raw.github.com/cms-sw/cms-bot/master/categories.py').read()
exec(CategoriesSource)
Data['CMSSW_L1']         = globals()['CMSSW_L1']
Data['CMSSW_L2']         = globals()['CMSSW_L2']
Data['CMSSW_CATEGORIES'] = globals()['CMSSW_CATEGORIES']
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

Data['CMSSW_MAP']        = {'analysis':'Analysis', 'alca':'Calibration and Alignment', 'daq':'DAQ',
                            'dqm':'DQM', 'db':'Database', 'doc':'Documentation', 'fastsim':'Fast Simulation',
                            'simulation':'Full Simulation', 'generators':'Generators', 'geometry':'Geometry',
                            'hlt':'HLT', 'l1':'L1', 'operations':'Operations', 'reconstruction':'Reconstruction', 
                            'visualization':'Visualization'}

def GetResponsibles(cat):
    res = []
    for i in Data['CMSSW_L2']:
        if cat in Data['CMSSW_L2'][i]: res.append(i)
    return res

Data['CONTACTS']         = {}
for i in Data['CMSSW_MAP']:
    Data['CONTACTS'][Data['CMSSW_MAP'][i]] = GetResponsibles(i)

Data['GITHUB_PAGES']     = {}
for i in Data['CMSSW_L2']:
    Data['GITHUB_PAGES'][i] = 'https://github.com/%s' % i
for i in Data['CMSSW_L1']:
    Data['GITHUB_PAGES'][i] = 'https://github.com/%s' % i

print json.dumps(Data, indent = 1)
