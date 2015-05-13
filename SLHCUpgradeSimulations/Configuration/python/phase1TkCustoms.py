import FWCore.ParameterSet.Config as cms

from RecoTracker.IterativeTracking.iterativeTk_cff import *
from RecoTracker.IterativeTracking.ElectronSeeds_cff import *
from SLHCUpgradeSimulations.Configuration.customise_mixing import customise_pixelMixing_PU

def customise(process):
    if hasattr(process,'DigiToRaw'):
        process=customise_DigiToRaw(process)
    if hasattr(process,'RawToDigi'):
        process=customise_RawToDigi(process)
    n=0
    if hasattr(process,'reconstruction') or hasattr(process,'dqmoffline_step'):
        if hasattr(process,'mix'): 
            if hasattr(process.mix,'input'):
                n=process.mix.input.nbPileupEvents.averageNumber.value()
        else:
            print 'phase1TkCustoms requires a --pileup option to cmsDriver to run the reconstruction/dqm'
            print 'Please provide one!'
            sys.exit(1)
    if hasattr(process,'reconstruction'):
        process=customise_Reco(process,float(n))
                
    if hasattr(process,'digitisation_step'):
        process=customise_Digi(process)
    if hasattr(process,'dqmoffline_step'):
        process=customise_DQM(process,n)
    if hasattr(process,'dqmHarvesting'):
        process=customise_harvesting(process)
    if hasattr(process,'validation_step'):
        process=customise_Validation(process)
    process=customise_condOverRides(process)
    
    return process

def customise_DigiToRaw(process):
    process.digi2raw_step.remove(process.siPixelRawData)
    process.digi2raw_step.remove(process.castorRawData)
    return process

def customise_RawToDigi(process):
    process.raw2digi_step.remove(process.siPixelDigis)
    process.raw2digi_step.remove(process.castorDigis)
    return process

def customise_Digi(process):
    process.mix.digitizers.pixel.MissCalibrate = False
    process.mix.digitizers.pixel.LorentzAngle_DB = False
    process.mix.digitizers.pixel.killModules = True
    process.mix.digitizers.pixel.DeadModules = cms.VPSet(
    cms.PSet(Dead_detID = cms.int32(352871428), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352875524), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352879620), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352883716), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352887812), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352891908), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352896004), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352900100), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352904196), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352908292), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352912388), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352973828), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352977924), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352982020), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352986116), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352990212), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352994308), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352998404), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353002500), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353006596), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353010692), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353014788), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353018884), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353022980), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353027076), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353031172), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353035268), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353039364), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352872452), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352876548), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352880644), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352884740), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352888836), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352892932), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352897028), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352901124), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352905220), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352909316), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352913412), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352974852), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352978948), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352983044), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352987140), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352991236), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352995332), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352999428), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353003524), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353007620), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353011716), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353015812), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353019908), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353024004), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353028100), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353032196), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353036292), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353040388), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353133572), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353137668), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353141764), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353145860), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353149956), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353154052), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353158148), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353162244), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353166340), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353170436), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353174532), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353235972), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353240068), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353244164), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353248260), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353252356), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353256452), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353260548), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353264644), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353268740), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353272836), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353276932), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353281028), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353285124), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353289220), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353293316), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353297412), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353301508), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353134596), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353138692), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353142788), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353146884), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353150980), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353155076), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353159172), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353163268), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353167364), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353171460), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353175556), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353236996), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353241092), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353245188), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353249284), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353253380), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353257476), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353261572), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353265668), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353269764), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353273860), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353277956), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353282052), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353286148), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353290244), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353294340), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353298436), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(353302532), Module = cms.string('whole'))
    )


    process.mix.digitizers.pixel.useDB = False
    process.mix.digitizers.pixel.DeadModules_DB = False
    process.mix.digitizers.pixel.NumPixelBarrel = cms.int32(4)
    process.mix.digitizers.pixel.NumPixelEndcap = cms.int32(3)
    process.mix.digitizers.pixel.ThresholdInElectrons_FPix = cms.double(2000.0)
    process.mix.digitizers.pixel.ThresholdInElectrons_BPix = cms.double(2000.0)
    process.mix.digitizers.pixel.ThresholdInElectrons_BPix_L1 = cms.double(2000.0)
    process.mix.digitizers.pixel.thePixelColEfficiency_BPix4 = cms.double(0.999)
    process.mix.digitizers.pixel.thePixelEfficiency_BPix4 = cms.double(0.999)
    process.mix.digitizers.pixel.thePixelChipEfficiency_BPix4 = cms.double(0.999)
    process.mix.digitizers.pixel.thePixelColEfficiency_FPix3 = cms.double(0.999)
    process.mix.digitizers.pixel.thePixelEfficiency_FPix3 = cms.double(0.999)
    process.mix.digitizers.pixel.thePixelChipEfficiency_FPix3 = cms.double(0.999)
    process.mix.digitizers.pixel.AddPixelInefficiencyFromPython = cms.bool(True)

    process=customise_pixelMixing_PU(process)
    return process


