// -*- C++ -*-
//
// Package:    Phase2OuterTracker
// Class:      Phase2OuterTracker
// 
/**\class Phase2OuterTracker OuterTrackerMonitorL1ClusterClient.cc DQM/Phase2OuterTracker/plugins/OuterTrackerMonitorL1ClusterClient.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Isabelle Helena J De Bruyn
//         Created:  Mon, 10 Feb 2014 13:57:08 GMT
// 

// system include files
#include <memory>
#include <vector>
#include <numeric>
#include <fstream>
#include <math.h>
#include "TNamed.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

#include "DataFormats/Common/interface/DetSetVector.h"
#include "DataFormats/Common/interface/DetSetVectorNew.h"
#include "DQM/SiStripCommon/interface/SiStripFolderOrganizer.h"
#include "DQM/Phase2OuterTracker/interface/OuterTrackerMonitorL1ClusterClient.h"
#include "DQMServices/Core/interface/DQMStore.h"
#include "DQMServices/Core/interface/MonitorElement.h"

#include "CommonTools/TriggerUtils/interface/GenericTriggerEventFlag.h"

#include "TMath.h"
#include <iostream>

//
// constructors and destructor
//
OuterTrackerMonitorL1ClusterClient::OuterTrackerMonitorL1ClusterClient(const edm::ParameterSet& iConfig)
{
 
}


OuterTrackerMonitorL1ClusterClient::~OuterTrackerMonitorL1ClusterClient()
{
 

}


//
// member functions
//

// ------------ method called for each event  ------------
void
OuterTrackerMonitorL1ClusterClient::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  
}


// ------------ method called once each job just before starting event loop  ------------
void 
OuterTrackerMonitorL1ClusterClient::beginRun(const edm::Run& run, const edm::EventSetup& es)
{


}//end of method


// ------------ method called once each job just after ending the event loop  ------------
void 
OuterTrackerMonitorL1ClusterClient::endJob(void) 
{

}

DEFINE_FWK_MODULE(OuterTrackerMonitorL1ClusterClient);
