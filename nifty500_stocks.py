"""
NIFTY 500 STOCKS DATABASE v7.0
================================
Updated: January 2026 (from NSE official website)
Total Stocks: 501
"""

from typing import List, Dict

NIFTY_500_STOCKS = {
    '360ONE.NS': {
        'name': '360 ONE WAM Ltd.',
        'sector': 'Financial Services',
        'symbol': '360ONE'
    },
    '3MINDIA.NS': {
        'name': '3M India Ltd.',
        'sector': 'Diversified',
        'symbol': '3MINDIA'
    },
    'ABB.NS': {
        'name': 'ABB India Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'ABB'
    },
    'ACC.NS': {
        'name': 'ACC Ltd.',
        'sector': 'Construction Materials',
        'symbol': 'ACC'
    },
    'ACMESOLAR.NS': {
        'name': 'ACME Solar Holdings Ltd.',
        'sector': 'Power',
        'symbol': 'ACMESOLAR'
    },
    'AIAENG.NS': {
        'name': 'AIA Engineering Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'AIAENG'
    },
    'APLAPOLLO.NS': {
        'name': 'APL Apollo Tubes Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'APLAPOLLO'
    },
    'AUBANK.NS': {
        'name': 'AU Small Finance Bank Ltd.',
        'sector': 'Financial Services',
        'symbol': 'AUBANK'
    },
    'AWL.NS': {
        'name': 'AWL Agri Business Ltd.',
        'sector': 'Fast Moving Consumer Goods',
        'symbol': 'AWL'
    },
    'AADHARHFC.NS': {
        'name': 'Aadhar Housing Finance Ltd.',
        'sector': 'Financial Services',
        'symbol': 'AADHARHFC'
    },
    'AARTIIND.NS': {
        'name': 'Aarti Industries Ltd.',
        'sector': 'Chemicals',
        'symbol': 'AARTIIND'
    },
    'AAVAS.NS': {
        'name': 'Aavas Financiers Ltd.',
        'sector': 'Financial Services',
        'symbol': 'AAVAS'
    },
    'ABBOTINDIA.NS': {
        'name': 'Abbott India Ltd.',
        'sector': 'Healthcare',
        'symbol': 'ABBOTINDIA'
    },
    'ACE.NS': {
        'name': 'Action Construction Equipment Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'ACE'
    },
    'ADANIENSOL.NS': {
        'name': 'Adani Energy Solutions Ltd.',
        'sector': 'Power',
        'symbol': 'ADANIENSOL'
    },
    'ADANIENT.NS': {
        'name': 'Adani Enterprises Ltd.',
        'sector': 'Metals & Mining',
        'symbol': 'ADANIENT'
    },
    'ADANIGREEN.NS': {
        'name': 'Adani Green Energy Ltd.',
        'sector': 'Power',
        'symbol': 'ADANIGREEN'
    },
    'ADANIPORTS.NS': {
        'name': 'Adani Ports and Special Economic Zone Ltd.',
        'sector': 'Services',
        'symbol': 'ADANIPORTS'
    },
    'ADANIPOWER.NS': {
        'name': 'Adani Power Ltd.',
        'sector': 'Power',
        'symbol': 'ADANIPOWER'
    },
    'ATGL.NS': {
        'name': 'Adani Total Gas Ltd.',
        'sector': 'Oil Gas & Consumable Fuels',
        'symbol': 'ATGL'
    },
    'ABCAPITAL.NS': {
        'name': 'Aditya Birla Capital Ltd.',
        'sector': 'Financial Services',
        'symbol': 'ABCAPITAL'
    },
    'ABFRL.NS': {
        'name': 'Aditya Birla Fashion and Retail Ltd.',
        'sector': 'Consumer Services',
        'symbol': 'ABFRL'
    },
    'ABLBL.NS': {
        'name': 'Aditya Birla Lifestyle Brands Ltd.',
        'sector': 'Consumer Services',
        'symbol': 'ABLBL'
    },
    'ABREL.NS': {
        'name': 'Aditya Birla Real Estate Ltd.',
        'sector': 'Forest Materials',
        'symbol': 'ABREL'
    },
    'ABSLAMC.NS': {
        'name': 'Aditya Birla Sun Life AMC Ltd.',
        'sector': 'Financial Services',
        'symbol': 'ABSLAMC'
    },
    'AEGISLOG.NS': {
        'name': 'Aegis Logistics Ltd.',
        'sector': 'Oil Gas & Consumable Fuels',
        'symbol': 'AEGISLOG'
    },
    'AEGISVOPAK.NS': {
        'name': 'Aegis Vopak Terminals Ltd.',
        'sector': 'Oil Gas & Consumable Fuels',
        'symbol': 'AEGISVOPAK'
    },
    'AFCONS.NS': {
        'name': 'Afcons Infrastructure Ltd.',
        'sector': 'Construction',
        'symbol': 'AFCONS'
    },
    'AFFLE.NS': {
        'name': 'Affle 3i Ltd.',
        'sector': 'Information Technology',
        'symbol': 'AFFLE'
    },
    'AJANTPHARM.NS': {
        'name': 'Ajanta Pharmaceuticals Ltd.',
        'sector': 'Healthcare',
        'symbol': 'AJANTPHARM'
    },
    'AKUMS.NS': {
        'name': 'Akums Drugs and Pharmaceuticals Ltd.',
        'sector': 'Healthcare',
        'symbol': 'AKUMS'
    },
    'AKZOINDIA.NS': {
        'name': 'Akzo Nobel India Ltd.',
        'sector': 'Consumer Durables',
        'symbol': 'AKZOINDIA'
    },
    'APLLTD.NS': {
        'name': 'Alembic Pharmaceuticals Ltd.',
        'sector': 'Healthcare',
        'symbol': 'APLLTD'
    },
    'ALKEM.NS': {
        'name': 'Alkem Laboratories Ltd.',
        'sector': 'Healthcare',
        'symbol': 'ALKEM'
    },
    'ALKYLAMINE.NS': {
        'name': 'Alkyl Amines Chemicals Ltd.',
        'sector': 'Chemicals',
        'symbol': 'ALKYLAMINE'
    },
    'ALOKINDS.NS': {
        'name': 'Alok Industries Ltd.',
        'sector': 'Textiles',
        'symbol': 'ALOKINDS'
    },
    'ARE&M.NS': {
        'name': 'Amara Raja Energy & Mobility Ltd.',
        'sector': 'Automobile and Auto Components',
        'symbol': 'ARE&M'
    },
    'AMBER.NS': {
        'name': 'Amber Enterprises India Ltd.',
        'sector': 'Consumer Durables',
        'symbol': 'AMBER'
    },
    'AMBUJACEM.NS': {
        'name': 'Ambuja Cements Ltd.',
        'sector': 'Construction Materials',
        'symbol': 'AMBUJACEM'
    },
    'ANANDRATHI.NS': {
        'name': 'Anand Rathi Wealth Ltd.',
        'sector': 'Financial Services',
        'symbol': 'ANANDRATHI'
    },
    'ANANTRAJ.NS': {
        'name': 'Anant Raj Ltd.',
        'sector': 'Realty',
        'symbol': 'ANANTRAJ'
    },
    'ANGELONE.NS': {
        'name': 'Angel One Ltd.',
        'sector': 'Financial Services',
        'symbol': 'ANGELONE'
    },
    'APARINDS.NS': {
        'name': 'Apar Industries Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'APARINDS'
    },
    'APOLLOHOSP.NS': {
        'name': 'Apollo Hospitals Enterprise Ltd.',
        'sector': 'Healthcare',
        'symbol': 'APOLLOHOSP'
    },
    'APOLLOTYRE.NS': {
        'name': 'Apollo Tyres Ltd.',
        'sector': 'Automobile and Auto Components',
        'symbol': 'APOLLOTYRE'
    },
    'APTUS.NS': {
        'name': 'Aptus Value Housing Finance India Ltd.',
        'sector': 'Financial Services',
        'symbol': 'APTUS'
    },
    'ASAHIINDIA.NS': {
        'name': 'Asahi India Glass Ltd.',
        'sector': 'Automobile and Auto Components',
        'symbol': 'ASAHIINDIA'
    },
    'ASHOKLEY.NS': {
        'name': 'Ashok Leyland Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'ASHOKLEY'
    },
    'ASIANPAINT.NS': {
        'name': 'Asian Paints Ltd.',
        'sector': 'Consumer Durables',
        'symbol': 'ASIANPAINT'
    },
    'ASTERDM.NS': {
        'name': 'Aster DM Healthcare Ltd.',
        'sector': 'Healthcare',
        'symbol': 'ASTERDM'
    },
    'ASTRAZEN.NS': {
        'name': 'AstraZenca Pharma India Ltd.',
        'sector': 'Healthcare',
        'symbol': 'ASTRAZEN'
    },
    'ASTRAL.NS': {
        'name': 'Astral Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'ASTRAL'
    },
    'ATHERENERG.NS': {
        'name': 'Ather Energy Ltd.',
        'sector': 'Automobile and Auto Components',
        'symbol': 'ATHERENERG'
    },
    'ATUL.NS': {
        'name': 'Atul Ltd.',
        'sector': 'Chemicals',
        'symbol': 'ATUL'
    },
    'AUROPHARMA.NS': {
        'name': 'Aurobindo Pharma Ltd.',
        'sector': 'Healthcare',
        'symbol': 'AUROPHARMA'
    },
    'AIIL.NS': {
        'name': 'Authum Investment & Infrastructure Ltd.',
        'sector': 'Financial Services',
        'symbol': 'AIIL'
    },
    'DMART.NS': {
        'name': 'Avenue Supermarts Ltd.',
        'sector': 'Consumer Services',
        'symbol': 'DMART'
    },
    'AXISBANK.NS': {
        'name': 'Axis Bank Ltd.',
        'sector': 'Financial Services',
        'symbol': 'AXISBANK'
    },
    'BASF.NS': {
        'name': 'BASF India Ltd.',
        'sector': 'Chemicals',
        'symbol': 'BASF'
    },
    'BEML.NS': {
        'name': 'BEML Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'BEML'
    },
    'BLS.NS': {
        'name': 'BLS International Services Ltd.',
        'sector': 'Consumer Services',
        'symbol': 'BLS'
    },
    'BSE.NS': {
        'name': 'BSE Ltd.',
        'sector': 'Financial Services',
        'symbol': 'BSE'
    },
    'BAJAJ-AUTO.NS': {
        'name': 'Bajaj Auto Ltd.',
        'sector': 'Automobile and Auto Components',
        'symbol': 'BAJAJ-AUTO'
    },
    'BAJFINANCE.NS': {
        'name': 'Bajaj Finance Ltd.',
        'sector': 'Financial Services',
        'symbol': 'BAJFINANCE'
    },
    'BAJAJFINSV.NS': {
        'name': 'Bajaj Finserv Ltd.',
        'sector': 'Financial Services',
        'symbol': 'BAJAJFINSV'
    },
    'BAJAJHLDNG.NS': {
        'name': 'Bajaj Holdings & Investment Ltd.',
        'sector': 'Financial Services',
        'symbol': 'BAJAJHLDNG'
    },
    'BAJAJHFL.NS': {
        'name': 'Bajaj Housing Finance Ltd.',
        'sector': 'Financial Services',
        'symbol': 'BAJAJHFL'
    },
    'BALKRISIND.NS': {
        'name': 'Balkrishna Industries Ltd.',
        'sector': 'Automobile and Auto Components',
        'symbol': 'BALKRISIND'
    },
    'BALRAMCHIN.NS': {
        'name': 'Balrampur Chini Mills Ltd.',
        'sector': 'Fast Moving Consumer Goods',
        'symbol': 'BALRAMCHIN'
    },
    'BANDHANBNK.NS': {
        'name': 'Bandhan Bank Ltd.',
        'sector': 'Financial Services',
        'symbol': 'BANDHANBNK'
    },
    'BANKBARODA.NS': {
        'name': 'Bank of Baroda',
        'sector': 'Financial Services',
        'symbol': 'BANKBARODA'
    },
    'BANKINDIA.NS': {
        'name': 'Bank of India',
        'sector': 'Financial Services',
        'symbol': 'BANKINDIA'
    },
    'MAHABANK.NS': {
        'name': 'Bank of Maharashtra',
        'sector': 'Financial Services',
        'symbol': 'MAHABANK'
    },
    'BATAINDIA.NS': {
        'name': 'Bata India Ltd.',
        'sector': 'Consumer Durables',
        'symbol': 'BATAINDIA'
    },
    'BAYERCROP.NS': {
        'name': 'Bayer Cropscience Ltd.',
        'sector': 'Chemicals',
        'symbol': 'BAYERCROP'
    },
    'BERGEPAINT.NS': {
        'name': 'Berger Paints India Ltd.',
        'sector': 'Consumer Durables',
        'symbol': 'BERGEPAINT'
    },
    'BDL.NS': {
        'name': 'Bharat Dynamics Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'BDL'
    },
    'BEL.NS': {
        'name': 'Bharat Electronics Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'BEL'
    },
    'BHARATFORG.NS': {
        'name': 'Bharat Forge Ltd.',
        'sector': 'Automobile and Auto Components',
        'symbol': 'BHARATFORG'
    },
    'BHEL.NS': {
        'name': 'Bharat Heavy Electricals Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'BHEL'
    },
    'BPCL.NS': {
        'name': 'Bharat Petroleum Corporation Ltd.',
        'sector': 'Oil Gas & Consumable Fuels',
        'symbol': 'BPCL'
    },
    'BHARTIARTL.NS': {
        'name': 'Bharti Airtel Ltd.',
        'sector': 'Telecommunication',
        'symbol': 'BHARTIARTL'
    },
    'BHARTIHEXA.NS': {
        'name': 'Bharti Hexacom Ltd.',
        'sector': 'Telecommunication',
        'symbol': 'BHARTIHEXA'
    },
    'BIKAJI.NS': {
        'name': 'Bikaji Foods International Ltd.',
        'sector': 'Fast Moving Consumer Goods',
        'symbol': 'BIKAJI'
    },
    'BIOCON.NS': {
        'name': 'Biocon Ltd.',
        'sector': 'Healthcare',
        'symbol': 'BIOCON'
    },
    'BSOFT.NS': {
        'name': 'Birlasoft Ltd.',
        'sector': 'Information Technology',
        'symbol': 'BSOFT'
    },
    'BLUEDART.NS': {
        'name': 'Blue Dart Express Ltd.',
        'sector': 'Services',
        'symbol': 'BLUEDART'
    },
    'BLUEJET.NS': {
        'name': 'Blue Jet Healthcare Ltd.',
        'sector': 'Healthcare',
        'symbol': 'BLUEJET'
    },
    'BLUESTARCO.NS': {
        'name': 'Blue Star Ltd.',
        'sector': 'Consumer Durables',
        'symbol': 'BLUESTARCO'
    },
    'BBTC.NS': {
        'name': 'Bombay Burmah Trading Corporation Ltd.',
        'sector': 'Fast Moving Consumer Goods',
        'symbol': 'BBTC'
    },
    'BOSCHLTD.NS': {
        'name': 'Bosch Ltd.',
        'sector': 'Automobile and Auto Components',
        'symbol': 'BOSCHLTD'
    },
    'FIRSTCRY.NS': {
        'name': 'Brainbees Solutions Ltd.',
        'sector': 'Consumer Services',
        'symbol': 'FIRSTCRY'
    },
    'BRIGADE.NS': {
        'name': 'Brigade Enterprises Ltd.',
        'sector': 'Realty',
        'symbol': 'BRIGADE'
    },
    'BRITANNIA.NS': {
        'name': 'Britannia Industries Ltd.',
        'sector': 'Fast Moving Consumer Goods',
        'symbol': 'BRITANNIA'
    },
    'MAPMYINDIA.NS': {
        'name': 'C.E. Info Systems Ltd.',
        'sector': 'Information Technology',
        'symbol': 'MAPMYINDIA'
    },
    'CCL.NS': {
        'name': 'CCL Products (I) Ltd.',
        'sector': 'Fast Moving Consumer Goods',
        'symbol': 'CCL'
    },
    'CESC.NS': {
        'name': 'CESC Ltd.',
        'sector': 'Power',
        'symbol': 'CESC'
    },
    'CGPOWER.NS': {
        'name': 'CG Power and Industrial Solutions Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'CGPOWER'
    },
    'CRISIL.NS': {
        'name': 'CRISIL Ltd.',
        'sector': 'Financial Services',
        'symbol': 'CRISIL'
    },
    'CAMPUS.NS': {
        'name': 'Campus Activewear Ltd.',
        'sector': 'Consumer Durables',
        'symbol': 'CAMPUS'
    },
    'CANFINHOME.NS': {
        'name': 'Can Fin Homes Ltd.',
        'sector': 'Financial Services',
        'symbol': 'CANFINHOME'
    },
    'CANBK.NS': {
        'name': 'Canara Bank',
        'sector': 'Financial Services',
        'symbol': 'CANBK'
    },
    'CAPLIPOINT.NS': {
        'name': 'Caplin Point Laboratories Ltd.',
        'sector': 'Healthcare',
        'symbol': 'CAPLIPOINT'
    },
    'CGCL.NS': {
        'name': 'Capri Global Capital Ltd.',
        'sector': 'Financial Services',
        'symbol': 'CGCL'
    },
    'CARBORUNIV.NS': {
        'name': 'Carborundum Universal Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'CARBORUNIV'
    },
    'CASTROLIND.NS': {
        'name': 'Castrol India Ltd.',
        'sector': 'Oil Gas & Consumable Fuels',
        'symbol': 'CASTROLIND'
    },
    'CEATLTD.NS': {
        'name': 'Ceat Ltd.',
        'sector': 'Automobile and Auto Components',
        'symbol': 'CEATLTD'
    },
    'CENTRALBK.NS': {
        'name': 'Central Bank of India',
        'sector': 'Financial Services',
        'symbol': 'CENTRALBK'
    },
    'CDSL.NS': {
        'name': 'Central Depository Services (India) Ltd.',
        'sector': 'Financial Services',
        'symbol': 'CDSL'
    },
    'CENTURYPLY.NS': {
        'name': 'Century Plyboards (India) Ltd.',
        'sector': 'Consumer Durables',
        'symbol': 'CENTURYPLY'
    },
    'CERA.NS': {
        'name': 'Cera Sanitaryware Ltd',
        'sector': 'Consumer Durables',
        'symbol': 'CERA'
    },
    'CHALET.NS': {
        'name': 'Chalet Hotels Ltd.',
        'sector': 'Consumer Services',
        'symbol': 'CHALET'
    },
    'CHAMBLFERT.NS': {
        'name': 'Chambal Fertilizers & Chemicals Ltd.',
        'sector': 'Chemicals',
        'symbol': 'CHAMBLFERT'
    },
    'CHENNPETRO.NS': {
        'name': 'Chennai Petroleum Corporation Ltd.',
        'sector': 'Oil Gas & Consumable Fuels',
        'symbol': 'CHENNPETRO'
    },
    'CHOICEIN.NS': {
        'name': 'Choice International Ltd.',
        'sector': 'Financial Services',
        'symbol': 'CHOICEIN'
    },
    'CHOLAHLDNG.NS': {
        'name': 'Cholamandalam Financial Holdings Ltd.',
        'sector': 'Financial Services',
        'symbol': 'CHOLAHLDNG'
    },
    'CHOLAFIN.NS': {
        'name': 'Cholamandalam Investment and Finance Company Ltd.',
        'sector': 'Financial Services',
        'symbol': 'CHOLAFIN'
    },
    'CIPLA.NS': {
        'name': 'Cipla Ltd.',
        'sector': 'Healthcare',
        'symbol': 'CIPLA'
    },
    'CUB.NS': {
        'name': 'City Union Bank Ltd.',
        'sector': 'Financial Services',
        'symbol': 'CUB'
    },
    'CLEAN.NS': {
        'name': 'Clean Science and Technology Ltd.',
        'sector': 'Chemicals',
        'symbol': 'CLEAN'
    },
    'COALINDIA.NS': {
        'name': 'Coal India Ltd.',
        'sector': 'Oil Gas & Consumable Fuels',
        'symbol': 'COALINDIA'
    },
    'COCHINSHIP.NS': {
        'name': 'Cochin Shipyard Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'COCHINSHIP'
    },
    'COFORGE.NS': {
        'name': 'Coforge Ltd.',
        'sector': 'Information Technology',
        'symbol': 'COFORGE'
    },
    'COHANCE.NS': {
        'name': 'Cohance Lifesciences Ltd.',
        'sector': 'Healthcare',
        'symbol': 'COHANCE'
    },
    'COLPAL.NS': {
        'name': 'Colgate Palmolive (India) Ltd.',
        'sector': 'Fast Moving Consumer Goods',
        'symbol': 'COLPAL'
    },
    'CAMS.NS': {
        'name': 'Computer Age Management Services Ltd.',
        'sector': 'Financial Services',
        'symbol': 'CAMS'
    },
    'CONCORDBIO.NS': {
        'name': 'Concord Biotech Ltd.',
        'sector': 'Healthcare',
        'symbol': 'CONCORDBIO'
    },
    'CONCOR.NS': {
        'name': 'Container Corporation of India Ltd.',
        'sector': 'Services',
        'symbol': 'CONCOR'
    },
    'COROMANDEL.NS': {
        'name': 'Coromandel International Ltd.',
        'sector': 'Chemicals',
        'symbol': 'COROMANDEL'
    },
    'CRAFTSMAN.NS': {
        'name': 'Craftsman Automation Ltd.',
        'sector': 'Automobile and Auto Components',
        'symbol': 'CRAFTSMAN'
    },
    'CREDITACC.NS': {
        'name': 'CreditAccess Grameen Ltd.',
        'sector': 'Financial Services',
        'symbol': 'CREDITACC'
    },
    'CROMPTON.NS': {
        'name': 'Crompton Greaves Consumer Electricals Ltd.',
        'sector': 'Consumer Durables',
        'symbol': 'CROMPTON'
    },
    'CUMMINSIND.NS': {
        'name': 'Cummins India Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'CUMMINSIND'
    },
    'CYIENT.NS': {
        'name': 'Cyient Ltd.',
        'sector': 'Information Technology',
        'symbol': 'CYIENT'
    },
    'DCMSHRIRAM.NS': {
        'name': 'DCM Shriram Ltd.',
        'sector': 'Diversified',
        'symbol': 'DCMSHRIRAM'
    },
    'DLF.NS': {
        'name': 'DLF Ltd.',
        'sector': 'Realty',
        'symbol': 'DLF'
    },
    'DOMS.NS': {
        'name': 'DOMS Industries Ltd.',
        'sector': 'Fast Moving Consumer Goods',
        'symbol': 'DOMS'
    },
    'DABUR.NS': {
        'name': 'Dabur India Ltd.',
        'sector': 'Fast Moving Consumer Goods',
        'symbol': 'DABUR'
    },
    'DALBHARAT.NS': {
        'name': 'Dalmia Bharat Ltd.',
        'sector': 'Construction Materials',
        'symbol': 'DALBHARAT'
    },
    'DATAPATTNS.NS': {
        'name': 'Data Patterns (India) Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'DATAPATTNS'
    },
    'DEEPAKFERT.NS': {
        'name': 'Deepak Fertilisers & Petrochemicals Corp. Ltd.',
        'sector': 'Chemicals',
        'symbol': 'DEEPAKFERT'
    },
    'DEEPAKNTR.NS': {
        'name': 'Deepak Nitrite Ltd.',
        'sector': 'Chemicals',
        'symbol': 'DEEPAKNTR'
    },
    'DELHIVERY.NS': {
        'name': 'Delhivery Ltd.',
        'sector': 'Services',
        'symbol': 'DELHIVERY'
    },
    'DEVYANI.NS': {
        'name': 'Devyani International Ltd.',
        'sector': 'Consumer Services',
        'symbol': 'DEVYANI'
    },
    'DIVISLAB.NS': {
        'name': 'Divi\'s Laboratories Ltd.',
        'sector': 'Healthcare',
        'symbol': 'DIVISLAB'
    },
    'DIXON.NS': {
        'name': 'Dixon Technologies (India) Ltd.',
        'sector': 'Consumer Durables',
        'symbol': 'DIXON'
    },
    'AGARWALEYE.NS': {
        'name': 'Dr. Agarwal\'s Health Care Ltd.',
        'sector': 'Healthcare',
        'symbol': 'AGARWALEYE'
    },
    'LALPATHLAB.NS': {
        'name': 'Dr. Lal Path Labs Ltd.',
        'sector': 'Healthcare',
        'symbol': 'LALPATHLAB'
    },
    'DRREDDY.NS': {
        'name': 'Dr. Reddy\'s Laboratories Ltd.',
        'sector': 'Healthcare',
        'symbol': 'DRREDDY'
    },
    'DUMMYHDLVR.NS': {
        'name': 'Dummy Hindustan Unilever Ltd.',
        'sector': 'Fast Moving Consumer Goods',
        'symbol': 'DUMMYHDLVR'
    },
    'EIDPARRY.NS': {
        'name': 'E.I.D. Parry (India) Ltd.',
        'sector': 'Fast Moving Consumer Goods',
        'symbol': 'EIDPARRY'
    },
    'EIHOTEL.NS': {
        'name': 'EIH Ltd.',
        'sector': 'Consumer Services',
        'symbol': 'EIHOTEL'
    },
    'EICHERMOT.NS': {
        'name': 'Eicher Motors Ltd.',
        'sector': 'Automobile and Auto Components',
        'symbol': 'EICHERMOT'
    },
    'ELECON.NS': {
        'name': 'Elecon Engineering Co. Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'ELECON'
    },
    'ELGIEQUIP.NS': {
        'name': 'Elgi Equipments Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'ELGIEQUIP'
    },
    'EMAMILTD.NS': {
        'name': 'Emami Ltd.',
        'sector': 'Fast Moving Consumer Goods',
        'symbol': 'EMAMILTD'
    },
    'EMCURE.NS': {
        'name': 'Emcure Pharmaceuticals Ltd.',
        'sector': 'Healthcare',
        'symbol': 'EMCURE'
    },
    'ENDURANCE.NS': {
        'name': 'Endurance Technologies Ltd.',
        'sector': 'Automobile and Auto Components',
        'symbol': 'ENDURANCE'
    },
    'ENGINERSIN.NS': {
        'name': 'Engineers India Ltd.',
        'sector': 'Construction',
        'symbol': 'ENGINERSIN'
    },
    'ERIS.NS': {
        'name': 'Eris Lifesciences Ltd.',
        'sector': 'Healthcare',
        'symbol': 'ERIS'
    },
    'ESCORTS.NS': {
        'name': 'Escorts Kubota Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'ESCORTS'
    },
    'ETERNAL.NS': {
        'name': 'Eternal Ltd.',
        'sector': 'Consumer Services',
        'symbol': 'ETERNAL'
    },
    'EXIDEIND.NS': {
        'name': 'Exide Industries Ltd.',
        'sector': 'Automobile and Auto Components',
        'symbol': 'EXIDEIND'
    },
    'NYKAA.NS': {
        'name': 'FSN E-Commerce Ventures Ltd.',
        'sector': 'Consumer Services',
        'symbol': 'NYKAA'
    },
    'FEDERALBNK.NS': {
        'name': 'Federal Bank Ltd.',
        'sector': 'Financial Services',
        'symbol': 'FEDERALBNK'
    },
    'FACT.NS': {
        'name': 'Fertilisers and Chemicals Travancore Ltd.',
        'sector': 'Chemicals',
        'symbol': 'FACT'
    },
    'FINCABLES.NS': {
        'name': 'Finolex Cables Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'FINCABLES'
    },
    'FINPIPE.NS': {
        'name': 'Finolex Industries Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'FINPIPE'
    },
    'FSL.NS': {
        'name': 'Firstsource Solutions Ltd.',
        'sector': 'Services',
        'symbol': 'FSL'
    },
    'FIVESTAR.NS': {
        'name': 'Five-Star Business Finance Ltd.',
        'sector': 'Financial Services',
        'symbol': 'FIVESTAR'
    },
    'FORCEMOT.NS': {
        'name': 'Force Motors Ltd.',
        'sector': 'Automobile and Auto Components',
        'symbol': 'FORCEMOT'
    },
    'FORTIS.NS': {
        'name': 'Fortis Healthcare Ltd.',
        'sector': 'Healthcare',
        'symbol': 'FORTIS'
    },
    'GAIL.NS': {
        'name': 'GAIL (India) Ltd.',
        'sector': 'Oil Gas & Consumable Fuels',
        'symbol': 'GAIL'
    },
    'GVT&D.NS': {
        'name': 'GE Vernova T&D India Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'GVT&D'
    },
    'GMRAIRPORT.NS': {
        'name': 'GMR Airports Ltd.',
        'sector': 'Services',
        'symbol': 'GMRAIRPORT'
    },
    'GRSE.NS': {
        'name': 'Garden Reach Shipbuilders & Engineers Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'GRSE'
    },
    'GICRE.NS': {
        'name': 'General Insurance Corporation of India',
        'sector': 'Financial Services',
        'symbol': 'GICRE'
    },
    'GILLETTE.NS': {
        'name': 'Gillette India Ltd.',
        'sector': 'Fast Moving Consumer Goods',
        'symbol': 'GILLETTE'
    },
    'GLAND.NS': {
        'name': 'Gland Pharma Ltd.',
        'sector': 'Healthcare',
        'symbol': 'GLAND'
    },
    'GLAXO.NS': {
        'name': 'Glaxosmithkline Pharmaceuticals Ltd.',
        'sector': 'Healthcare',
        'symbol': 'GLAXO'
    },
    'GLENMARK.NS': {
        'name': 'Glenmark Pharmaceuticals Ltd.',
        'sector': 'Healthcare',
        'symbol': 'GLENMARK'
    },
    'MEDANTA.NS': {
        'name': 'Global Health Ltd.',
        'sector': 'Healthcare',
        'symbol': 'MEDANTA'
    },
    'GODIGIT.NS': {
        'name': 'Go Digit General Insurance Ltd.',
        'sector': 'Financial Services',
        'symbol': 'GODIGIT'
    },
    'GPIL.NS': {
        'name': 'Godawari Power & Ispat Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'GPIL'
    },
    'GODFRYPHLP.NS': {
        'name': 'Godfrey Phillips India Ltd.',
        'sector': 'Fast Moving Consumer Goods',
        'symbol': 'GODFRYPHLP'
    },
    'GODREJAGRO.NS': {
        'name': 'Godrej Agrovet Ltd.',
        'sector': 'Fast Moving Consumer Goods',
        'symbol': 'GODREJAGRO'
    },
    'GODREJCP.NS': {
        'name': 'Godrej Consumer Products Ltd.',
        'sector': 'Fast Moving Consumer Goods',
        'symbol': 'GODREJCP'
    },
    'GODREJIND.NS': {
        'name': 'Godrej Industries Ltd.',
        'sector': 'Diversified',
        'symbol': 'GODREJIND'
    },
    'GODREJPROP.NS': {
        'name': 'Godrej Properties Ltd.',
        'sector': 'Realty',
        'symbol': 'GODREJPROP'
    },
    'GRANULES.NS': {
        'name': 'Granules India Ltd.',
        'sector': 'Healthcare',
        'symbol': 'GRANULES'
    },
    'GRAPHITE.NS': {
        'name': 'Graphite India Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'GRAPHITE'
    },
    'GRASIM.NS': {
        'name': 'Grasim Industries Ltd.',
        'sector': 'Construction Materials',
        'symbol': 'GRASIM'
    },
    'GRAVITA.NS': {
        'name': 'Gravita India Ltd.',
        'sector': 'Metals & Mining',
        'symbol': 'GRAVITA'
    },
    'GESHIP.NS': {
        'name': 'Great Eastern Shipping Co. Ltd.',
        'sector': 'Services',
        'symbol': 'GESHIP'
    },
    'FLUOROCHEM.NS': {
        'name': 'Gujarat Fluorochemicals Ltd.',
        'sector': 'Chemicals',
        'symbol': 'FLUOROCHEM'
    },
    'GUJGASLTD.NS': {
        'name': 'Gujarat Gas Ltd.',
        'sector': 'Oil Gas & Consumable Fuels',
        'symbol': 'GUJGASLTD'
    },
    'GMDCLTD.NS': {
        'name': 'Gujarat Mineral Development Corporation Ltd.',
        'sector': 'Metals & Mining',
        'symbol': 'GMDCLTD'
    },
    'GSPL.NS': {
        'name': 'Gujarat State Petronet Ltd.',
        'sector': 'Oil Gas & Consumable Fuels',
        'symbol': 'GSPL'
    },
    'HEG.NS': {
        'name': 'H.E.G. Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'HEG'
    },
    'HBLENGINE.NS': {
        'name': 'HBL Engineering Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'HBLENGINE'
    },
    'HCLTECH.NS': {
        'name': 'HCL Technologies Ltd.',
        'sector': 'Information Technology',
        'symbol': 'HCLTECH'
    },
    'HDFCAMC.NS': {
        'name': 'HDFC Asset Management Company Ltd.',
        'sector': 'Financial Services',
        'symbol': 'HDFCAMC'
    },
    'HDFCBANK.NS': {
        'name': 'HDFC Bank Ltd.',
        'sector': 'Financial Services',
        'symbol': 'HDFCBANK'
    },
    'HDFCLIFE.NS': {
        'name': 'HDFC Life Insurance Company Ltd.',
        'sector': 'Financial Services',
        'symbol': 'HDFCLIFE'
    },
    'HFCL.NS': {
        'name': 'HFCL Ltd.',
        'sector': 'Telecommunication',
        'symbol': 'HFCL'
    },
    'HAPPSTMNDS.NS': {
        'name': 'Happiest Minds Technologies Ltd.',
        'sector': 'Information Technology',
        'symbol': 'HAPPSTMNDS'
    },
    'HAVELLS.NS': {
        'name': 'Havells India Ltd.',
        'sector': 'Consumer Durables',
        'symbol': 'HAVELLS'
    },
    'HEROMOTOCO.NS': {
        'name': 'Hero MotoCorp Ltd.',
        'sector': 'Automobile and Auto Components',
        'symbol': 'HEROMOTOCO'
    },
    'HEXT.NS': {
        'name': 'Hexaware Technologies Ltd.',
        'sector': 'Information Technology',
        'symbol': 'HEXT'
    },
    'HSCL.NS': {
        'name': 'Himadri Speciality Chemical Ltd.',
        'sector': 'Chemicals',
        'symbol': 'HSCL'
    },
    'HINDALCO.NS': {
        'name': 'Hindalco Industries Ltd.',
        'sector': 'Metals & Mining',
        'symbol': 'HINDALCO'
    },
    'HAL.NS': {
        'name': 'Hindustan Aeronautics Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'HAL'
    },
    'HINDCOPPER.NS': {
        'name': 'Hindustan Copper Ltd.',
        'sector': 'Metals & Mining',
        'symbol': 'HINDCOPPER'
    },
    'HINDPETRO.NS': {
        'name': 'Hindustan Petroleum Corporation Ltd.',
        'sector': 'Oil Gas & Consumable Fuels',
        'symbol': 'HINDPETRO'
    },
    'HINDUNILVR.NS': {
        'name': 'Hindustan Unilever Ltd.',
        'sector': 'Fast Moving Consumer Goods',
        'symbol': 'HINDUNILVR'
    },
    'HINDZINC.NS': {
        'name': 'Hindustan Zinc Ltd.',
        'sector': 'Metals & Mining',
        'symbol': 'HINDZINC'
    },
    'POWERINDIA.NS': {
        'name': 'Hitachi Energy India Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'POWERINDIA'
    },
    'HOMEFIRST.NS': {
        'name': 'Home First Finance Company India Ltd.',
        'sector': 'Financial Services',
        'symbol': 'HOMEFIRST'
    },
    'HONASA.NS': {
        'name': 'Honasa Consumer Ltd.',
        'sector': 'Fast Moving Consumer Goods',
        'symbol': 'HONASA'
    },
    'HONAUT.NS': {
        'name': 'Honeywell Automation India Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'HONAUT'
    },
    'HUDCO.NS': {
        'name': 'Housing & Urban Development Corporation Ltd.',
        'sector': 'Financial Services',
        'symbol': 'HUDCO'
    },
    'HYUNDAI.NS': {
        'name': 'Hyundai Motor India Ltd.',
        'sector': 'Automobile and Auto Components',
        'symbol': 'HYUNDAI'
    },
    'ICICIBANK.NS': {
        'name': 'ICICI Bank Ltd.',
        'sector': 'Financial Services',
        'symbol': 'ICICIBANK'
    },
    'ICICIGI.NS': {
        'name': 'ICICI Lombard General Insurance Company Ltd.',
        'sector': 'Financial Services',
        'symbol': 'ICICIGI'
    },
    'ICICIPRULI.NS': {
        'name': 'ICICI Prudential Life Insurance Company Ltd.',
        'sector': 'Financial Services',
        'symbol': 'ICICIPRULI'
    },
    'IDBI.NS': {
        'name': 'IDBI Bank Ltd.',
        'sector': 'Financial Services',
        'symbol': 'IDBI'
    },
    'IDFCFIRSTB.NS': {
        'name': 'IDFC First Bank Ltd.',
        'sector': 'Financial Services',
        'symbol': 'IDFCFIRSTB'
    },
    'IFCI.NS': {
        'name': 'IFCI Ltd.',
        'sector': 'Financial Services',
        'symbol': 'IFCI'
    },
    'IIFL.NS': {
        'name': 'IIFL Finance Ltd.',
        'sector': 'Financial Services',
        'symbol': 'IIFL'
    },
    'INOXINDIA.NS': {
        'name': 'INOX India Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'INOXINDIA'
    },
    'IRB.NS': {
        'name': 'IRB Infrastructure Developers Ltd.',
        'sector': 'Construction',
        'symbol': 'IRB'
    },
    'IRCON.NS': {
        'name': 'IRCON International Ltd.',
        'sector': 'Construction',
        'symbol': 'IRCON'
    },
    'ITCHOTELS.NS': {
        'name': 'ITC Hotels Ltd.',
        'sector': 'Consumer Services',
        'symbol': 'ITCHOTELS'
    },
    'ITC.NS': {
        'name': 'ITC Ltd.',
        'sector': 'Fast Moving Consumer Goods',
        'symbol': 'ITC'
    },
    'ITI.NS': {
        'name': 'ITI Ltd.',
        'sector': 'Telecommunication',
        'symbol': 'ITI'
    },
    'INDGN.NS': {
        'name': 'Indegene Ltd.',
        'sector': 'Healthcare',
        'symbol': 'INDGN'
    },
    'INDIACEM.NS': {
        'name': 'India Cements Ltd.',
        'sector': 'Construction Materials',
        'symbol': 'INDIACEM'
    },
    'INDIAMART.NS': {
        'name': 'Indiamart Intermesh Ltd.',
        'sector': 'Consumer Services',
        'symbol': 'INDIAMART'
    },
    'INDIANB.NS': {
        'name': 'Indian Bank',
        'sector': 'Financial Services',
        'symbol': 'INDIANB'
    },
    'IEX.NS': {
        'name': 'Indian Energy Exchange Ltd.',
        'sector': 'Financial Services',
        'symbol': 'IEX'
    },
    'INDHOTEL.NS': {
        'name': 'Indian Hotels Co. Ltd.',
        'sector': 'Consumer Services',
        'symbol': 'INDHOTEL'
    },
    'IOC.NS': {
        'name': 'Indian Oil Corporation Ltd.',
        'sector': 'Oil Gas & Consumable Fuels',
        'symbol': 'IOC'
    },
    'IOB.NS': {
        'name': 'Indian Overseas Bank',
        'sector': 'Financial Services',
        'symbol': 'IOB'
    },
    'IRCTC.NS': {
        'name': 'Indian Railway Catering And Tourism Corporation Ltd.',
        'sector': 'Consumer Services',
        'symbol': 'IRCTC'
    },
    'IRFC.NS': {
        'name': 'Indian Railway Finance Corporation Ltd.',
        'sector': 'Financial Services',
        'symbol': 'IRFC'
    },
    'IREDA.NS': {
        'name': 'Indian Renewable Energy Development Agency Ltd.',
        'sector': 'Financial Services',
        'symbol': 'IREDA'
    },
    'IGL.NS': {
        'name': 'Indraprastha Gas Ltd.',
        'sector': 'Oil Gas & Consumable Fuels',
        'symbol': 'IGL'
    },
    'INDUSTOWER.NS': {
        'name': 'Indus Towers Ltd.',
        'sector': 'Telecommunication',
        'symbol': 'INDUSTOWER'
    },
    'INDUSINDBK.NS': {
        'name': 'IndusInd Bank Ltd.',
        'sector': 'Financial Services',
        'symbol': 'INDUSINDBK'
    },
    'NAUKRI.NS': {
        'name': 'Info Edge (India) Ltd.',
        'sector': 'Consumer Services',
        'symbol': 'NAUKRI'
    },
    'INFY.NS': {
        'name': 'Infosys Ltd.',
        'sector': 'Information Technology',
        'symbol': 'INFY'
    },
    'INOXWIND.NS': {
        'name': 'Inox Wind Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'INOXWIND'
    },
    'INTELLECT.NS': {
        'name': 'Intellect Design Arena Ltd.',
        'sector': 'Information Technology',
        'symbol': 'INTELLECT'
    },
    'INDIGO.NS': {
        'name': 'InterGlobe Aviation Ltd.',
        'sector': 'Services',
        'symbol': 'INDIGO'
    },
    'IGIL.NS': {
        'name': 'International Gemmological Institute (India) Ltd.',
        'sector': 'Services',
        'symbol': 'IGIL'
    },
    'IKS.NS': {
        'name': 'Inventurus Knowledge Solutions Ltd.',
        'sector': 'Information Technology',
        'symbol': 'IKS'
    },
    'IPCALAB.NS': {
        'name': 'Ipca Laboratories Ltd.',
        'sector': 'Healthcare',
        'symbol': 'IPCALAB'
    },
    'JBCHEPHARM.NS': {
        'name': 'J.B. Chemicals & Pharmaceuticals Ltd.',
        'sector': 'Healthcare',
        'symbol': 'JBCHEPHARM'
    },
    'JKCEMENT.NS': {
        'name': 'J.K. Cement Ltd.',
        'sector': 'Construction Materials',
        'symbol': 'JKCEMENT'
    },
    'JBMA.NS': {
        'name': 'JBM Auto Ltd.',
        'sector': 'Automobile and Auto Components',
        'symbol': 'JBMA'
    },
    'JKTYRE.NS': {
        'name': 'JK Tyre & Industries Ltd.',
        'sector': 'Automobile and Auto Components',
        'symbol': 'JKTYRE'
    },
    'JMFINANCIL.NS': {
        'name': 'JM Financial Ltd.',
        'sector': 'Financial Services',
        'symbol': 'JMFINANCIL'
    },
    'JSWCEMENT.NS': {
        'name': 'JSW Cement Ltd.',
        'sector': 'Construction Materials',
        'symbol': 'JSWCEMENT'
    },
    'JSWENERGY.NS': {
        'name': 'JSW Energy Ltd.',
        'sector': 'Power',
        'symbol': 'JSWENERGY'
    },
    'JSWINFRA.NS': {
        'name': 'JSW Infrastructure Ltd.',
        'sector': 'Services',
        'symbol': 'JSWINFRA'
    },
    'JSWSTEEL.NS': {
        'name': 'JSW Steel Ltd.',
        'sector': 'Metals & Mining',
        'symbol': 'JSWSTEEL'
    },
    'JPPOWER.NS': {
        'name': 'Jaiprakash Power Ventures Ltd.',
        'sector': 'Power',
        'symbol': 'JPPOWER'
    },
    'J&KBANK.NS': {
        'name': 'Jammu & Kashmir Bank Ltd.',
        'sector': 'Financial Services',
        'symbol': 'J&KBANK'
    },
    'JINDALSAW.NS': {
        'name': 'Jindal Saw Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'JINDALSAW'
    },
    'JSL.NS': {
        'name': 'Jindal Stainless Ltd.',
        'sector': 'Metals & Mining',
        'symbol': 'JSL'
    },
    'JINDALSTEL.NS': {
        'name': 'Jindal Steel Ltd.',
        'sector': 'Metals & Mining',
        'symbol': 'JINDALSTEL'
    },
    'JIOFIN.NS': {
        'name': 'Jio Financial Services Ltd.',
        'sector': 'Financial Services',
        'symbol': 'JIOFIN'
    },
    'JUBLFOOD.NS': {
        'name': 'Jubilant Foodworks Ltd.',
        'sector': 'Consumer Services',
        'symbol': 'JUBLFOOD'
    },
    'JUBLINGREA.NS': {
        'name': 'Jubilant Ingrevia Ltd.',
        'sector': 'Chemicals',
        'symbol': 'JUBLINGREA'
    },
    'JUBLPHARMA.NS': {
        'name': 'Jubilant Pharmova Ltd.',
        'sector': 'Healthcare',
        'symbol': 'JUBLPHARMA'
    },
    'JWL.NS': {
        'name': 'Jupiter Wagons Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'JWL'
    },
    'JYOTHYLAB.NS': {
        'name': 'Jyothy Labs Ltd.',
        'sector': 'Fast Moving Consumer Goods',
        'symbol': 'JYOTHYLAB'
    },
    'JYOTICNC.NS': {
        'name': 'Jyoti CNC Automation Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'JYOTICNC'
    },
    'KPRMILL.NS': {
        'name': 'K.P.R. Mill Ltd.',
        'sector': 'Textiles',
        'symbol': 'KPRMILL'
    },
    'KEI.NS': {
        'name': 'KEI Industries Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'KEI'
    },
    'KPITTECH.NS': {
        'name': 'KPIT Technologies Ltd.',
        'sector': 'Information Technology',
        'symbol': 'KPITTECH'
    },
    'KSB.NS': {
        'name': 'KSB Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'KSB'
    },
    'KAJARIACER.NS': {
        'name': 'Kajaria Ceramics Ltd.',
        'sector': 'Consumer Durables',
        'symbol': 'KAJARIACER'
    },
    'KPIL.NS': {
        'name': 'Kalpataru Projects International Ltd.',
        'sector': 'Construction',
        'symbol': 'KPIL'
    },
    'KALYANKJIL.NS': {
        'name': 'Kalyan Jewellers India Ltd.',
        'sector': 'Consumer Durables',
        'symbol': 'KALYANKJIL'
    },
    'KARURVYSYA.NS': {
        'name': 'Karur Vysya Bank Ltd.',
        'sector': 'Financial Services',
        'symbol': 'KARURVYSYA'
    },
    'KAYNES.NS': {
        'name': 'Kaynes Technology India Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'KAYNES'
    },
    'KEC.NS': {
        'name': 'Kec International Ltd.',
        'sector': 'Construction',
        'symbol': 'KEC'
    },
    'KFINTECH.NS': {
        'name': 'Kfin Technologies Ltd.',
        'sector': 'Financial Services',
        'symbol': 'KFINTECH'
    },
    'KIRLOSBROS.NS': {
        'name': 'Kirloskar Brothers Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'KIRLOSBROS'
    },
    'KIRLOSENG.NS': {
        'name': 'Kirloskar Oil Eng Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'KIRLOSENG'
    },
    'KOTAKBANK.NS': {
        'name': 'Kotak Mahindra Bank Ltd.',
        'sector': 'Financial Services',
        'symbol': 'KOTAKBANK'
    },
    'KIMS.NS': {
        'name': 'Krishna Institute of Medical Sciences Ltd.',
        'sector': 'Healthcare',
        'symbol': 'KIMS'
    },
    'LTF.NS': {
        'name': 'L&T Finance Ltd.',
        'sector': 'Financial Services',
        'symbol': 'LTF'
    },
    'LTTS.NS': {
        'name': 'L&T Technology Services Ltd.',
        'sector': 'Information Technology',
        'symbol': 'LTTS'
    },
    'LICHSGFIN.NS': {
        'name': 'LIC Housing Finance Ltd.',
        'sector': 'Financial Services',
        'symbol': 'LICHSGFIN'
    },
    'LTFOODS.NS': {
        'name': 'LT Foods Ltd.',
        'sector': 'Fast Moving Consumer Goods',
        'symbol': 'LTFOODS'
    },
    'LTIM.NS': {
        'name': 'LTIMindtree Ltd.',
        'sector': 'Information Technology',
        'symbol': 'LTIM'
    },
    'LT.NS': {
        'name': 'Larsen & Toubro Ltd.',
        'sector': 'Construction',
        'symbol': 'LT'
    },
    'LATENTVIEW.NS': {
        'name': 'Latent View Analytics Ltd.',
        'sector': 'Information Technology',
        'symbol': 'LATENTVIEW'
    },
    'LAURUSLABS.NS': {
        'name': 'Laurus Labs Ltd.',
        'sector': 'Healthcare',
        'symbol': 'LAURUSLABS'
    },
    'THELEELA.NS': {
        'name': 'Leela Palaces Hotels & Resorts Ltd.',
        'sector': 'Consumer Services',
        'symbol': 'THELEELA'
    },
    'LEMONTREE.NS': {
        'name': 'Lemon Tree Hotels Ltd.',
        'sector': 'Consumer Services',
        'symbol': 'LEMONTREE'
    },
    'LICI.NS': {
        'name': 'Life Insurance Corporation of India',
        'sector': 'Financial Services',
        'symbol': 'LICI'
    },
    'LINDEINDIA.NS': {
        'name': 'Linde India Ltd.',
        'sector': 'Chemicals',
        'symbol': 'LINDEINDIA'
    },
    'LLOYDSME.NS': {
        'name': 'Lloyds Metals And Energy Ltd.',
        'sector': 'Metals & Mining',
        'symbol': 'LLOYDSME'
    },
    'LODHA.NS': {
        'name': 'Lodha Developers Ltd.',
        'sector': 'Realty',
        'symbol': 'LODHA'
    },
    'LUPIN.NS': {
        'name': 'Lupin Ltd.',
        'sector': 'Healthcare',
        'symbol': 'LUPIN'
    },
    'MMTC.NS': {
        'name': 'MMTC Ltd.',
        'sector': 'Services',
        'symbol': 'MMTC'
    },
    'MRF.NS': {
        'name': 'MRF Ltd.',
        'sector': 'Automobile and Auto Components',
        'symbol': 'MRF'
    },
    'MGL.NS': {
        'name': 'Mahanagar Gas Ltd.',
        'sector': 'Oil Gas & Consumable Fuels',
        'symbol': 'MGL'
    },
    'MAHSCOOTER.NS': {
        'name': 'Maharashtra Scooters Ltd.',
        'sector': 'Financial Services',
        'symbol': 'MAHSCOOTER'
    },
    'MAHSEAMLES.NS': {
        'name': 'Maharashtra Seamless Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'MAHSEAMLES'
    },
    'M&MFIN.NS': {
        'name': 'Mahindra & Mahindra Financial Services Ltd.',
        'sector': 'Financial Services',
        'symbol': 'M&MFIN'
    },
    'M&M.NS': {
        'name': 'Mahindra & Mahindra Ltd.',
        'sector': 'Automobile and Auto Components',
        'symbol': 'M&M'
    },
    'MANAPPURAM.NS': {
        'name': 'Manappuram Finance Ltd.',
        'sector': 'Financial Services',
        'symbol': 'MANAPPURAM'
    },
    'MRPL.NS': {
        'name': 'Mangalore Refinery & Petrochemicals Ltd.',
        'sector': 'Oil Gas & Consumable Fuels',
        'symbol': 'MRPL'
    },
    'MANKIND.NS': {
        'name': 'Mankind Pharma Ltd.',
        'sector': 'Healthcare',
        'symbol': 'MANKIND'
    },
    'MARICO.NS': {
        'name': 'Marico Ltd.',
        'sector': 'Fast Moving Consumer Goods',
        'symbol': 'MARICO'
    },
    'MARUTI.NS': {
        'name': 'Maruti Suzuki India Ltd.',
        'sector': 'Automobile and Auto Components',
        'symbol': 'MARUTI'
    },
    'MFSL.NS': {
        'name': 'Max Financial Services Ltd.',
        'sector': 'Financial Services',
        'symbol': 'MFSL'
    },
    'MAXHEALTH.NS': {
        'name': 'Max Healthcare Institute Ltd.',
        'sector': 'Healthcare',
        'symbol': 'MAXHEALTH'
    },
    'MAZDOCK.NS': {
        'name': 'Mazagoan Dock Shipbuilders Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'MAZDOCK'
    },
    'METROPOLIS.NS': {
        'name': 'Metropolis Healthcare Ltd.',
        'sector': 'Healthcare',
        'symbol': 'METROPOLIS'
    },
    'MINDACORP.NS': {
        'name': 'Minda Corporation Ltd.',
        'sector': 'Automobile and Auto Components',
        'symbol': 'MINDACORP'
    },
    'MSUMI.NS': {
        'name': 'Motherson Sumi Wiring India Ltd.',
        'sector': 'Automobile and Auto Components',
        'symbol': 'MSUMI'
    },
    'MOTILALOFS.NS': {
        'name': 'Motilal Oswal Financial Services Ltd.',
        'sector': 'Financial Services',
        'symbol': 'MOTILALOFS'
    },
    'MPHASIS.NS': {
        'name': 'MphasiS Ltd.',
        'sector': 'Information Technology',
        'symbol': 'MPHASIS'
    },
    'MCX.NS': {
        'name': 'Multi Commodity Exchange of India Ltd.',
        'sector': 'Financial Services',
        'symbol': 'MCX'
    },
    'MUTHOOTFIN.NS': {
        'name': 'Muthoot Finance Ltd.',
        'sector': 'Financial Services',
        'symbol': 'MUTHOOTFIN'
    },
    'NATCOPHARM.NS': {
        'name': 'NATCO Pharma Ltd.',
        'sector': 'Healthcare',
        'symbol': 'NATCOPHARM'
    },
    'NBCC.NS': {
        'name': 'NBCC (India) Ltd.',
        'sector': 'Construction',
        'symbol': 'NBCC'
    },
    'NCC.NS': {
        'name': 'NCC Ltd.',
        'sector': 'Construction',
        'symbol': 'NCC'
    },
    'NHPC.NS': {
        'name': 'NHPC Ltd.',
        'sector': 'Power',
        'symbol': 'NHPC'
    },
    'NLCINDIA.NS': {
        'name': 'NLC India Ltd.',
        'sector': 'Power',
        'symbol': 'NLCINDIA'
    },
    'NMDC.NS': {
        'name': 'NMDC Ltd.',
        'sector': 'Metals & Mining',
        'symbol': 'NMDC'
    },
    'NSLNISP.NS': {
        'name': 'NMDC Steel Ltd.',
        'sector': 'Metals & Mining',
        'symbol': 'NSLNISP'
    },
    'NTPCGREEN.NS': {
        'name': 'NTPC Green Energy Ltd.',
        'sector': 'Power',
        'symbol': 'NTPCGREEN'
    },
    'NTPC.NS': {
        'name': 'NTPC Ltd.',
        'sector': 'Power',
        'symbol': 'NTPC'
    },
    'NH.NS': {
        'name': 'Narayana Hrudayalaya Ltd.',
        'sector': 'Healthcare',
        'symbol': 'NH'
    },
    'NATIONALUM.NS': {
        'name': 'National Aluminium Co. Ltd.',
        'sector': 'Metals & Mining',
        'symbol': 'NATIONALUM'
    },
    'NAVA.NS': {
        'name': 'Nava Ltd.',
        'sector': 'Power',
        'symbol': 'NAVA'
    },
    'NAVINFLUOR.NS': {
        'name': 'Navin Fluorine International Ltd.',
        'sector': 'Chemicals',
        'symbol': 'NAVINFLUOR'
    },
    'NESTLEIND.NS': {
        'name': 'Nestle India Ltd.',
        'sector': 'Fast Moving Consumer Goods',
        'symbol': 'NESTLEIND'
    },
    'NETWEB.NS': {
        'name': 'Netweb Technologies India Ltd.',
        'sector': 'Information Technology',
        'symbol': 'NETWEB'
    },
    'NEULANDLAB.NS': {
        'name': 'Neuland Laboratories Ltd.',
        'sector': 'Healthcare',
        'symbol': 'NEULANDLAB'
    },
    'NEWGEN.NS': {
        'name': 'Newgen Software Technologies Ltd.',
        'sector': 'Information Technology',
        'symbol': 'NEWGEN'
    },
    'NAM-INDIA.NS': {
        'name': 'Nippon Life India Asset Management Ltd.',
        'sector': 'Financial Services',
        'symbol': 'NAM-INDIA'
    },
    'NIVABUPA.NS': {
        'name': 'Niva Bupa Health Insurance Company Ltd.',
        'sector': 'Financial Services',
        'symbol': 'NIVABUPA'
    },
    'NUVAMA.NS': {
        'name': 'Nuvama Wealth Management Ltd.',
        'sector': 'Financial Services',
        'symbol': 'NUVAMA'
    },
    'NUVOCO.NS': {
        'name': 'Nuvoco Vistas Corporation Ltd.',
        'sector': 'Construction Materials',
        'symbol': 'NUVOCO'
    },
    'OBEROIRLTY.NS': {
        'name': 'Oberoi Realty Ltd.',
        'sector': 'Realty',
        'symbol': 'OBEROIRLTY'
    },
    'ONGC.NS': {
        'name': 'Oil & Natural Gas Corporation Ltd.',
        'sector': 'Oil Gas & Consumable Fuels',
        'symbol': 'ONGC'
    },
    'OIL.NS': {
        'name': 'Oil India Ltd.',
        'sector': 'Oil Gas & Consumable Fuels',
        'symbol': 'OIL'
    },
    'OLAELEC.NS': {
        'name': 'Ola Electric Mobility Ltd.',
        'sector': 'Automobile and Auto Components',
        'symbol': 'OLAELEC'
    },
    'OLECTRA.NS': {
        'name': 'Olectra Greentech Ltd.',
        'sector': 'Automobile and Auto Components',
        'symbol': 'OLECTRA'
    },
    'PAYTM.NS': {
        'name': 'One 97 Communications Ltd.',
        'sector': 'Financial Services',
        'symbol': 'PAYTM'
    },
    'ONESOURCE.NS': {
        'name': 'Onesource Specialty Pharma Ltd.',
        'sector': 'Healthcare',
        'symbol': 'ONESOURCE'
    },
    'OFSS.NS': {
        'name': 'Oracle Financial Services Software Ltd.',
        'sector': 'Information Technology',
        'symbol': 'OFSS'
    },
    'POLICYBZR.NS': {
        'name': 'PB Fintech Ltd.',
        'sector': 'Financial Services',
        'symbol': 'POLICYBZR'
    },
    'PCBL.NS': {
        'name': 'PCBL Chemical Ltd.',
        'sector': 'Chemicals',
        'symbol': 'PCBL'
    },
    'PGEL.NS': {
        'name': 'PG Electroplast Ltd.',
        'sector': 'Consumer Durables',
        'symbol': 'PGEL'
    },
    'PIIND.NS': {
        'name': 'PI Industries Ltd.',
        'sector': 'Chemicals',
        'symbol': 'PIIND'
    },
    'PNBHOUSING.NS': {
        'name': 'PNB Housing Finance Ltd.',
        'sector': 'Financial Services',
        'symbol': 'PNBHOUSING'
    },
    'PTCIL.NS': {
        'name': 'PTC Industries Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'PTCIL'
    },
    'PVRINOX.NS': {
        'name': 'PVR INOX Ltd.',
        'sector': 'Media Entertainment & Publication',
        'symbol': 'PVRINOX'
    },
    'PAGEIND.NS': {
        'name': 'Page Industries Ltd.',
        'sector': 'Textiles',
        'symbol': 'PAGEIND'
    },
    'PATANJALI.NS': {
        'name': 'Patanjali Foods Ltd.',
        'sector': 'Fast Moving Consumer Goods',
        'symbol': 'PATANJALI'
    },
    'PERSISTENT.NS': {
        'name': 'Persistent Systems Ltd.',
        'sector': 'Information Technology',
        'symbol': 'PERSISTENT'
    },
    'PETRONET.NS': {
        'name': 'Petronet LNG Ltd.',
        'sector': 'Oil Gas & Consumable Fuels',
        'symbol': 'PETRONET'
    },
    'PFIZER.NS': {
        'name': 'Pfizer Ltd.',
        'sector': 'Healthcare',
        'symbol': 'PFIZER'
    },
    'PHOENIXLTD.NS': {
        'name': 'Phoenix Mills Ltd.',
        'sector': 'Realty',
        'symbol': 'PHOENIXLTD'
    },
    'PIDILITIND.NS': {
        'name': 'Pidilite Industries Ltd.',
        'sector': 'Chemicals',
        'symbol': 'PIDILITIND'
    },
    'PPLPHARMA.NS': {
        'name': 'Piramal Pharma Ltd.',
        'sector': 'Healthcare',
        'symbol': 'PPLPHARMA'
    },
    'POLYMED.NS': {
        'name': 'Poly Medicure Ltd.',
        'sector': 'Healthcare',
        'symbol': 'POLYMED'
    },
    'POLYCAB.NS': {
        'name': 'Polycab India Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'POLYCAB'
    },
    'POONAWALLA.NS': {
        'name': 'Poonawalla Fincorp Ltd.',
        'sector': 'Financial Services',
        'symbol': 'POONAWALLA'
    },
    'PFC.NS': {
        'name': 'Power Finance Corporation Ltd.',
        'sector': 'Financial Services',
        'symbol': 'PFC'
    },
    'POWERGRID.NS': {
        'name': 'Power Grid Corporation of India Ltd.',
        'sector': 'Power',
        'symbol': 'POWERGRID'
    },
    'PRAJIND.NS': {
        'name': 'Praj Industries Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'PRAJIND'
    },
    'PREMIERENE.NS': {
        'name': 'Premier Energies Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'PREMIERENE'
    },
    'PRESTIGE.NS': {
        'name': 'Prestige Estates Projects Ltd.',
        'sector': 'Realty',
        'symbol': 'PRESTIGE'
    },
    'PGHH.NS': {
        'name': 'Procter & Gamble Hygiene & Health Care Ltd.',
        'sector': 'Fast Moving Consumer Goods',
        'symbol': 'PGHH'
    },
    'PNB.NS': {
        'name': 'Punjab National Bank',
        'sector': 'Financial Services',
        'symbol': 'PNB'
    },
    'RRKABEL.NS': {
        'name': 'R R Kabel Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'RRKABEL'
    },
    'RBLBANK.NS': {
        'name': 'RBL Bank Ltd.',
        'sector': 'Financial Services',
        'symbol': 'RBLBANK'
    },
    'RECLTD.NS': {
        'name': 'REC Ltd.',
        'sector': 'Financial Services',
        'symbol': 'RECLTD'
    },
    'RHIM.NS': {
        'name': 'RHI MAGNESITA INDIA LTD.',
        'sector': 'Capital Goods',
        'symbol': 'RHIM'
    },
    'RITES.NS': {
        'name': 'RITES Ltd.',
        'sector': 'Construction',
        'symbol': 'RITES'
    },
    'RADICO.NS': {
        'name': 'Radico Khaitan Ltd',
        'sector': 'Fast Moving Consumer Goods',
        'symbol': 'RADICO'
    },
    'RVNL.NS': {
        'name': 'Rail Vikas Nigam Ltd.',
        'sector': 'Construction',
        'symbol': 'RVNL'
    },
    'RAILTEL.NS': {
        'name': 'Railtel Corporation Of India Ltd.',
        'sector': 'Telecommunication',
        'symbol': 'RAILTEL'
    },
    'RAINBOW.NS': {
        'name': 'Rainbow Childrens Medicare Ltd.',
        'sector': 'Healthcare',
        'symbol': 'RAINBOW'
    },
    'RKFORGE.NS': {
        'name': 'Ramkrishna Forgings Ltd.',
        'sector': 'Automobile and Auto Components',
        'symbol': 'RKFORGE'
    },
    'RCF.NS': {
        'name': 'Rashtriya Chemicals & Fertilizers Ltd.',
        'sector': 'Chemicals',
        'symbol': 'RCF'
    },
    'REDINGTON.NS': {
        'name': 'Redington Ltd.',
        'sector': 'Services',
        'symbol': 'REDINGTON'
    },
    'RELIANCE.NS': {
        'name': 'Reliance Industries Ltd.',
        'sector': 'Oil Gas & Consumable Fuels',
        'symbol': 'RELIANCE'
    },
    'RELINFRA.NS': {
        'name': 'Reliance Infrastructure Ltd.',
        'sector': 'Power',
        'symbol': 'RELINFRA'
    },
    'RPOWER.NS': {
        'name': 'Reliance Power Ltd.',
        'sector': 'Power',
        'symbol': 'RPOWER'
    },
    'SBFC.NS': {
        'name': 'SBFC Finance Ltd.',
        'sector': 'Financial Services',
        'symbol': 'SBFC'
    },
    'SBICARD.NS': {
        'name': 'SBI Cards and Payment Services Ltd.',
        'sector': 'Financial Services',
        'symbol': 'SBICARD'
    },
    'SBILIFE.NS': {
        'name': 'SBI Life Insurance Company Ltd.',
        'sector': 'Financial Services',
        'symbol': 'SBILIFE'
    },
    'SJVN.NS': {
        'name': 'SJVN Ltd.',
        'sector': 'Power',
        'symbol': 'SJVN'
    },
    'SRF.NS': {
        'name': 'SRF Ltd.',
        'sector': 'Chemicals',
        'symbol': 'SRF'
    },
    'SAGILITY.NS': {
        'name': 'Sagility Ltd.',
        'sector': 'Information Technology',
        'symbol': 'SAGILITY'
    },
    'SAILIFE.NS': {
        'name': 'Sai Life Sciences Ltd.',
        'sector': 'Healthcare',
        'symbol': 'SAILIFE'
    },
    'SAMMAANCAP.NS': {
        'name': 'Sammaan Capital Ltd.',
        'sector': 'Financial Services',
        'symbol': 'SAMMAANCAP'
    },
    'MOTHERSON.NS': {
        'name': 'Samvardhana Motherson International Ltd.',
        'sector': 'Automobile and Auto Components',
        'symbol': 'MOTHERSON'
    },
    'SAPPHIRE.NS': {
        'name': 'Sapphire Foods India Ltd.',
        'sector': 'Consumer Services',
        'symbol': 'SAPPHIRE'
    },
    'SARDAEN.NS': {
        'name': 'Sarda Energy and Minerals Ltd.',
        'sector': 'Metals & Mining',
        'symbol': 'SARDAEN'
    },
    'SAREGAMA.NS': {
        'name': 'Saregama India Ltd',
        'sector': 'Media Entertainment & Publication',
        'symbol': 'SAREGAMA'
    },
    'SCHAEFFLER.NS': {
        'name': 'Schaeffler India Ltd.',
        'sector': 'Automobile and Auto Components',
        'symbol': 'SCHAEFFLER'
    },
    'SCHNEIDER.NS': {
        'name': 'Schneider Electric Infrastructure Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'SCHNEIDER'
    },
    'SCI.NS': {
        'name': 'Shipping Corporation of India Ltd.',
        'sector': 'Services',
        'symbol': 'SCI'
    },
    'SHREECEM.NS': {
        'name': 'Shree Cement Ltd.',
        'sector': 'Construction Materials',
        'symbol': 'SHREECEM'
    },
    'SHRIRAMFIN.NS': {
        'name': 'Shriram Finance Ltd.',
        'sector': 'Financial Services',
        'symbol': 'SHRIRAMFIN'
    },
    'SHYAMMETL.NS': {
        'name': 'Shyam Metalics and Energy Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'SHYAMMETL'
    },
    'ENRIN.NS': {
        'name': 'Siemens Energy India Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'ENRIN'
    },
    'SIEMENS.NS': {
        'name': 'Siemens Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'SIEMENS'
    },
    'SIGNATURE.NS': {
        'name': 'Signatureglobal (India) Ltd.',
        'sector': 'Realty',
        'symbol': 'SIGNATURE'
    },
    'SOBHA.NS': {
        'name': 'Sobha Ltd.',
        'sector': 'Realty',
        'symbol': 'SOBHA'
    },
    'SOLARINDS.NS': {
        'name': 'Solar Industries India Ltd.',
        'sector': 'Chemicals',
        'symbol': 'SOLARINDS'
    },
    'SONACOMS.NS': {
        'name': 'Sona BLW Precision Forgings Ltd.',
        'sector': 'Automobile and Auto Components',
        'symbol': 'SONACOMS'
    },
    'SONATSOFTW.NS': {
        'name': 'Sonata Software Ltd.',
        'sector': 'Information Technology',
        'symbol': 'SONATSOFTW'
    },
    'STARHEALTH.NS': {
        'name': 'Star Health and Allied Insurance Company Ltd.',
        'sector': 'Financial Services',
        'symbol': 'STARHEALTH'
    },
    'SBIN.NS': {
        'name': 'State Bank of India',
        'sector': 'Financial Services',
        'symbol': 'SBIN'
    },
    'SAIL.NS': {
        'name': 'Steel Authority of India Ltd.',
        'sector': 'Metals & Mining',
        'symbol': 'SAIL'
    },
    'SUMICHEM.NS': {
        'name': 'Sumitomo Chemical India Ltd.',
        'sector': 'Chemicals',
        'symbol': 'SUMICHEM'
    },
    'SUNPHARMA.NS': {
        'name': 'Sun Pharmaceutical Industries Ltd.',
        'sector': 'Healthcare',
        'symbol': 'SUNPHARMA'
    },
    'SUNTV.NS': {
        'name': 'Sun TV Network Ltd.',
        'sector': 'Media Entertainment & Publication',
        'symbol': 'SUNTV'
    },
    'SUNDARMFIN.NS': {
        'name': 'Sundaram Finance Ltd.',
        'sector': 'Financial Services',
        'symbol': 'SUNDARMFIN'
    },
    'SUNDRMFAST.NS': {
        'name': 'Sundram Fasteners Ltd.',
        'sector': 'Automobile and Auto Components',
        'symbol': 'SUNDRMFAST'
    },
    'SUPREMEIND.NS': {
        'name': 'Supreme Industries Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'SUPREMEIND'
    },
    'SUZLON.NS': {
        'name': 'Suzlon Energy Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'SUZLON'
    },
    'SWANCORP.NS': {
        'name': 'Swan Corp Ltd.',
        'sector': 'Chemicals',
        'symbol': 'SWANCORP'
    },
    'SWIGGY.NS': {
        'name': 'Swiggy Ltd.',
        'sector': 'Consumer Services',
        'symbol': 'SWIGGY'
    },
    'SYNGENE.NS': {
        'name': 'Syngene International Ltd.',
        'sector': 'Healthcare',
        'symbol': 'SYNGENE'
    },
    'SYRMA.NS': {
        'name': 'Syrma SGS Technology Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'SYRMA'
    },
    'TBOTEK.NS': {
        'name': 'TBO Tek Ltd.',
        'sector': 'Consumer Services',
        'symbol': 'TBOTEK'
    },
    'TVSMOTOR.NS': {
        'name': 'TVS Motor Company Ltd.',
        'sector': 'Automobile and Auto Components',
        'symbol': 'TVSMOTOR'
    },
    'TATACHEM.NS': {
        'name': 'Tata Chemicals Ltd.',
        'sector': 'Chemicals',
        'symbol': 'TATACHEM'
    },
    'TATACOMM.NS': {
        'name': 'Tata Communications Ltd.',
        'sector': 'Telecommunication',
        'symbol': 'TATACOMM'
    },
    'TCS.NS': {
        'name': 'Tata Consultancy Services Ltd.',
        'sector': 'Information Technology',
        'symbol': 'TCS'
    },
    'TATACONSUM.NS': {
        'name': 'Tata Consumer Products Ltd.',
        'sector': 'Fast Moving Consumer Goods',
        'symbol': 'TATACONSUM'
    },
    'TATAELXSI.NS': {
        'name': 'Tata Elxsi Ltd.',
        'sector': 'Information Technology',
        'symbol': 'TATAELXSI'
    },
    'TATAINVEST.NS': {
        'name': 'Tata Investment Corporation Ltd.',
        'sector': 'Financial Services',
        'symbol': 'TATAINVEST'
    },
    'TMPV.NS': {
        'name': 'Tata Motors Passenger Vehicles Ltd.',
        'sector': 'Automobile and Auto Components',
        'symbol': 'TMPV'
    },
    'TATAPOWER.NS': {
        'name': 'Tata Power Co. Ltd.',
        'sector': 'Power',
        'symbol': 'TATAPOWER'
    },
    'TATASTEEL.NS': {
        'name': 'Tata Steel Ltd.',
        'sector': 'Metals & Mining',
        'symbol': 'TATASTEEL'
    },
    'TATATECH.NS': {
        'name': 'Tata Technologies Ltd.',
        'sector': 'Information Technology',
        'symbol': 'TATATECH'
    },
    'TTML.NS': {
        'name': 'Tata Teleservices (Maharashtra) Ltd.',
        'sector': 'Telecommunication',
        'symbol': 'TTML'
    },
    'TECHM.NS': {
        'name': 'Tech Mahindra Ltd.',
        'sector': 'Information Technology',
        'symbol': 'TECHM'
    },
    'TECHNOE.NS': {
        'name': 'Techno Electric & Engineering Company Ltd.',
        'sector': 'Construction',
        'symbol': 'TECHNOE'
    },
    'TEJASNET.NS': {
        'name': 'Tejas Networks Ltd.',
        'sector': 'Telecommunication',
        'symbol': 'TEJASNET'
    },
    'NIACL.NS': {
        'name': 'The New India Assurance Company Ltd.',
        'sector': 'Financial Services',
        'symbol': 'NIACL'
    },
    'RAMCOCEM.NS': {
        'name': 'The Ramco Cements Ltd.',
        'sector': 'Construction Materials',
        'symbol': 'RAMCOCEM'
    },
    'THERMAX.NS': {
        'name': 'Thermax Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'THERMAX'
    },
    'TIMKEN.NS': {
        'name': 'Timken India Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'TIMKEN'
    },
    'TITAGARH.NS': {
        'name': 'Titagarh Rail Systems Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'TITAGARH'
    },
    'TITAN.NS': {
        'name': 'Titan Company Ltd.',
        'sector': 'Consumer Durables',
        'symbol': 'TITAN'
    },
    'TORNTPHARM.NS': {
        'name': 'Torrent Pharmaceuticals Ltd.',
        'sector': 'Healthcare',
        'symbol': 'TORNTPHARM'
    },
    'TORNTPOWER.NS': {
        'name': 'Torrent Power Ltd.',
        'sector': 'Power',
        'symbol': 'TORNTPOWER'
    },
    'TARIL.NS': {
        'name': 'Transformers And Rectifiers (India) Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'TARIL'
    },
    'TRENT.NS': {
        'name': 'Trent Ltd.',
        'sector': 'Consumer Services',
        'symbol': 'TRENT'
    },
    'TRIDENT.NS': {
        'name': 'Trident Ltd.',
        'sector': 'Textiles',
        'symbol': 'TRIDENT'
    },
    'TRIVENI.NS': {
        'name': 'Triveni Engineering & Industries Ltd.',
        'sector': 'Fast Moving Consumer Goods',
        'symbol': 'TRIVENI'
    },
    'TRITURBINE.NS': {
        'name': 'Triveni Turbine Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'TRITURBINE'
    },
    'TIINDIA.NS': {
        'name': 'Tube Investments of India Ltd.',
        'sector': 'Automobile and Auto Components',
        'symbol': 'TIINDIA'
    },
    'UCOBANK.NS': {
        'name': 'UCO Bank',
        'sector': 'Financial Services',
        'symbol': 'UCOBANK'
    },
    'UNOMINDA.NS': {
        'name': 'UNO Minda Ltd.',
        'sector': 'Automobile and Auto Components',
        'symbol': 'UNOMINDA'
    },
    'UPL.NS': {
        'name': 'UPL Ltd.',
        'sector': 'Chemicals',
        'symbol': 'UPL'
    },
    'UTIAMC.NS': {
        'name': 'UTI Asset Management Company Ltd.',
        'sector': 'Financial Services',
        'symbol': 'UTIAMC'
    },
    'ULTRACEMCO.NS': {
        'name': 'UltraTech Cement Ltd.',
        'sector': 'Construction Materials',
        'symbol': 'ULTRACEMCO'
    },
    'UNIONBANK.NS': {
        'name': 'Union Bank of India',
        'sector': 'Financial Services',
        'symbol': 'UNIONBANK'
    },
    'UBL.NS': {
        'name': 'United Breweries Ltd.',
        'sector': 'Fast Moving Consumer Goods',
        'symbol': 'UBL'
    },
    'UNITDSPR.NS': {
        'name': 'United Spirits Ltd.',
        'sector': 'Fast Moving Consumer Goods',
        'symbol': 'UNITDSPR'
    },
    'USHAMART.NS': {
        'name': 'Usha Martin Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'USHAMART'
    },
    'VGUARD.NS': {
        'name': 'V-Guard Industries Ltd.',
        'sector': 'Consumer Durables',
        'symbol': 'VGUARD'
    },
    'DBREALTY.NS': {
        'name': 'Valor Estate Ltd.',
        'sector': 'Consumer Services',
        'symbol': 'DBREALTY'
    },
    'VTL.NS': {
        'name': 'Vardhman Textiles Ltd.',
        'sector': 'Textiles',
        'symbol': 'VTL'
    },
    'VBL.NS': {
        'name': 'Varun Beverages Ltd.',
        'sector': 'Fast Moving Consumer Goods',
        'symbol': 'VBL'
    },
    'MANYAVAR.NS': {
        'name': 'Vedant Fashions Ltd.',
        'sector': 'Consumer Services',
        'symbol': 'MANYAVAR'
    },
    'VEDL.NS': {
        'name': 'Vedanta Ltd.',
        'sector': 'Metals & Mining',
        'symbol': 'VEDL'
    },
    'VENTIVE.NS': {
        'name': 'Ventive Hospitality Ltd.',
        'sector': 'Consumer Services',
        'symbol': 'VENTIVE'
    },
    'VIJAYA.NS': {
        'name': 'Vijaya Diagnostic Centre Ltd.',
        'sector': 'Healthcare',
        'symbol': 'VIJAYA'
    },
    'VMM.NS': {
        'name': 'Vishal Mega Mart Ltd.',
        'sector': 'Consumer Services',
        'symbol': 'VMM'
    },
    'IDEA.NS': {
        'name': 'Vodafone Idea Ltd.',
        'sector': 'Telecommunication',
        'symbol': 'IDEA'
    },
    'VOLTAS.NS': {
        'name': 'Voltas Ltd.',
        'sector': 'Consumer Durables',
        'symbol': 'VOLTAS'
    },
    'WAAREEENER.NS': {
        'name': 'Waaree Energies Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'WAAREEENER'
    },
    'WELCORP.NS': {
        'name': 'Welspun Corp Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'WELCORP'
    },
    'WELSPUNLIV.NS': {
        'name': 'Welspun Living Ltd.',
        'sector': 'Textiles',
        'symbol': 'WELSPUNLIV'
    },
    'WHIRLPOOL.NS': {
        'name': 'Whirlpool of India Ltd.',
        'sector': 'Consumer Durables',
        'symbol': 'WHIRLPOOL'
    },
    'WIPRO.NS': {
        'name': 'Wipro Ltd.',
        'sector': 'Information Technology',
        'symbol': 'WIPRO'
    },
    'WOCKPHARMA.NS': {
        'name': 'Wockhardt Ltd.',
        'sector': 'Healthcare',
        'symbol': 'WOCKPHARMA'
    },
    'YESBANK.NS': {
        'name': 'Yes Bank Ltd.',
        'sector': 'Financial Services',
        'symbol': 'YESBANK'
    },
    'ZFCVINDIA.NS': {
        'name': 'ZF Commercial Vehicle Control Systems India Ltd.',
        'sector': 'Automobile and Auto Components',
        'symbol': 'ZFCVINDIA'
    },
    'ZEEL.NS': {
        'name': 'Zee Entertainment Enterprises Ltd.',
        'sector': 'Media Entertainment & Publication',
        'symbol': 'ZEEL'
    },
    'ZENTEC.NS': {
        'name': 'Zen Technologies Ltd.',
        'sector': 'Capital Goods',
        'symbol': 'ZENTEC'
    },
    'ZENSARTECH.NS': {
        'name': 'Zensar Technolgies Ltd.',
        'sector': 'Information Technology',
        'symbol': 'ZENSARTECH'
    },
    'ZYDUSLIFE.NS': {
        'name': 'Zydus Lifesciences Ltd.',
        'sector': 'Healthcare',
        'symbol': 'ZYDUSLIFE'
    },
    'ECLERX.NS': {
        'name': 'eClerx Services Ltd.',
        'sector': 'Services',
        'symbol': 'ECLERX'
    }
}


