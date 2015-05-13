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
    cms.PSet(Dead_detID = cms.int32(352588804), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352592900), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352596996), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352601092), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352605188), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352609284), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352613380), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352617476), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352621572), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352625668), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352629764), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352633860), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352637956), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352642052), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352646148), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352650244), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352654340), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352658436), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352662532), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352666628), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352670724), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352674820), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352678916), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352683012), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352687108), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352691204), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352695300), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352699396), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352703492), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352707588), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352711684), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352715780), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352719876), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352723972), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352728068), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352732164), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352736260), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352740356), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352744452), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352748548), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352752644), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352756740), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352760836), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352764932), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352769028), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352773124), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352777220), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352781316), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352785412), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352789508), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352793604), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352797700), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352801796), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352805892), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352809988), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352814084), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352589828), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352593924), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352598020), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352602116), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352606212), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352610308), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352614404), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352618500), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352622596), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352626692), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352630788), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352634884), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352638980), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352643076), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352647172), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352651268), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352655364), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352659460), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352663556), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352667652), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352671748), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352675844), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352679940), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352684036), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352688132), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352692228), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352696324), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352700420), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352704516), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352708612), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352712708), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352716804), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352720900), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352724996), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352729092), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352733188), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352737284), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352741380), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352745476), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352749572), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352753668), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352757764), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352761860), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352765956), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352770052), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352774148), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352778244), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352782340), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352786436), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352790532), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352794628), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352798724), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352802820), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352806916), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352811012), Module = cms.string('whole')),
    cms.PSet(Dead_detID = cms.int32(352815108), Module = cms.string('whole'))
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
