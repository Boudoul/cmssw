import FWCore.ParameterSet.Config as cms

from DQM.Phase2OuterTracker.OuterTrackerMonitorL1ClusterClient_cfi import *
from DQM.Phase2OuterTracker.OuterTrackerMonitorStubClient_cfi import *
#from DQM.Phase2OuterTracker.OuterTrackerMonitorL1TrackClient_cfi import *

OuterTrackerClient = cms.Sequence(OuterTrackerMonitorL1ClusterClient
				  * OuterTrackerMonitorStubClient
#				  * OuterTrackerMonitorL1TrackClient
          )

