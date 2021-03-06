"""plot_roh.py:2

Plot ROH.
"""
    
__author__           = "Dilawar Singh"
__copyright__        = "Copyright 2017-, Dilawar Singh"
__version__          = "1.0.0"
__maintainer__       = "Dilawar Singh"
__email__            = "dilawars@ncbs.res.in"
__status__           = "Development"

background_ = False

import sys
import os
import pandas as pd
import numpy as np
import glob

try:
    import cPickle as pickle
except ImportError as e:
    import pickle

if not background_:
    import matplotlib as mpl
    mpl.use( 'Agg' )
    import matplotlib.cm as cm
    import matplotlib.pyplot as plt
    from matplotlib.colors import Normalize
    import PyGnuplot as gp
    mpl.rcParams['text.usetex'] = False
    mpl.rcParams['lines.linewidth'] = 4.0

from collections import defaultdict
import shutil

# colormap
def getColor( val ):
    cmap = cm.seismic_r
    norm = Normalize( vmin = 0, vmax = 100 )
    return cmap( norm( val ) )

dataDir = '_temp_data'
if os.path.exists( dataDir ):
    shutil.rmtree( dataDir )

imgDir = '_images'
if os.path.exists( imgDir ):
    shutil.rmtree( imgDir )

os.makedirs( dataDir )
os.makedirs( imgDir )

cols = [ 'Chromosome', 'Position', 'State' ]

def find_connected_segments( data ):
    # find indices where data is 1 
    flag, seg = False, [0,0]
    segs = [ ]
    for i, row in data.iterrows( ):
        if not flag and row[ 'State' ] == 1.0:
            flag = True
            seg[0] = row[ 'Position' ]
        elif flag and row[ 'State' ] == 0.0:
            flag = False
            seg[1] = row[ 'Position' ]
            segs.append( seg )
            seg = [0,0]

    return segs

def plotROH( files, ax = None ):
    """Each file is plotted
    """
    global background_
    img = [ ]
    chromosomes = defaultdict( list )
    for  i, f in enumerate( files ):
        print( '[INFO] Processing %s' % f )
        data = pd.read_csv( f, comment = '#', sep = '\t', names = cols
                , usecols = [0,1,2], dtype = int 
                )
        allchoromosomes = set( data[ 'Chromosome' ] )
        for chromo in allchoromosomes:
            cdata = data[ data[ 'Chromosome' ] == chromo ]
            chromosomes[ chromo ].append( (f, cdata ) ) 

    # img = np.zeros( shape = (len(chromosomes), maxlength ) )
    for i, chromo in enumerate( chromosomes ):
        df = { }
        print( 'CHROMOSOME : %s' % chromo )
        dataWithFs = chromosomes[ chromo ]
        df[ 'data_with_fs' ] = dataWithFs

        ytick, yticklabel = [], []

        if not background_:
            plt.figure( figsize=(12, 2*len(dataWithFs)) )
            ax1 = plt.subplot( 211 )

        maxX, allSegs = 0, [ ]
        for ii, (f, cdata) in enumerate(dataWithFs):
            print( '   - Individual %s' % f )
            segments = find_connected_segments( cdata )
            allSegs.append( segments )
            y = ii 
            ytick.append( y )
            ff = os.path.basename( f ).split( '.')[0]
            yticklabel.append( r'%s' % ff )
            for x1, x2 in segments:
                if not background_:
                    plt.plot( [x1, x2], [y, y], color = getColor( ii)  )
                if x2 > maxX:
                    maxX = x2

        if not background_:
            plt.xlabel( r'Position' )
            plt.yticks( ytick, yticklabel ) 

        df[ 'all_segments' ] = allSegs

        # Compute the overlap
        yo = [ ]
        xo = np.arange( 0, maxX, 2 )
        for x in xo:
            o = 0
            for segs in allSegs:
                for x1, x2 in segs:
                    assert x1 < x2, '%s and %s' % (x1,x2)
                    if x >= x1 and x <= x2:
                        o += 1
                        break

            yo.append( o )

        if not background_:
            ax2 = plt.subplot( 212, sharex = ax1 )
            plt.plot( xo, yo )
            plt.title( 'Overlap' )

            plt.suptitle( r'Chormosome %s' % chromo )
            plt.tight_layout( )
            outfile = os.path.join( imgDir, '%s.png' % chromo )
            plt.savefig( outfile )
            plt.close( )
            print( 'Saved to %s' % outfile )

        df[ 'xo' ] = xo
        df[ 'yo' ] = yo

        with open( '%s.pickle' % chromo, 'wb' ) as f:
            pickle.dump( df, f )
        print( 'Data saved to %s.pickle' % chromo )

def main( ):
    datadir = sys.argv[1]
    files = glob.glob( "%s/*" % datadir )
    #ax = plt.subplot( 111 )
    plotROH( files )
    #plt.show( )

if __name__ == '__main__':
    main()

