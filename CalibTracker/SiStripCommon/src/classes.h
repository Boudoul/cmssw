#include <vector>
#include "DataFormats/Common/interface/Wrapper.h"

namespace {
  struct dictionary {
    std::vector<std::vector<float> > vvf;    
    edm::Wrapper<std::vector<std::vector<float> > >wvvf;    
    std::vector<std::vector<char> > vvc;   
    edm::Wrapper<std::vector<std::vector<char> > > wvvc;
  };  
}
