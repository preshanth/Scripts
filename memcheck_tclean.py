from __future__ import print_function,division
from recipes import imager_resource_predictor as imrpredict

imParams = imrpredict.ImagerParameters(field="2",spw="8~56",antenna="",scan="",
datacolumn="corrected",imagename="blah",imsize=6144,cell=0.75,phasecenter="",
stokes="IV",projection="SIN",startmodel="",specmode="mfs",reffreq="",nchan=-1,start="",width="",
outframe="LSRK",veltype="radio",restfreq=[],interpolation="linear",perchanweightdensity=True,
gridder="awproject",facets=1,chanchunks=1,wprojplanes=32,vptable="",mosweight=False,aterm=True,
psterm=False,wbawp=True,conjbeams=True,cfcache="",usepointing=False, computepastep=360.0,
rotatepastep=5.0,pointingoffsetsigdev=[],pblimit=-0.01,normtype="flatnoise",
deconvolver="mtmfs",scales=[],nterms=2,
restoringbeam=[''],outlierfile="",weighting="briggs",robust=0.0,
noise="1.0Jy",npixels=0,uvtaper=[],niter=100,threshold=0.0,nsigma=0.0,
cycleniter=-1,cyclefactor=1.0,minpsffraction=0.05,maxpsffraction=0.8,interactive=False,
usemask="user",mask="",pbmask=0.0,sidelobethreshold=3.0,noisethreshold=5.0,
lownoisethreshold=1.5,negativethreshold=0.0,smoothfactor=1.0,minbeamfrac=0.3,
cutthreshold=0.01,growiterations=75,dogrowprune=True,minpercentchange=-1.0,
verbose=False,fastnoise=True,restart=True,savemodel="none")

mem_required = imrpredict.predict_tclean_mem_use(imParams)

mem_total = abs(mem_required['peak_in_major_cycle']) + abs(mem_required['peak_in_minor_cycle'])

print("Memory required per process is : " ,mem_total)
