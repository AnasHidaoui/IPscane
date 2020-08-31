

class Ipinfo:
    '''
    Ipinfo class created by A.Hidaoui
    You can use this class for find usful imphormation about an Ip address
    '''
    def __init__(self) :
        self.welcome()
        self.client()
    
    def welcome(self) :
        if getos().lower()[0] is not "w" :
            system("clear")

        else:
            system("cls")
        wel = '''
                +$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$+
                [[--------------Ipinfo v0.1---------------]]
                |    By: ANAS HIDAOUI   August 30 20202    |
                |     E-mail:anas12hid@gmail.com           |
                +------------------------------------------+
                |        www.github.com/AnasHidaoui        |
                +$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$+
        '''
        self.thanks = '''
                          +$$$$$$$$$$$$$$$$$$$$$$$$$$$$+
                          [[THANK YOU FOR USING IPINFO]]
                          +$$$$$$$$$$$$$$$$$$$$$$$$$$$$+
        '''
        print(cs(wel,"purple4").bold())
    


    def client(self) :
        print(cs('\t\t\t    [1] Get your IP adress','#C0FFF2').bold())
        print(cs('\t\t\t    [2] Scane an IP adress','#C0FFF2').bold())
        print(cs('\t\t\t    [3] Quit','#C0FFF2').bold())
        while True :
            option = input(cs('\n[Ipinfo$] Please chose 1,2 or 3 :','#C0FFF2'))
            try :
                self.option = int(option)
                assert self.option in [1,2,3]
            except AssertionError :
                print(cs('Invalid chose !!! try again','#ff0009').bold())
            except Exception as e :
                print(cs(e,'#ff0009').bold())
            else :
                self.option_manager(self.option)
                break
    
    def getip(self) :
        try :
            http = PoolManager()
            res  = http.request('GET','https://api.ipify.org?format=json')
        except Exception as e :
            print(cs(e,'#ff0009').bold())
        else :
            ############################################################
            # print the ip
            ############################################################
            data = json.loads(res.data.decode('utf-8'))
            result = 'Your IP address is:'+str(data['ip'])
            print(cs(result,'#FFFF00'))
            print('\n')
            self.client()
            

    def scane(self) :
        #######################################################################
        # GET THE IP FROM THE USER END SCAN IT
        #######################################################################
        ip   = input(cs('Pleaes entry the IP address: ','#C0FFF2')) 
        url  = f'https://geo.ipify.org/api/v1?apiKey=at_6RS1rrwLJeTv6UsxTCHp9lyevObwF&ipAddress={ip}'
        print(cs("Please wait....","#40ff00").bold())
        try :
            http = PoolManager()
            res  = http.request('GET',url)
        except Exception as e :
            print(cs(e,'#ff0009').bold())
        else :
            data = json.loads(res.data.decode('utf-8'))
            ###################################################################################
            # HUNDEL THE DATA 
            ####################################################################################
            try :
                location   = data['location']
                proxy      = data['proxy']
                ip_        = '\t[IP]       : ' + str(ip)
                country    = '\t[COUNTRY]  : ' + str(location['country'])
                region     = '\t[REGION]   : ' + str(location['region'])
                city       = '\t[CITY]     : ' + str(location['city'])
                latitude   = '\t[LATITUDE] : ' + str(location['lat'])
                longitude  = '\t[LONGITUDE]: ' + str(location['lng'])
                postalCode = '\t[POSTALECODE]: ' + str(location['postalCode'])
                timezone   = '\t[TIMEZONE] : ' + str(location['timezone'])
                geonameId  = '\t[GEONAME]  : ' + str(location['geonameId'])
                domains    = '\t[DOMAINS]  : ' + str(data['domains'])
                roote      = '\t[ROUTE]    : ' + str(data['as']['route'])
                asn        = '\t[ASN]      : ' + str(data['as']['asn'])
                as_name    = '\t[ASN_NAME] : ' + str(data['as']['name'])
                domain     = '\t[OMAIN]    : ' + str(data['as']['domain'])
                type_      = '\t[TYPE]     : ' + str(data['as']['type'])
                isp        = '\t[ISP]      : ' + str(data['isp'])
                proxy_     = '\t[PROXY]    : ' + str(proxy['proxy'])
                vpn        = '\t[VPN]      : ' + str(proxy['vpn'])
                tor        = '\t[TOR]      : ' + str(proxy['tor'])
            except Exception :
                import sys
                print(cs('Oops!something went wrong.Tckeck yur connection ,the IP address and try again','#ff0009').bold())
                sys.exit()
            else :

                ###########################################################################
                # PRINT THE DATAT FOR THE USER
                ############################################################################
                print(cs(ip_,'#FFFF00').bold())
                print(cs(country,'#FFFF00').bold())
                print(cs(region,'#FFFF00').bold())
                print(cs(city,'#FFFF00').bold())
                print(cs(latitude,'#FFFF00').bold())
                print(cs(longitude,'#FFFF00').bold())
                print(cs(postalCode,'#FFFF00').bold())
                print(cs(timezone,'#FFFF00').bold())
                print(cs(geonameId,'#FFFF00').bold())
                print(cs(domains,'#FFFF00').bold())
                print(cs(roote,'#FFFF00').bold())
                print(cs(asn,'#FFFF00').bold())
                print(cs(as_name,'#FFFF00').bold())
                print(cs(domain,'#FFFF00').bold())
                print(cs(type_,'#FFFF00').bold())
                print(cs(isp,'#FFFF00').bold())
                print(cs(vpn,'#FFFF00').bold())
                print(cs(tor,'#FFFF00').bold())

                ###########################################################
                # QUIT THE PROGRAMME
                ############################################################
                print(cs(self.thanks,"purple4").bold())
                import sys
                sys.exit()


    def option_manager(self,opt) :
        #################################################################
        # MANAGER THE OPTIONS AND RUN THE VALID FUNCTION
        ##################################################################
        if opt == 1 :
            print(cs("Please wait....","#40ff00").bold())
            self.getip()
            
        elif opt == 2 :
            self.scane()

        elif opt == 3 :
            print(cs(self.thanks,"purple4").bold())
            import sys
            sys.exit()
# Run the Programme
if __name__ == '__main__' :

    ########################################################
    # IMPORT THE MODULES 
    #########################################################
    from urllib3 import PoolManager
    import json
    from stringcolor import *
    from os import system
    from sys import exit
    from platform import system as getos

    #########################################################
    # MAKE AN IPinfo OBJECT
    ###########################################################

    ip_info_obj = Ipinfo()  
