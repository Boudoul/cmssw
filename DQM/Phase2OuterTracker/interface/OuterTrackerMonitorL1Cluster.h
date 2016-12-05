#ifndef Phase2OuterTracker_OuterTrackerMonitorL1Cluster_h
#define Phase2OuterTracker_OuterTrackerMonitorL1Cluster_h

#include <vector>
#include <memory>
#include "FWCore/Utilities/interface/EDGetToken.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "DQMServices/Core/interface/MonitorElement.h"
#include "DQMServices/Core/interface/DQMStore.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "DQM/SiStripCommon/interface/TkHistoMap.h"
#include "DataFormats/Common/interface/DetSetVector.h"
#include "DataFormats/Common/interface/DetSetVectorNew.h"
#include "DataFormats/L1TrackTrigger/interface/TTTypes.h"


class DQMStore;

class OuterTrackerMonitorL1Cluster : public edm::EDAnalyzer {

public:
  explicit OuterTrackerMonitorL1Cluster(const edm::ParameterSet&);
  ~OuterTrackerMonitorL1Cluster();
  virtual void analyze(const edm::Event&, const edm::EventSetup&);
  virtual void endJob() ;
  virtual void beginRun(const edm::Run&, const edm::EventSetup&);
 
  // TTCluster stacks
  MonitorElement* Cluster_IMem_Barrel = 0;
  MonitorElement* Cluster_IMem_Endcap_Disc = 0;
  MonitorElement* Cluster_IMem_Endcap_Ring = 0;
  MonitorElement* Cluster_IMem_Endcap_Ring_Fw[5] = {0, 0, 0, 0, 0};
  MonitorElement* Cluster_IMem_Endcap_Ring_Bw[5] = {0, 0, 0, 0, 0};
  MonitorElement* Cluster_OMem_Barrel = 0;
  MonitorElement* Cluster_OMem_Endcap_Disc = 0;
  MonitorElement* Cluster_OMem_Endcap_Ring = 0;
  MonitorElement* Cluster_OMem_Endcap_Ring_Fw[5] = {0, 0, 0, 0, 0};
  MonitorElement* Cluster_OMem_Endcap_Ring_Bw[5] = {0, 0, 0, 0, 0};
  MonitorElement* Cluster_W = 0;
  MonitorElement* Cluster_Eta = 0;
  
  MonitorElement* Cluster_Barrel_XY = 0;
  MonitorElement* Cluster_Barrel_XY_Zoom = 0;
  MonitorElement* Cluster_Endcap_Fw_XY = 0;
  MonitorElement* Cluster_Endcap_Bw_XY = 0;
  MonitorElement* Cluster_RZ = 0;
  MonitorElement* Cluster_Endcap_Fw_RZ_Zoom = 0;
  MonitorElement* Cluster_Endcap_Bw_RZ_Zoom = 0;

 private:
  DQMStore* dqmStore_;
  edm::ParameterSet conf_;
  edm::EDGetTokenT<edmNew::DetSetVector< TTCluster< Ref_Phase2TrackerDigi_ > > >  tagTTClustersToken_;

  std::string topFolderName_;
};
#endif
