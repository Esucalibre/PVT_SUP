WEBSITE_LIST = {"https://www.lenovo.com":
                {"specifics":"ablock=true;",
                 "main_menu":'refresh_sens:id;guide-icon',
                 "endpoints":
                 { 
                  "PC&Tablets":  'partial link text;PC & TABLETS',
                  "Servers":  'partial link text;SERVERS',
                  "Devices": 'partial link text;SMART DEVICES',
                  "Services&Solutions": 'partial link text;SERVICES & SOLUTIONS',
                  "Our Company": 'partial link text;Our Company',
                  "Contact Us": 'partial link text;Contact Us',
                  "Small Business Solutions":'partial link text;Small Business Solutions'
                 },
                  "sub-endpoints":
                  {
                      
                        "PC&Tablets":{"PC&Tablets dropdown":'rand_ind:class name;second_list_item',
                                      "PC&Tablets Products":'rand_ind:class name;Products',
                                      "PC&Tablets Product Catagory":'rand_ind:class name;product-category-item',
                                      "PC&Tablets E-Spots Catagory":'rand_ind:class name;E-Spots-mask',
                                      },
                        
                        "Servers":{"Server dropdown":'rand_ind:class name;second_list_item',
                                   "Random Server Catagory":'rand_ind:class name;filterText'
                                  },
                        "Devices":{"Random Device Product":'rand_ind:class name;Products',
                                   "Devices E-Spots Catagory":'rand_ind:class name;E-Spots-mask', 
                                   "Smart Devices Banner":'rand_ind:class name;filterText',
                                   },
                        "Services&Solutions":{"Services Products":'rand_ind:class name;Products',
                                              "Services E-Spots Mask":'rand_ind:class name;E-Spots-mask',
                                              "Services Product Catagory":'rand_ind:class name;product-category-item',
                                              },       
                        "Our Company":{"Company Products":'rand_ind:class name;Products',
                                       "Company E-spots Mask": 'rand_ind:class name;E-Spots-mask',
                                       "Company Banner": 'rand_ind:class name;filterText',
                                       
                                
                        },
                        "Contact Us":  {"Contact Sales":'partial link text;Contact Sales',
                                        "Contact Order Support":'partial link text;Contact Order Support',
                                        "Contact Technical Support":'partial link text;Contact Technical Support',
                                        "Order Lookup":'partial link text;Order Lookup',
                                        "Laptop Buying Guide":'partial link text;Laptop Buying Guide]',

                                
                        },       
                        "Small Business Solutions":{"Small Business E-spot Mask":'rand_ind:class name;E-Spots-mask',
                                                    "Small Business Financing":'partial link text;Lenovo Financing',
                                                    "Small Business Lenovo Pro":'class name;lenovoproimgClass',
                                                    "small Business Filtertext":'class name;filterText',
                                                    "small Business Solutions":'rand_ind:class name;resource_oneline',
                                                    
                                
                        },
                      },
                  }
                 }

WEBSITE_LIST = {"https://www.intel.com":
                 {"specifics":"ablock=true;",
                 "main_menu":'refresh_sens:id;guide-icon',
                 "endpoints":
                 { 
                  'Products':'partial link text;Products',
                  'Support':'partial link text;Support',
                  'Gaming':'direct-link;/content/www/us/en/gaming/serious-gaming.html',
                  'Developers':'direct-link;/content/www/us/en/developer/overview.html',
                  'Partners':'direct-link;/content/www/us/en/partner-alliance/overview.html'
                 },
                  "sub-endpoints":
                  {
                        
                        "Products":{"Intel Xeon Scalable Processors":'relies_prev~refresh_sens:partial link text;Intel® Xeon® Scalable Processors',
                                    "Intel Xeon Platinum Processors":'relies_prev~refresh_sens:partial link text;Intel® Xeon® Platinum Processors',
                                    "Intel xeon Platinum Blade Item":'relies_prev:rand_ind:class name;blade-item-heading',

                                    },
                        "Products":{"Intel Xeon Processors":'refresh_sens:partial link text;Intel® Xeon® Processors',
                                    "Intel Xeon Cpu Max Processors":'relies_prev:partial link text;Intel® Xeon® CPU Max Series',
                                    "Intel Xeon Cpu Product Brief":'partial link text;Product brief: Intel® Xeon® CPU Max Series ›',

                                    },
                        "Support":{"Specifications":'partial link text;Specifications',
                                   "Company Overview":'partial link text;Company Overview',
                                   "Our Values":'partial link text;Our Values',

                                   },
                        "Gaming":{"Fix High CPU Usage":'relies_prev:partial link text;How to Fix High CPU Usage',
                                  "Choose Gaming CPU":'relies_prev:partial link text;How to Choose a Gaming CPU',
                                  "Gaming Desktop":'relies_prev:partial link text;gaming desktop',
                                  "Get The Details":'relies_prev:partial link text;Get the details',

                                    },
                        "Developers":{"Programs":'relies-prev:partial link text;Programs',
                                      "Program Catagory":'relies_prev~rand_ind:class name;content-media',
                                
                                    },
                        "Partners":{"Partner Learn More":'relies_prev:partial link text;Learn more',
                                    "Join Intel":'relies_prev:partial link text;Join the Intel® Partner Alliance',
                                    "Terms of Servicec":"relies_prev:partial link text;Terms of Service",
                                
                                    },
                        },
                          
                      },
                  }