# DQM steps change
def customise_DQM(process,pileup):
    # We cut down the number of iterative tracking steps
    process.dqmoffline_step.remove(process.muonAnalyzer)
    process.dqmoffline_step.remove(process.jetMETAnalyzer)

    #put isUpgrade flag==true
    process.SiPixelRawDataErrorSource.isUpgrade = cms.untracked.bool(True)
    process.SiPixelDigiSource.isUpgrade = cms.untracked.bool(True)
    process.SiPixelClusterSource.isUpgrade = cms.untracked.bool(True)
    process.SiPixelRecHitSource.isUpgrade = cms.untracked.bool(True)
    process.SiPixelTrackResidualSource.isUpgrade = cms.untracked.bool(True)
    process.SiPixelHitEfficiencySource.isUpgrade = cms.untracked.bool(True)

    from DQM.TrackingMonitor.customizeTrackingMonitorSeedNumber import customise_trackMon_IterativeTracking_PHASE1PU140
    from DQM.TrackingMonitor.customizeTrackingMonitorSeedNumber import customise_trackMon_IterativeTracking_PHASE1PU70

    if pileup>100:
        process=customise_trackMon_IterativeTracking_PHASE1PU140(process)
    else:
        process=customise_trackMon_IterativeTracking_PHASE1PU70(process)
    return process

def customise_Validation(process):
    process.validation_step.remove(process.PixelTrackingRecHitsValid)
    # We don't run the HLT
    process.validation_step.remove(process.HLTSusyExoVal)
    process.validation_step.remove(process.hltHiggsValidator)
    process.validation_step.remove(process.relvalMuonBits)
    return process

def customise_Validation_Trackingonly(process):

    #To allow Tracking to perform special tracking only validation 
    process.trackValidator.label=cms.VInputTag(cms.InputTag("cutsRecoTracksHp"))
    process.tracksValidationSelectors = cms.Sequence(process.cutsRecoTracksHp)
    process.globalValidation.remove(process.recoMuonValidation)
    process.validation.remove(process.recoMuonValidation)
    process.validation_preprod.remove(process.recoMuonValidation)
    process.validation_step.remove(process.recoMuonValidation)
    process.validation.remove(process.globalrechitsanalyze)
    process.validation_prod.remove(process.globalrechitsanalyze)
    process.validation_step.remove(process.globalrechitsanalyze)
    process.validation.remove(process.stripRecHitsValid)
    process.validation_step.remove(process.stripRecHitsValid)
    process.validation_step.remove(process.StripTrackingRecHitsValid)
    process.globalValidation.remove(process.vertexValidation)
    process.validation.remove(process.vertexValidation)
    process.validation_step.remove(process.vertexValidation)
    process.mix.input.nbPileupEvents.averageNumber = cms.double(0.0)
    process.mix.minBunch = cms.int32(0)
    process.mix.maxBunch = cms.int32(0)
    return process

def customise_harvesting(process):
    process.dqmHarvesting.remove(process.jetMETDQMOfflineClient)
    process.dqmHarvesting.remove(process.dataCertificationJetMET)
    #######process.dqmHarvesting.remove(process.sipixelEDAClient)
    process.sipixelEDAClient.isUpgrade = cms.untracked.bool(True)
    process.dqmHarvesting.remove(process.sipixelCertification)
    return (process)        

