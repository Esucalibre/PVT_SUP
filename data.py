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
                  'Products'
                  'Support'
                  'Solutions'
                  'Developers'
                  'Partners'
                 },
                  "sub-endpoints":
                  {
                      "main_menu":{"trending":'relies_prev:partial link text;Trending',
                                   "music":   'relies_prev:partial link text;Music',
                                   "gaming":  'relies_prev:partial link text;Gaming',
                                   "news":    'relies_prev:partial link text;News',
                                   "sports":  'relies_prev:partial link text;Sports',
                                   "learning":'relies_prev:partial link text;Learning'
                                   },
                      "trending":{"video":'rand_ind:css selector;ytd-video-renderer'
                                  },
                      "music":{"video":'rand_ind:css selector;ytd-video-renderer'
                               },
                      "gaming":{"video":"rand_ind:css selector;ytd-video-renderer"
                          
                      },
                  }
                 }
                }
