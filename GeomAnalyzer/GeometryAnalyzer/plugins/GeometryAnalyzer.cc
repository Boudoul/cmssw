// -*- C++ -*-
//
// Package:    GeomAnalyzer/GeometryAnalyzer
// Class:      GeometryAnalyzer
// 
/**\class GeometryAnalyzer GeometryAnalyzer.cc GeomAnalyzer/GeometryAnalyzer/plugins/GeometryAnalyzer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Gaelle Boudoul
//         Created:  Thu, 03 Aug 2017 15:07:22 GMT
//
//


// system include files
#include <memory>
#include <iostream>
// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/SiPixelDetId/interface/PixelSubdetector.h"
#include "DataFormats/SiStripDetId/interface/StripSubdetector.h"
#include "FWCore/Framework/interface/ESHandle.h" 
#include "Geometry/TrackerGeometryBuilder/interface/TrackerGeometry.h" 
#include "Geometry/Records/interface/TrackerDigiGeometryRecord.h"

#include "DataFormats/TrackerCommon/interface/TrackerTopology.h"
#include "Geometry/Records/interface/TrackerTopologyRcd.h"
//
// class declaration
//

// If the analyzer does not use TFileService, please remove
// the template argument to the base class so the class inherits
// from  edm::one::EDAnalyzer<> and also remove the line from
// constructor "usesResource("TFileService");"
// This will improve performance in multithreaded jobs.

class GeometryAnalyzer : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
   public:
      explicit GeometryAnalyzer(const edm::ParameterSet&);
      ~GeometryAnalyzer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;

      // ----------member data ---------------------------
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
GeometryAnalyzer::GeometryAnalyzer(const edm::ParameterSet& iConfig)

{
   //now do what ever initialization is needed
   usesResource("TFileService");

}


GeometryAnalyzer::~GeometryAnalyzer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
GeometryAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

std::cout << "GeometryAnalyzer::analyze() - Run : " << iEvent.run() << "/ Event : " <<iEvent.id().event() << std::endl; 
  //Retrieve tracker topology from geometry
  edm::ESHandle<TrackerTopology> tTopoHandle;
  iSetup.get<TrackerTopologyRcd>().get(tTopoHandle);
  const TrackerTopology* const tTopo = tTopoHandle.product();

  typedef std::vector<DetId> DetIdContainer;

  edm::ESHandle<TrackerGeometry> geo;
  iSetup.get<TrackerDigiGeometryRecord>().get(geo);
std::string DetIdPrint;
DetIdContainer allIds=geo->detIds();


for( DetIdContainer::const_iterator id = allIds.begin(), detUnitIdEnd = allIds.end(); id != detUnitIdEnd; ++id ) {
  if ( id->det()==DetId::Tracker ) {
	unsigned int subdet=id->subdetId();

      if (subdet == PixelSubdetector::PixelBarrel) {
	DetIdPrint = tTopo->print(*id);
	std::cout << DetIdPrint << std::endl;
	std::cout <<" Layer " <<  tTopo->pxbLayer(*id) <<std::endl;
	std::cout <<" Module " <<  tTopo->pxbModule(*id) <<std::endl;
	std::cout <<" Ladder " <<  tTopo->pxbLadder(*id) <<std::endl;
      }
      else if (subdet == PixelSubdetector::PixelEndcap) {
	DetIdPrint = tTopo->print(*id);
	std::cout << DetIdPrint << std::endl;
	std::cout <<" Disk " <<  tTopo->pxfDisk(*id) <<std::endl;
	std::cout <<" Module " <<  tTopo->pxfModule(*id) <<std::endl;
	std::cout <<" Side " <<  tTopo->pxfSide(*id) <<std::endl;
	std::cout <<" Blade " <<  tTopo->pxfBlade(*id) <<std::endl;
	std::cout <<" Panel " <<  tTopo->pxfPanel(*id) <<std::endl;
      }
      else if (subdet == StripSubdetector::TIB) {
	DetIdPrint = tTopo->print(*id);
	std::cout << DetIdPrint << std::endl;
	std::cout <<" Layer " <<  tTopo->tibLayer(*id) <<std::endl;
	std::cout <<" Module " <<  tTopo->tibModule(*id) <<std::endl;
	std::cout <<" Side " <<  tTopo->tibSide(*id) <<std::endl;
	std::cout <<" Order " <<  tTopo->tibOrder(*id) <<std::endl;
	std::cout <<" DoubleSide " <<  tTopo->tibIsDoubleSide(*id) <<std::endl;
	std::cout <<" isRphi " <<  tTopo->tibIsRPhi(*id) <<std::endl;
	std::cout <<" IsStereo " <<  tTopo->tibIsStereo(*id) <<std::endl;
	std::cout <<" IsZPlusSide " <<  tTopo->tibIsZPlusSide(*id) <<std::endl;
	std::cout <<" IsZMinusSide " <<  tTopo->tibIsZMinusSide(*id) <<std::endl;
	std::cout <<" String " <<  tTopo->tibString(*id) <<std::endl;
	std::cout <<" 12 " <<  tTopo->tibIsInternalString(*id) <<std::endl;
	std::cout <<" 13 " <<  tTopo->tibIsExternalString(*id) <<std::endl;

      }
      else if (subdet == StripSubdetector::TID) {
	DetIdPrint = tTopo->print(*id);
	std::cout << DetIdPrint << std::endl;
	std::cout <<" Wheel " <<  tTopo->tidWheel(*id) <<std::endl;
	std::cout <<" Module " <<  tTopo->tidModule(*id) <<std::endl;
	std::cout <<" Side " <<  tTopo->tidSide(*id) <<std::endl;
	std::cout <<" Order " <<  tTopo->tidOrder(*id) <<std::endl;
	std::cout <<" Ring " <<  tTopo->tidRing(*id) <<std::endl;
	std::cout <<" IsDoubleSide " <<  tTopo->tidIsDoubleSide(*id) <<std::endl;
	std::cout <<" IsRPhi " <<  tTopo->tidIsRPhi(*id) <<std::endl;
	std::cout <<" IsStereo " <<  tTopo->tidIsStereo(*id) <<std::endl;
	std::cout <<" IsZPlusSide " <<  tTopo->tidIsZPlusSide(*id) <<std::endl;
	std::cout <<" IsZMinusSide " <<  tTopo->tidIsZMinusSide(*id) <<std::endl;
	std::cout <<" IsBackRing " <<  tTopo->tidIsBackRing(*id) <<std::endl;
	std::cout <<" IsFrontRing " <<  tTopo->tidIsFrontRing(*id) <<std::endl;
      }
      else if (subdet == StripSubdetector::TOB) {
	DetIdPrint = tTopo->print(*id);
	std::cout << DetIdPrint << std::endl;
	std::cout <<" Layer " <<  tTopo->tobLayer(*id) <<std::endl;
	std::cout <<" Module " <<  tTopo->tobModule(*id) <<std::endl;
	std::cout <<" Side " <<  tTopo->tobSide(*id) <<std::endl;
	std::cout <<" Rod " <<  tTopo->tobRod(*id) <<std::endl;
	std::cout <<" IsDoubleSide " <<  tTopo->tobIsDoubleSide(*id) <<std::endl;
	std::cout <<" isRphi " <<  tTopo->tobIsRPhi(*id) <<std::endl;
	std::cout <<" IsStereo " <<  tTopo->tobIsStereo(*id) <<std::endl;
	std::cout <<" IsZplusSide " <<  tTopo->tobIsZPlusSide(*id) <<std::endl;
	std::cout <<" IsZMinusSide " <<  tTopo->tobIsZMinusSide(*id) <<std::endl;
	}
	      else if (subdet == StripSubdetector::TEC) {
	DetIdPrint = tTopo->print(*id);
	std::cout << DetIdPrint << std::endl;
	std::cout <<" Wheel " <<  tTopo->tecWheel(*id) <<std::endl;
	std::cout <<" Module " <<  tTopo->tecModule(*id) <<std::endl;
	std::cout <<" Side " <<  tTopo->tecSide(*id) <<std::endl;
	std::cout <<" Order " <<  tTopo->tecOrder(*id) <<std::endl;
	std::cout <<" Ring " <<  tTopo->tecRing(*id) <<std::endl;
	std::cout <<" PetalNumber " <<  tTopo->tecPetalNumber(*id) <<std::endl;
	std::cout <<" IsDoubleSide " <<  tTopo->tecIsDoubleSide(*id) <<std::endl;
	std::cout <<" IsRPhi " <<  tTopo->tecIsRPhi(*id) <<std::endl;
	std::cout <<" IsStereo " <<  tTopo->tecIsStereo(*id) <<std::endl;
	std::cout <<" IsBackPetal " <<  tTopo->tecIsBackPetal(*id) <<std::endl;
	std::cout <<" IsFrontPetal " <<  tTopo->tecIsFrontPetal(*id) <<std::endl;
	}
   }//end if Tracker
  }//loop detids 
  
   

#ifdef THIS_IS_AN_EVENT_EXAMPLE
   Handle<ExampleData> pIn;
   iEvent.getByLabel("example",pIn);
#endif
   
#ifdef THIS_IS_AN_EVENTSETUP_EXAMPLE
   ESHandle<SetupData> pSetup;
   iSetup.get<SetupRecord>().get(pSetup);
#endif
}


// ------------ method called once each job just before starting event loop  ------------
void 
GeometryAnalyzer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
GeometryAnalyzer::endJob() 
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
GeometryAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(GeometryAnalyzer);