def customise_condOverRides(process):
    process.trackerTopologyConstants.pxb_layerStartBit = cms.uint32(20)
    process.trackerTopologyConstants.pxb_ladderStartBit = cms.uint32(12)
    process.trackerTopologyConstants.pxb_moduleStartBit = cms.uint32(2)
    process.trackerTopologyConstants.pxb_layerMask = cms.uint32(15)
    process.trackerTopologyConstants.pxb_ladderMask = cms.uint32(255)
    process.trackerTopologyConstants.pxb_moduleMask = cms.uint32(1023)
    process.trackerTopologyConstants.pxf_diskStartBit = cms.uint32(18)
    process.trackerTopologyConstants.pxf_bladeStartBit = cms.uint32(12)
    process.trackerTopologyConstants.pxf_panelStartBit = cms.uint32(10)
    process.trackerTopologyConstants.pxf_moduleMask = cms.uint32(255)
    return process

def add_detailed_pixel_dqm(process):
    #enable modOn
    process.SiPixelRawDataErrorSource.modOn = cms.untracked.bool(True)
    process.SiPixelDigiSource.modOn = cms.untracked.bool(True)
    process.SiPixelClusterSource.modOn = cms.untracked.bool(True)
    process.SiPixelRecHitSource.modOn = cms.untracked.bool(True)
    process.SiPixelTrackResidualSource.modOn = cms.untracked.bool(True)
    process.SiPixelHitEfficiencySource.modOn = cms.untracked.bool(True)

    return process


def remove_pixel_ineff(process):
    if hasattr(process,'mix'):
        process.mix.digitizers.pixel.AddPixelInefficiencyFromPython = cms.bool(False) 

    return process
    