WEBSITE_LIST = {"https://www.uber.com":
                 {"specifics":"ablock=true;",
                 "main_menu":'refresh_sens:id;guide-icon',
                 "endpoints":
                 { 
                  "See How":'partial link text;See how',
                  "Help":'partial link text;Help',
                  "Random Endpoint From Home":'rand_ind:css selector;.css-fwsLmT',
                  "Random Endpoint2":'rand_ind:css selector;.css-qNlYD'

                 },
                  "sub-endpoints":
                  {
                      "See How":{"How to Get Started":'relies_prev:partial link text;How to get started',
                                 "Corporate Traveler":'relies_prev:partial link text;Read the article',  
                                 "Get Started":'relies_prev:partial link text;VGet started',   
                                 "Visit Help Center":'Visit Help Center'     
                                  },
                      "Help":{"Random support":'relies_prev~rand_ind:css selector;._dr',
                              "Random Sub Tab":'rand_ind:css selector;._jh',
                              },
                      "Random Endpoint From Home":{"Random Sub endpoint1":'relies_prev~rand_ind:css selector;.css-fwsLmT',
                                                   "Random Sub endpoint2":'relies_prev~rand_ind:css selector;.css-fwsLmT',
                                                  }
                        },
                          
                      },
                  }

WEBSITE_LIST = {"https://www.python.org":
                 {"specifics":"ablock=true;",
                 "main_menu":'refresh_sens:id;guide-icon',
                 "endpoints":
                 { 
                  "Top Bar":'rand_ind:css selector;.top-bar li',
                  "Nav Bar":'rand_ind:id;mainnav',
                  "Sub Nav Bar":'rand_ind:css selector;.sitemap .subnav',
                 },
                  "sub-endpoints":
                  {
                      "Top Bar":{"Random Top Bar Sub-endpoint":'rand_ind~relies_prev:css selector;a:-webkit-any-link',
                                  },
                      "Nav Bar":{"Random Top Bar Sub-endpoint":'rand_ind~relies_prev:css selector;a:-webkit-any-link',
                                  },
                      "Sub Nav Bar":{"link to nav bar":'rand_ind:css selector;.sitemap .subnav',
                                     },
                        },
                          
                      },
                  }

WEBSITE_LIST = {"https://www.askubuntu.com":
                 {"specifics":"ablock=true;",
                 "main_menu":'refresh_sens:id;guide-icon',
                 "endpoints":
                 { 
                  "Home Bar":'rand_ind:css selector;.truncate',
                  "Random Post":'rand_ind:css selector;.s-post-summary .s-post-summary--content-title a',
                  "Random footer link":'rand_ind:css selector;.site-footer .-list'
                 },
                  "sub-endpoints":
                  {
                      "Random Post":{"Home Bar redirect":'rand_ind:css selector;.truncate',
                                     "Ask Question":'relies_prev:partial link text;Ask Question',
                                    },
                      
                    },
                  },
                 },

WEBSITE_LIST = {"https://www.ieee.org":
                 {"specifics":"ablock=true;",
                 "main_menu":'refresh_sens:id;guide-icon',
                 "endpoints":
                 { 
                  "Random Header Bar":'rand_ind:css selector;.site-navigation .main-menu',
                  "Random top nav bar":'id;util-left',
                  "Sign-up Page":'css selector;.site-navigation a.btn-blue',
                  },
                  "sub-endpoints":
                  {
                    "Sign-up Page":{'relies_prev~rand_ind:css selector;.link-list li a',
                                    }
                      
                      },
                    },
                    #awful site
                  },

              
WEBSITE_LIST = {"https://www.cisco.com":
                 {"specifics":"ablock=true;",
                 "main_menu":'refresh_sens:id;guide-icon',
                 "endpoints":
                 { 
                  "Random quick task":'rand_ind:class name;cds-c-quicktasks__item',
                  "Random top bar nav":'rand_ind:css selector;.fw-c-header__tophat .fw-c-header__button',

                 },
                  "sub-endpoints":
                  {
                      "Random top bar nav":{"top bar link":'rand_ind:css selector;.fw-c-header__dropdown a, .fw-c-header__dropdown a:active, .fw-c-header__dropdown a:visited',
                                     
                                     
                                    },
                      
                    },
                  },
                  #awful site
                 },

