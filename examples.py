from pprint import pprint
import sys
 
 import market_proto
 from androidmarket import MarketSession
if __name__ == "__main__":
     session.login("user@gmail.com", "password")
     
     # Search for "bankdroid" on the market and print the first result
     results = session.getApps()
     pprint(results)
    
     categories = session.getCategories()
     pprint(categories)
    
     sys.exit()
    
     results = session.searchApp("bankdroid")
     if len(results) == 0:
         print "No results found"