def customise_Reco(process,pileup):

    #this code supports either 70 or 140 pileup configurations - should fix as to support 0
    nPU=70
    if pileup>100: nPU=140
    
    #use with latest pixel geometry
    process.ClusterShapeHitFilterESProducer.PixelShapeFile = cms.string('RecoPixelVertexing/PixelLowPtUtilities/data/pixelShape_Phase1Tk.par')
    # Need this line to stop error about missing siPixelDigis.
    process.MeasurementTracker.inactivePixelDetectorLabels = cms.VInputTag()

    # new layer list (3/4 pixel seeding) in InitialStep and pixelTracks
    process.pixellayertriplets.layerList = cms.vstring( 'BPix1+BPix2+BPix3',
                                                        'BPix2+BPix3+BPix4',
                                                        'BPix1+BPix3+BPix4',
                                                        'BPix1+BPix2+BPix4',
                                                        'BPix2+BPix3+FPix1_pos',
                                                        'BPix2+BPix3+FPix1_neg',
                                                        'BPix1+BPix2+FPix1_pos',
                                                        'BPix1+BPix2+FPix1_neg',
                                                        'BPix2+FPix1_pos+FPix2_pos',
                                                        'BPix2+FPix1_neg+FPix2_neg',
                                                        'BPix1+FPix1_pos+FPix2_pos',
                                                        'BPix1+FPix1_neg+FPix2_neg',
                                                        'FPix1_pos+FPix2_pos+FPix3_pos',
                                                        'FPix1_neg+FPix2_neg+FPix3_neg' )

    # New tracking.  This is really ugly because it redefines globalreco and reconstruction.
    # It can be removed if change one line in Configuration/StandardSequences/python/Reconstruction_cff.py
    # from RecoTracker_cff.py to RecoTrackerPhase1PU140_cff.py

    # remove all the tracking first
    itIndex=process.globalreco.index(process.trackingGlobalReco)
    grIndex=process.reconstruction.index(process.globalreco)

    process.reconstruction.remove(process.globalreco)
    process.globalreco.remove(process.iterTracking)
    process.globalreco.remove(process.electronSeedsSeq)
    process.reconstruction_fromRECO.remove(process.trackingGlobalReco)
    del process.iterTracking
    del process.ckftracks
    del process.ckftracks_woBH
    del process.ckftracks_wodEdX
    del process.ckftracks_plus_pixelless
    del process.trackingGlobalReco
    del process.electronSeedsSeq
    del process.InitialStep
    del process.LowPtTripletStep
    del process.PixelPairStep
    del process.DetachedTripletStep
    del process.MixedTripletStep
    del process.PixelLessStep
    del process.TobTecStep
    del process.earlyGeneralTracks
    del process.ConvStep
    # add the correct tracking back in
    process.load("RecoTracker.Configuration.RecoTrackerPhase1PU"+str(nPU)+"_cff")

    process.globalreco.insert(itIndex,process.trackingGlobalReco)
    process.reconstruction.insert(grIndex,process.globalreco)
    #Note process.reconstruction_fromRECO is broken
    
    # End of new tracking configuration which can be removed if new Reconstruction is used.


    process.reconstruction.remove(process.castorreco)
    process.reconstruction.remove(process.CastorTowerReco)
    process.reconstruction.remove(process.ak7BasicJets)
    process.reconstruction.remove(process.ak7CastorJetID)

    #the quadruplet merger configuration     
    process.load("RecoPixelVertexing.PixelTriplets.quadrupletseedmerging_cff")
    process.pixelseedmergerlayers.BPix.TTRHBuilder = cms.string("PixelTTRHBuilderWithoutAngle" )
    process.pixelseedmergerlayers.BPix.HitProducer = cms.string("siPixelRecHits" )
    process.pixelseedmergerlayers.FPix.TTRHBuilder = cms.string("PixelTTRHBuilderWithoutAngle" )
    process.pixelseedmergerlayers.FPix.HitProducer = cms.string("siPixelRecHits" )    
    
    # Need these until pixel templates are used
    process.load("SLHCUpgradeSimulations.Geometry.recoFromSimDigis_cff")
    # PixelCPEGeneric #
    process.PixelCPEGenericESProducer.Upgrade = cms.bool(True)
    process.PixelCPEGenericESProducer.UseErrorsFromTemplates = cms.bool(False)
    process.PixelCPEGenericESProducer.LoadTemplatesFromDB = cms.bool(False)
    process.PixelCPEGenericESProducer.TruncatePixelCharge = cms.bool(False)
    process.PixelCPEGenericESProducer.IrradiationBiasCorrection = False
    process.PixelCPEGenericESProducer.DoCosmics = False
    # CPE for other steps
    process.siPixelRecHits.CPE = cms.string('PixelCPEGeneric')
    # Turn of template use in tracking (iterative steps handled inside their configs)
    process.mergedDuplicateTracks.TTRHBuilder = 'WithTrackAngle'
    process.ctfWithMaterialTracks.TTRHBuilder = 'WithTrackAngle'
    process.muonSeededSeedsInOut.TrackerRecHitBuilder=cms.string('WithTrackAngle')
    process.muonSeededTracksInOut.TTRHBuilder=cms.string('WithTrackAngle')
    process.muonSeededTracksOutIn.TTRHBuilder=cms.string('WithTrackAngle')
    process.muons1stStep.TrackerKinkFinderParameters.TrackerRecHitBuilder=cms.string('WithTrackAngle')
    process.regionalCosmicTracks.TTRHBuilder=cms.string('WithTrackAngle')
    process.cosmicsVetoTracksRaw.TTRHBuilder=cms.string('WithTrackAngle')
    # End of pixel template needed section
    
    # Make pixelTracks use quadruplets
    process.pixelTracks.SeedMergerPSet = cms.PSet(
        layerListName = cms.string('PixelSeedMergerQuadruplets'),
        addRemainingTriplets = cms.bool(False),
        mergeTriplets = cms.bool(True),
        ttrhBuilderLabel = cms.string('PixelTTRHBuilderWithoutAngle')
        )
    process.pixelTracks.FilterPSet.chi2 = cms.double(50.0)
    process.pixelTracks.FilterPSet.tipMax = cms.double(0.05)
    process.pixelTracks.RegionFactoryPSet.RegionPSet.originRadius =  cms.double(0.02)



    return process
