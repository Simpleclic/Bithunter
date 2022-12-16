import id_user

########## API ##########
API_KEY=id_user.API_KEY
API_SECRET=id_user.API_SECRET

testnet = True 

###localisation ###
directory = 'C:/Hub-Hunter/Bithunter_client_dev/'  #exemple: 'C:/Hub-Hunter/Bithunter_client/' 

###### POSITION #######
size_position = '0.5'  ## position amount (% of wallet)
limite_position = '5' ### Limit of a position (% of wallet)
max_open ='8' ### Number of simultaneous positions allowed

##### DCA #####
DCA = "25"		#### % ROI before buyout
DCA_ONE = "50"   #### Negative % ROI for triggering - Tier 1 
DCA_TWO = '75'	#### Negative % ROI for triggering - Tier 2 
multiplier_ONE = '2' ### size_positon multiplication amount - Step 1
multiplier_TWO = '4' ### size_positon multiplication amount - Step 2

#### Take Profit ####
open_size_ONE = '35' #### Percentage of the maximum allocation of a position before going to takeprofit_one
open_size_TWO = '70' #### Percentage of maximum allocation of a position before moving to takeprofit_two

takeprofit = '10'
takeprofit_ONE = '7' #### Whole number in % compared to the purchase price, attention too low amount ex=1% can not pass if the price of the coin is too low
takeprofit_TWO = '5' #### Whole number in % compared to the purchase price, attention too low amount ex=1% can not pass if the price of the coin is too low

contre_tendance = True ## resale in case of counter-trend
safe_sell = '1' ### Minimum ROI before resale

###### Levier ######### 
leverage = '3'

##### WALLET ##########
wallet_engage = '70' #### % Percentage of the wallet that will not be committed

####### Liste #####
liste = ['ADAUSD','AVAXUSD','AXSUSD','BCHUSD','BNBUSD','DOGEUSD','DOTUSD','EOSUSD','ETHUSD','GMTUSD','LINKUSD','LTCUSD','SOLUSD','XRPUSD','XBTUSD']

##### Indicateur ###
timeframe = "1h"
timeframe2 = "1d"
double_timeframe = True


##### liq auto ###
liq_auto = True ## defined if you use our algorithm to update the liquidation in real time

######### LICK SYMBOLE ####
##### Perpetual ###########
ADAUSD_LIQ = '1'
APEUSD_LIQ = '3'
AVAXUSD_LIQ = '5'
AXSUSD_LIQ = '7'
BCHUSD_LIQ = '9'
BNBUSD_LIQ = '11'
DOGEUSD_LIQ = '13'
DOTUSD_LIQ = '15'
EOSUSD_LIQ = '17'
ETHUSD_LIQ = '19'
GMTUSD_LIQ = '21'
LINKUSD_LIQ = '23'
LTCUSD_LIQ = '25'
SOLUSD_LIQ = '27'
XRPUSD_LIQ = '29'
XBTUSD_LIQ = '31'

#### rebuy ###
ADAUSD_REBUY_LIQ = '2'
APEUSD_REBUY_LIQ = '4'
AVAXUSD_REBUY_LIQ = '6'
AXSUSD_REBUY_LIQ = '8'
BCHUSD_REBUY_LIQ = '10'
BNBUSD_REBUY_LIQ = '12'
DOGEUSD_REBUY_LIQ = '14'
DOTUSD_REBUY_LIQ = '16'
EOSUSD_REBUY_LIQ = '18'
ETHUSD_REBUY_LIQ = '20'
GMTUSD_REBUY_LIQ = '22'
LINKUSD_REBUY_LIQ = '24'
LTCUSD_REBUY_LIQ = '26'
SOLUSD_REBUY_LIQ = '28'
XRPUSD_REBUY_LIQ = '30'
XBTUSD_REBUY_LIQ = '32'

bitapi = 'externe'