def get_all_stocks() -> List[str]:
    """Get list of all NSE 500 tickers."""
    return list(NIFTY_500_STOCKS.keys())


def get_all_sectors() -> List[str]:
    """Get list of all unique sectors."""
    sectors = set()
    for stock_data in NIFTY_500_STOCKS.values():
        sectors.add(stock_data['sector'])
    return sorted(list(sectors))


def search_stocks(query: str) -> List[str]:
    """
    Search stocks by name or symbol.
    
    Args:
        query: Search term (case-insensitive)
        
    Returns:
        List of matching tickers
    """
    query = query.upper()
    results = []
    
    for ticker, data in NIFTY_500_STOCKS.items():
        if (query in data['name'].upper() or 
            query in data['symbol'].upper() or
            query in ticker.upper()):
            results.append(ticker)
    
    return results


def get_stock_info(ticker: str) -> Dict:
    """
    Get detailed info about a stock.
    
    Args:
        ticker: Stock ticker (e.g., 'RELIANCE.NS')
        
    Returns:
        Dictionary with stock information
    """
    return NIFTY_500_STOCKS.get(ticker, {})


def get_stocks_by_sector(sector: str) -> List[str]:
    """
    Get all stocks in a specific sector.
    
    Args:
        sector: Sector name
        
    Returns:
        List of tickers in that sector
    """
    results = []
    for ticker, data in NIFTY_500_STOCKS.items():
        if data['sector'] == sector:
            results.append(ticker)
    return results
