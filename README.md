# netCscan-C-
C段80端口扫描工具。

如何使用？

            _    _____                                                                                                                                                              
           | |  / ____|                                                                                                                                                             
 _ __   ___| |_| |     ___  ___ __ _ _ __                                                                                                                                           
| '_ \ / _ \ __| |    / __|/ __/ _` | '_ \                                                                                                                                          
| | | |  __/ |_| |____\__ \ (_| (_| | | | |                                                                                                                                         
|_| |_|\___|\__|\_____|___/\___\__,_|_| |_|     netCscan_Version 1.1.1                                                                                                              
                                                                                                                                                                                    
                                                                                                                                                                                    
Usage: sscan.py [options]

Options:
  -h, --help            show this help message and exit
  -u FILE, --url=FILE   Target URL (e.g. http://www.demo.com/)
  -c FILE, --cpart=FILE
                        Please enter an IP paragraph (e.g. 127.0.0)

URL:
python3 netCscan.py -u https://www.demo.com/

IP:
python3 netCscan.py -c 127.0.0.1