WEBSITE_LIST = {"https://www.tomshardware.com/":
                 {"specifics":"ablock=true;",
                 "main_menu":'refresh_sens:id;guide-icon',
                 "endpoints":
                 { 
                  "Best Picks":'partial link text;Best Picks',
                  "Raspberry Pi":'partial link text;Raspberry Pi',
                  "CPUs":'partial link text:CPUs',
                  "GPUs":'partial link text:GPUs',
                  "Coupons":'partial link text:Coupons'
                 },
                  "sub-endpoints":
                  {
                      "Best Picks":{"Random Article":'relies_prev:css selector;.listingResult .article-name'
                          
                      },
                      "Raspberry Pi":{"Random Article":'relies_prev:css selector;.listingResult .article-name'
                          
                      },
                      "CPUs":{"Random Article":'relies_prev:css selector;.listingResult .article-name'
                          
                      },
                      "GPUs":{"Random Article":'relies_prev:css selector;.listingResult .article-name'
                          
                      },
                      "Coupons":{"View all":'relies_prec~rand_ind:css selector;.fa, .fa-stack, .fa:after, .fa:before'
                          
                      },

                  },
                  },
                 },

WEBSITE_LIST = {"https://www.eventbrite.ca/?_gl=1*ram3vq*_up*MQ..&gclid=EAIaIQobChMI4bei-Z-T_wIV1i7UAR3CHwphEAAYASAAEgLuA_D_BwE&gclsrc=aw.ds":
                 {"specifics":"ablock=true;",
                 "main_menu":'refresh_sens:id;guide-icon',
                 "endpoints":
                 { 
                  "Random trending":'rand_ind:css selector;.tile',  
                  "Sitemap":'partial link text;Sitemap',
                  "Pricing":'partial link text;Pricing',
                  "Event Payment System":'partial link text;Event Payment System',
                  "Contact Support":'partial link text;Contact Support'

                 },
                  "sub-endpoints":
                  {
                      "Sitemap":{'partial link text;About Us'
                                    },
                      "Sitemap":{'partial link text;Contact Us'
                      },
                      "Sitemap":{'partial link text;Impact'
                          
                      },
                      "Contact Support":{'partial link text;terms of service'
                      },
                       "Contact Support":{'partial link text;privacy policy'
                      },

                      
                    },
                  },
                 },               
    
WEBSITE_LIST = {"https://www.latimes.com/":
                 {"specifics":"ablock=true;",
                 "main_menu":'refresh_sens:id;guide-icon',
                 "endpoints":
                 { 
                  "California":'partial link text;California',
                  "Entertainment":'partial link text;Entertainment',
                  "Sports":'partial link text;Sports',
                  "Food":'partial link text;food',
                  "Climate":'partial link text;Climate',
                  "Image":'partial link text;Image',
                  "Opinion":'partial link text;Opinion',

                 },
                  "sub-endpoints":
                  {
                      "California":{"Random cali article":'relies_prev~rand_ind:css selector;.promo-small .promo-title'
                                    },
                      "Entertainment":{"Random entertainment article":'relies_prev~rand_ind:css selector;.promo-small .promo-title'
                                    },
                      "Sports":{"Random Sports article":'relies_prev~rand_ind:css selector;.promo-small .promo-title'
                                    },
                      "Food":{"Random Food article":'relies_prev~rand_ind:css selector;.promo-small .promo-title'
                                    },
                      "Climate":{"Random climate article":'relies_prev~rand_ind:css selector;.promo-small .promo-title'
                                    },
                      "Image":{"Random Image article":'relies_prev~rand_ind:css selector;.promo-small .promo-title'
                                    },
                      "Opinion":{"Random Opinion article":'relies_prev~rand_ind:css selector;.promo-small .promo-title'
                                    },

                  },
                  },
                 },

WEBSITE_LIST = {"https://www.timeanddate.com/":
                 {"specifics":"ablock=true;",
                 "main_menu":'refresh_sens:id;guide-icon',
                 "endpoints":
                 { 
                  "World Clock":'partial link text;World Clock',
                  "Time Zones":'partial link text;Time Zones',
                  "Calendar":'partiall ink text;Calendar',
                  "Weather":'partial link text;Weather',
                  "Sun & Moon":'partial link text;Sun & Moon'
                 },
                  "sub-endpoints":
                  {
                      "World Clock":{"Daylight Savings":'partial link text;Daylight Saving Time',
                                    "Random Daylight article":'relies_prev~rand_ind:class name;blk-series__item'
                                    },
                      "Time Zones":{"Time Zone Map":'partial link text;Time Zone Map',
                                    "UTC":'partial link text;Coordinated Universal Time (UTC)'
                                    
                                    },
                      "Calendar":{"Gregorian calendar":'partial link text;Gregorian calendar',
                                  "Calendar History":'relies_prev~rand_ind:class name;blk-series__item'
                                    
                                    },
                      "Weather":{"Weather Terms":'relies_prev:partial link text;Weather words and terminology',
                                 "Jumplist":'relies_prev~rand_ind:css selector;.jumplist'
                          
                                    },
                      "Sun & Moon":{"Sky Tonight":'partial link text;The Sky Tonight',
                                   },
                       "Sun & Moon":{"planets and stuff":'partial link text;Planets: Distance, Size & Brightness',
                                     "Planets":'relies_prev~rand_ind:class name;planet-links'
                                    },
                    },
                  },
                 },     

                 
    
                 
                
