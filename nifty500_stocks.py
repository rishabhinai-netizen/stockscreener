"""
NIFTY 500 STOCKS DATABASE - COMPLETE EDITION
=============================================
All 500 stocks from NSE Nifty 500 Index with Yahoo Finance ticker symbols.
Organized by sector for easy filtering.

Last Updated: December 2024
Total Stocks: 500
"""

# Complete Nifty 500 stocks with Yahoo Finance format (.NS suffix)
NIFTY_500_STOCKS = {
    # ═══════════════════════════════════════════════════════════════════
    # NIFTY 50 - Large Cap Blue Chips (50 stocks)
    # ═══════════════════════════════════════════════════════════════════
    "NIFTY 50": [
        {"symbol": "RELIANCE.NS", "name": "Reliance Industries", "sector": "Oil & Gas", "mcap": "Large"},
        {"symbol": "TCS.NS", "name": "Tata Consultancy Services", "sector": "IT", "mcap": "Large"},
        {"symbol": "HDFCBANK.NS", "name": "HDFC Bank", "sector": "Banking", "mcap": "Large"},
        {"symbol": "ICICIBANK.NS", "name": "ICICI Bank", "sector": "Banking", "mcap": "Large"},
        {"symbol": "BHARTIARTL.NS", "name": "Bharti Airtel", "sector": "Telecom", "mcap": "Large"},
        {"symbol": "INFY.NS", "name": "Infosys", "sector": "IT", "mcap": "Large"},
        {"symbol": "SBIN.NS", "name": "State Bank of India", "sector": "Banking", "mcap": "Large"},
        {"symbol": "ITC.NS", "name": "ITC Limited", "sector": "FMCG", "mcap": "Large"},
        {"symbol": "HINDUNILVR.NS", "name": "Hindustan Unilever", "sector": "FMCG", "mcap": "Large"},
        {"symbol": "LT.NS", "name": "Larsen & Toubro", "sector": "Infrastructure", "mcap": "Large"},
        {"symbol": "KOTAKBANK.NS", "name": "Kotak Mahindra Bank", "sector": "Banking", "mcap": "Large"},
        {"symbol": "HCLTECH.NS", "name": "HCL Technologies", "sector": "IT", "mcap": "Large"},
        {"symbol": "AXISBANK.NS", "name": "Axis Bank", "sector": "Banking", "mcap": "Large"},
        {"symbol": "BAJFINANCE.NS", "name": "Bajaj Finance", "sector": "NBFC", "mcap": "Large"},
        {"symbol": "ASIANPAINT.NS", "name": "Asian Paints", "sector": "Paints", "mcap": "Large"},
        {"symbol": "MARUTI.NS", "name": "Maruti Suzuki", "sector": "Auto", "mcap": "Large"},
        {"symbol": "TITAN.NS", "name": "Titan Company", "sector": "Consumer Durables", "mcap": "Large"},
        {"symbol": "SUNPHARMA.NS", "name": "Sun Pharmaceutical", "sector": "Pharma", "mcap": "Large"},
        {"symbol": "TATAMOTORS.NS", "name": "Tata Motors", "sector": "Auto", "mcap": "Large"},
        {"symbol": "ULTRACEMCO.NS", "name": "UltraTech Cement", "sector": "Cement", "mcap": "Large"},
        {"symbol": "WIPRO.NS", "name": "Wipro", "sector": "IT", "mcap": "Large"},
        {"symbol": "NESTLEIND.NS", "name": "Nestle India", "sector": "FMCG", "mcap": "Large"},
        {"symbol": "M&M.NS", "name": "Mahindra & Mahindra", "sector": "Auto", "mcap": "Large"},
        {"symbol": "BAJAJFINSV.NS", "name": "Bajaj Finserv", "sector": "NBFC", "mcap": "Large"},
        {"symbol": "NTPC.NS", "name": "NTPC", "sector": "Power", "mcap": "Large"},
        {"symbol": "POWERGRID.NS", "name": "Power Grid Corporation", "sector": "Power", "mcap": "Large"},
        {"symbol": "TATASTEEL.NS", "name": "Tata Steel", "sector": "Metals", "mcap": "Large"},
        {"symbol": "ONGC.NS", "name": "ONGC", "sector": "Oil & Gas", "mcap": "Large"},
        {"symbol": "JSWSTEEL.NS", "name": "JSW Steel", "sector": "Metals", "mcap": "Large"},
        {"symbol": "TECHM.NS", "name": "Tech Mahindra", "sector": "IT", "mcap": "Large"},
        {"symbol": "ADANIENT.NS", "name": "Adani Enterprises", "sector": "Diversified", "mcap": "Large"},
        {"symbol": "ADANIPORTS.NS", "name": "Adani Ports", "sector": "Infrastructure", "mcap": "Large"},
        {"symbol": "HDFCLIFE.NS", "name": "HDFC Life Insurance", "sector": "Insurance", "mcap": "Large"},
        {"symbol": "COALINDIA.NS", "name": "Coal India", "sector": "Mining", "mcap": "Large"},
        {"symbol": "HINDALCO.NS", "name": "Hindalco Industries", "sector": "Metals", "mcap": "Large"},
        {"symbol": "SBILIFE.NS", "name": "SBI Life Insurance", "sector": "Insurance", "mcap": "Large"},
        {"symbol": "GRASIM.NS", "name": "Grasim Industries", "sector": "Cement", "mcap": "Large"},
        {"symbol": "BRITANNIA.NS", "name": "Britannia Industries", "sector": "FMCG", "mcap": "Large"},
        {"symbol": "BAJAJ-AUTO.NS", "name": "Bajaj Auto", "sector": "Auto", "mcap": "Large"},
        {"symbol": "DIVISLAB.NS", "name": "Divi's Laboratories", "sector": "Pharma", "mcap": "Large"},
        {"symbol": "DRREDDY.NS", "name": "Dr. Reddy's Laboratories", "sector": "Pharma", "mcap": "Large"},
        {"symbol": "CIPLA.NS", "name": "Cipla", "sector": "Pharma", "mcap": "Large"},
        {"symbol": "EICHERMOT.NS", "name": "Eicher Motors", "sector": "Auto", "mcap": "Large"},
        {"symbol": "INDUSINDBK.NS", "name": "IndusInd Bank", "sector": "Banking", "mcap": "Large"},
        {"symbol": "APOLLOHOSP.NS", "name": "Apollo Hospitals", "sector": "Healthcare", "mcap": "Large"},
        {"symbol": "HEROMOTOCO.NS", "name": "Hero MotoCorp", "sector": "Auto", "mcap": "Large"},
        {"symbol": "BPCL.NS", "name": "Bharat Petroleum", "sector": "Oil & Gas", "mcap": "Large"},
        {"symbol": "TATACONSUM.NS", "name": "Tata Consumer Products", "sector": "FMCG", "mcap": "Large"},
        {"symbol": "SHRIRAMFIN.NS", "name": "Shriram Finance", "sector": "NBFC", "mcap": "Large"},
        {"symbol": "LTIM.NS", "name": "LTIMindtree", "sector": "IT", "mcap": "Large"},
    ],
    
    # ═══════════════════════════════════════════════════════════════════
    # NIFTY NEXT 50 - Large Cap (50 stocks)
    # ═══════════════════════════════════════════════════════════════════
    "NIFTY NEXT 50": [
        {"symbol": "ADANIGREEN.NS", "name": "Adani Green Energy", "sector": "Power", "mcap": "Large"},
        {"symbol": "ADANIPOWER.NS", "name": "Adani Power", "sector": "Power", "mcap": "Large"},
        {"symbol": "AMBUJACEM.NS", "name": "Ambuja Cements", "sector": "Cement", "mcap": "Large"},
        {"symbol": "ATGL.NS", "name": "Adani Total Gas", "sector": "Gas Distribution", "mcap": "Large"},
        {"symbol": "AWL.NS", "name": "Adani Wilmar", "sector": "FMCG", "mcap": "Mid"},
        {"symbol": "BANKBARODA.NS", "name": "Bank of Baroda", "sector": "Banking", "mcap": "Large"},
        {"symbol": "BEL.NS", "name": "Bharat Electronics", "sector": "Defence", "mcap": "Large"},
        {"symbol": "BERGEPAINT.NS", "name": "Berger Paints", "sector": "Paints", "mcap": "Large"},
        {"symbol": "BOSCHLTD.NS", "name": "Bosch", "sector": "Auto Ancillary", "mcap": "Large"},
        {"symbol": "CANBK.NS", "name": "Canara Bank", "sector": "Banking", "mcap": "Large"},
        {"symbol": "CHOLAFIN.NS", "name": "Cholamandalam Investment", "sector": "NBFC", "mcap": "Large"},
        {"symbol": "COLPAL.NS", "name": "Colgate-Palmolive", "sector": "FMCG", "mcap": "Large"},
        {"symbol": "DLF.NS", "name": "DLF", "sector": "Real Estate", "mcap": "Large"},
        {"symbol": "DABUR.NS", "name": "Dabur India", "sector": "FMCG", "mcap": "Large"},
        {"symbol": "GODREJCP.NS", "name": "Godrej Consumer Products", "sector": "FMCG", "mcap": "Large"},
        {"symbol": "GAIL.NS", "name": "GAIL India", "sector": "Gas", "mcap": "Large"},
        {"symbol": "HAL.NS", "name": "Hindustan Aeronautics", "sector": "Defence", "mcap": "Large"},
        {"symbol": "HAVELLS.NS", "name": "Havells India", "sector": "Consumer Durables", "mcap": "Large"},
        {"symbol": "ICICIGI.NS", "name": "ICICI Lombard", "sector": "Insurance", "mcap": "Large"},
        {"symbol": "ICICIPRULI.NS", "name": "ICICI Prudential Life", "sector": "Insurance", "mcap": "Large"},
        {"symbol": "INDUSTOWER.NS", "name": "Indus Towers", "sector": "Telecom", "mcap": "Large"},
        {"symbol": "IOC.NS", "name": "Indian Oil Corporation", "sector": "Oil & Gas", "mcap": "Large"},
        {"symbol": "IRCTC.NS", "name": "IRCTC", "sector": "Tourism", "mcap": "Mid"},
        {"symbol": "JINDALSTEL.NS", "name": "Jindal Steel & Power", "sector": "Metals", "mcap": "Large"},
        {"symbol": "JIOFIN.NS", "name": "Jio Financial Services", "sector": "NBFC", "mcap": "Large"},
        {"symbol": "LICI.NS", "name": "Life Insurance Corporation", "sector": "Insurance", "mcap": "Large"},
        {"symbol": "LUPIN.NS", "name": "Lupin", "sector": "Pharma", "mcap": "Large"},
        {"symbol": "MARICO.NS", "name": "Marico", "sector": "FMCG", "mcap": "Large"},
        {"symbol": "NAUKRI.NS", "name": "Info Edge (Naukri)", "sector": "Internet", "mcap": "Large"},
        {"symbol": "PAYTM.NS", "name": "One 97 Communications", "sector": "Fintech", "mcap": "Mid"},
        {"symbol": "PFC.NS", "name": "Power Finance Corporation", "sector": "NBFC", "mcap": "Large"},
        {"symbol": "PIDILITIND.NS", "name": "Pidilite Industries", "sector": "Chemicals", "mcap": "Large"},
        {"symbol": "PNB.NS", "name": "Punjab National Bank", "sector": "Banking", "mcap": "Large"},
        {"symbol": "RECLTD.NS", "name": "REC Limited", "sector": "NBFC", "mcap": "Large"},
        {"symbol": "SIEMENS.NS", "name": "Siemens", "sector": "Capital Goods", "mcap": "Large"},
        {"symbol": "SRF.NS", "name": "SRF", "sector": "Chemicals", "mcap": "Large"},
        {"symbol": "TATAPOWER.NS", "name": "Tata Power", "sector": "Power", "mcap": "Large"},
        {"symbol": "TORNTPHARM.NS", "name": "Torrent Pharmaceuticals", "sector": "Pharma", "mcap": "Large"},
        {"symbol": "TRENT.NS", "name": "Trent", "sector": "Retail", "mcap": "Large"},
        {"symbol": "UNIONBANK.NS", "name": "Union Bank of India", "sector": "Banking", "mcap": "Large"},
        {"symbol": "VEDL.NS", "name": "Vedanta", "sector": "Metals", "mcap": "Large"},
        {"symbol": "ZOMATO.NS", "name": "Zomato", "sector": "Internet", "mcap": "Large"},
        {"symbol": "ZYDUSLIFE.NS", "name": "Zydus Lifesciences", "sector": "Pharma", "mcap": "Large"},
        {"symbol": "DMART.NS", "name": "Avenue Supermarts", "sector": "Retail", "mcap": "Large"},
        {"symbol": "ABB.NS", "name": "ABB India", "sector": "Capital Goods", "mcap": "Large"},
        {"symbol": "PERSISTENT.NS", "name": "Persistent Systems", "sector": "IT", "mcap": "Large"},
        {"symbol": "MUTHOOTFIN.NS", "name": "Muthoot Finance", "sector": "NBFC", "mcap": "Large"},
        {"symbol": "PIIND.NS", "name": "PI Industries", "sector": "Chemicals", "mcap": "Large"},
        {"symbol": "POLYCAB.NS", "name": "Polycab India", "sector": "Capital Goods", "mcap": "Large"},
        {"symbol": "MAXHEALTH.NS", "name": "Max Healthcare", "sector": "Healthcare", "mcap": "Large"},
    ],
    
    # ═══════════════════════════════════════════════════════════════════
    # BANKING & FINANCIAL SERVICES (40 stocks)
    # ═══════════════════════════════════════════════════════════════════
    "BANKING & FINANCE": [
        {"symbol": "AUBANK.NS", "name": "AU Small Finance Bank", "sector": "Banking", "mcap": "Mid"},
        {"symbol": "BANDHANBNK.NS", "name": "Bandhan Bank", "sector": "Banking", "mcap": "Mid"},
        {"symbol": "FEDERALBNK.NS", "name": "Federal Bank", "sector": "Banking", "mcap": "Mid"},
        {"symbol": "IDFCFIRSTB.NS", "name": "IDFC First Bank", "sector": "Banking", "mcap": "Mid"},
        {"symbol": "RBLBANK.NS", "name": "RBL Bank", "sector": "Banking", "mcap": "Mid"},
        {"symbol": "YESBANK.NS", "name": "Yes Bank", "sector": "Banking", "mcap": "Mid"},
        {"symbol": "IDBI.NS", "name": "IDBI Bank", "sector": "Banking", "mcap": "Mid"},
        {"symbol": "INDIANB.NS", "name": "Indian Bank", "sector": "Banking", "mcap": "Mid"},
        {"symbol": "IOB.NS", "name": "Indian Overseas Bank", "sector": "Banking", "mcap": "Small"},
        {"symbol": "CENTRALBK.NS", "name": "Central Bank of India", "sector": "Banking", "mcap": "Small"},
        {"symbol": "MAHABANK.NS", "name": "Bank of Maharashtra", "sector": "Banking", "mcap": "Mid"},
        {"symbol": "UCOBANK.NS", "name": "UCO Bank", "sector": "Banking", "mcap": "Small"},
        {"symbol": "BANKINDIA.NS", "name": "Bank of India", "sector": "Banking", "mcap": "Mid"},
        {"symbol": "PSB.NS", "name": "Punjab & Sind Bank", "sector": "Banking", "mcap": "Small"},
        {"symbol": "KARURVYSYA.NS", "name": "Karur Vysya Bank", "sector": "Banking", "mcap": "Small"},
        {"symbol": "KTKBANK.NS", "name": "Karnataka Bank", "sector": "Banking", "mcap": "Small"},
        {"symbol": "SOUTHBANK.NS", "name": "South Indian Bank", "sector": "Banking", "mcap": "Small"},
        {"symbol": "TMB.NS", "name": "Tamilnad Mercantile Bank", "sector": "Banking", "mcap": "Small"},
        {"symbol": "CUB.NS", "name": "City Union Bank", "sector": "Banking", "mcap": "Small"},
        {"symbol": "DCB.NS", "name": "DCB Bank", "sector": "Banking", "mcap": "Small"},
        {"symbol": "EQUITASBNK.NS", "name": "Equitas Small Finance Bank", "sector": "Banking", "mcap": "Small"},
        {"symbol": "UJJIVANSFB.NS", "name": "Ujjivan Small Finance Bank", "sector": "Banking", "mcap": "Small"},
        {"symbol": "MANAPPURAM.NS", "name": "Manappuram Finance", "sector": "NBFC", "mcap": "Mid"},
        {"symbol": "L&TFH.NS", "name": "L&T Finance Holdings", "sector": "NBFC", "mcap": "Mid"},
        {"symbol": "POONAWALLA.NS", "name": "Poonawalla Fincorp", "sector": "NBFC", "mcap": "Mid"},
        {"symbol": "LICHSGFIN.NS", "name": "LIC Housing Finance", "sector": "NBFC", "mcap": "Mid"},
        {"symbol": "CANFINHOME.NS", "name": "Can Fin Homes", "sector": "NBFC", "mcap": "Small"},
        {"symbol": "CREDITACC.NS", "name": "CreditAccess Grameen", "sector": "NBFC", "mcap": "Mid"},
        {"symbol": "AAVAS.NS", "name": "Aavas Financiers", "sector": "NBFC", "mcap": "Small"},
        {"symbol": "APTUS.NS", "name": "Aptus Value Housing", "sector": "NBFC", "mcap": "Small"},
        {"symbol": "HOMEFIRST.NS", "name": "Home First Finance", "sector": "NBFC", "mcap": "Small"},
        {"symbol": "SUNDARMFIN.NS", "name": "Sundaram Finance", "sector": "NBFC", "mcap": "Mid"},
        {"symbol": "M&MFIN.NS", "name": "Mahindra & Mahindra Financial", "sector": "NBFC", "mcap": "Mid"},
        {"symbol": "IRFC.NS", "name": "Indian Railway Finance Corp", "sector": "NBFC", "mcap": "Large"},
        {"symbol": "HUDCO.NS", "name": "Housing & Urban Development", "sector": "NBFC", "mcap": "Mid"},
        {"symbol": "SBFC.NS", "name": "SBFC Finance", "sector": "NBFC", "mcap": "Small"},
        {"symbol": "FIVESTAR.NS", "name": "Five-Star Business Finance", "sector": "NBFC", "mcap": "Small"},
        {"symbol": "ANGELONE.NS", "name": "Angel One", "sector": "Broking", "mcap": "Mid"},
        {"symbol": "MOTILALOFS.NS", "name": "Motilal Oswal Financial", "sector": "Broking", "mcap": "Mid"},
        {"symbol": "IIFL.NS", "name": "IIFL Finance", "sector": "NBFC", "mcap": "Mid"},
    ],
    
    # ═══════════════════════════════════════════════════════════════════
    # IT & TECHNOLOGY (35 stocks)
    # ═══════════════════════════════════════════════════════════════════
    "IT & TECHNOLOGY": [
        {"symbol": "COFORGE.NS", "name": "Coforge", "sector": "IT", "mcap": "Large"},
        {"symbol": "MPHASIS.NS", "name": "Mphasis", "sector": "IT", "mcap": "Large"},
        {"symbol": "LTTS.NS", "name": "L&T Technology Services", "sector": "IT", "mcap": "Large"},
        {"symbol": "HAPPSTMNDS.NS", "name": "Happiest Minds", "sector": "IT", "mcap": "Mid"},
        {"symbol": "CYIENT.NS", "name": "Cyient", "sector": "IT", "mcap": "Mid"},
        {"symbol": "TATAELXSI.NS", "name": "Tata Elxsi", "sector": "IT", "mcap": "Large"},
        {"symbol": "KPITTECH.NS", "name": "KPIT Technologies", "sector": "IT", "mcap": "Large"},
        {"symbol": "SONATSOFTW.NS", "name": "Sonata Software", "sector": "IT", "mcap": "Mid"},
        {"symbol": "ZENSARTECH.NS", "name": "Zensar Technologies", "sector": "IT", "mcap": "Mid"},
        {"symbol": "BIRLASOFT.NS", "name": "Birlasoft", "sector": "IT", "mcap": "Mid"},
        {"symbol": "MASTEK.NS", "name": "Mastek", "sector": "IT", "mcap": "Mid"},
        {"symbol": "NIITLTD.NS", "name": "NIIT Ltd", "sector": "IT", "mcap": "Small"},
        {"symbol": "NEWGEN.NS", "name": "Newgen Software", "sector": "IT", "mcap": "Small"},
        {"symbol": "INTELLECT.NS", "name": "Intellect Design Arena", "sector": "IT", "mcap": "Mid"},
        {"symbol": "TANLA.NS", "name": "Tanla Platforms", "sector": "IT", "mcap": "Mid"},
        {"symbol": "ROUTE.NS", "name": "Route Mobile", "sector": "IT", "mcap": "Mid"},
        {"symbol": "ECLERX.NS", "name": "eClerx Services", "sector": "IT", "mcap": "Mid"},
        {"symbol": "FIRSTSOUR.NS", "name": "Firstsource Solutions", "sector": "IT", "mcap": "Mid"},
        {"symbol": "NAZARA.NS", "name": "Nazara Technologies", "sector": "Gaming", "mcap": "Small"},
        {"symbol": "LATENTVIEW.NS", "name": "Latent View Analytics", "sector": "IT", "mcap": "Mid"},
        {"symbol": "DATAPATTNS.NS", "name": "Data Patterns", "sector": "Defence IT", "mcap": "Mid"},
        {"symbol": "MAPMY.NS", "name": "MapmyIndia", "sector": "IT", "mcap": "Mid"},
        {"symbol": "NETWEB.NS", "name": "Netweb Technologies", "sector": "IT", "mcap": "Small"},
        {"symbol": "TATATECH.NS", "name": "Tata Technologies", "sector": "IT", "mcap": "Large"},
        {"symbol": "OFSS.NS", "name": "Oracle Financial Services", "sector": "IT", "mcap": "Large"},
        {"symbol": "INFIBEAM.NS", "name": "Infibeam Avenues", "sector": "Fintech", "mcap": "Mid"},
        {"symbol": "FSL.NS", "name": "Firstsource Solutions", "sector": "IT", "mcap": "Mid"},
        {"symbol": "RATEGAIN.NS", "name": "RateGain Travel", "sector": "IT", "mcap": "Mid"},
        {"symbol": "BSOFT.NS", "name": "BSOFT", "sector": "IT", "mcap": "Mid"},
        {"symbol": "TTML.NS", "name": "Tata Teleservices", "sector": "Telecom", "mcap": "Mid"},
        {"symbol": "QUICKHEAL.NS", "name": "Quick Heal Technologies", "sector": "IT", "mcap": "Small"},
        {"symbol": "SUBEX.NS", "name": "Subex Limited", "sector": "IT", "mcap": "Small"},
        {"symbol": "ZENTEC.NS", "name": "Zen Technologies", "sector": "Defence IT", "mcap": "Mid"},
        {"symbol": "SAKSOFT.NS", "name": "Saksoft", "sector": "IT", "mcap": "Small"},
        {"symbol": "HCLTECH.NS", "name": "HCL Technologies", "sector": "IT", "mcap": "Large"},
    ],
    
    # ═══════════════════════════════════════════════════════════════════
    # PHARMA & HEALTHCARE (40 stocks)
    # ═══════════════════════════════════════════════════════════════════
    "PHARMA & HEALTHCARE": [
        {"symbol": "BIOCON.NS", "name": "Biocon", "sector": "Pharma", "mcap": "Large"},
        {"symbol": "AUROPHARMA.NS", "name": "Aurobindo Pharma", "sector": "Pharma", "mcap": "Large"},
        {"symbol": "ALKEM.NS", "name": "Alkem Laboratories", "sector": "Pharma", "mcap": "Large"},
        {"symbol": "ABBOTINDIA.NS", "name": "Abbott India", "sector": "Pharma", "mcap": "Large"},
        {"symbol": "GLAXO.NS", "name": "GlaxoSmithKline Pharma", "sector": "Pharma", "mcap": "Mid"},
        {"symbol": "PFIZER.NS", "name": "Pfizer", "sector": "Pharma", "mcap": "Mid"},
        {"symbol": "SANOFI.NS", "name": "Sanofi India", "sector": "Pharma", "mcap": "Mid"},
        {"symbol": "GLAND.NS", "name": "Gland Pharma", "sector": "Pharma", "mcap": "Large"},
        {"symbol": "LAURUSLABS.NS", "name": "Laurus Labs", "sector": "Pharma", "mcap": "Mid"},
        {"symbol": "GRANULES.NS", "name": "Granules India", "sector": "Pharma", "mcap": "Mid"},
        {"symbol": "IPCALAB.NS", "name": "IPCA Laboratories", "sector": "Pharma", "mcap": "Mid"},
        {"symbol": "NATCOPHARMA.NS", "name": "Natco Pharma", "sector": "Pharma", "mcap": "Mid"},
        {"symbol": "AJANTPHARM.NS", "name": "Ajanta Pharma", "sector": "Pharma", "mcap": "Mid"},
        {"symbol": "GLENMARK.NS", "name": "Glenmark Pharmaceuticals", "sector": "Pharma", "mcap": "Mid"},
        {"symbol": "APLLTD.NS", "name": "Alembic Pharmaceuticals", "sector": "Pharma", "mcap": "Mid"},
        {"symbol": "SYNGENE.NS", "name": "Syngene International", "sector": "Pharma", "mcap": "Large"},
        {"symbol": "NEULANDLAB.NS", "name": "Neuland Laboratories", "sector": "Pharma", "mcap": "Mid"},
        {"symbol": "FORTIS.NS", "name": "Fortis Healthcare", "sector": "Healthcare", "mcap": "Large"},
        {"symbol": "METROPOLIS.NS", "name": "Metropolis Healthcare", "sector": "Healthcare", "mcap": "Mid"},
        {"symbol": "LALPATHLAB.NS", "name": "Dr Lal PathLabs", "sector": "Healthcare", "mcap": "Large"},
        {"symbol": "KIMS.NS", "name": "Krishna Institute of Medical Sciences", "sector": "Healthcare", "mcap": "Mid"},
        {"symbol": "MEDANTA.NS", "name": "Global Health (Medanta)", "sector": "Healthcare", "mcap": "Mid"},
        {"symbol": "RAINBOW.NS", "name": "Rainbow Children's Medicare", "sector": "Healthcare", "mcap": "Mid"},
        {"symbol": "SHALBY.NS", "name": "Shalby", "sector": "Healthcare", "mcap": "Small"},
        {"symbol": "NH.NS", "name": "Narayana Hrudayalaya", "sector": "Healthcare", "mcap": "Mid"},
        {"symbol": "ERIS.NS", "name": "Eris Lifesciences", "sector": "Pharma", "mcap": "Mid"},
        {"symbol": "MANKIND.NS", "name": "Mankind Pharma", "sector": "Pharma", "mcap": "Large"},
        {"symbol": "JBCHEPHARM.NS", "name": "J B Chemicals & Pharmaceuticals", "sector": "Pharma", "mcap": "Mid"},
        {"symbol": "SUVEN.NS", "name": "Suven Pharmaceuticals", "sector": "Pharma", "mcap": "Mid"},
        {"symbol": "PGHL.NS", "name": "Procter & Gamble Health", "sector": "Pharma", "mcap": "Mid"},
        {"symbol": "ASTRAZEN.NS", "name": "AstraZeneca Pharma", "sector": "Pharma", "mcap": "Mid"},
        {"symbol": "CONCORD.NS", "name": "Concord Biotech", "sector": "Pharma", "mcap": "Mid"},
        {"symbol": "MARKSANS.NS", "name": "Marksans Pharma", "sector": "Pharma", "mcap": "Small"},
        {"symbol": "SHILPAMED.NS", "name": "Shilpa Medicare", "sector": "Pharma", "mcap": "Small"},
        {"symbol": "SOLARA.NS", "name": "Solara Active Pharma", "sector": "Pharma", "mcap": "Small"},
        {"symbol": "BLISSGVS.NS", "name": "Bliss GVS Pharma", "sector": "Pharma", "mcap": "Small"},
        {"symbol": "CAPLIPOINT.NS", "name": "Caplin Point Laboratories", "sector": "Pharma", "mcap": "Small"},
        {"symbol": "SEQUENT.NS", "name": "Sequent Scientific", "sector": "Pharma", "mcap": "Small"},
        {"symbol": "THYROCARE.NS", "name": "Thyrocare Technologies", "sector": "Healthcare", "mcap": "Mid"},
        {"symbol": "KRSNAA.NS", "name": "Krsnaa Diagnostics", "sector": "Healthcare", "mcap": "Small"},
    ],
    
    # ═══════════════════════════════════════════════════════════════════
    # AUTO & AUTO ANCILLARY (35 stocks)
    # ═══════════════════════════════════════════════════════════════════
    "AUTO & AUTO ANCILLARY": [
        {"symbol": "ASHOKLEY.NS", "name": "Ashok Leyland", "sector": "Auto", "mcap": "Large"},
        {"symbol": "TVSMOTOR.NS", "name": "TVS Motor", "sector": "Auto", "mcap": "Large"},
        {"symbol": "ESCORTS.NS", "name": "Escorts Kubota", "sector": "Auto", "mcap": "Large"},
        {"symbol": "FORCEMOT.NS", "name": "Force Motors", "sector": "Auto", "mcap": "Mid"},
        {"symbol": "BHARATFORG.NS", "name": "Bharat Forge", "sector": "Auto Ancillary", "mcap": "Large"},
        {"symbol": "MOTHERSON.NS", "name": "Samvardhana Motherson", "sector": "Auto Ancillary", "mcap": "Large"},
        {"symbol": "BALKRISIND.NS", "name": "Balkrishna Industries", "sector": "Tyres", "mcap": "Large"},
        {"symbol": "MRF.NS", "name": "MRF", "sector": "Tyres", "mcap": "Large"},
        {"symbol": "APOLLOTYRE.NS", "name": "Apollo Tyres", "sector": "Tyres", "mcap": "Mid"},
        {"symbol": "CEAT.NS", "name": "CEAT", "sector": "Tyres", "mcap": "Mid"},
        {"symbol": "JKTYRE.NS", "name": "JK Tyre", "sector": "Tyres", "mcap": "Small"},
        {"symbol": "EXIDEIND.NS", "name": "Exide Industries", "sector": "Auto Ancillary", "mcap": "Mid"},
        {"symbol": "AMARAJABAT.NS", "name": "Amara Raja Energy", "sector": "Auto Ancillary", "mcap": "Mid"},
        {"symbol": "SUNDRMFAST.NS", "name": "Sundram Fasteners", "sector": "Auto Ancillary", "mcap": "Mid"},
        {"symbol": "ENDURANCE.NS", "name": "Endurance Technologies", "sector": "Auto Ancillary", "mcap": "Mid"},
        {"symbol": "SUPRAJIT.NS", "name": "Suprajit Engineering", "sector": "Auto Ancillary", "mcap": "Small"},
        {"symbol": "SCHAEFFLER.NS", "name": "Schaeffler India", "sector": "Auto Ancillary", "mcap": "Large"},
        {"symbol": "UNOMINDA.NS", "name": "Uno Minda", "sector": "Auto Ancillary", "mcap": "Large"},
        {"symbol": "OLECTRA.NS", "name": "Olectra Greentech", "sector": "Auto", "mcap": "Mid"},
        {"symbol": "SONACOMS.NS", "name": "Sona BLW Precision", "sector": "Auto Ancillary", "mcap": "Large"},
        {"symbol": "SWARAJENG.NS", "name": "Swaraj Engines", "sector": "Auto Ancillary", "mcap": "Small"},
        {"symbol": "SAMVARDHAN.NS", "name": "Samvardhana Motherson", "sector": "Auto Ancillary", "mcap": "Large"},
        {"symbol": "CRAFTSMAN.NS", "name": "Craftsman Automation", "sector": "Auto Ancillary", "mcap": "Mid"},
        {"symbol": "GABRIEL.NS", "name": "Gabriel India", "sector": "Auto Ancillary", "mcap": "Small"},
        {"symbol": "BOSCH.NS", "name": "Bosch", "sector": "Auto Ancillary", "mcap": "Large"},
        {"symbol": "SWARAJENG.NS", "name": "Swaraj Engines", "sector": "Auto Ancillary", "mcap": "Small"},
        {"symbol": "SUBROS.NS", "name": "Subros", "sector": "Auto Ancillary", "mcap": "Small"},
        {"symbol": "MAHINDCIE.NS", "name": "Mahindra CIE", "sector": "Auto Ancillary", "mcap": "Mid"},
        {"symbol": "WHEELS.NS", "name": "Wheels India", "sector": "Auto Ancillary", "mcap": "Small"},
        {"symbol": "VSTTILLERS.NS", "name": "VST Tillers Tractors", "sector": "Auto", "mcap": "Small"},
        {"symbol": "SHARDACROP.NS", "name": "Sharda Cropchem", "sector": "Agrochemicals", "mcap": "Small"},
        {"symbol": "AUTOAXLES.NS", "name": "Automotive Axles", "sector": "Auto Ancillary", "mcap": "Small"},
        {"symbol": "GNA.NS", "name": "GNA Axles", "sector": "Auto Ancillary", "mcap": "Small"},
        {"symbol": "SANDHAR.NS", "name": "Sandhar Technologies", "sector": "Auto Ancillary", "mcap": "Small"},
        {"symbol": "LUMAXTECH.NS", "name": "Lumax Auto Technologies", "sector": "Auto Ancillary", "mcap": "Small"},
    ],
    
    # ═══════════════════════════════════════════════════════════════════
    # FMCG & CONSUMER (30 stocks)
    # ═══════════════════════════════════════════════════════════════════
    "FMCG & CONSUMER": [
        {"symbol": "EMAMILTD.NS", "name": "Emami", "sector": "FMCG", "mcap": "Mid"},
        {"symbol": "GODREJIND.NS", "name": "Godrej Industries", "sector": "FMCG", "mcap": "Mid"},
        {"symbol": "JYOTHYLAB.NS", "name": "Jyothy Labs", "sector": "FMCG", "mcap": "Mid"},
        {"symbol": "RADICO.NS", "name": "Radico Khaitan", "sector": "Beverages", "mcap": "Mid"},
        {"symbol": "UBL.NS", "name": "United Breweries", "sector": "Beverages", "mcap": "Mid"},
        {"symbol": "MCDOWELL-N.NS", "name": "United Spirits", "sector": "Beverages", "mcap": "Large"},
        {"symbol": "VBL.NS", "name": "Varun Beverages", "sector": "Beverages", "mcap": "Large"},
        {"symbol": "PGHH.NS", "name": "Procter & Gamble Hygiene", "sector": "FMCG", "mcap": "Large"},
        {"symbol": "GILLETTE.NS", "name": "Gillette India", "sector": "FMCG", "mcap": "Mid"},
        {"symbol": "BIKAJI.NS", "name": "Bikaji Foods", "sector": "FMCG", "mcap": "Mid"},
        {"symbol": "PATANJALI.NS", "name": "Patanjali Foods", "sector": "FMCG", "mcap": "Mid"},
        {"symbol": "KRBL.NS", "name": "KRBL", "sector": "FMCG", "mcap": "Mid"},
        {"symbol": "VENKEYS.NS", "name": "Venky's India", "sector": "FMCG", "mcap": "Small"},
        {"symbol": "ZYDUSWELL.NS", "name": "Zydus Wellness", "sector": "FMCG", "mcap": "Mid"},
        {"symbol": "BALRAMCHIN.NS", "name": "Balrampur Chini Mills", "sector": "Sugar", "mcap": "Mid"},
        {"symbol": "TRIVENI.NS", "name": "Triveni Engineering", "sector": "Sugar", "mcap": "Small"},
        {"symbol": "DWARIKESH.NS", "name": "Dwarikesh Sugar", "sector": "Sugar", "mcap": "Small"},
        {"symbol": "RENUKA.NS", "name": "Shree Renuka Sugars", "sector": "Sugar", "mcap": "Small"},
        {"symbol": "BAJAJCON.NS", "name": "Bajaj Consumer Care", "sector": "FMCG", "mcap": "Small"},
        {"symbol": "HATSUN.NS", "name": "Hatsun Agro", "sector": "FMCG", "mcap": "Mid"},
        {"symbol": "WESTLIFE.NS", "name": "Westlife Foodworld", "sector": "QSR", "mcap": "Mid"},
        {"symbol": "DEVYANI.NS", "name": "Devyani International", "sector": "QSR", "mcap": "Mid"},
        {"symbol": "SAPPHIRE.NS", "name": "Sapphire Foods", "sector": "QSR", "mcap": "Mid"},
        {"symbol": "JUBLFOOD.NS", "name": "Jubilant Foodworks", "sector": "QSR", "mcap": "Large"},
        {"symbol": "BURGERKING.NS", "name": "Burger King India", "sector": "QSR", "mcap": "Small"},
        {"symbol": "VSTIND.NS", "name": "VST Industries", "sector": "FMCG", "mcap": "Mid"},
        {"symbol": "GODFRYPHLP.NS", "name": "Godfrey Phillips", "sector": "FMCG", "mcap": "Mid"},
        {"symbol": "CCL.NS", "name": "CCL Products", "sector": "FMCG", "mcap": "Mid"},
        {"symbol": "TATAELX.NS", "name": "Tata Elxsi", "sector": "IT", "mcap": "Large"},
        {"symbol": "HONAUT.NS", "name": "Honeywell Automation", "sector": "Capital Goods", "mcap": "Large"},
    ],
    
    # ═══════════════════════════════════════════════════════════════════
    # METALS & MINING (25 stocks)
    # ═══════════════════════════════════════════════════════════════════
    "METALS & MINING": [
        {"symbol": "NATIONALUM.NS", "name": "National Aluminium", "sector": "Metals", "mcap": "Mid"},
        {"symbol": "NMDC.NS", "name": "NMDC", "sector": "Mining", "mcap": "Large"},
        {"symbol": "SAIL.NS", "name": "Steel Authority of India", "sector": "Metals", "mcap": "Mid"},
        {"symbol": "MOIL.NS", "name": "MOIL", "sector": "Mining", "mcap": "Small"},
        {"symbol": "HINDCOPPER.NS", "name": "Hindustan Copper", "sector": "Mining", "mcap": "Mid"},
        {"symbol": "RATNAMANI.NS", "name": "Ratnamani Metals", "sector": "Metals", "mcap": "Mid"},
        {"symbol": "APLAPOLLO.NS", "name": "APL Apollo Tubes", "sector": "Metals", "mcap": "Large"},
        {"symbol": "WELCORP.NS", "name": "Welspun Corp", "sector": "Metals", "mcap": "Mid"},
        {"symbol": "JINDALSAW.NS", "name": "Jindal Saw", "sector": "Metals", "mcap": "Mid"},
        {"symbol": "KIOCL.NS", "name": "KIOCL", "sector": "Mining", "mcap": "Small"},
        {"symbol": "JSL.NS", "name": "Jindal Stainless", "sector": "Metals", "mcap": "Large"},
        {"symbol": "HINDZINC.NS", "name": "Hindustan Zinc", "sector": "Metals", "mcap": "Large"},
        {"symbol": "NSLNISP.NS", "name": "NMDC Steel", "sector": "Metals", "mcap": "Mid"},
        {"symbol": "GPIL.NS", "name": "Godawari Power & Ispat", "sector": "Metals", "mcap": "Mid"},
        {"symbol": "LLOYDSME.NS", "name": "Lloyds Metals", "sector": "Metals", "mcap": "Mid"},
        {"symbol": "SARDAEN.NS", "name": "Sarda Energy", "sector": "Metals", "mcap": "Mid"},
        {"symbol": "SHYAMMET.NS", "name": "Shyam Metalics", "sector": "Metals", "mcap": "Mid"},
        {"symbol": "GALLANTT.NS", "name": "Gallantt Ispat", "sector": "Metals", "mcap": "Small"},
        {"symbol": "MIDHANI.NS", "name": "Mishra Dhatu Nigam", "sector": "Defence Metals", "mcap": "Mid"},
        {"symbol": "TIRUMALCHM.NS", "name": "Tirumala Chemicals", "sector": "Chemicals", "mcap": "Small"},
        {"symbol": "GRAVITA.NS", "name": "Gravita India", "sector": "Metals", "mcap": "Mid"},
        {"symbol": "HGINFRA.NS", "name": "H.G. Infra Engineering", "sector": "Infrastructure", "mcap": "Mid"},
        {"symbol": "UNIPARTS.NS", "name": "Uniparts India", "sector": "Auto Ancillary", "mcap": "Small"},
        {"symbol": "WELENT.NS", "name": "Welspun Enterprises", "sector": "Infrastructure", "mcap": "Mid"},
        {"symbol": "PRAKASH.NS", "name": "Prakash Industries", "sector": "Metals", "mcap": "Small"},
    ],
    
    # ═══════════════════════════════════════════════════════════════════
    # ENERGY & POWER (30 stocks)
    # ═══════════════════════════════════════════════════════════════════
    "ENERGY & POWER": [
        {"symbol": "NHPC.NS", "name": "NHPC", "sector": "Power", "mcap": "Large"},
        {"symbol": "SJVN.NS", "name": "SJVN", "sector": "Power", "mcap": "Mid"},
        {"symbol": "TORNTPOWER.NS", "name": "Torrent Power", "sector": "Power", "mcap": "Large"},
        {"symbol": "CESC.NS", "name": "CESC", "sector": "Power", "mcap": "Mid"},
        {"symbol": "JSWENERGY.NS", "name": "JSW Energy", "sector": "Power", "mcap": "Large"},
        {"symbol": "RPOWER.NS", "name": "Reliance Power", "sector": "Power", "mcap": "Mid"},
        {"symbol": "JPPOWER.NS", "name": "Jaiprakash Power", "sector": "Power", "mcap": "Small"},
        {"symbol": "NLCINDIA.NS", "name": "NLC India", "sector": "Power", "mcap": "Mid"},
        {"symbol": "IEX.NS", "name": "Indian Energy Exchange", "sector": "Power", "mcap": "Mid"},
        {"symbol": "PETRONET.NS", "name": "Petronet LNG", "sector": "Gas", "mcap": "Large"},
        {"symbol": "MGL.NS", "name": "Mahanagar Gas", "sector": "Gas Distribution", "mcap": "Mid"},
        {"symbol": "IGL.NS", "name": "Indraprastha Gas", "sector": "Gas Distribution", "mcap": "Large"},
        {"symbol": "GUJGASLTD.NS", "name": "Gujarat Gas", "sector": "Gas Distribution", "mcap": "Mid"},
        {"symbol": "GSPL.NS", "name": "Gujarat State Petronet", "sector": "Gas", "mcap": "Mid"},
        {"symbol": "HINDPETRO.NS", "name": "Hindustan Petroleum", "sector": "Oil & Gas", "mcap": "Large"},
        {"symbol": "MRPL.NS", "name": "Mangalore Refinery", "sector": "Oil & Gas", "mcap": "Mid"},
        {"symbol": "CHENNPETRO.NS", "name": "Chennai Petroleum", "sector": "Oil & Gas", "mcap": "Mid"},
        {"symbol": "OIL.NS", "name": "Oil India", "sector": "Oil & Gas", "mcap": "Large"},
        {"symbol": "CASTROLIND.NS", "name": "Castrol India", "sector": "Oil & Gas", "mcap": "Mid"},
        {"symbol": "SUZLON.NS", "name": "Suzlon Energy", "sector": "Renewable", "mcap": "Mid"},
        {"symbol": "INOXWIND.NS", "name": "Inox Wind", "sector": "Renewable", "mcap": "Small"},
        {"symbol": "ORIENTGREEN.NS", "name": "Orient Green Power", "sector": "Renewable", "mcap": "Small"},
        {"symbol": "TATAPOWER.NS", "name": "Tata Power", "sector": "Power", "mcap": "Large"},
        {"symbol": "RELINFRA.NS", "name": "Reliance Infrastructure", "sector": "Infrastructure", "mcap": "Mid"},
        {"symbol": "GIPCL.NS", "name": "Gujarat Industries Power", "sector": "Power", "mcap": "Small"},
        {"symbol": "KPTL.NS", "name": "Kalpataru Projects", "sector": "Infrastructure", "mcap": "Mid"},
        {"symbol": "PGEL.NS", "name": "PG Electroplast", "sector": "Electronics", "mcap": "Mid"},
        {"symbol": "WAREEENER.NS", "name": "Waaree Energies", "sector": "Renewable", "mcap": "Large"},
        {"symbol": "PREMIERPOL.NS", "name": "Premier Polyfilm", "sector": "Chemicals", "mcap": "Small"},
        {"symbol": "POWERMECH.NS", "name": "Power Mech Projects", "sector": "Infrastructure", "mcap": "Mid"},
    ],
    
    # ═══════════════════════════════════════════════════════════════════
    # INFRASTRUCTURE & REAL ESTATE (35 stocks)
    # ═══════════════════════════════════════════════════════════════════
    "INFRASTRUCTURE & REAL ESTATE": [
        {"symbol": "IRB.NS", "name": "IRB Infrastructure", "sector": "Infrastructure", "mcap": "Mid"},
        {"symbol": "PEL.NS", "name": "Piramal Enterprises", "sector": "Diversified", "mcap": "Large"},
        {"symbol": "NBCC.NS", "name": "NBCC India", "sector": "Infrastructure", "mcap": "Mid"},
        {"symbol": "NCC.NS", "name": "NCC", "sector": "Infrastructure", "mcap": "Mid"},
        {"symbol": "KEC.NS", "name": "KEC International", "sector": "Infrastructure", "mcap": "Mid"},
        {"symbol": "KALPATPOWR.NS", "name": "Kalpataru Power", "sector": "Infrastructure", "mcap": "Mid"},
        {"symbol": "ENGINERSIN.NS", "name": "Engineers India", "sector": "Infrastructure", "mcap": "Mid"},
        {"symbol": "RVNL.NS", "name": "Rail Vikas Nigam", "sector": "Infrastructure", "mcap": "Large"},
        {"symbol": "IRCON.NS", "name": "Ircon International", "sector": "Infrastructure", "mcap": "Mid"},
        {"symbol": "HCC.NS", "name": "Hindustan Construction", "sector": "Infrastructure", "mcap": "Small"},
        {"symbol": "PNCINFRA.NS", "name": "PNC Infratech", "sector": "Infrastructure", "mcap": "Mid"},
        {"symbol": "ASHOKA.NS", "name": "Ashoka Buildcon", "sector": "Infrastructure", "mcap": "Small"},
        {"symbol": "GPPL.NS", "name": "Gujarat Pipavav Port", "sector": "Infrastructure", "mcap": "Small"},
        {"symbol": "COCHINSHIP.NS", "name": "Cochin Shipyard", "sector": "Infrastructure", "mcap": "Large"},
        {"symbol": "GODREJPROP.NS", "name": "Godrej Properties", "sector": "Real Estate", "mcap": "Large"},
        {"symbol": "OBEROIRLTY.NS", "name": "Oberoi Realty", "sector": "Real Estate", "mcap": "Large"},
        {"symbol": "PRESTIGE.NS", "name": "Prestige Estates", "sector": "Real Estate", "mcap": "Large"},
        {"symbol": "BRIGADE.NS", "name": "Brigade Enterprises", "sector": "Real Estate", "mcap": "Mid"},
        {"symbol": "PHOENIXLTD.NS", "name": "Phoenix Mills", "sector": "Real Estate", "mcap": "Large"},
        {"symbol": "SOBHA.NS", "name": "Sobha", "sector": "Real Estate", "mcap": "Mid"},
        {"symbol": "SUNTECK.NS", "name": "Sunteck Realty", "sector": "Real Estate", "mcap": "Mid"},
        {"symbol": "LODHA.NS", "name": "Macrotech Developers", "sector": "Real Estate", "mcap": "Large"},
        {"symbol": "MAHLIFE.NS", "name": "Mahindra Lifespace", "sector": "Real Estate", "mcap": "Mid"},
        {"symbol": "PURVA.NS", "name": "Puravankara", "sector": "Real Estate", "mcap": "Small"},
        {"symbol": "RAYMOND.NS", "name": "Raymond", "sector": "Textiles", "mcap": "Mid"},
        {"symbol": "GMRINFRA.NS", "name": "GMR Airports Infrastructure", "sector": "Infrastructure", "mcap": "Large"},
        {"symbol": "ADANIPORTS.NS", "name": "Adani Ports", "sector": "Infrastructure", "mcap": "Large"},
        {"symbol": "JSWINFRA.NS", "name": "JSW Infrastructure", "sector": "Infrastructure", "mcap": "Large"},
        {"symbol": "AHLUCONT.NS", "name": "Ahluwalia Contracts", "sector": "Infrastructure", "mcap": "Small"},
        {"symbol": "CAPACITE.NS", "name": "Capacite Infraprojects", "sector": "Infrastructure", "mcap": "Small"},
        {"symbol": "RITES.NS", "name": "RITES", "sector": "Infrastructure", "mcap": "Mid"},
        {"symbol": "RAILTEL.NS", "name": "Railtel Corporation", "sector": "Telecom", "mcap": "Mid"},
        {"symbol": "GRSE.NS", "name": "Garden Reach Shipbuilders", "sector": "Defence", "mcap": "Mid"},
        {"symbol": "MAZAGON.NS", "name": "Mazagon Dock Shipbuilders", "sector": "Defence", "mcap": "Large"},
        {"symbol": "BDL.NS", "name": "Bharat Dynamics", "sector": "Defence", "mcap": "Large"},
    ],
    
    # ═══════════════════════════════════════════════════════════════════
    # CHEMICALS & FERTILIZERS (35 stocks)
    # ═══════════════════════════════════════════════════════════════════
    "CHEMICALS & FERTILIZERS": [
        {"symbol": "ATUL.NS", "name": "Atul", "sector": "Chemicals", "mcap": "Large"},
        {"symbol": "DEEPAKNI.NS", "name": "Deepak Nitrite", "sector": "Chemicals", "mcap": "Large"},
        {"symbol": "NAVINFLUOR.NS", "name": "Navin Fluorine", "sector": "Chemicals", "mcap": "Large"},
        {"symbol": "FLUOROCHEM.NS", "name": "Gujarat Fluorochemicals", "sector": "Chemicals", "mcap": "Large"},
        {"symbol": "CLEAN.NS", "name": "Clean Science", "sector": "Chemicals", "mcap": "Mid"},
        {"symbol": "FINEORG.NS", "name": "Fine Organic Industries", "sector": "Chemicals", "mcap": "Large"},
        {"symbol": "TATACHEM.NS", "name": "Tata Chemicals", "sector": "Chemicals", "mcap": "Large"},
        {"symbol": "AARTIIND.NS", "name": "Aarti Industries", "sector": "Chemicals", "mcap": "Large"},
        {"symbol": "BASF.NS", "name": "BASF India", "sector": "Chemicals", "mcap": "Mid"},
        {"symbol": "ALKYLAMINE.NS", "name": "Alkyl Amines", "sector": "Chemicals", "mcap": "Mid"},
        {"symbol": "GALAXYSURF.NS", "name": "Galaxy Surfactants", "sector": "Chemicals", "mcap": "Mid"},
        {"symbol": "VINATI.NS", "name": "Vinati Organics", "sector": "Chemicals", "mcap": "Large"},
        {"symbol": "NOCIL.NS", "name": "NOCIL", "sector": "Chemicals", "mcap": "Small"},
        {"symbol": "SUMICHEM.NS", "name": "Sumitomo Chemical", "sector": "Chemicals", "mcap": "Mid"},
        {"symbol": "UPL.NS", "name": "UPL", "sector": "Agrochemicals", "mcap": "Large"},
        {"symbol": "RALLIS.NS", "name": "Rallis India", "sector": "Agrochemicals", "mcap": "Mid"},
        {"symbol": "BAYERCROP.NS", "name": "Bayer CropScience", "sector": "Agrochemicals", "mcap": "Large"},
        {"symbol": "DHANUKA.NS", "name": "Dhanuka Agritech", "sector": "Agrochemicals", "mcap": "Small"},
        {"symbol": "COROMANDEL.NS", "name": "Coromandel International", "sector": "Fertilizers", "mcap": "Large"},
        {"symbol": "CHAMBLFERT.NS", "name": "Chambal Fertilisers", "sector": "Fertilizers", "mcap": "Mid"},
        {"symbol": "GNFC.NS", "name": "Gujarat Narmada Valley", "sector": "Fertilizers", "mcap": "Mid"},
        {"symbol": "GSFC.NS", "name": "Gujarat State Fertilizers", "sector": "Fertilizers", "mcap": "Mid"},
        {"symbol": "NFL.NS", "name": "National Fertilizers", "sector": "Fertilizers", "mcap": "Small"},
        {"symbol": "RCF.NS", "name": "Rashtriya Chemicals", "sector": "Fertilizers", "mcap": "Mid"},
        {"symbol": "FACT.NS", "name": "Fertilisers and Chemicals Travancore", "sector": "Fertilizers", "mcap": "Small"},
        {"symbol": "DEEPAKFERT.NS", "name": "Deepak Fertilisers", "sector": "Fertilizers", "mcap": "Mid"},
        {"symbol": "ANURAS.NS", "name": "Anupam Rasayan", "sector": "Chemicals", "mcap": "Mid"},
        {"symbol": "NEOGEN.NS", "name": "Neogen Chemicals", "sector": "Chemicals", "mcap": "Mid"},
        {"symbol": "AETHER.NS", "name": "Aether Industries", "sector": "Chemicals", "mcap": "Mid"},
        {"symbol": "TATVA.NS", "name": "Tatva Chintan Pharma", "sector": "Chemicals", "mcap": "Small"},
        {"symbol": "LXCHEM.NS", "name": "Laxmi Organic Industries", "sector": "Chemicals", "mcap": "Mid"},
        {"symbol": "CHEMCON.NS", "name": "Chemcon Speciality", "sector": "Chemicals", "mcap": "Small"},
        {"symbol": "ROSSARI.NS", "name": "Rossari Biotech", "sector": "Chemicals", "mcap": "Mid"},
        {"symbol": "ARCHIDPLY.NS", "name": "Archidply Industries", "sector": "Building Materials", "mcap": "Small"},
        {"symbol": "SUDARSCHEM.NS", "name": "Sudarshan Chemical", "sector": "Chemicals", "mcap": "Mid"},
    ],
    
    # ═══════════════════════════════════════════════════════════════════
    # CEMENT & BUILDING MATERIALS (20 stocks)
    # ═══════════════════════════════════════════════════════════════════
    "CEMENT & BUILDING MATERIALS": [
        {"symbol": "SHREECEM.NS", "name": "Shree Cement", "sector": "Cement", "mcap": "Large"},
        {"symbol": "ACC.NS", "name": "ACC", "sector": "Cement", "mcap": "Large"},
        {"symbol": "DALBHARAT.NS", "name": "Dalmia Bharat", "sector": "Cement", "mcap": "Large"},
        {"symbol": "RAMCOCEM.NS", "name": "Ramco Cements", "sector": "Cement", "mcap": "Mid"},
        {"symbol": "JKCEMENT.NS", "name": "JK Cement", "sector": "Cement", "mcap": "Large"},
        {"symbol": "BIRLACORPN.NS", "name": "Birla Corporation", "sector": "Cement", "mcap": "Mid"},
        {"symbol": "HEIDELBERG.NS", "name": "HeidelbergCement India", "sector": "Cement", "mcap": "Mid"},
        {"symbol": "INDIACEM.NS", "name": "India Cements", "sector": "Cement", "mcap": "Small"},
        {"symbol": "PRSMJOHNSN.NS", "name": "Prism Johnson", "sector": "Cement", "mcap": "Small"},
        {"symbol": "ORIENTCEM.NS", "name": "Orient Cement", "sector": "Cement", "mcap": "Small"},
        {"symbol": "JKLAKSHMI.NS", "name": "JK Lakshmi Cement", "sector": "Cement", "mcap": "Mid"},
        {"symbol": "STARCEMENT.NS", "name": "Star Cement", "sector": "Cement", "mcap": "Small"},
        {"symbol": "NUVOCO.NS", "name": "Nuvoco Vistas", "sector": "Cement", "mcap": "Mid"},
        {"symbol": "SAGCEM.NS", "name": "Sagar Cements", "sector": "Cement", "mcap": "Small"},
        {"symbol": "KESORAMIND.NS", "name": "Kesoram Industries", "sector": "Cement", "mcap": "Small"},
        {"symbol": "HEIDELBERG.NS", "name": "HeidelbergCement India", "sector": "Cement", "mcap": "Mid"},
        {"symbol": "DECCAN.NS", "name": "Deccan Cements", "sector": "Cement", "mcap": "Small"},
        {"symbol": "GREENPLY.NS", "name": "Greenply Industries", "sector": "Building Materials", "mcap": "Small"},
        {"symbol": "CENTURYPLY.NS", "name": "Century Plyboards", "sector": "Building Materials", "mcap": "Mid"},
        {"symbol": "ASTRAL.NS", "name": "Astral", "sector": "Building Materials", "mcap": "Large"},
    ],
    
    # ═══════════════════════════════════════════════════════════════════
    # CAPITAL GOODS & ENGINEERING (35 stocks)
    # ═══════════════════════════════════════════════════════════════════
    "CAPITAL GOODS & ENGINEERING": [
        {"symbol": "THERMAX.NS", "name": "Thermax", "sector": "Capital Goods", "mcap": "Large"},
        {"symbol": "CUMMINSIND.NS", "name": "Cummins India", "sector": "Capital Goods", "mcap": "Large"},
        {"symbol": "AIAENG.NS", "name": "AIA Engineering", "sector": "Capital Goods", "mcap": "Large"},
        {"symbol": "GRINDWELL.NS", "name": "Grindwell Norton", "sector": "Capital Goods", "mcap": "Mid"},
        {"symbol": "CARBORUNIV.NS", "name": "Carborundum Universal", "sector": "Capital Goods", "mcap": "Mid"},
        {"symbol": "ELGIEQUIP.NS", "name": "Elgi Equipments", "sector": "Capital Goods", "mcap": "Mid"},
        {"symbol": "BLUESTARCO.NS", "name": "Blue Star", "sector": "Consumer Durables", "mcap": "Large"},
        {"symbol": "VOLTAS.NS", "name": "Voltas", "sector": "Consumer Durables", "mcap": "Large"},
        {"symbol": "WHIRLPOOL.NS", "name": "Whirlpool of India", "sector": "Consumer Durables", "mcap": "Mid"},
        {"symbol": "CROMPTON.NS", "name": "Crompton Greaves Consumer", "sector": "Consumer Durables", "mcap": "Large"},
        {"symbol": "BAJAJELEC.NS", "name": "Bajaj Electricals", "sector": "Consumer Durables", "mcap": "Mid"},
        {"symbol": "ORIENTELEC.NS", "name": "Orient Electric", "sector": "Consumer Durables", "mcap": "Mid"},
        {"symbol": "VGUARD.NS", "name": "V-Guard Industries", "sector": "Consumer Durables", "mcap": "Mid"},
        {"symbol": "DIXON.NS", "name": "Dixon Technologies", "sector": "Consumer Electronics", "mcap": "Large"},
        {"symbol": "AMBER.NS", "name": "Amber Enterprises", "sector": "Consumer Electronics", "mcap": "Mid"},
        {"symbol": "KAYNES.NS", "name": "Kaynes Technology", "sector": "Electronics", "mcap": "Large"},
        {"symbol": "SYRMA.NS", "name": "Syrma SGS Technology", "sector": "Electronics", "mcap": "Mid"},
        {"symbol": "CGPOWER.NS", "name": "CG Power & Industrial", "sector": "Capital Goods", "mcap": "Large"},
        {"symbol": "TITAGARH.NS", "name": "Titagarh Rail Systems", "sector": "Capital Goods", "mcap": "Mid"},
        {"symbol": "TEXMACO.NS", "name": "Texmaco Rail", "sector": "Capital Goods", "mcap": "Small"},
        {"symbol": "BEML.NS", "name": "BEML", "sector": "Defence", "mcap": "Mid"},
        {"symbol": "BHEL.NS", "name": "BHEL", "sector": "Capital Goods", "mcap": "Large"},
        {"symbol": "TRITURBINE.NS", "name": "Triveni Turbine", "sector": "Capital Goods", "mcap": "Mid"},
        {"symbol": "KSB.NS", "name": "KSB", "sector": "Capital Goods", "mcap": "Mid"},
        {"symbol": "INGERRAND.NS", "name": "Ingersoll Rand India", "sector": "Capital Goods", "mcap": "Mid"},
        {"symbol": "SKF.NS", "name": "SKF India", "sector": "Capital Goods", "mcap": "Large"},
        {"symbol": "TIMKEN.NS", "name": "Timken India", "sector": "Capital Goods", "mcap": "Large"},
        {"symbol": "ELECON.NS", "name": "Elecon Engineering", "sector": "Capital Goods", "mcap": "Mid"},
        {"symbol": "FINCABLES.NS", "name": "Finolex Cables", "sector": "Capital Goods", "mcap": "Mid"},
        {"symbol": "KEI.NS", "name": "KEI Industries", "sector": "Capital Goods", "mcap": "Large"},
        {"symbol": "RRKABEL.NS", "name": "R R Kabel", "sector": "Capital Goods", "mcap": "Mid"},
        {"symbol": "PRICOL.NS", "name": "Pricol", "sector": "Auto Ancillary", "mcap": "Small"},
        {"symbol": "SKIPPER.NS", "name": "Skipper", "sector": "Capital Goods", "mcap": "Small"},
        {"symbol": "SWSOLAR.NS", "name": "Sterling and Wilson Solar", "sector": "Capital Goods", "mcap": "Mid"},
        {"symbol": "HLEGLAS.NS", "name": "HLE Glascoat", "sector": "Capital Goods", "mcap": "Small"},
    ],
    
    # ═══════════════════════════════════════════════════════════════════
    # DEFENCE (15 stocks)
    # ═══════════════════════════════════════════════════════════════════
    "DEFENCE": [
        {"symbol": "HAL.NS", "name": "Hindustan Aeronautics", "sector": "Defence", "mcap": "Large"},
        {"symbol": "BEL.NS", "name": "Bharat Electronics", "sector": "Defence", "mcap": "Large"},
        {"symbol": "BDL.NS", "name": "Bharat Dynamics", "sector": "Defence", "mcap": "Large"},
        {"symbol": "BEML.NS", "name": "BEML", "sector": "Defence", "mcap": "Mid"},
        {"symbol": "MIDHANI.NS", "name": "Mishra Dhatu Nigam", "sector": "Defence", "mcap": "Mid"},
        {"symbol": "GRSE.NS", "name": "Garden Reach Shipbuilders", "sector": "Defence", "mcap": "Mid"},
        {"symbol": "MAZAGON.NS", "name": "Mazagon Dock Shipbuilders", "sector": "Defence", "mcap": "Large"},
        {"symbol": "DATAPATTNS.NS", "name": "Data Patterns", "sector": "Defence", "mcap": "Mid"},
        {"symbol": "PARAS.NS", "name": "Paras Defence", "sector": "Defence", "mcap": "Small"},
        {"symbol": "ZENTEC.NS", "name": "Zen Technologies", "sector": "Defence", "mcap": "Mid"},
        {"symbol": "COCHINSHIP.NS", "name": "Cochin Shipyard", "sector": "Defence", "mcap": "Large"},
        {"symbol": "SOLARINDS.NS", "name": "Solar Industries", "sector": "Defence", "mcap": "Large"},
        {"symbol": "ASTRA.NS", "name": "Astra Microwave", "sector": "Defence", "mcap": "Mid"},
        {"symbol": "IDEAFORGE.NS", "name": "ideaForge Technology", "sector": "Defence", "mcap": "Small"},
        {"symbol": "DCX.NS", "name": "DCX Systems", "sector": "Defence", "mcap": "Small"},
    ],
    
    # ═══════════════════════════════════════════════════════════════════
    # TEXTILES & APPAREL (20 stocks)
    # ═══════════════════════════════════════════════════════════════════
    "TEXTILES & APPAREL": [
        {"symbol": "PAGEIND.NS", "name": "Page Industries", "sector": "Textiles", "mcap": "Large"},
        {"symbol": "ARVIND.NS", "name": "Arvind", "sector": "Textiles", "mcap": "Mid"},
        {"symbol": "TRIDENT.NS", "name": "Trident", "sector": "Textiles", "mcap": "Mid"},
        {"symbol": "WELSPUNIND.NS", "name": "Welspun India", "sector": "Textiles", "mcap": "Mid"},
        {"symbol": "KPRMILL.NS", "name": "K.P.R. Mill", "sector": "Textiles", "mcap": "Mid"},
        {"symbol": "GOKEX.NS", "name": "Gokaldas Exports", "sector": "Textiles", "mcap": "Mid"},
        {"symbol": "VARDHMAN.NS", "name": "Vardhman Textiles", "sector": "Textiles", "mcap": "Mid"},
        {"symbol": "LAXMIMACH.NS", "name": "Lakshmi Machine Works", "sector": "Capital Goods", "mcap": "Mid"},
        {"symbol": "SOMANYCERA.NS", "name": "Somany Ceramics", "sector": "Building Materials", "mcap": "Small"},
        {"symbol": "CENTURYTEX.NS", "name": "Century Textiles", "sector": "Textiles", "mcap": "Mid"},
        {"symbol": "KITEX.NS", "name": "Kitex Garments", "sector": "Textiles", "mcap": "Small"},
        {"symbol": "INDIANCARD.NS", "name": "Indian Card Clothing", "sector": "Textiles", "mcap": "Small"},
        {"symbol": "MAFANG.NS", "name": "Mafatlal Industries", "sector": "Textiles", "mcap": "Small"},
        {"symbol": "MORARJEE.NS", "name": "Morarjee Textiles", "sector": "Textiles", "mcap": "Small"},
        {"symbol": "NITIRAJ.NS", "name": "Nitiraj Engineers", "sector": "Capital Goods", "mcap": "Small"},
        {"symbol": "SPYL.NS", "name": "SPL Industries", "sector": "Textiles", "mcap": "Small"},
        {"symbol": "PREMEXPLN.NS", "name": "Premier Explosives", "sector": "Defence", "mcap": "Small"},
        {"symbol": "RAYMOND.NS", "name": "Raymond", "sector": "Textiles", "mcap": "Mid"},
        {"symbol": "PGEL.NS", "name": "PG Electroplast", "sector": "Electronics", "mcap": "Mid"},
        {"symbol": "BSLTD.NS", "name": "BSL", "sector": "Textiles", "mcap": "Small"},
    ],
    
    # ═══════════════════════════════════════════════════════════════════
    # RETAIL & E-COMMERCE (20 stocks)
    # ═══════════════════════════════════════════════════════════════════
    "RETAIL & E-COMMERCE": [
        {"symbol": "DMART.NS", "name": "Avenue Supermarts", "sector": "Retail", "mcap": "Large"},
        {"symbol": "TRENT.NS", "name": "Trent", "sector": "Retail", "mcap": "Large"},
        {"symbol": "SHOPERSTOP.NS", "name": "Shoppers Stop", "sector": "Retail", "mcap": "Mid"},
        {"symbol": "VMART.NS", "name": "V-Mart Retail", "sector": "Retail", "mcap": "Small"},
        {"symbol": "ABFRL.NS", "name": "Aditya Birla Fashion", "sector": "Retail", "mcap": "Mid"},
        {"symbol": "BATA.NS", "name": "Bata India", "sector": "Retail", "mcap": "Mid"},
        {"symbol": "RELAXO.NS", "name": "Relaxo Footwears", "sector": "Retail", "mcap": "Mid"},
        {"symbol": "METROBRAND.NS", "name": "Metro Brands", "sector": "Retail", "mcap": "Mid"},
        {"symbol": "CAMPUS.NS", "name": "Campus Activewear", "sector": "Retail", "mcap": "Mid"},
        {"symbol": "ZOMATO.NS", "name": "Zomato", "sector": "Internet", "mcap": "Large"},
        {"symbol": "NYKAA.NS", "name": "FSN E-Commerce (Nykaa)", "sector": "Internet", "mcap": "Large"},
        {"symbol": "POLICYBZR.NS", "name": "PB Fintech", "sector": "Fintech", "mcap": "Large"},
        {"symbol": "CARTRADE.NS", "name": "CarTrade Tech", "sector": "Internet", "mcap": "Small"},
        {"symbol": "EASEMYTRIP.NS", "name": "Easy Trip Planners", "sector": "Internet", "mcap": "Small"},
        {"symbol": "RATEGAIN.NS", "name": "RateGain Travel", "sector": "Internet", "mcap": "Mid"},
        {"symbol": "MAPMYINDIA.NS", "name": "CE Info Systems", "sector": "Internet", "mcap": "Mid"},
        {"symbol": "DELHIVERY.NS", "name": "Delhivery", "sector": "Logistics", "mcap": "Large"},
        {"symbol": "INDIAMART.NS", "name": "IndiaMART InterMESH", "sector": "Internet", "mcap": "Mid"},
        {"symbol": "JUSTDIAL.NS", "name": "Just Dial", "sector": "Internet", "mcap": "Mid"},
        {"symbol": "DREAMFOLK.NS", "name": "Dreamfolks Services", "sector": "Services", "mcap": "Small"},
    ],
    
    # ═══════════════════════════════════════════════════════════════════
    # LOGISTICS & TRANSPORTATION (15 stocks)
    # ═══════════════════════════════════════════════════════════════════
    "LOGISTICS & TRANSPORTATION": [
        {"symbol": "CONCOR.NS", "name": "Container Corporation", "sector": "Logistics", "mcap": "Large"},
        {"symbol": "BLUEDART.NS", "name": "Blue Dart Express", "sector": "Logistics", "mcap": "Mid"},
        {"symbol": "TCI.NS", "name": "Transport Corporation of India", "sector": "Logistics", "mcap": "Mid"},
        {"symbol": "MAHSEAMLES.NS", "name": "Maharashtra Seamless", "sector": "Logistics", "mcap": "Mid"},
        {"symbol": "GATEWAY.NS", "name": "Gateway Distriparks", "sector": "Logistics", "mcap": "Small"},
        {"symbol": "ALLCARGO.NS", "name": "Allcargo Logistics", "sector": "Logistics", "mcap": "Mid"},
        {"symbol": "AEGISCHEM.NS", "name": "Aegis Logistics", "sector": "Logistics", "mcap": "Mid"},
        {"symbol": "INDIGO.NS", "name": "InterGlobe Aviation", "sector": "Aviation", "mcap": "Large"},
        {"symbol": "SPICEJET.NS", "name": "SpiceJet", "sector": "Aviation", "mcap": "Small"},
        {"symbol": "MAHLOG.NS", "name": "Mahindra Logistics", "sector": "Logistics", "mcap": "Small"},
        {"symbol": "DELHIVERY.NS", "name": "Delhivery", "sector": "Logistics", "mcap": "Large"},
        {"symbol": "XPRSINDIA.NS", "name": "Xpressbees Logistics", "sector": "Logistics", "mcap": "Mid"},
        {"symbol": "VRL.NS", "name": "VRL Logistics", "sector": "Logistics", "mcap": "Mid"},
        {"symbol": "GATI.NS", "name": "Gati", "sector": "Logistics", "mcap": "Small"},
        {"symbol": "SNOWMAN.NS", "name": "Snowman Logistics", "sector": "Logistics", "mcap": "Small"},
    ],
    
    # ═══════════════════════════════════════════════════════════════════
    # MEDIA & ENTERTAINMENT (15 stocks)
    # ═══════════════════════════════════════════════════════════════════
    "MEDIA & ENTERTAINMENT": [
        {"symbol": "SUNTV.NS", "name": "Sun TV Network", "sector": "Media", "mcap": "Large"},
        {"symbol": "ZEEL.NS", "name": "Zee Entertainment", "sector": "Media", "mcap": "Mid"},
        {"symbol": "PVRINOX.NS", "name": "PVR Inox", "sector": "Media", "mcap": "Mid"},
        {"symbol": "NETWORK18.NS", "name": "Network18 Media", "sector": "Media", "mcap": "Mid"},
        {"symbol": "TV18BRDCST.NS", "name": "TV18 Broadcast", "sector": "Media", "mcap": "Small"},
        {"symbol": "SAREGAMA.NS", "name": "Saregama India", "sector": "Media", "mcap": "Mid"},
        {"symbol": "TIPS.NS", "name": "Tips Industries", "sector": "Media", "mcap": "Small"},
        {"symbol": "NAVNETEDUL.NS", "name": "Navneet Education", "sector": "Education", "mcap": "Small"},
        {"symbol": "NAZARA.NS", "name": "Nazara Technologies", "sector": "Gaming", "mcap": "Small"},
        {"symbol": "DIGICONT.NS", "name": "Digi Content", "sector": "Media", "mcap": "Small"},
        {"symbol": "BALAJITELE.NS", "name": "Balaji Telefilms", "sector": "Media", "mcap": "Small"},
        {"symbol": "HATHWAY.NS", "name": "Hathway Cable", "sector": "Media", "mcap": "Small"},
        {"symbol": "DEN.NS", "name": "DEN Networks", "sector": "Media", "mcap": "Small"},
        {"symbol": "DB.NS", "name": "DB Corp", "sector": "Media", "mcap": "Small"},
        {"symbol": "JAGRAN.NS", "name": "Jagran Prakashan", "sector": "Media", "mcap": "Small"},
    ],
    
    # ═══════════════════════════════════════════════════════════════════
    # HOTELS & TOURISM (10 stocks)
    # ═══════════════════════════════════════════════════════════════════
    "HOTELS & TOURISM": [
        {"symbol": "INDHOTEL.NS", "name": "Indian Hotels", "sector": "Hotels", "mcap": "Large"},
        {"symbol": "LEMONTREE.NS", "name": "Lemon Tree Hotels", "sector": "Hotels", "mcap": "Mid"},
        {"symbol": "CHALET.NS", "name": "Chalet Hotels", "sector": "Hotels", "mcap": "Mid"},
        {"symbol": "EIHOTEL.NS", "name": "EIH", "sector": "Hotels", "mcap": "Mid"},
        {"symbol": "IRCTC.NS", "name": "IRCTC", "sector": "Tourism", "mcap": "Mid"},
        {"symbol": "THOMASCOOK.NS", "name": "Thomas Cook India", "sector": "Tourism", "mcap": "Small"},
        {"symbol": "MAHINDCIE.NS", "name": "Mahindra CIE", "sector": "Auto Ancillary", "mcap": "Mid"},
        {"symbol": "TAJGVK.NS", "name": "Taj GVK Hotels", "sector": "Hotels", "mcap": "Small"},
        {"symbol": "ORIENTHOT.NS", "name": "Oriental Hotels", "sector": "Hotels", "mcap": "Small"},
        {"symbol": "ROYALORCHD.NS", "name": "Royal Orchid Hotels", "sector": "Hotels", "mcap": "Small"},
    ],
    
    # ═══════════════════════════════════════════════════════════════════
    # INSURANCE (10 stocks)
    # ═══════════════════════════════════════════════════════════════════
    "INSURANCE": [
        {"symbol": "LICI.NS", "name": "Life Insurance Corporation", "sector": "Insurance", "mcap": "Large"},
        {"symbol": "SBILIFE.NS", "name": "SBI Life Insurance", "sector": "Insurance", "mcap": "Large"},
        {"symbol": "HDFCLIFE.NS", "name": "HDFC Life Insurance", "sector": "Insurance", "mcap": "Large"},
        {"symbol": "ICICIPRULI.NS", "name": "ICICI Prudential Life", "sector": "Insurance", "mcap": "Large"},
        {"symbol": "ICICIGI.NS", "name": "ICICI Lombard", "sector": "Insurance", "mcap": "Large"},
        {"symbol": "BAJAJFINSV.NS", "name": "Bajaj Finserv", "sector": "Insurance", "mcap": "Large"},
        {"symbol": "MAXLIFE.NS", "name": "Max Financial Services", "sector": "Insurance", "mcap": "Large"},
        {"symbol": "STARHEALTH.NS", "name": "Star Health Insurance", "sector": "Insurance", "mcap": "Mid"},
        {"symbol": "GICRE.NS", "name": "General Insurance Corporation", "sector": "Insurance", "mcap": "Mid"},
        {"symbol": "NIACL.NS", "name": "New India Assurance", "sector": "Insurance", "mcap": "Mid"},
    ],
}

