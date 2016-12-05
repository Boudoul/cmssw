import FWCore.ParameterSet.Config as cms

from DQM.Phase2OuterTracker.OuterTrackerMonitorL1Cluster_cfi import *
from DQM.Phase2OuterTracker.OuterTrackerMonitorStub_cfi import *
#from DQM.Phase2OuterTracker.OuterTrackerMonitorTrack_cfi import *

OuterTrackerSource = cms.Sequence(OuterTrackerMonitorL1Cluster
				  * OuterTrackerMonitorStub
#				  * OuterTrackerMonitorTrack
          )

#from Configuration.Eras.Modifier_phase2_tracker_cff import phase2_tracker
#phase2_tracker.toReplaceWith(OuterTrackerSource)
#phase2_tracker.toModify(OuterTrackerSource)
