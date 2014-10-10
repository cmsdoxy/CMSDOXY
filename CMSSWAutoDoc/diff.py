import os, sys
import tools.url, tools.fileOps

print 'ho ho o'
if (not 'DATA' in os.environ) or (not 'TMP' in os.environ):
    print >> sys.stderr, 'ERROR: TMP and DATA variables could not be found. (do you forget the source init.sh?)'
    sys.exit(1)
data = os.environ['DATA']
tmp  = os.environ['TMP']
