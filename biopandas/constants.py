from typing import Dict

ATOMIC_MASSES: Dict[str, float] = {"C": 12.0107, "O": 15.9994, "N": 14.0067, "S": 32.065}

protein_letters_3to1_extended: Dict[str, str] = {
    "A5N": "N", "A8E": "V", "A9D": "S", "AA3": "A", "AA4": "A", "AAR": "R",
    "ABA": "A", "ACL": "R", "AEA": "C", "AEI": "D", "AFA": "N", "AGM": "R",
    "AGQ": "Y", "AGT": "C", "AHB": "N", "AHL": "R", "AHO": "A", "AHP": "A",
    "AIB": "A", "AKL": "D", "AKZ": "D", "ALA": "A", "ALC": "A", "ALM": "A",
    "ALN": "A", "ALO": "T", "ALS": "A", "ALT": "A", "ALV": "A", "ALY": "K",
    "AME": "M", "AN6": "L", "AN8": "A", "API": "K", "APK": "K", "AR2": "R",
    "AR4": "E", "AR7": "R", "ARG": "R", "ARM": "R", "ARO": "R", "AS7": "N",
    "ASA": "D", "ASB": "D", "ASI": "D", "ASK": "D", "ASL": "D", "ASN": "N",
    "ASP": "D", "ASQ": "D", "AYA": "A", "AZH": "A", "AZK": "K", "AZS": "S",
    "AZY": "Y", "AVJ": "H", "A30": "Y", "A3U": "F", "ECC": "Q", "ECX": "C",
    "EFC": "C", "EHP": "F", "ELY": "K", "EME": "E", "EPM": "M", "EPQ": "Q",
    "ESB": "Y", "ESC": "M", "EXY": "L", "EXA": "K", "E0Y": "P", "E9V": "H",
    "E9M": "W", "EJA": "C", "EUP": "T", "EZY": "G", "E9C": "Y", "EW6": "S",
    "EXL": "W", "I2M": "I", "I4G": "G", "I58": "K", "IAM": "A", "IAR": "R",
    "ICY": "C", "IEL": "K", "IGL": "G", "IIL": "I", "ILE": "I", "ILG": "E",
    "ILM": "I", "ILX": "I", "ILY": "K", "IML": "I", "IOR": "R", "IPG": "G",
    "IT1": "K", "IYR": "Y", "IZO": "M", "IC0": "G", "M0H": "C", "M2L": "K",
    "M2S": "M", "M30": "G", "M3L": "K", "M3R": "K", "MA ": "A", "MAA": "A",
    "MAI": "R", "MBQ": "Y", "MC1": "S", "MCL": "K", "MCS": "C", "MD3": "C",
    "MD5": "C", "MD6": "G", "MDF": "Y", "ME0": "M", "MEA": "F", "MEG": "E",
    "MEN": "N", "MEQ": "Q", "MET": "M", "MEU": "G", "MFN": "E", "MGG": "R",
    "MGN": "Q", "MGY": "G", "MH1": "H", "MH6": "S", "MHL": "L", "MHO": "M",
    "MHS": "H", "MHU": "F", "MIR": "S", "MIS": "S", "MK8": "L", "ML3": "K",
    "MLE": "L", "MLL": "L", "MLY": "K", "MLZ": "K", "MME": "M", "MMO": "R",
    "MNL": "L", "MNV": "V", "MP8": "P", "MPQ": "G", "MSA": "G", "MSE": "M",
    "MSL": "M", "MSO": "M", "MT2": "M", "MTY": "Y", "MVA": "V", "MYK": "K",
    "MYN": "R", "QCS": "C", "QIL": "I", "QMM": "Q", "QPA": "C", "QPH": "F",
    "Q3P": "K", "QVA": "C", "QX7": "A", "Q2E": "W", "Q75": "M", "Q78": "F",
    "QM8": "L", "QMB": "A", "QNQ": "C", "QNT": "C", "QNW": "C", "QO2": "C",
    "QO5": "C", "QO8": "C", "QQ8": "Q", "U2X": "Y", "U3X": "F", "UF0": "S",
    "UGY": "G", "UM1": "A", "UM2": "A", "UMA": "A", "UQK": "A", "UX8": "W",
    "UXQ": "F", "YCM": "C", "YOF": "Y", "YPR": "P", "YPZ": "Y", "YTH": "T",
    "Y1V": "L", "Y57": "K", "YHA": "K", "200": "F", "23F": "F", "23P": "A",
    "26B": "T", "28X": "T", "2AG": "A", "2CO": "C", "2FM": "M", "2GX": "F",
    "2HF": "H", "2JG": "S", "2KK": "K", "2KP": "K", "2LT": "Y", "2LU": "L",
    "2ML": "L", "2MR": "R", "2MT": "P", "2OR": "R", "2P0": "P", "2QZ": "T",
    "2R3": "Y", "2RA": "A", "2RX": "S", "2SO": "H", "2TY": "Y", "2VA": "V",
    "2XA": "C", "2ZC": "S", "6CL": "K", "6CW": "W", "6GL": "A", "6HN": "K",
    "60F": "C", "66D": "I", "6CV": "A", "6M6": "C", "6V1": "C", "6WK": "C",
    "6Y9": "P", "6DN": "K", "DA2": "R", "DAB": "A", "DAH": "F", "DBS": "S",
    "DBU": "T", "DBY": "Y", "DBZ": "A", "DC2": "C", "DDE": "H", "DDZ": "A",
    "DI7": "Y", "DHA": "S", "DHN": "V", "DIR": "R", "DLS": "K", "DM0": "K",
    "DMH": "N", "DMK": "D", "DNL": "K", "DNP": "A", "DNS": "K", "DNW": "A",
    "DOH": "D", "DON": "L", "DP1": "R", "DPL": "P", "DPP": "A", "DPQ": "Y",
    "DYS": "C", "D2T": "D", "DYA": "D", "DJD": "F", "DYJ": "P", "DV9": "E",
    "H14": "F", "H1D": "M", "H5M": "P", "HAC": "A", "HAR": "R", "HBN": "H",
    "HCM": "C", "HGY": "G", "HHI": "H", "HIA": "H", "HIC": "H", "HIP": "H",
    "HIQ": "H", "HIS": "H", "HL2": "L", "HLU": "L", "HMR": "R", "HNC": "C",
    "HOX": "F", "HPC": "F", "HPE": "F", "HPH": "F", "HPQ": "F", "HQA": "A",
    "HR7": "R", "HRG": "R", "HRP": "W", "HS8": "H", "HS9": "H", "HSE": "S",
    "HSK": "H", "HSL": "S", "HSO": "H", "HT7": "W", "HTI": "C", "HTR": "W",
    "HV5": "A", "HVA": "V", "HY3": "P", "HYI": "M", "HYP": "P", "HZP": "P",
    "HIX": "A", "HSV": "H", "HLY": "K", "HOO": "H", "H7V": "A", "L5P": "K",
    "LRK": "K", "L3O": "L", "LA2": "K", "LAA": "D", "LAL": "A", "LBY": "K",
    "LCK": "K", "LCX": "K", "LDH": "K", "LE1": "V", "LED": "L", "LEF": "L",
    "LEH": "L", "LEM": "L", "LEN": "L", "LET": "K", "LEU": "L", "LEX": "L",
    "LGY": "K", "LLO": "K", "LLP": "K", "LLY": "K", "LLZ": "K", "LME": "E",
    "LMF": "K", "LMQ": "Q", "LNE": "L", "LNM": "L", "LP6": "K", "LPD": "P",
    "LPG": "G", "LPS": "S", "LSO": "K", "LTR": "W", "LVG": "G", "LVN": "V",
    "LWY": "P", "LYF": "K", "LYK": "K", "LYM": "K", "LYN": "K", "LYO": "K",
    "LYP": "K", "LYR": "K", "LYS": "K", "LYU": "K", "LYX": "K", "LYZ": "K",
    "LAY": "L", "LWI": "F", "LBZ": "K", "P1L": "C", "P2Q": "Y", "P2Y": "P",
    "P3Q": "Y", "PAQ": "Y", "PAS": "D", "PAT": "W", "PBB": "C", "PBF": "F",
    "PCA": "Q", "PCC": "P", "PCS": "F", "PE1": "K", "PEC": "C", "PF5": "F",
    "PFF": "F", "PG1": "S", "PGY": "G", "PHA": "F", "PHD": "D", "PHE": "F",
    "PHI": "F", "PHL": "F", "PHM": "F", "PKR": "P", "PLJ": "P", "PM3": "F",
    "POM": "P", "PPN": "F", "PR3": "C", "PR4": "P", "PR7": "P", "PR9": "P",
    "PRJ": "P", "PRK": "K", "PRO": "P", "PRS": "P", "PRV": "G", "PSA": "F",
    "PSH": "H", "PTH": "Y", "PTM": "Y", "PTR": "Y", "PVH": "H", "PXU": "P",
    "PYA": "A", "PYH": "K", "PYX": "C", "PH6": "P", "P9S": "C", "P5U": "S",
    "POK": "R", "T0I": "Y", "T11": "F", "TAV": "D", "TBG": "V", "TBM": "T",
    "TCQ": "Y", "TCR": "W", "TEF": "F", "TFQ": "F", "TH5": "T", "TH6": "T",
    "THC": "T", "THR": "T", "THZ": "R", "TIH": "A", "TIS": "S", "TLY": "K",
    "TMB": "T", "TMD": "T", "TNB": "C", "TNR": "S", "TNY": "T", "TOQ": "W",
    "TOX": "W", "TPJ": "P", "TPK": "P", "TPL": "W", "TPO": "T", "TPQ": "Y",
    "TQI": "W", "TQQ": "W", "TQZ": "C", "TRF": "W", "TRG": "K", "TRN": "W",
    "TRO": "W", "TRP": "W", "TRQ": "W", "TRW": "W", "TRX": "W", "TRY": "W",
    "TS9": "I", "TSY": "C", "TTQ": "W", "TTS": "Y", "TXY": "Y", "TY1": "Y",
    "TY2": "Y", "TY3": "Y", "TY5": "Y", "TY8": "Y", "TY9": "Y", "TYB": "Y",
    "TYC": "Y", "TYE": "Y", "TYI": "Y", "TYJ": "Y", "TYN": "Y", "TYO": "Y",
    "TYQ": "Y", "TYR": "Y", "TYS": "Y", "TYT": "Y", "TYW": "Y", "TYY": "Y",
    "T8L": "T", "T9E": "T", "TNQ": "W", "TSQ": "F", "TGH": "W", "X2W": "E",
    "XCN": "C", "XPR": "P", "XSN": "N", "XW1": "A", "XX1": "K", "XYC": "A",
    "XA6": "F", "11Q": "P", "11W": "E", "12L": "P", "12X": "P", "12Y": "P",
    "143": "C", "1AC": "A", "1L1": "A", "1OP": "Y", "1PA": "F", "1PI": "A",
    "1TQ": "W", "1TY": "Y", "1X6": "S", "56A": "H", "5AB": "A", "5CS": "C",
    "5CW": "W", "5HP": "E", "5OH": "A", "5PG": "G", "51T": "Y", "54C": "W",
    "5CR": "F", "5CT": "K", "5FQ": "A", "5GM": "I", "5JP": "S", "5T3": "K",
    "5MW": "K", "5OW": "K", "5R5": "S", "5VV": "N", "5XU": "A", "55I": "F",
    "999": "D", "9DN": "N", "9NE": "E", "9NF": "F", "9NR": "R", "9NV": "V",
    "9E7": "K", "9KP": "K", "9WV": "A", "9TR": "K", "9TU": "K", "9TX": "K",
    "9U0": "K", "9IJ": "F", "B1F": "F", "B27": "T", "B2A": "A", "B2F": "F",
    "B2I": "I", "B2V": "V", "B3A": "A", "B3D": "D", "B3E": "E", "B3K": "K",
    "B3U": "H", "B3X": "N", "B3Y": "Y", "BB6": "C", "BB7": "C", "BB8": "F",
    "BB9": "C", "BBC": "C", "BCS": "C", "BCX": "C", "BFD": "D", "BG1": "S",
    "BH2": "D", "BHD": "D", "BIF": "F", "BIU": "I", "BL2": "L", "BLE": "L",
    "BLY": "K", "BMT": "T", "BNN": "F", "BOR": "R", "BP5": "A", "BPE": "C",
    "BSE": "S", "BTA": "L", "BTC": "C", "BTK": "K", "BTR": "W", "BUC": "C",
    "BUG": "V", "BYR": "Y", "BWV": "R", "BWB": "S", "BXT": "S", "F2F": "F",
    "F2Y": "Y", "FAK": "K", "FB5": "A", "FB6": "A", "FC0": "F", "FCL": "F",
    "FDL": "K", "FFM": "C", "FGL": "G", "FGP": "S", "FH7": "K", "FHL": "K",
    "FHO": "K", "FIO": "R", "FLA": "A", "FLE": "L", "FLT": "Y", "FME": "M",
    "FOE": "C", "FP9": "P", "FPK": "P", "FT6": "W", "FTR": "W", "FTY": "Y",
    "FVA": "V", "FZN": "K", "FY3": "Y", "F7W": "W", "FY2": "Y", "FQA": "K",
    "F7Q": "Y", "FF9": "K", "FL6": "D", "JJJ": "C", "JJK": "C", "JJL": "C",
    "JLP": "K", "J3D": "C", "J9Y": "R", "J8W": "S", "JKH": "P", "N10": "S",
    "N7P": "P", "NA8": "A", "NAL": "A", "NAM": "A", "NBQ": "Y", "NC1": "S",
    "NCB": "A", "NEM": "H", "NEP": "H", "NFA": "F", "NIY": "Y", "NLB": "L",
    "NLE": "L", "NLN": "L", "NLO": "L", "NLP": "L", "NLQ": "Q", "NLY": "G",
    "NMC": "G", "NMM": "R", "NNH": "R", "NOT": "L", "NPH": "C", "NPI": "A",
    "NTR": "Y", "NTY": "Y", "NVA": "V", "NWD": "A", "NYB": "C", "NYS": "C",
    "NZH": "H", "N80": "P", "NZC": "T", "NLW": "L", "N0A": "F", "N9P": "A",
    "N65": "K", "R1A": "C", "R4K": "W", "RE0": "W", "RE3": "W", "RGL": "R",
    "RGP": "E", "RT0": "P", "RVX": "S", "RZ4": "S", "RPI": "R", "RVJ": "A",
    "VAD": "V", "VAF": "V", "VAH": "V", "VAI": "V", "VAL": "V", "VB1": "K",
    "VH0": "P", "VR0": "R", "V44": "C", "V61": "F", "VPV": "K", "V5N": "H",
    "V7T": "K", "Z01": "A", "Z3E": "T", "Z70": "H", "ZBZ": "C", "ZCL": "F",
    "ZU0": "T", "ZYJ": "P", "ZYK": "P", "ZZD": "C", "ZZJ": "A", "ZIQ": "W",
    "ZPO": "P", "ZDJ": "Y", "ZT1": "K", "30V": "C", "31Q": "C", "33S": "F",
    "33W": "A", "34E": "V", "3AH": "H", "3BY": "P", "3CF": "F", "3CT": "Y",
    "3GA": "A", "3GL": "E", "3MD": "D", "3MY": "Y", "3NF": "Y", "3O3": "E",
    "3PX": "P", "3QN": "K", "3TT": "P", "3XH": "G", "3YM": "Y", "3WS": "A",
    "3WX": "P", "3X9": "C", "3ZH": "H", "7JA": "I", "73C": "S", "73N": "R",
    "73O": "Y", "73P": "K", "74P": "K", "7N8": "F", "7O5": "A", "7XC": "F",
    "7ID": "D", "7OZ": "A", "C1S": "C", "C1T": "C", "C1X": "K", "C22": "A",
    "C3Y": "C", "C4R": "C", "C5C": "C", "C6C": "C", "CAF": "C", "CAS": "C",
    "CAY": "C", "CCS": "C", "CEA": "C", "CGA": "E", "CGU": "E", "CGV": "C",
    "CHP": "G", "CIR": "R", "CLE": "L", "CLG": "K", "CLH": "K", "CME": "C",
    "CMH": "C", "CML": "C", "CMT": "C", "CR5": "G", "CS0": "C", "CS1": "C",
    "CS3": "C", "CS4": "C", "CSA": "C", "CSB": "C", "CSD": "C", "CSE": "C",
    "CSJ": "C", "CSO": "C", "CSP": "C", "CSR": "C", "CSS": "C", "CSU": "C",
    "CSW": "C", "CSX": "C", "CSZ": "C", "CTE": "W", "CTH": "T", "CWD": "A",
    "CWR": "S", "CXM": "M", "CY0": "C", "CY1": "C", "CY3": "C", "CY4": "C",
    "CYA": "C", "CYD": "C", "CYF": "C", "CYG": "C", "CYJ": "K", "CYM": "C",
    "CYQ": "C", "CYR": "C", "CYS": "C", "CYW": "C", "CZ2": "C", "CZZ": "C",
    "CG6": "C", "C1J": "R", "C4G": "R", "C67": "R", "C6D": "R", "CE7": "N",
    "CZS": "A", "G01": "E", "G8M": "E", "GAU": "E", "GEE": "G", "GFT": "S",
    "GHC": "E", "GHG": "Q", "GHW": "E", "GL3": "G", "GLH": "Q", "GLJ": "E",
    "GLK": "E", "GLN": "Q", "GLQ": "E", "GLU": "E", "GLY": "G", "GLZ": "G",
    "GMA": "E", "GME": "E", "GNC": "Q", "GPL": "K", "GSC": "G", "GSU": "E",
    "GT9": "C", "GVL": "S", "G3M": "R", "G5G": "L", "G1X": "Y", "G8X": "P",
    "K1R": "C", "KBE": "K", "KCX": "K", "KFP": "K", "KGC": "K", "KNB": "A",
    "KOR": "M", "KPI": "K", "KPY": "K", "KST": "K", "KYN": "W", "KYQ": "K",
    "KCR": "K", "KPF": "K", "K5L": "S", "KEO": "K", "KHB": "K", "KKD": "D",
    "K5H": "C", "K7K": "S", "OAR": "R", "OAS": "S", "OBS": "K", "OCS": "C",
    "OCY": "C", "OHI": "H", "OHS": "D", "OLD": "H", "OLT": "T", "OLZ": "S",
    "OMH": "S", "OMT": "M", "OMX": "Y", "OMY": "Y", "ONH": "A", "ORN": "A",
    "ORQ": "R", "OSE": "S", "OTH": "T", "OXX": "D", "OYL": "H", "O7A": "T",
    "O7D": "W", "O7G": "V", "O2E": "S", "O6H": "W", "OZW": "F", "S12": "S",
    "S1H": "S", "S2C": "C", "S2P": "A", "SAC": "S", "SAH": "C", "SAR": "G",
    "SBG": "S", "SBL": "S", "SCH": "C", "SCS": "C", "SCY": "C", "SD4": "N",
    "SDB": "S", "SDP": "S", "SEB": "S", "SEE": "S", "SEG": "A", "SEL": "S",
    "SEM": "S", "SEN": "S", "SEP": "S", "SER": "S", "SET": "S", "SGB": "S",
    "SHC": "C", "SHP": "G", "SHR": "K", "SIB": "C", "SLL": "K", "SLZ": "K",
    "SMC": "C", "SME": "M", "SMF": "F", "SNC": "C", "SNN": "N", "SOY": "S",
    "SRZ": "S", "STY": "Y", "SUN": "S", "SVA": "S", "SVV": "S", "SVW": "S",
    "SVX": "S", "SVY": "S", "SVZ": "S", "SXE": "S", "SKH": "K", "SNM": "S",
    "SNK": "H", "SWW": "S", "WFP": "F", "WLU": "L", "WPA": "F", "WRP": "W",
    "WVL": "V", "02K": "A", "02L": "N", "02O": "A", "02Y": "A", "033": "V",
    "037": "P", "03Y": "C", "04U": "P", "04V": "P", "05N": "P", "07O": "C",
    "0A0": "D", "0A1": "Y", "0A2": "K", "0A8": "C", "0A9": "F", "0AA": "V",
    "0AB": "V", "0AC": "G", "0AF": "W", "0AG": "L", "0AH": "S", "0AK": "D",
    "0AR": "R", "0BN": "F", "0CS": "A", "0E5": "T", "0EA": "Y", "0FL": "A",
    "0LF": "P", "0NC": "A", "0PR": "Y", "0QL": "C", "0TD": "D", "0UO": "W",
    "0WZ": "Y", "0X9": "R", "0Y8": "P", "4AF": "F", "4AR": "R", "4AW": "W",
    "4BF": "F", "4CF": "F", "4CY": "M", "4DP": "W", "4FB": "P", "4FW": "W",
    "4HL": "Y", "4HT": "W", "4IN": "W", "4MM": "M", "4PH": "F", "4U7": "A",
    "41H": "F", "41Q": "N", "42Y": "S", "432": "S", "45F": "P", "4AK": "K",
    "4D4": "R", "4GJ": "C", "4KY": "P", "4L0": "P", "4LZ": "Y", "4N7": "P",
    "4N8": "P", "4N9": "P", "4OG": "W", "4OU": "F", "4OV": "S", "4OZ": "S",
    "4PQ": "W", "4SJ": "F", "4WQ": "A", "4HH": "S", "4HJ": "S", "4J4": "C",
    "4J5": "R", "4II": "F", "4VI": "R", "823": "N", "8SP": "S", "8AY": "A",
}