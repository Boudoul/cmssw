import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
                    fileNames = cms.untracked.vstring(
        "/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/E0845AB9-9513-E111-A07A-BCAEC518FF63.root"
#"/store/hidata/HIRun2011/HIMinBiasUPC/RAW/v1/000/182/124/0011F55A-8F13-E111-A987-003048F118C6.root"
#        "/store/data/Commissioning2014/Cosmics/RAW//v3/000/224/380/00000/E05943D1-1227-E411-BB8E-02163E00F0C4.root"
#    "/store/data/Commissioning2014/Cosmics/RAW/v3/000/224/380/00000/68FDADE5-1227-E411-8AA6-02163E00A10C.root"
        )
)
maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
#    input = cms.untracked.int32(1000)
)

# Parameters for runType
import FWCore.ParameterSet.VarParsing as VarParsing
import sys
from dqmPythonTypes import *

options = VarParsing.VarParsing('analysis')

options.register ('runkey',
          'cosmic_run',
          VarParsing.VarParsing.multiplicity.singleton,
          VarParsing.VarParsing.varType.string,
          "Run Keys of CMS")

options.parseArguments()

# Fix to allow scram to compile
#if len(sys.argv) > 1:
#  options.parseArguments()

runType = RunType()
#if not options.runkey.strip():
options.runkey = 'hi_run'

runType.setRunType(options.runkey.strip())
