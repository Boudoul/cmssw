
#
import FWCore.ParameterSet.Config as cms

process = cms.Process("simTest")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.MessageLogger = cms.Service("MessageLogger",
    debugModules = cms.untracked.vstring('PixelSimHitsTest'),
    destinations = cms.untracked.vstring('cout'),
#    destinations = cms.untracked.vstring("log","cout"),
    cout = cms.untracked.PSet(
        threshold = cms.untracked.string('ERROR')
    )
#    log = cms.untracked.PSet(
#        threshold = cms.untracked.string('DEBUG')
#    )
)

process.source = cms.Source("PoolSource",
    fileNames =  cms.untracked.vstring(
#    '/store/user/kotlinski/mu100/simhits/simHits.root',
#    'file:simHits.root'
    '/store/relval/CMSSW_9_0_0_pre4/RelValTTbar_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PU25ns_90X_mcRun2_asymptotic_v1_resub-v1/10000/00E374A6-B8EC-E611-BE24-0025905B85AA.root'
    )
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string('sim_histos.root')
)

process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')

# needed for global transformation
# process.load("Configuration.StandardSequences.FakeConditions_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")# Choose the global tag here:
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')
# ideal
#process.GlobalTag.globaltag = 'MC_70_V1::All'
# realistiv alignment and calibrations 
#process.GlobalTag.globaltag = 'START70_V1::All'

process.analysis =  cms.EDAnalyzer("PixelSimHitsTest",
	src = cms.string("g4SimHits"),
#	list = cms.string("TrackerHitsPixelBarrelLowTof"),
#	list = cms.string("TrackerHitsPixelBarrelHighTof"),
	list = cms.string("TrackerHitsPixelEndcapLowTof"),
#	list = cms.string("TrackerHitsPixelEndcapHighTof"),
        TECsimhitsXFTag = cms.InputTag("mix","g4SimHitsTrackerHitsTECLowTof"),
        Verbosity = cms.untracked.bool(False),
#        mode = cms.untracked.string("bpix"),
        mode = cms.untracked.string("fpix"),
)

process.p = cms.Path(process.analysis)