# Flat list of all symbols for easy access
def get_all_stocks():
    """Get all Nifty 500 stocks as a flat list."""
    all_stocks = []
    for category, stocks in NIFTY_500_STOCKS.items():
        for stock in stocks:
            stock_copy = stock.copy()
            stock_copy['category'] = category
            all_stocks.append(stock_copy)
    return all_stocks

def get_all_symbols():
    """Get just the ticker symbols."""
    return [s['symbol'] for s in get_all_stocks()]

def get_all_sectors():
    """Get unique sectors."""
    all_stocks = get_all_stocks()
    return list(set(s['sector'] for s in all_stocks))

def get_all_categories():
    """Get all categories."""
    return list(NIFTY_500_STOCKS.keys())

def search_stocks(query: str):
    """Search stocks by name or symbol."""
    query = query.lower()
    all_stocks = get_all_stocks()
    return [s for s in all_stocks if query in s['symbol'].lower() or query in s['name'].lower()]

def get_stocks_by_sector(sector: str):
    """Get stocks filtered by sector."""
    all_stocks = get_all_stocks()
    return [s for s in all_stocks if s['sector'].lower() == sector.lower()]

# Index symbols
INDICES = {
    "NIFTY 50": "^NSEI",
    "NIFTY BANK": "^NSEBANK",
    "NIFTY IT": "^CNXIT",
    "NIFTY NEXT 50": "^NSMIDCP",
    "INDIA VIX": "^INDIAVIX",
    "NIFTY PHARMA": "^CNXPHARMA",
    "NIFTY AUTO": "^CNXAUTO",
    "NIFTY METAL": "^CNXMETAL",
    "NIFTY REALTY": "^CNXREALTY",
    "NIFTY ENERGY": "^CNXENERGY",
    "NIFTY FMCG": "^CNXFMCG",
    "NIFTY PSU BANK": "^CNXPSUBANK",
    "NIFTY FINANCIAL SERVICES": "^CNXFIN",
    "NIFTY MIDCAP 50": "^NSEMDCP50",
    "NIFTY SMALLCAP 50": "^NSESMLCP50",
}

if __name__ == "__main__":
    all_stocks = get_all_stocks()
    print(f"Total stocks in database: {len(all_stocks)}")
    print(f"Total sectors: {len(get_all_sectors())}")
    print(f"Categories: {get_all_categories()}")
    print(f"\nStocks per category:")
    for cat, stocks in NIFTY_500_STOCKS.items():
        print(f"  {cat}: {len(stocks)}")
