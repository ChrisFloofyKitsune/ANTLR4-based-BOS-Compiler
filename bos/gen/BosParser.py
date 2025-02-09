# Generated from E:/antlr_domain_specifc_lang_stuff/book/part2/bos/BosParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,87,506,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,58,2,59,
        7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,1,0,5,0,130,8,0,10,
        0,12,0,133,9,0,1,1,1,1,1,1,3,1,138,8,1,1,2,1,2,1,2,1,2,5,2,144,8,
        2,10,2,12,2,147,9,2,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,4,5,4,157,8,4,
        10,4,12,4,160,9,4,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,
        6,173,8,6,1,6,1,6,1,7,1,7,1,8,3,8,180,8,8,1,9,1,9,1,9,5,9,185,8,
        9,10,9,12,9,188,9,9,1,10,1,10,1,11,1,11,5,11,194,8,11,10,11,12,11,
        197,9,11,1,11,1,11,3,11,201,8,11,1,12,1,12,1,12,1,12,1,12,1,12,1,
        12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,216,8,12,1,13,1,13,1,13,1,
        13,1,13,1,13,3,13,224,8,13,1,14,1,14,1,14,1,15,1,15,1,15,1,16,1,
        16,1,16,1,16,1,16,1,16,3,16,238,8,16,1,17,1,17,1,17,1,18,1,18,1,
        18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,257,
        8,19,1,19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,
        1,20,1,20,1,20,3,20,287,8,20,1,21,1,21,3,21,291,8,21,1,22,1,22,1,
        22,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,25,1,25,1,26,1,26,1,
        27,1,27,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,1,28,1,
        28,1,29,1,29,1,29,3,29,325,8,29,1,30,1,30,1,30,1,30,1,30,1,30,1,
        30,3,30,334,8,30,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,3,32,344,
        8,32,1,33,1,33,1,33,1,34,1,34,1,34,1,34,1,34,1,35,1,35,1,35,1,35,
        1,35,1,36,1,36,1,36,1,36,1,36,1,37,1,37,1,37,1,37,1,37,1,37,1,37,
        1,38,1,38,1,38,1,39,1,39,1,39,1,40,1,40,1,40,1,40,1,40,1,41,1,41,
        1,41,1,41,1,41,1,41,1,42,1,42,1,42,1,42,1,42,1,42,1,43,1,43,1,43,
        1,44,1,44,1,44,1,45,1,45,1,45,1,45,1,45,1,46,1,46,1,46,1,47,1,47,
        1,47,1,48,1,48,1,48,1,49,1,49,1,49,1,50,1,50,1,50,1,51,3,51,421,
        8,51,1,52,1,52,5,52,425,8,52,10,52,12,52,428,9,52,1,53,1,53,1,53,
        1,53,1,53,3,53,435,8,53,1,53,3,53,438,8,53,1,53,3,53,441,8,53,1,
        53,1,53,1,53,1,53,3,53,447,8,53,1,54,1,54,1,54,1,55,1,55,5,55,454,
        8,55,10,55,12,55,457,9,55,1,56,1,56,1,56,1,57,1,57,1,57,1,57,1,57,
        1,57,1,57,1,57,1,57,1,57,1,57,1,57,3,57,474,8,57,1,58,1,58,1,58,
        1,58,1,58,1,58,1,58,1,59,1,59,1,60,1,60,1,60,1,60,1,60,1,60,1,60,
        1,60,1,60,1,60,3,60,495,8,60,1,61,1,61,1,62,1,62,1,62,1,62,1,62,
        1,63,1,63,1,63,0,0,64,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
        32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,
        76,78,80,82,84,86,88,90,92,94,96,98,100,102,104,106,108,110,112,
        114,116,118,120,122,124,126,0,7,1,0,72,74,2,0,11,11,28,28,1,0,12,
        14,1,0,10,11,1,0,22,25,1,0,20,21,1,0,76,79,511,0,131,1,0,0,0,2,137,
        1,0,0,0,4,139,1,0,0,0,6,150,1,0,0,0,8,152,1,0,0,0,10,163,1,0,0,0,
        12,165,1,0,0,0,14,176,1,0,0,0,16,179,1,0,0,0,18,181,1,0,0,0,20,189,
        1,0,0,0,22,200,1,0,0,0,24,215,1,0,0,0,26,223,1,0,0,0,28,225,1,0,
        0,0,30,228,1,0,0,0,32,231,1,0,0,0,34,239,1,0,0,0,36,242,1,0,0,0,
        38,248,1,0,0,0,40,286,1,0,0,0,42,288,1,0,0,0,44,292,1,0,0,0,46,295,
        1,0,0,0,48,298,1,0,0,0,50,303,1,0,0,0,52,305,1,0,0,0,54,307,1,0,
        0,0,56,314,1,0,0,0,58,324,1,0,0,0,60,326,1,0,0,0,62,335,1,0,0,0,
        64,338,1,0,0,0,66,345,1,0,0,0,68,348,1,0,0,0,70,353,1,0,0,0,72,358,
        1,0,0,0,74,363,1,0,0,0,76,370,1,0,0,0,78,373,1,0,0,0,80,376,1,0,
        0,0,82,381,1,0,0,0,84,387,1,0,0,0,86,393,1,0,0,0,88,396,1,0,0,0,
        90,399,1,0,0,0,92,404,1,0,0,0,94,407,1,0,0,0,96,410,1,0,0,0,98,413,
        1,0,0,0,100,416,1,0,0,0,102,420,1,0,0,0,104,422,1,0,0,0,106,446,
        1,0,0,0,108,448,1,0,0,0,110,451,1,0,0,0,112,458,1,0,0,0,114,473,
        1,0,0,0,116,475,1,0,0,0,118,482,1,0,0,0,120,494,1,0,0,0,122,496,
        1,0,0,0,124,498,1,0,0,0,126,503,1,0,0,0,128,130,3,2,1,0,129,128,
        1,0,0,0,130,133,1,0,0,0,131,129,1,0,0,0,131,132,1,0,0,0,132,1,1,
        0,0,0,133,131,1,0,0,0,134,138,3,4,2,0,135,138,3,8,4,0,136,138,3,
        12,6,0,137,134,1,0,0,0,137,135,1,0,0,0,137,136,1,0,0,0,138,3,1,0,
        0,0,139,140,5,36,0,0,140,145,3,6,3,0,141,142,5,1,0,0,142,144,3,6,
        3,0,143,141,1,0,0,0,144,147,1,0,0,0,145,143,1,0,0,0,145,146,1,0,
        0,0,146,148,1,0,0,0,147,145,1,0,0,0,148,149,5,8,0,0,149,5,1,0,0,
        0,150,151,5,86,0,0,151,7,1,0,0,0,152,153,5,34,0,0,153,158,3,10,5,
        0,154,155,5,1,0,0,155,157,3,10,5,0,156,154,1,0,0,0,157,160,1,0,0,
        0,158,156,1,0,0,0,158,159,1,0,0,0,159,161,1,0,0,0,160,158,1,0,0,
        0,161,162,5,8,0,0,162,9,1,0,0,0,163,164,5,86,0,0,164,11,1,0,0,0,
        165,172,3,14,7,0,166,167,5,2,0,0,167,173,5,3,0,0,168,169,5,2,0,0,
        169,170,3,16,8,0,170,171,5,3,0,0,171,173,1,0,0,0,172,166,1,0,0,0,
        172,168,1,0,0,0,173,174,1,0,0,0,174,175,3,22,11,0,175,13,1,0,0,0,
        176,177,5,86,0,0,177,15,1,0,0,0,178,180,3,18,9,0,179,178,1,0,0,0,
        179,180,1,0,0,0,180,17,1,0,0,0,181,186,3,20,10,0,182,183,5,1,0,0,
        183,185,3,20,10,0,184,182,1,0,0,0,185,188,1,0,0,0,186,184,1,0,0,
        0,186,187,1,0,0,0,187,19,1,0,0,0,188,186,1,0,0,0,189,190,5,86,0,
        0,190,21,1,0,0,0,191,195,5,4,0,0,192,194,3,24,12,0,193,192,1,0,0,
        0,194,197,1,0,0,0,195,193,1,0,0,0,195,196,1,0,0,0,196,198,1,0,0,
        0,197,195,1,0,0,0,198,201,5,5,0,0,199,201,3,24,12,0,200,191,1,0,
        0,0,200,199,1,0,0,0,201,23,1,0,0,0,202,203,3,40,20,0,203,204,5,8,
        0,0,204,216,1,0,0,0,205,206,3,46,23,0,206,207,5,8,0,0,207,216,1,
        0,0,0,208,216,3,32,16,0,209,216,3,36,18,0,210,216,3,38,19,0,211,
        212,3,26,13,0,212,213,5,8,0,0,213,216,1,0,0,0,214,216,5,8,0,0,215,
        202,1,0,0,0,215,205,1,0,0,0,215,208,1,0,0,0,215,209,1,0,0,0,215,
        210,1,0,0,0,215,211,1,0,0,0,215,214,1,0,0,0,216,25,1,0,0,0,217,218,
        3,10,5,0,218,219,5,9,0,0,219,220,3,110,55,0,220,224,1,0,0,0,221,
        224,3,28,14,0,222,224,3,30,15,0,223,217,1,0,0,0,223,221,1,0,0,0,
        223,222,1,0,0,0,224,27,1,0,0,0,225,226,5,15,0,0,226,227,3,10,5,0,
        227,29,1,0,0,0,228,229,5,16,0,0,229,230,3,10,5,0,230,31,1,0,0,0,
        231,232,5,30,0,0,232,233,5,2,0,0,233,234,3,110,55,0,234,235,5,3,
        0,0,235,237,3,22,11,0,236,238,3,34,17,0,237,236,1,0,0,0,237,238,
        1,0,0,0,238,33,1,0,0,0,239,240,5,31,0,0,240,241,3,22,11,0,241,35,
        1,0,0,0,242,243,5,32,0,0,243,244,5,2,0,0,244,245,3,110,55,0,245,
        246,5,3,0,0,246,247,3,22,11,0,247,37,1,0,0,0,248,249,5,33,0,0,249,
        250,5,2,0,0,250,251,3,110,55,0,251,252,5,8,0,0,252,253,3,110,55,
        0,253,254,5,8,0,0,254,256,3,110,55,0,255,257,5,8,0,0,256,255,1,0,
        0,0,256,257,1,0,0,0,257,258,1,0,0,0,258,259,5,3,0,0,259,260,3,22,
        11,0,260,39,1,0,0,0,261,287,3,82,41,0,262,287,3,84,42,0,263,287,
        3,60,30,0,264,287,3,64,32,0,265,287,3,54,27,0,266,287,3,56,28,0,
        267,287,3,68,34,0,268,287,3,70,35,0,269,287,3,72,36,0,270,287,3,
        44,22,0,271,287,3,76,38,0,272,287,3,78,39,0,273,287,3,80,40,0,274,
        287,3,86,43,0,275,287,3,88,44,0,276,287,3,48,24,0,277,287,3,50,25,
        0,278,287,3,90,45,0,279,287,3,92,46,0,280,287,3,42,21,0,281,287,
        3,74,37,0,282,287,3,94,47,0,283,287,3,96,48,0,284,287,3,98,49,0,
        285,287,3,100,50,0,286,261,1,0,0,0,286,262,1,0,0,0,286,263,1,0,0,
        0,286,264,1,0,0,0,286,265,1,0,0,0,286,266,1,0,0,0,286,267,1,0,0,
        0,286,268,1,0,0,0,286,269,1,0,0,0,286,270,1,0,0,0,286,271,1,0,0,
        0,286,272,1,0,0,0,286,273,1,0,0,0,286,274,1,0,0,0,286,275,1,0,0,
        0,286,276,1,0,0,0,286,277,1,0,0,0,286,278,1,0,0,0,286,279,1,0,0,
        0,286,280,1,0,0,0,286,281,1,0,0,0,286,282,1,0,0,0,286,283,1,0,0,
        0,286,284,1,0,0,0,286,285,1,0,0,0,287,41,1,0,0,0,288,290,5,66,0,
        0,289,291,3,110,55,0,290,289,1,0,0,0,290,291,1,0,0,0,291,43,1,0,
        0,0,292,293,5,57,0,0,293,294,3,110,55,0,294,45,1,0,0,0,295,296,5,
        35,0,0,296,297,3,18,9,0,297,47,1,0,0,0,298,299,5,51,0,0,299,300,
        3,110,55,0,300,301,5,41,0,0,301,302,3,110,55,0,302,49,1,0,0,0,303,
        304,3,106,53,0,304,51,1,0,0,0,305,306,7,0,0,0,306,53,1,0,0,0,307,
        308,5,37,0,0,308,309,3,6,3,0,309,310,5,41,0,0,310,311,3,52,26,0,
        311,312,3,110,55,0,312,313,3,58,29,0,313,55,1,0,0,0,314,315,5,39,
        0,0,315,316,3,6,3,0,316,317,5,41,0,0,317,318,3,52,26,0,318,319,3,
        110,55,0,319,320,3,58,29,0,320,57,1,0,0,0,321,325,5,43,0,0,322,323,
        5,44,0,0,323,325,3,110,55,0,324,321,1,0,0,0,324,322,1,0,0,0,325,
        59,1,0,0,0,326,327,5,45,0,0,327,328,3,6,3,0,328,329,5,38,0,0,329,
        330,3,52,26,0,330,331,5,44,0,0,331,333,3,110,55,0,332,334,3,62,31,
        0,333,332,1,0,0,0,333,334,1,0,0,0,334,61,1,0,0,0,335,336,5,46,0,
        0,336,337,3,110,55,0,337,63,1,0,0,0,338,339,5,47,0,0,339,340,3,6,
        3,0,340,341,5,38,0,0,341,343,3,52,26,0,342,344,3,66,33,0,343,342,
        1,0,0,0,343,344,1,0,0,0,344,65,1,0,0,0,345,346,5,48,0,0,346,347,
        3,110,55,0,347,67,1,0,0,0,348,349,5,49,0,0,349,350,3,6,3,0,350,351,
        5,38,0,0,351,352,3,52,26,0,352,69,1,0,0,0,353,354,5,50,0,0,354,355,
        3,6,3,0,355,356,5,40,0,0,356,357,3,52,26,0,357,71,1,0,0,0,358,359,
        5,56,0,0,359,360,3,110,55,0,360,361,5,42,0,0,361,362,3,6,3,0,362,
        73,1,0,0,0,363,364,5,71,0,0,364,365,5,2,0,0,365,366,3,126,63,0,366,
        367,5,1,0,0,367,368,3,110,55,0,368,369,5,3,0,0,369,75,1,0,0,0,370,
        371,5,58,0,0,371,372,3,6,3,0,372,77,1,0,0,0,373,374,5,59,0,0,374,
        375,3,6,3,0,375,79,1,0,0,0,376,377,5,60,0,0,377,378,3,6,3,0,378,
        379,5,61,0,0,379,380,3,110,55,0,380,81,1,0,0,0,381,382,5,54,0,0,
        382,383,3,14,7,0,383,384,5,2,0,0,384,385,3,102,51,0,385,386,5,3,
        0,0,386,83,1,0,0,0,387,388,5,55,0,0,388,389,3,14,7,0,389,390,5,2,
        0,0,390,391,3,102,51,0,391,392,5,3,0,0,392,85,1,0,0,0,393,394,5,
        62,0,0,394,395,3,110,55,0,395,87,1,0,0,0,396,397,5,63,0,0,397,398,
        3,110,55,0,398,89,1,0,0,0,399,400,5,64,0,0,400,401,3,110,55,0,401,
        402,5,41,0,0,402,403,3,110,55,0,403,91,1,0,0,0,404,405,5,65,0,0,
        405,406,3,110,55,0,406,93,1,0,0,0,407,408,5,67,0,0,408,409,3,6,3,
        0,409,95,1,0,0,0,410,411,5,68,0,0,411,412,3,6,3,0,412,97,1,0,0,0,
        413,414,5,69,0,0,414,415,3,6,3,0,415,99,1,0,0,0,416,417,5,70,0,0,
        417,418,3,6,3,0,418,101,1,0,0,0,419,421,3,104,52,0,420,419,1,0,0,
        0,420,421,1,0,0,0,421,103,1,0,0,0,422,426,3,110,55,0,423,425,3,108,
        54,0,424,423,1,0,0,0,425,428,1,0,0,0,426,424,1,0,0,0,426,427,1,0,
        0,0,427,105,1,0,0,0,428,426,1,0,0,0,429,430,5,52,0,0,430,431,3,114,
        57,0,431,432,5,2,0,0,432,434,3,110,55,0,433,435,3,108,54,0,434,433,
        1,0,0,0,434,435,1,0,0,0,435,437,1,0,0,0,436,438,3,108,54,0,437,436,
        1,0,0,0,437,438,1,0,0,0,438,440,1,0,0,0,439,441,3,108,54,0,440,439,
        1,0,0,0,440,441,1,0,0,0,441,442,1,0,0,0,442,443,5,3,0,0,443,447,
        1,0,0,0,444,445,5,52,0,0,445,447,3,114,57,0,446,429,1,0,0,0,446,
        444,1,0,0,0,447,107,1,0,0,0,448,449,5,1,0,0,449,450,3,110,55,0,450,
        109,1,0,0,0,451,455,3,114,57,0,452,454,3,112,56,0,453,452,1,0,0,
        0,454,457,1,0,0,0,455,453,1,0,0,0,455,456,1,0,0,0,456,111,1,0,0,
        0,457,455,1,0,0,0,458,459,3,120,60,0,459,460,3,114,57,0,460,113,
        1,0,0,0,461,474,3,106,53,0,462,474,3,116,58,0,463,464,5,2,0,0,464,
        465,3,110,55,0,465,466,5,3,0,0,466,474,1,0,0,0,467,468,3,118,59,
        0,468,469,3,114,57,0,469,474,1,0,0,0,470,474,3,10,5,0,471,474,3,
        122,61,0,472,474,3,124,62,0,473,461,1,0,0,0,473,462,1,0,0,0,473,
        463,1,0,0,0,473,467,1,0,0,0,473,470,1,0,0,0,473,471,1,0,0,0,473,
        472,1,0,0,0,474,115,1,0,0,0,475,476,5,75,0,0,476,477,5,2,0,0,477,
        478,3,110,55,0,478,479,5,1,0,0,479,480,3,110,55,0,480,481,5,3,0,
        0,481,117,1,0,0,0,482,483,7,1,0,0,483,119,1,0,0,0,484,495,7,2,0,
        0,485,495,7,3,0,0,486,495,7,4,0,0,487,495,7,5,0,0,488,495,5,17,0,
        0,489,495,5,18,0,0,490,495,5,19,0,0,491,495,5,26,0,0,492,495,5,27,
        0,0,493,495,5,29,0,0,494,484,1,0,0,0,494,485,1,0,0,0,494,486,1,0,
        0,0,494,487,1,0,0,0,494,488,1,0,0,0,494,489,1,0,0,0,494,490,1,0,
        0,0,494,491,1,0,0,0,494,492,1,0,0,0,494,493,1,0,0,0,495,121,1,0,
        0,0,496,497,7,6,0,0,497,123,1,0,0,0,498,499,5,53,0,0,499,500,5,2,
        0,0,500,501,5,79,0,0,501,502,5,3,0,0,502,125,1,0,0,0,503,504,5,87,
        0,0,504,127,1,0,0,0,27,131,137,145,158,172,179,186,195,200,215,223,
        237,256,286,290,324,333,343,420,426,434,437,440,446,455,473,494
    ]

class BosParser ( Parser ):

    grammarFileName = "BosParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'('", "')'", "'{'", "'}'", "'['", 
                     "']'", "';'", "'='", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'++'", "'--'", "'&'", "'|'", "'^'", "'=='", "'!='", 
                     "'<'", "'<='", "'>'", "'>='", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'if'", "'else'", "'while'", 
                     "'for'", "'static-var'", "'var'", "'piece'", "'turn'", 
                     "'around'", "'move'", "'along'", "'to'", "'from'", 
                     "'now'", "'speed'", "'spin'", "'accelerate'", "<INVALID>", 
                     "'decelerate'", "<INVALID>", "<INVALID>", "'set'", 
                     "'get'", "'UNKNOWN_UNIT_VALUE'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'sleep'", "'hide'", "'show'", "'explode'", 
                     "'type'", "'signal'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'return'", "'cache'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'rand'" ]

    symbolicNames = [ "<INVALID>", "COMMA", "L_PAREN", "R_PAREN", "L_BRACE", 
                      "R_BRACE", "L_SQUARE_BRACKET", "R_SQUARE_BRACKET", 
                      "SEMICOLON", "ASSIGN", "OP_ADD", "OP_MINUS", "OP_MULT", 
                      "OP_DIV", "OP_MOD", "OP_INCREMENT", "OP_DECREMENT", 
                      "BITWISE_AND", "BITWISE_OR", "BITWISE_XOR", "COMP_EQUAL", 
                      "COMP_NOT_EQUAL", "COMP_LESS", "COMP_LESS_EQUAL", 
                      "COMP_GREATER", "COMP_GREATER_EQUAL", "LOGICAL_AND", 
                      "LOGICAL_OR", "LOGICAL_NOT", "LOGICAL_XOR", "IF", 
                      "ELSE", "WHILE", "FOR", "STATIC_VAR", "VAR", "PIECE", 
                      "TURN", "AROUND", "MOVE", "ALONG", "TO", "FROM", "NOW", 
                      "SPEED", "SPIN", "ACCELERATE", "STOP_SPIN", "DECELERATE", 
                      "WAIT_FOR_TURN", "WAIT_FOR_MOVE", "SET", "GET", "UNKNOWN_UNIT_VALUE", 
                      "CALL_SCRIPT", "START_SCRIPT", "EMIT_SFX", "SLEEP", 
                      "HIDE", "SHOW", "EXPLODE", "TYPE", "SIGNAL", "SET_SIGNAL_MASK", 
                      "ATTACH_UNIT", "DROP_UNIT", "RETURN", "CACHE", "DONT_CACHE", 
                      "DONT_SHADOW", "DONT_SHADE", "PLAY_SOUND", "X_AXIS", 
                      "Y_AXIS", "Z_AXIS", "RAND", "LINEAR_CONSTANT", "DEGREES_CONSTANT", 
                      "FLOAT", "INT", "MULTI_LINE_MACRO", "DIRECTIVE", "LINE_COMMENT", 
                      "BLOCK_COMMENT", "WHITESPACE", "NEWLINE", "ID", "STRING" ]

    RULE_file = 0
    RULE_declaration = 1
    RULE_pieceDecl = 2
    RULE_pieceName = 3
    RULE_staticVarDecl = 4
    RULE_varName = 5
    RULE_funcDecl = 6
    RULE_funcName = 7
    RULE_argumentList = 8
    RULE_arguments = 9
    RULE_argName = 10
    RULE_statementBlock = 11
    RULE_statement = 12
    RULE_assignStatement = 13
    RULE_incStatement = 14
    RULE_decStatement = 15
    RULE_ifStatement = 16
    RULE_elseBlock = 17
    RULE_whileStatement = 18
    RULE_forStatement = 19
    RULE_keywordStatement = 20
    RULE_returnStatement = 21
    RULE_sleepStatement = 22
    RULE_varStatement = 23
    RULE_setStatement = 24
    RULE_getStatement = 25
    RULE_axis = 26
    RULE_turnStatement = 27
    RULE_moveStatement = 28
    RULE_speedOrNow = 29
    RULE_spinStatement = 30
    RULE_acceleration = 31
    RULE_stopSpinStatement = 32
    RULE_deceleration = 33
    RULE_waitForTurnStatement = 34
    RULE_waitForMoveStatement = 35
    RULE_emitSfxStatement = 36
    RULE_playSoundStatement = 37
    RULE_hideStatement = 38
    RULE_showStatement = 39
    RULE_explodeStatement = 40
    RULE_callStatement = 41
    RULE_startStatement = 42
    RULE_signalStatement = 43
    RULE_setSignalMaskStatement = 44
    RULE_attachUnitStatement = 45
    RULE_dropUnitStatement = 46
    RULE_cacheStatement = 47
    RULE_dontCacheStatement = 48
    RULE_dontShadowStatement = 49
    RULE_dontShadeStatement = 50
    RULE_expressionList = 51
    RULE_expressions = 52
    RULE_getTerm = 53
    RULE_commaExpression = 54
    RULE_expression = 55
    RULE_opterm = 56
    RULE_term = 57
    RULE_rand = 58
    RULE_unaryOp = 59
    RULE_op = 60
    RULE_constant = 61
    RULE_unknown_unit_value = 62
    RULE_stringConstant = 63

    ruleNames =  [ "file", "declaration", "pieceDecl", "pieceName", "staticVarDecl", 
                   "varName", "funcDecl", "funcName", "argumentList", "arguments", 
                   "argName", "statementBlock", "statement", "assignStatement", 
                   "incStatement", "decStatement", "ifStatement", "elseBlock", 
                   "whileStatement", "forStatement", "keywordStatement", 
                   "returnStatement", "sleepStatement", "varStatement", 
                   "setStatement", "getStatement", "axis", "turnStatement", 
                   "moveStatement", "speedOrNow", "spinStatement", "acceleration", 
                   "stopSpinStatement", "deceleration", "waitForTurnStatement", 
                   "waitForMoveStatement", "emitSfxStatement", "playSoundStatement", 
                   "hideStatement", "showStatement", "explodeStatement", 
                   "callStatement", "startStatement", "signalStatement", 
                   "setSignalMaskStatement", "attachUnitStatement", "dropUnitStatement", 
                   "cacheStatement", "dontCacheStatement", "dontShadowStatement", 
                   "dontShadeStatement", "expressionList", "expressions", 
                   "getTerm", "commaExpression", "expression", "opterm", 
                   "term", "rand", "unaryOp", "op", "constant", "unknown_unit_value", 
                   "stringConstant" ]

    EOF = Token.EOF
    COMMA=1
    L_PAREN=2
    R_PAREN=3
    L_BRACE=4
    R_BRACE=5
    L_SQUARE_BRACKET=6
    R_SQUARE_BRACKET=7
    SEMICOLON=8
    ASSIGN=9
    OP_ADD=10
    OP_MINUS=11
    OP_MULT=12
    OP_DIV=13
    OP_MOD=14
    OP_INCREMENT=15
    OP_DECREMENT=16
    BITWISE_AND=17
    BITWISE_OR=18
    BITWISE_XOR=19
    COMP_EQUAL=20
    COMP_NOT_EQUAL=21
    COMP_LESS=22
    COMP_LESS_EQUAL=23
    COMP_GREATER=24
    COMP_GREATER_EQUAL=25
    LOGICAL_AND=26
    LOGICAL_OR=27
    LOGICAL_NOT=28
    LOGICAL_XOR=29
    IF=30
    ELSE=31
    WHILE=32
    FOR=33
    STATIC_VAR=34
    VAR=35
    PIECE=36
    TURN=37
    AROUND=38
    MOVE=39
    ALONG=40
    TO=41
    FROM=42
    NOW=43
    SPEED=44
    SPIN=45
    ACCELERATE=46
    STOP_SPIN=47
    DECELERATE=48
    WAIT_FOR_TURN=49
    WAIT_FOR_MOVE=50
    SET=51
    GET=52
    UNKNOWN_UNIT_VALUE=53
    CALL_SCRIPT=54
    START_SCRIPT=55
    EMIT_SFX=56
    SLEEP=57
    HIDE=58
    SHOW=59
    EXPLODE=60
    TYPE=61
    SIGNAL=62
    SET_SIGNAL_MASK=63
    ATTACH_UNIT=64
    DROP_UNIT=65
    RETURN=66
    CACHE=67
    DONT_CACHE=68
    DONT_SHADOW=69
    DONT_SHADE=70
    PLAY_SOUND=71
    X_AXIS=72
    Y_AXIS=73
    Z_AXIS=74
    RAND=75
    LINEAR_CONSTANT=76
    DEGREES_CONSTANT=77
    FLOAT=78
    INT=79
    MULTI_LINE_MACRO=80
    DIRECTIVE=81
    LINE_COMMENT=82
    BLOCK_COMMENT=83
    WHITESPACE=84
    NEWLINE=85
    ID=86
    STRING=87

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class FileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BosParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(BosParser.DeclarationContext,i)


        def getRuleIndex(self):
            return BosParser.RULE_file

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFile" ):
                listener.enterFile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFile" ):
                listener.exitFile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFile" ):
                return visitor.visitFile(self)
            else:
                return visitor.visitChildren(self)




    def file_(self):

        localctx = BosParser.FileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_file)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 34)) & ~0x3f) == 0 and ((1 << (_la - 34)) & 4503599627370501) != 0):
                self.state = 128
                self.declaration()
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pieceDecl(self):
            return self.getTypedRuleContext(BosParser.PieceDeclContext,0)


        def staticVarDecl(self):
            return self.getTypedRuleContext(BosParser.StaticVarDeclContext,0)


        def funcDecl(self):
            return self.getTypedRuleContext(BosParser.FuncDeclContext,0)


        def getRuleIndex(self):
            return BosParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = BosParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.state = 137
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.pieceDecl()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.staticVarDecl()
                pass
            elif token in [86]:
                self.enterOuterAlt(localctx, 3)
                self.state = 136
                self.funcDecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PieceDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PIECE(self):
            return self.getToken(BosParser.PIECE, 0)

        def pieceName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BosParser.PieceNameContext)
            else:
                return self.getTypedRuleContext(BosParser.PieceNameContext,i)


        def SEMICOLON(self):
            return self.getToken(BosParser.SEMICOLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BosParser.COMMA)
            else:
                return self.getToken(BosParser.COMMA, i)

        def getRuleIndex(self):
            return BosParser.RULE_pieceDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPieceDecl" ):
                listener.enterPieceDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPieceDecl" ):
                listener.exitPieceDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPieceDecl" ):
                return visitor.visitPieceDecl(self)
            else:
                return visitor.visitChildren(self)




    def pieceDecl(self):

        localctx = BosParser.PieceDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_pieceDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(BosParser.PIECE)
            self.state = 140
            self.pieceName()
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 141
                self.match(BosParser.COMMA)
                self.state = 142
                self.pieceName()
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 148
            self.match(BosParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PieceNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BosParser.ID, 0)

        def getRuleIndex(self):
            return BosParser.RULE_pieceName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPieceName" ):
                listener.enterPieceName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPieceName" ):
                listener.exitPieceName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPieceName" ):
                return visitor.visitPieceName(self)
            else:
                return visitor.visitChildren(self)




    def pieceName(self):

        localctx = BosParser.PieceNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_pieceName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(BosParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StaticVarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATIC_VAR(self):
            return self.getToken(BosParser.STATIC_VAR, 0)

        def varName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BosParser.VarNameContext)
            else:
                return self.getTypedRuleContext(BosParser.VarNameContext,i)


        def SEMICOLON(self):
            return self.getToken(BosParser.SEMICOLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BosParser.COMMA)
            else:
                return self.getToken(BosParser.COMMA, i)

        def getRuleIndex(self):
            return BosParser.RULE_staticVarDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStaticVarDecl" ):
                listener.enterStaticVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStaticVarDecl" ):
                listener.exitStaticVarDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStaticVarDecl" ):
                return visitor.visitStaticVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def staticVarDecl(self):

        localctx = BosParser.StaticVarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_staticVarDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(BosParser.STATIC_VAR)
            self.state = 153
            self.varName()
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 154
                self.match(BosParser.COMMA)
                self.state = 155
                self.varName()
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 161
            self.match(BosParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BosParser.ID, 0)

        def getRuleIndex(self):
            return BosParser.RULE_varName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarName" ):
                listener.enterVarName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarName" ):
                listener.exitVarName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarName" ):
                return visitor.visitVarName(self)
            else:
                return visitor.visitChildren(self)




    def varName(self):

        localctx = BosParser.VarNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_varName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(BosParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcName(self):
            return self.getTypedRuleContext(BosParser.FuncNameContext,0)


        def statementBlock(self):
            return self.getTypedRuleContext(BosParser.StatementBlockContext,0)


        def L_PAREN(self):
            return self.getToken(BosParser.L_PAREN, 0)

        def R_PAREN(self):
            return self.getToken(BosParser.R_PAREN, 0)

        def argumentList(self):
            return self.getTypedRuleContext(BosParser.ArgumentListContext,0)


        def getRuleIndex(self):
            return BosParser.RULE_funcDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncDecl" ):
                listener.enterFuncDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncDecl" ):
                listener.exitFuncDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDecl" ):
                return visitor.visitFuncDecl(self)
            else:
                return visitor.visitChildren(self)




    def funcDecl(self):

        localctx = BosParser.FuncDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_funcDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.funcName()
            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 166
                self.match(BosParser.L_PAREN)
                self.state = 167
                self.match(BosParser.R_PAREN)
                pass

            elif la_ == 2:
                self.state = 168
                self.match(BosParser.L_PAREN)
                self.state = 169
                self.argumentList()
                self.state = 170
                self.match(BosParser.R_PAREN)
                pass


            self.state = 174
            self.statementBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BosParser.ID, 0)

        def getRuleIndex(self):
            return BosParser.RULE_funcName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncName" ):
                listener.enterFuncName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncName" ):
                listener.exitFuncName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncName" ):
                return visitor.visitFuncName(self)
            else:
                return visitor.visitChildren(self)




    def funcName(self):

        localctx = BosParser.FuncNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_funcName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(BosParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arguments(self):
            return self.getTypedRuleContext(BosParser.ArgumentsContext,0)


        def getRuleIndex(self):
            return BosParser.RULE_argumentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentList" ):
                listener.enterArgumentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentList" ):
                listener.exitArgumentList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentList" ):
                return visitor.visitArgumentList(self)
            else:
                return visitor.visitChildren(self)




    def argumentList(self):

        localctx = BosParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==86:
                self.state = 178
                self.arguments()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BosParser.ArgNameContext)
            else:
                return self.getTypedRuleContext(BosParser.ArgNameContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BosParser.COMMA)
            else:
                return self.getToken(BosParser.COMMA, i)

        def getRuleIndex(self):
            return BosParser.RULE_arguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArguments" ):
                listener.enterArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArguments" ):
                listener.exitArguments(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArguments" ):
                return visitor.visitArguments(self)
            else:
                return visitor.visitChildren(self)




    def arguments(self):

        localctx = BosParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.argName()
            self.state = 186
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 182
                self.match(BosParser.COMMA)
                self.state = 183
                self.argName()
                self.state = 188
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BosParser.ID, 0)

        def getRuleIndex(self):
            return BosParser.RULE_argName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgName" ):
                listener.enterArgName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgName" ):
                listener.exitArgName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgName" ):
                return visitor.visitArgName(self)
            else:
                return visitor.visitChildren(self)




    def argName(self):

        localctx = BosParser.ArgNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_argName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(BosParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_BRACE(self):
            return self.getToken(BosParser.L_BRACE, 0)

        def R_BRACE(self):
            return self.getToken(BosParser.R_BRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BosParser.StatementContext)
            else:
                return self.getTypedRuleContext(BosParser.StatementContext,i)


        def getRuleIndex(self):
            return BosParser.RULE_statementBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementBlock" ):
                listener.enterStatementBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementBlock" ):
                listener.exitStatementBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementBlock" ):
                return visitor.visitStatementBlock(self)
            else:
                return visitor.visitChildren(self)




    def statementBlock(self):

        localctx = BosParser.StatementBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_statementBlock)
        self._la = 0 # Token type
        try:
            self.state = 200
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.match(BosParser.L_BRACE)
                self.state = 195
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & -2315236501048164096) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 4194559) != 0):
                    self.state = 192
                    self.statement()
                    self.state = 197
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 198
                self.match(BosParser.R_BRACE)
                pass
            elif token in [8, 15, 16, 30, 32, 33, 35, 37, 39, 45, 47, 49, 50, 51, 52, 54, 55, 56, 57, 58, 59, 60, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 86]:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
                self.statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def keywordStatement(self):
            return self.getTypedRuleContext(BosParser.KeywordStatementContext,0)


        def SEMICOLON(self):
            return self.getToken(BosParser.SEMICOLON, 0)

        def varStatement(self):
            return self.getTypedRuleContext(BosParser.VarStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(BosParser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(BosParser.WhileStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(BosParser.ForStatementContext,0)


        def assignStatement(self):
            return self.getTypedRuleContext(BosParser.AssignStatementContext,0)


        def getRuleIndex(self):
            return BosParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = BosParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_statement)
        try:
            self.state = 215
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37, 39, 45, 47, 49, 50, 51, 52, 54, 55, 56, 57, 58, 59, 60, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.keywordStatement()
                self.state = 203
                self.match(BosParser.SEMICOLON)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 2)
                self.state = 205
                self.varStatement()
                self.state = 206
                self.match(BosParser.SEMICOLON)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 3)
                self.state = 208
                self.ifStatement()
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 4)
                self.state = 209
                self.whileStatement()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 5)
                self.state = 210
                self.forStatement()
                pass
            elif token in [15, 16, 86]:
                self.enterOuterAlt(localctx, 6)
                self.state = 211
                self.assignStatement()
                self.state = 212
                self.match(BosParser.SEMICOLON)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 7)
                self.state = 214
                self.match(BosParser.SEMICOLON)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varName(self):
            return self.getTypedRuleContext(BosParser.VarNameContext,0)


        def ASSIGN(self):
            return self.getToken(BosParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(BosParser.ExpressionContext,0)


        def incStatement(self):
            return self.getTypedRuleContext(BosParser.IncStatementContext,0)


        def decStatement(self):
            return self.getTypedRuleContext(BosParser.DecStatementContext,0)


        def getRuleIndex(self):
            return BosParser.RULE_assignStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStatement" ):
                listener.enterAssignStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStatement" ):
                listener.exitAssignStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStatement" ):
                return visitor.visitAssignStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignStatement(self):

        localctx = BosParser.AssignStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_assignStatement)
        try:
            self.state = 223
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [86]:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.varName()
                self.state = 218
                self.match(BosParser.ASSIGN)
                self.state = 219
                self.expression()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self.incStatement()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 222
                self.decStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IncStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_INCREMENT(self):
            return self.getToken(BosParser.OP_INCREMENT, 0)

        def varName(self):
            return self.getTypedRuleContext(BosParser.VarNameContext,0)


        def getRuleIndex(self):
            return BosParser.RULE_incStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncStatement" ):
                listener.enterIncStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncStatement" ):
                listener.exitIncStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIncStatement" ):
                return visitor.visitIncStatement(self)
            else:
                return visitor.visitChildren(self)




    def incStatement(self):

        localctx = BosParser.IncStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_incStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(BosParser.OP_INCREMENT)
            self.state = 226
            self.varName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_DECREMENT(self):
            return self.getToken(BosParser.OP_DECREMENT, 0)

        def varName(self):
            return self.getTypedRuleContext(BosParser.VarNameContext,0)


        def getRuleIndex(self):
            return BosParser.RULE_decStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecStatement" ):
                listener.enterDecStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecStatement" ):
                listener.exitDecStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecStatement" ):
                return visitor.visitDecStatement(self)
            else:
                return visitor.visitChildren(self)




    def decStatement(self):

        localctx = BosParser.DecStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_decStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(BosParser.OP_DECREMENT)
            self.state = 229
            self.varName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BosParser.IF, 0)

        def L_PAREN(self):
            return self.getToken(BosParser.L_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(BosParser.ExpressionContext,0)


        def R_PAREN(self):
            return self.getToken(BosParser.R_PAREN, 0)

        def statementBlock(self):
            return self.getTypedRuleContext(BosParser.StatementBlockContext,0)


        def elseBlock(self):
            return self.getTypedRuleContext(BosParser.ElseBlockContext,0)


        def getRuleIndex(self):
            return BosParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = BosParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(BosParser.IF)
            self.state = 232
            self.match(BosParser.L_PAREN)
            self.state = 233
            self.expression()
            self.state = 234
            self.match(BosParser.R_PAREN)
            self.state = 235
            self.statementBlock()
            self.state = 237
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 236
                self.elseBlock()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(BosParser.ELSE, 0)

        def statementBlock(self):
            return self.getTypedRuleContext(BosParser.StatementBlockContext,0)


        def getRuleIndex(self):
            return BosParser.RULE_elseBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseBlock" ):
                listener.enterElseBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseBlock" ):
                listener.exitElseBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseBlock" ):
                return visitor.visitElseBlock(self)
            else:
                return visitor.visitChildren(self)




    def elseBlock(self):

        localctx = BosParser.ElseBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_elseBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(BosParser.ELSE)
            self.state = 240
            self.statementBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(BosParser.WHILE, 0)

        def L_PAREN(self):
            return self.getToken(BosParser.L_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(BosParser.ExpressionContext,0)


        def R_PAREN(self):
            return self.getToken(BosParser.R_PAREN, 0)

        def statementBlock(self):
            return self.getTypedRuleContext(BosParser.StatementBlockContext,0)


        def getRuleIndex(self):
            return BosParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = BosParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(BosParser.WHILE)
            self.state = 243
            self.match(BosParser.L_PAREN)
            self.state = 244
            self.expression()
            self.state = 245
            self.match(BosParser.R_PAREN)
            self.state = 246
            self.statementBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BosParser.FOR, 0)

        def L_PAREN(self):
            return self.getToken(BosParser.L_PAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BosParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BosParser.ExpressionContext,i)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(BosParser.SEMICOLON)
            else:
                return self.getToken(BosParser.SEMICOLON, i)

        def R_PAREN(self):
            return self.getToken(BosParser.R_PAREN, 0)

        def statementBlock(self):
            return self.getTypedRuleContext(BosParser.StatementBlockContext,0)


        def getRuleIndex(self):
            return BosParser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = BosParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(BosParser.FOR)
            self.state = 249
            self.match(BosParser.L_PAREN)
            self.state = 250
            self.expression()
            self.state = 251
            self.match(BosParser.SEMICOLON)
            self.state = 252
            self.expression()
            self.state = 253
            self.match(BosParser.SEMICOLON)
            self.state = 254
            self.expression()
            self.state = 256
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 255
                self.match(BosParser.SEMICOLON)


            self.state = 258
            self.match(BosParser.R_PAREN)
            self.state = 259
            self.statementBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeywordStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def callStatement(self):
            return self.getTypedRuleContext(BosParser.CallStatementContext,0)


        def startStatement(self):
            return self.getTypedRuleContext(BosParser.StartStatementContext,0)


        def spinStatement(self):
            return self.getTypedRuleContext(BosParser.SpinStatementContext,0)


        def stopSpinStatement(self):
            return self.getTypedRuleContext(BosParser.StopSpinStatementContext,0)


        def turnStatement(self):
            return self.getTypedRuleContext(BosParser.TurnStatementContext,0)


        def moveStatement(self):
            return self.getTypedRuleContext(BosParser.MoveStatementContext,0)


        def waitForTurnStatement(self):
            return self.getTypedRuleContext(BosParser.WaitForTurnStatementContext,0)


        def waitForMoveStatement(self):
            return self.getTypedRuleContext(BosParser.WaitForMoveStatementContext,0)


        def emitSfxStatement(self):
            return self.getTypedRuleContext(BosParser.EmitSfxStatementContext,0)


        def sleepStatement(self):
            return self.getTypedRuleContext(BosParser.SleepStatementContext,0)


        def hideStatement(self):
            return self.getTypedRuleContext(BosParser.HideStatementContext,0)


        def showStatement(self):
            return self.getTypedRuleContext(BosParser.ShowStatementContext,0)


        def explodeStatement(self):
            return self.getTypedRuleContext(BosParser.ExplodeStatementContext,0)


        def signalStatement(self):
            return self.getTypedRuleContext(BosParser.SignalStatementContext,0)


        def setSignalMaskStatement(self):
            return self.getTypedRuleContext(BosParser.SetSignalMaskStatementContext,0)


        def setStatement(self):
            return self.getTypedRuleContext(BosParser.SetStatementContext,0)


        def getStatement(self):
            return self.getTypedRuleContext(BosParser.GetStatementContext,0)


        def attachUnitStatement(self):
            return self.getTypedRuleContext(BosParser.AttachUnitStatementContext,0)


        def dropUnitStatement(self):
            return self.getTypedRuleContext(BosParser.DropUnitStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(BosParser.ReturnStatementContext,0)


        def playSoundStatement(self):
            return self.getTypedRuleContext(BosParser.PlaySoundStatementContext,0)


        def cacheStatement(self):
            return self.getTypedRuleContext(BosParser.CacheStatementContext,0)


        def dontCacheStatement(self):
            return self.getTypedRuleContext(BosParser.DontCacheStatementContext,0)


        def dontShadowStatement(self):
            return self.getTypedRuleContext(BosParser.DontShadowStatementContext,0)


        def dontShadeStatement(self):
            return self.getTypedRuleContext(BosParser.DontShadeStatementContext,0)


        def getRuleIndex(self):
            return BosParser.RULE_keywordStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeywordStatement" ):
                listener.enterKeywordStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeywordStatement" ):
                listener.exitKeywordStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeywordStatement" ):
                return visitor.visitKeywordStatement(self)
            else:
                return visitor.visitChildren(self)




    def keywordStatement(self):

        localctx = BosParser.KeywordStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_keywordStatement)
        try:
            self.state = 286
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [54]:
                self.enterOuterAlt(localctx, 1)
                self.state = 261
                self.callStatement()
                pass
            elif token in [55]:
                self.enterOuterAlt(localctx, 2)
                self.state = 262
                self.startStatement()
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 3)
                self.state = 263
                self.spinStatement()
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 4)
                self.state = 264
                self.stopSpinStatement()
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 5)
                self.state = 265
                self.turnStatement()
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 6)
                self.state = 266
                self.moveStatement()
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 7)
                self.state = 267
                self.waitForTurnStatement()
                pass
            elif token in [50]:
                self.enterOuterAlt(localctx, 8)
                self.state = 268
                self.waitForMoveStatement()
                pass
            elif token in [56]:
                self.enterOuterAlt(localctx, 9)
                self.state = 269
                self.emitSfxStatement()
                pass
            elif token in [57]:
                self.enterOuterAlt(localctx, 10)
                self.state = 270
                self.sleepStatement()
                pass
            elif token in [58]:
                self.enterOuterAlt(localctx, 11)
                self.state = 271
                self.hideStatement()
                pass
            elif token in [59]:
                self.enterOuterAlt(localctx, 12)
                self.state = 272
                self.showStatement()
                pass
            elif token in [60]:
                self.enterOuterAlt(localctx, 13)
                self.state = 273
                self.explodeStatement()
                pass
            elif token in [62]:
                self.enterOuterAlt(localctx, 14)
                self.state = 274
                self.signalStatement()
                pass
            elif token in [63]:
                self.enterOuterAlt(localctx, 15)
                self.state = 275
                self.setSignalMaskStatement()
                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 16)
                self.state = 276
                self.setStatement()
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 17)
                self.state = 277
                self.getStatement()
                pass
            elif token in [64]:
                self.enterOuterAlt(localctx, 18)
                self.state = 278
                self.attachUnitStatement()
                pass
            elif token in [65]:
                self.enterOuterAlt(localctx, 19)
                self.state = 279
                self.dropUnitStatement()
                pass
            elif token in [66]:
                self.enterOuterAlt(localctx, 20)
                self.state = 280
                self.returnStatement()
                pass
            elif token in [71]:
                self.enterOuterAlt(localctx, 21)
                self.state = 281
                self.playSoundStatement()
                pass
            elif token in [67]:
                self.enterOuterAlt(localctx, 22)
                self.state = 282
                self.cacheStatement()
                pass
            elif token in [68]:
                self.enterOuterAlt(localctx, 23)
                self.state = 283
                self.dontCacheStatement()
                pass
            elif token in [69]:
                self.enterOuterAlt(localctx, 24)
                self.state = 284
                self.dontShadowStatement()
                pass
            elif token in [70]:
                self.enterOuterAlt(localctx, 25)
                self.state = 285
                self.dontShadeStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BosParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(BosParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BosParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = BosParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.match(BosParser.RETURN)
            self.state = 290
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 13510799150548996) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & 2079) != 0):
                self.state = 289
                self.expression()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SleepStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SLEEP(self):
            return self.getToken(BosParser.SLEEP, 0)

        def expression(self):
            return self.getTypedRuleContext(BosParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BosParser.RULE_sleepStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSleepStatement" ):
                listener.enterSleepStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSleepStatement" ):
                listener.exitSleepStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSleepStatement" ):
                return visitor.visitSleepStatement(self)
            else:
                return visitor.visitChildren(self)




    def sleepStatement(self):

        localctx = BosParser.SleepStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_sleepStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.match(BosParser.SLEEP)
            self.state = 293
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BosParser.VAR, 0)

        def arguments(self):
            return self.getTypedRuleContext(BosParser.ArgumentsContext,0)


        def getRuleIndex(self):
            return BosParser.RULE_varStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarStatement" ):
                listener.enterVarStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarStatement" ):
                listener.exitVarStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarStatement" ):
                return visitor.visitVarStatement(self)
            else:
                return visitor.visitChildren(self)




    def varStatement(self):

        localctx = BosParser.VarStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_varStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.match(BosParser.VAR)
            self.state = 296
            self.arguments()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SetStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SET(self):
            return self.getToken(BosParser.SET, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BosParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BosParser.ExpressionContext,i)


        def TO(self):
            return self.getToken(BosParser.TO, 0)

        def getRuleIndex(self):
            return BosParser.RULE_setStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetStatement" ):
                listener.enterSetStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetStatement" ):
                listener.exitSetStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetStatement" ):
                return visitor.visitSetStatement(self)
            else:
                return visitor.visitChildren(self)




    def setStatement(self):

        localctx = BosParser.SetStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_setStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.match(BosParser.SET)
            self.state = 299
            self.expression()
            self.state = 300
            self.match(BosParser.TO)
            self.state = 301
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GetStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getTerm(self):
            return self.getTypedRuleContext(BosParser.GetTermContext,0)


        def getRuleIndex(self):
            return BosParser.RULE_getStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGetStatement" ):
                listener.enterGetStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGetStatement" ):
                listener.exitGetStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGetStatement" ):
                return visitor.visitGetStatement(self)
            else:
                return visitor.visitChildren(self)




    def getStatement(self):

        localctx = BosParser.GetStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_getStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.getTerm()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AxisContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def X_AXIS(self):
            return self.getToken(BosParser.X_AXIS, 0)

        def Y_AXIS(self):
            return self.getToken(BosParser.Y_AXIS, 0)

        def Z_AXIS(self):
            return self.getToken(BosParser.Z_AXIS, 0)

        def getRuleIndex(self):
            return BosParser.RULE_axis

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAxis" ):
                listener.enterAxis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAxis" ):
                listener.exitAxis(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAxis" ):
                return visitor.visitAxis(self)
            else:
                return visitor.visitChildren(self)




    def axis(self):

        localctx = BosParser.AxisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_axis)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            _la = self._input.LA(1)
            if not(((((_la - 72)) & ~0x3f) == 0 and ((1 << (_la - 72)) & 7) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TurnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TURN(self):
            return self.getToken(BosParser.TURN, 0)

        def pieceName(self):
            return self.getTypedRuleContext(BosParser.PieceNameContext,0)


        def TO(self):
            return self.getToken(BosParser.TO, 0)

        def axis(self):
            return self.getTypedRuleContext(BosParser.AxisContext,0)


        def expression(self):
            return self.getTypedRuleContext(BosParser.ExpressionContext,0)


        def speedOrNow(self):
            return self.getTypedRuleContext(BosParser.SpeedOrNowContext,0)


        def getRuleIndex(self):
            return BosParser.RULE_turnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTurnStatement" ):
                listener.enterTurnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTurnStatement" ):
                listener.exitTurnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTurnStatement" ):
                return visitor.visitTurnStatement(self)
            else:
                return visitor.visitChildren(self)




    def turnStatement(self):

        localctx = BosParser.TurnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_turnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.match(BosParser.TURN)
            self.state = 308
            self.pieceName()
            self.state = 309
            self.match(BosParser.TO)
            self.state = 310
            self.axis()
            self.state = 311
            self.expression()
            self.state = 312
            self.speedOrNow()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MoveStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MOVE(self):
            return self.getToken(BosParser.MOVE, 0)

        def pieceName(self):
            return self.getTypedRuleContext(BosParser.PieceNameContext,0)


        def TO(self):
            return self.getToken(BosParser.TO, 0)

        def axis(self):
            return self.getTypedRuleContext(BosParser.AxisContext,0)


        def expression(self):
            return self.getTypedRuleContext(BosParser.ExpressionContext,0)


        def speedOrNow(self):
            return self.getTypedRuleContext(BosParser.SpeedOrNowContext,0)


        def getRuleIndex(self):
            return BosParser.RULE_moveStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMoveStatement" ):
                listener.enterMoveStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMoveStatement" ):
                listener.exitMoveStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMoveStatement" ):
                return visitor.visitMoveStatement(self)
            else:
                return visitor.visitChildren(self)




    def moveStatement(self):

        localctx = BosParser.MoveStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_moveStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.match(BosParser.MOVE)
            self.state = 315
            self.pieceName()
            self.state = 316
            self.match(BosParser.TO)
            self.state = 317
            self.axis()
            self.state = 318
            self.expression()
            self.state = 319
            self.speedOrNow()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpeedOrNowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOW(self):
            return self.getToken(BosParser.NOW, 0)

        def SPEED(self):
            return self.getToken(BosParser.SPEED, 0)

        def expression(self):
            return self.getTypedRuleContext(BosParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BosParser.RULE_speedOrNow

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpeedOrNow" ):
                listener.enterSpeedOrNow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpeedOrNow" ):
                listener.exitSpeedOrNow(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpeedOrNow" ):
                return visitor.visitSpeedOrNow(self)
            else:
                return visitor.visitChildren(self)




    def speedOrNow(self):

        localctx = BosParser.SpeedOrNowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_speedOrNow)
        try:
            self.state = 324
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [43]:
                self.enterOuterAlt(localctx, 1)
                self.state = 321
                self.match(BosParser.NOW)
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 2)
                self.state = 322
                self.match(BosParser.SPEED)
                self.state = 323
                self.expression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpinStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SPIN(self):
            return self.getToken(BosParser.SPIN, 0)

        def pieceName(self):
            return self.getTypedRuleContext(BosParser.PieceNameContext,0)


        def AROUND(self):
            return self.getToken(BosParser.AROUND, 0)

        def axis(self):
            return self.getTypedRuleContext(BosParser.AxisContext,0)


        def SPEED(self):
            return self.getToken(BosParser.SPEED, 0)

        def expression(self):
            return self.getTypedRuleContext(BosParser.ExpressionContext,0)


        def acceleration(self):
            return self.getTypedRuleContext(BosParser.AccelerationContext,0)


        def getRuleIndex(self):
            return BosParser.RULE_spinStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpinStatement" ):
                listener.enterSpinStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpinStatement" ):
                listener.exitSpinStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpinStatement" ):
                return visitor.visitSpinStatement(self)
            else:
                return visitor.visitChildren(self)




    def spinStatement(self):

        localctx = BosParser.SpinStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_spinStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.match(BosParser.SPIN)
            self.state = 327
            self.pieceName()
            self.state = 328
            self.match(BosParser.AROUND)
            self.state = 329
            self.axis()
            self.state = 330
            self.match(BosParser.SPEED)
            self.state = 331
            self.expression()
            self.state = 333
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==46:
                self.state = 332
                self.acceleration()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AccelerationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ACCELERATE(self):
            return self.getToken(BosParser.ACCELERATE, 0)

        def expression(self):
            return self.getTypedRuleContext(BosParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BosParser.RULE_acceleration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAcceleration" ):
                listener.enterAcceleration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAcceleration" ):
                listener.exitAcceleration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAcceleration" ):
                return visitor.visitAcceleration(self)
            else:
                return visitor.visitChildren(self)




    def acceleration(self):

        localctx = BosParser.AccelerationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_acceleration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.match(BosParser.ACCELERATE)
            self.state = 336
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StopSpinStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STOP_SPIN(self):
            return self.getToken(BosParser.STOP_SPIN, 0)

        def pieceName(self):
            return self.getTypedRuleContext(BosParser.PieceNameContext,0)


        def AROUND(self):
            return self.getToken(BosParser.AROUND, 0)

        def axis(self):
            return self.getTypedRuleContext(BosParser.AxisContext,0)


        def deceleration(self):
            return self.getTypedRuleContext(BosParser.DecelerationContext,0)


        def getRuleIndex(self):
            return BosParser.RULE_stopSpinStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStopSpinStatement" ):
                listener.enterStopSpinStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStopSpinStatement" ):
                listener.exitStopSpinStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStopSpinStatement" ):
                return visitor.visitStopSpinStatement(self)
            else:
                return visitor.visitChildren(self)




    def stopSpinStatement(self):

        localctx = BosParser.StopSpinStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_stopSpinStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.match(BosParser.STOP_SPIN)
            self.state = 339
            self.pieceName()
            self.state = 340
            self.match(BosParser.AROUND)
            self.state = 341
            self.axis()
            self.state = 343
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==48:
                self.state = 342
                self.deceleration()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecelerationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECELERATE(self):
            return self.getToken(BosParser.DECELERATE, 0)

        def expression(self):
            return self.getTypedRuleContext(BosParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BosParser.RULE_deceleration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeceleration" ):
                listener.enterDeceleration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeceleration" ):
                listener.exitDeceleration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeceleration" ):
                return visitor.visitDeceleration(self)
            else:
                return visitor.visitChildren(self)




    def deceleration(self):

        localctx = BosParser.DecelerationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_deceleration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.match(BosParser.DECELERATE)
            self.state = 346
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WaitForTurnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WAIT_FOR_TURN(self):
            return self.getToken(BosParser.WAIT_FOR_TURN, 0)

        def pieceName(self):
            return self.getTypedRuleContext(BosParser.PieceNameContext,0)


        def AROUND(self):
            return self.getToken(BosParser.AROUND, 0)

        def axis(self):
            return self.getTypedRuleContext(BosParser.AxisContext,0)


        def getRuleIndex(self):
            return BosParser.RULE_waitForTurnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWaitForTurnStatement" ):
                listener.enterWaitForTurnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWaitForTurnStatement" ):
                listener.exitWaitForTurnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWaitForTurnStatement" ):
                return visitor.visitWaitForTurnStatement(self)
            else:
                return visitor.visitChildren(self)




    def waitForTurnStatement(self):

        localctx = BosParser.WaitForTurnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_waitForTurnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.match(BosParser.WAIT_FOR_TURN)
            self.state = 349
            self.pieceName()
            self.state = 350
            self.match(BosParser.AROUND)
            self.state = 351
            self.axis()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WaitForMoveStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WAIT_FOR_MOVE(self):
            return self.getToken(BosParser.WAIT_FOR_MOVE, 0)

        def pieceName(self):
            return self.getTypedRuleContext(BosParser.PieceNameContext,0)


        def ALONG(self):
            return self.getToken(BosParser.ALONG, 0)

        def axis(self):
            return self.getTypedRuleContext(BosParser.AxisContext,0)


        def getRuleIndex(self):
            return BosParser.RULE_waitForMoveStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWaitForMoveStatement" ):
                listener.enterWaitForMoveStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWaitForMoveStatement" ):
                listener.exitWaitForMoveStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWaitForMoveStatement" ):
                return visitor.visitWaitForMoveStatement(self)
            else:
                return visitor.visitChildren(self)




    def waitForMoveStatement(self):

        localctx = BosParser.WaitForMoveStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_waitForMoveStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 353
            self.match(BosParser.WAIT_FOR_MOVE)
            self.state = 354
            self.pieceName()
            self.state = 355
            self.match(BosParser.ALONG)
            self.state = 356
            self.axis()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EmitSfxStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EMIT_SFX(self):
            return self.getToken(BosParser.EMIT_SFX, 0)

        def expression(self):
            return self.getTypedRuleContext(BosParser.ExpressionContext,0)


        def FROM(self):
            return self.getToken(BosParser.FROM, 0)

        def pieceName(self):
            return self.getTypedRuleContext(BosParser.PieceNameContext,0)


        def getRuleIndex(self):
            return BosParser.RULE_emitSfxStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmitSfxStatement" ):
                listener.enterEmitSfxStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmitSfxStatement" ):
                listener.exitEmitSfxStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmitSfxStatement" ):
                return visitor.visitEmitSfxStatement(self)
            else:
                return visitor.visitChildren(self)




    def emitSfxStatement(self):

        localctx = BosParser.EmitSfxStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_emitSfxStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.match(BosParser.EMIT_SFX)
            self.state = 359
            self.expression()
            self.state = 360
            self.match(BosParser.FROM)
            self.state = 361
            self.pieceName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PlaySoundStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLAY_SOUND(self):
            return self.getToken(BosParser.PLAY_SOUND, 0)

        def L_PAREN(self):
            return self.getToken(BosParser.L_PAREN, 0)

        def stringConstant(self):
            return self.getTypedRuleContext(BosParser.StringConstantContext,0)


        def COMMA(self):
            return self.getToken(BosParser.COMMA, 0)

        def expression(self):
            return self.getTypedRuleContext(BosParser.ExpressionContext,0)


        def R_PAREN(self):
            return self.getToken(BosParser.R_PAREN, 0)

        def getRuleIndex(self):
            return BosParser.RULE_playSoundStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlaySoundStatement" ):
                listener.enterPlaySoundStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlaySoundStatement" ):
                listener.exitPlaySoundStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlaySoundStatement" ):
                return visitor.visitPlaySoundStatement(self)
            else:
                return visitor.visitChildren(self)




    def playSoundStatement(self):

        localctx = BosParser.PlaySoundStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_playSoundStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.match(BosParser.PLAY_SOUND)
            self.state = 364
            self.match(BosParser.L_PAREN)
            self.state = 365
            self.stringConstant()
            self.state = 366
            self.match(BosParser.COMMA)
            self.state = 367
            self.expression()
            self.state = 368
            self.match(BosParser.R_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HideStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HIDE(self):
            return self.getToken(BosParser.HIDE, 0)

        def pieceName(self):
            return self.getTypedRuleContext(BosParser.PieceNameContext,0)


        def getRuleIndex(self):
            return BosParser.RULE_hideStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHideStatement" ):
                listener.enterHideStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHideStatement" ):
                listener.exitHideStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHideStatement" ):
                return visitor.visitHideStatement(self)
            else:
                return visitor.visitChildren(self)




    def hideStatement(self):

        localctx = BosParser.HideStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_hideStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.match(BosParser.HIDE)
            self.state = 371
            self.pieceName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShowStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SHOW(self):
            return self.getToken(BosParser.SHOW, 0)

        def pieceName(self):
            return self.getTypedRuleContext(BosParser.PieceNameContext,0)


        def getRuleIndex(self):
            return BosParser.RULE_showStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShowStatement" ):
                listener.enterShowStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShowStatement" ):
                listener.exitShowStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShowStatement" ):
                return visitor.visitShowStatement(self)
            else:
                return visitor.visitChildren(self)




    def showStatement(self):

        localctx = BosParser.ShowStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_showStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            self.match(BosParser.SHOW)
            self.state = 374
            self.pieceName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExplodeStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXPLODE(self):
            return self.getToken(BosParser.EXPLODE, 0)

        def pieceName(self):
            return self.getTypedRuleContext(BosParser.PieceNameContext,0)


        def TYPE(self):
            return self.getToken(BosParser.TYPE, 0)

        def expression(self):
            return self.getTypedRuleContext(BosParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BosParser.RULE_explodeStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExplodeStatement" ):
                listener.enterExplodeStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExplodeStatement" ):
                listener.exitExplodeStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExplodeStatement" ):
                return visitor.visitExplodeStatement(self)
            else:
                return visitor.visitChildren(self)




    def explodeStatement(self):

        localctx = BosParser.ExplodeStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_explodeStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.match(BosParser.EXPLODE)
            self.state = 377
            self.pieceName()
            self.state = 378
            self.match(BosParser.TYPE)
            self.state = 379
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CALL_SCRIPT(self):
            return self.getToken(BosParser.CALL_SCRIPT, 0)

        def funcName(self):
            return self.getTypedRuleContext(BosParser.FuncNameContext,0)


        def L_PAREN(self):
            return self.getToken(BosParser.L_PAREN, 0)

        def expressionList(self):
            return self.getTypedRuleContext(BosParser.ExpressionListContext,0)


        def R_PAREN(self):
            return self.getToken(BosParser.R_PAREN, 0)

        def getRuleIndex(self):
            return BosParser.RULE_callStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallStatement" ):
                listener.enterCallStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallStatement" ):
                listener.exitCallStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallStatement" ):
                return visitor.visitCallStatement(self)
            else:
                return visitor.visitChildren(self)




    def callStatement(self):

        localctx = BosParser.CallStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_callStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.match(BosParser.CALL_SCRIPT)
            self.state = 382
            self.funcName()
            self.state = 383
            self.match(BosParser.L_PAREN)
            self.state = 384
            self.expressionList()
            self.state = 385
            self.match(BosParser.R_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StartStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def START_SCRIPT(self):
            return self.getToken(BosParser.START_SCRIPT, 0)

        def funcName(self):
            return self.getTypedRuleContext(BosParser.FuncNameContext,0)


        def L_PAREN(self):
            return self.getToken(BosParser.L_PAREN, 0)

        def expressionList(self):
            return self.getTypedRuleContext(BosParser.ExpressionListContext,0)


        def R_PAREN(self):
            return self.getToken(BosParser.R_PAREN, 0)

        def getRuleIndex(self):
            return BosParser.RULE_startStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStartStatement" ):
                listener.enterStartStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStartStatement" ):
                listener.exitStartStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStartStatement" ):
                return visitor.visitStartStatement(self)
            else:
                return visitor.visitChildren(self)




    def startStatement(self):

        localctx = BosParser.StartStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_startStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.match(BosParser.START_SCRIPT)
            self.state = 388
            self.funcName()
            self.state = 389
            self.match(BosParser.L_PAREN)
            self.state = 390
            self.expressionList()
            self.state = 391
            self.match(BosParser.R_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SignalStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SIGNAL(self):
            return self.getToken(BosParser.SIGNAL, 0)

        def expression(self):
            return self.getTypedRuleContext(BosParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BosParser.RULE_signalStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSignalStatement" ):
                listener.enterSignalStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSignalStatement" ):
                listener.exitSignalStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSignalStatement" ):
                return visitor.visitSignalStatement(self)
            else:
                return visitor.visitChildren(self)




    def signalStatement(self):

        localctx = BosParser.SignalStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_signalStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.match(BosParser.SIGNAL)
            self.state = 394
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SetSignalMaskStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SET_SIGNAL_MASK(self):
            return self.getToken(BosParser.SET_SIGNAL_MASK, 0)

        def expression(self):
            return self.getTypedRuleContext(BosParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BosParser.RULE_setSignalMaskStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetSignalMaskStatement" ):
                listener.enterSetSignalMaskStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetSignalMaskStatement" ):
                listener.exitSetSignalMaskStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetSignalMaskStatement" ):
                return visitor.visitSetSignalMaskStatement(self)
            else:
                return visitor.visitChildren(self)




    def setSignalMaskStatement(self):

        localctx = BosParser.SetSignalMaskStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_setSignalMaskStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self.match(BosParser.SET_SIGNAL_MASK)
            self.state = 397
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttachUnitStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ATTACH_UNIT(self):
            return self.getToken(BosParser.ATTACH_UNIT, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BosParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BosParser.ExpressionContext,i)


        def TO(self):
            return self.getToken(BosParser.TO, 0)

        def getRuleIndex(self):
            return BosParser.RULE_attachUnitStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttachUnitStatement" ):
                listener.enterAttachUnitStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttachUnitStatement" ):
                listener.exitAttachUnitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttachUnitStatement" ):
                return visitor.visitAttachUnitStatement(self)
            else:
                return visitor.visitChildren(self)




    def attachUnitStatement(self):

        localctx = BosParser.AttachUnitStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_attachUnitStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.match(BosParser.ATTACH_UNIT)
            self.state = 400
            self.expression()
            self.state = 401
            self.match(BosParser.TO)
            self.state = 402
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DropUnitStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DROP_UNIT(self):
            return self.getToken(BosParser.DROP_UNIT, 0)

        def expression(self):
            return self.getTypedRuleContext(BosParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BosParser.RULE_dropUnitStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDropUnitStatement" ):
                listener.enterDropUnitStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDropUnitStatement" ):
                listener.exitDropUnitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDropUnitStatement" ):
                return visitor.visitDropUnitStatement(self)
            else:
                return visitor.visitChildren(self)




    def dropUnitStatement(self):

        localctx = BosParser.DropUnitStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_dropUnitStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self.match(BosParser.DROP_UNIT)
            self.state = 405
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CacheStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CACHE(self):
            return self.getToken(BosParser.CACHE, 0)

        def pieceName(self):
            return self.getTypedRuleContext(BosParser.PieceNameContext,0)


        def getRuleIndex(self):
            return BosParser.RULE_cacheStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCacheStatement" ):
                listener.enterCacheStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCacheStatement" ):
                listener.exitCacheStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCacheStatement" ):
                return visitor.visitCacheStatement(self)
            else:
                return visitor.visitChildren(self)




    def cacheStatement(self):

        localctx = BosParser.CacheStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_cacheStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.match(BosParser.CACHE)
            self.state = 408
            self.pieceName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DontCacheStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DONT_CACHE(self):
            return self.getToken(BosParser.DONT_CACHE, 0)

        def pieceName(self):
            return self.getTypedRuleContext(BosParser.PieceNameContext,0)


        def getRuleIndex(self):
            return BosParser.RULE_dontCacheStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDontCacheStatement" ):
                listener.enterDontCacheStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDontCacheStatement" ):
                listener.exitDontCacheStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDontCacheStatement" ):
                return visitor.visitDontCacheStatement(self)
            else:
                return visitor.visitChildren(self)




    def dontCacheStatement(self):

        localctx = BosParser.DontCacheStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_dontCacheStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.match(BosParser.DONT_CACHE)
            self.state = 411
            self.pieceName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DontShadowStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DONT_SHADOW(self):
            return self.getToken(BosParser.DONT_SHADOW, 0)

        def pieceName(self):
            return self.getTypedRuleContext(BosParser.PieceNameContext,0)


        def getRuleIndex(self):
            return BosParser.RULE_dontShadowStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDontShadowStatement" ):
                listener.enterDontShadowStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDontShadowStatement" ):
                listener.exitDontShadowStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDontShadowStatement" ):
                return visitor.visitDontShadowStatement(self)
            else:
                return visitor.visitChildren(self)




    def dontShadowStatement(self):

        localctx = BosParser.DontShadowStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_dontShadowStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self.match(BosParser.DONT_SHADOW)
            self.state = 414
            self.pieceName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DontShadeStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DONT_SHADE(self):
            return self.getToken(BosParser.DONT_SHADE, 0)

        def pieceName(self):
            return self.getTypedRuleContext(BosParser.PieceNameContext,0)


        def getRuleIndex(self):
            return BosParser.RULE_dontShadeStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDontShadeStatement" ):
                listener.enterDontShadeStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDontShadeStatement" ):
                listener.exitDontShadeStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDontShadeStatement" ):
                return visitor.visitDontShadeStatement(self)
            else:
                return visitor.visitChildren(self)




    def dontShadeStatement(self):

        localctx = BosParser.DontShadeStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_dontShadeStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.match(BosParser.DONT_SHADE)
            self.state = 417
            self.pieceName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressions(self):
            return self.getTypedRuleContext(BosParser.ExpressionsContext,0)


        def getRuleIndex(self):
            return BosParser.RULE_expressionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionList" ):
                listener.enterExpressionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionList" ):
                listener.exitExpressionList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionList" ):
                return visitor.visitExpressionList(self)
            else:
                return visitor.visitChildren(self)




    def expressionList(self):

        localctx = BosParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 13510799150548996) != 0) or ((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & 2079) != 0):
                self.state = 419
                self.expressions()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(BosParser.ExpressionContext,0)


        def commaExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BosParser.CommaExpressionContext)
            else:
                return self.getTypedRuleContext(BosParser.CommaExpressionContext,i)


        def getRuleIndex(self):
            return BosParser.RULE_expressions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressions" ):
                listener.enterExpressions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressions" ):
                listener.exitExpressions(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressions" ):
                return visitor.visitExpressions(self)
            else:
                return visitor.visitChildren(self)




    def expressions(self):

        localctx = BosParser.ExpressionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_expressions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.expression()
            self.state = 426
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 423
                self.commaExpression()
                self.state = 428
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GetTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GET(self):
            return self.getToken(BosParser.GET, 0)

        def term(self):
            return self.getTypedRuleContext(BosParser.TermContext,0)


        def L_PAREN(self):
            return self.getToken(BosParser.L_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(BosParser.ExpressionContext,0)


        def R_PAREN(self):
            return self.getToken(BosParser.R_PAREN, 0)

        def commaExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BosParser.CommaExpressionContext)
            else:
                return self.getTypedRuleContext(BosParser.CommaExpressionContext,i)


        def getRuleIndex(self):
            return BosParser.RULE_getTerm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGetTerm" ):
                listener.enterGetTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGetTerm" ):
                listener.exitGetTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGetTerm" ):
                return visitor.visitGetTerm(self)
            else:
                return visitor.visitChildren(self)




    def getTerm(self):

        localctx = BosParser.GetTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_getTerm)
        self._la = 0 # Token type
        try:
            self.state = 446
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 429
                self.match(BosParser.GET)
                self.state = 430
                self.term()
                self.state = 431
                self.match(BosParser.L_PAREN)
                self.state = 432
                self.expression()
                self.state = 434
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                if la_ == 1:
                    self.state = 433
                    self.commaExpression()


                self.state = 437
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                if la_ == 1:
                    self.state = 436
                    self.commaExpression()


                self.state = 440
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 439
                    self.commaExpression()


                self.state = 442
                self.match(BosParser.R_PAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 444
                self.match(BosParser.GET)
                self.state = 445
                self.term()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommaExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(BosParser.COMMA, 0)

        def expression(self):
            return self.getTypedRuleContext(BosParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BosParser.RULE_commaExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommaExpression" ):
                listener.enterCommaExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommaExpression" ):
                listener.exitCommaExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommaExpression" ):
                return visitor.visitCommaExpression(self)
            else:
                return visitor.visitChildren(self)




    def commaExpression(self):

        localctx = BosParser.CommaExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_commaExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448
            self.match(BosParser.COMMA)
            self.state = 449
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self):
            return self.getTypedRuleContext(BosParser.TermContext,0)


        def opterm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BosParser.OptermContext)
            else:
                return self.getTypedRuleContext(BosParser.OptermContext,i)


        def getRuleIndex(self):
            return BosParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = BosParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.term()
            self.state = 455
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 805207040) != 0):
                self.state = 452
                self.opterm()
                self.state = 457
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OptermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def op(self):
            return self.getTypedRuleContext(BosParser.OpContext,0)


        def term(self):
            return self.getTypedRuleContext(BosParser.TermContext,0)


        def getRuleIndex(self):
            return BosParser.RULE_opterm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpterm" ):
                listener.enterOpterm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpterm" ):
                listener.exitOpterm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpterm" ):
                return visitor.visitOpterm(self)
            else:
                return visitor.visitChildren(self)




    def opterm(self):

        localctx = BosParser.OptermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_opterm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
            self.op()
            self.state = 459
            self.term()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getTerm(self):
            return self.getTypedRuleContext(BosParser.GetTermContext,0)


        def rand(self):
            return self.getTypedRuleContext(BosParser.RandContext,0)


        def L_PAREN(self):
            return self.getToken(BosParser.L_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(BosParser.ExpressionContext,0)


        def R_PAREN(self):
            return self.getToken(BosParser.R_PAREN, 0)

        def unaryOp(self):
            return self.getTypedRuleContext(BosParser.UnaryOpContext,0)


        def term(self):
            return self.getTypedRuleContext(BosParser.TermContext,0)


        def varName(self):
            return self.getTypedRuleContext(BosParser.VarNameContext,0)


        def constant(self):
            return self.getTypedRuleContext(BosParser.ConstantContext,0)


        def unknown_unit_value(self):
            return self.getTypedRuleContext(BosParser.Unknown_unit_valueContext,0)


        def getRuleIndex(self):
            return BosParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = BosParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_term)
        try:
            self.state = 473
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [52]:
                self.enterOuterAlt(localctx, 1)
                self.state = 461
                self.getTerm()
                pass
            elif token in [75]:
                self.enterOuterAlt(localctx, 2)
                self.state = 462
                self.rand()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 463
                self.match(BosParser.L_PAREN)
                self.state = 464
                self.expression()
                self.state = 465
                self.match(BosParser.R_PAREN)
                pass
            elif token in [11, 28]:
                self.enterOuterAlt(localctx, 4)
                self.state = 467
                self.unaryOp()
                self.state = 468
                self.term()
                pass
            elif token in [86]:
                self.enterOuterAlt(localctx, 5)
                self.state = 470
                self.varName()
                pass
            elif token in [76, 77, 78, 79]:
                self.enterOuterAlt(localctx, 6)
                self.state = 471
                self.constant()
                pass
            elif token in [53]:
                self.enterOuterAlt(localctx, 7)
                self.state = 472
                self.unknown_unit_value()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RAND(self):
            return self.getToken(BosParser.RAND, 0)

        def L_PAREN(self):
            return self.getToken(BosParser.L_PAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BosParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BosParser.ExpressionContext,i)


        def COMMA(self):
            return self.getToken(BosParser.COMMA, 0)

        def R_PAREN(self):
            return self.getToken(BosParser.R_PAREN, 0)

        def getRuleIndex(self):
            return BosParser.RULE_rand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRand" ):
                listener.enterRand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRand" ):
                listener.exitRand(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRand" ):
                return visitor.visitRand(self)
            else:
                return visitor.visitChildren(self)




    def rand(self):

        localctx = BosParser.RandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_rand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475
            self.match(BosParser.RAND)
            self.state = 476
            self.match(BosParser.L_PAREN)
            self.state = 477
            self.expression()
            self.state = 478
            self.match(BosParser.COMMA)
            self.state = 479
            self.expression()
            self.state = 480
            self.match(BosParser.R_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOGICAL_NOT(self):
            return self.getToken(BosParser.LOGICAL_NOT, 0)

        def OP_MINUS(self):
            return self.getToken(BosParser.OP_MINUS, 0)

        def getRuleIndex(self):
            return BosParser.RULE_unaryOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryOp" ):
                listener.enterUnaryOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryOp" ):
                listener.exitUnaryOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryOp" ):
                return visitor.visitUnaryOp(self)
            else:
                return visitor.visitChildren(self)




    def unaryOp(self):

        localctx = BosParser.UnaryOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_unaryOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 482
            _la = self._input.LA(1)
            if not(_la==11 or _la==28):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_MULT(self):
            return self.getToken(BosParser.OP_MULT, 0)

        def OP_DIV(self):
            return self.getToken(BosParser.OP_DIV, 0)

        def OP_MOD(self):
            return self.getToken(BosParser.OP_MOD, 0)

        def OP_ADD(self):
            return self.getToken(BosParser.OP_ADD, 0)

        def OP_MINUS(self):
            return self.getToken(BosParser.OP_MINUS, 0)

        def COMP_LESS(self):
            return self.getToken(BosParser.COMP_LESS, 0)

        def COMP_GREATER(self):
            return self.getToken(BosParser.COMP_GREATER, 0)

        def COMP_LESS_EQUAL(self):
            return self.getToken(BosParser.COMP_LESS_EQUAL, 0)

        def COMP_GREATER_EQUAL(self):
            return self.getToken(BosParser.COMP_GREATER_EQUAL, 0)

        def COMP_EQUAL(self):
            return self.getToken(BosParser.COMP_EQUAL, 0)

        def COMP_NOT_EQUAL(self):
            return self.getToken(BosParser.COMP_NOT_EQUAL, 0)

        def BITWISE_AND(self):
            return self.getToken(BosParser.BITWISE_AND, 0)

        def BITWISE_OR(self):
            return self.getToken(BosParser.BITWISE_OR, 0)

        def BITWISE_XOR(self):
            return self.getToken(BosParser.BITWISE_XOR, 0)

        def LOGICAL_AND(self):
            return self.getToken(BosParser.LOGICAL_AND, 0)

        def LOGICAL_OR(self):
            return self.getToken(BosParser.LOGICAL_OR, 0)

        def LOGICAL_XOR(self):
            return self.getToken(BosParser.LOGICAL_XOR, 0)

        def getRuleIndex(self):
            return BosParser.RULE_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp" ):
                listener.enterOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp" ):
                listener.exitOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp" ):
                return visitor.visitOp(self)
            else:
                return visitor.visitChildren(self)




    def op(self):

        localctx = BosParser.OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_op)
        self._la = 0 # Token type
        try:
            self.state = 494
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12, 13, 14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 484
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 28672) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [10, 11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 485
                _la = self._input.LA(1)
                if not(_la==10 or _la==11):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [22, 23, 24, 25]:
                self.enterOuterAlt(localctx, 3)
                self.state = 486
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 62914560) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [20, 21]:
                self.enterOuterAlt(localctx, 4)
                self.state = 487
                _la = self._input.LA(1)
                if not(_la==20 or _la==21):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 5)
                self.state = 488
                self.match(BosParser.BITWISE_AND)
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 6)
                self.state = 489
                self.match(BosParser.BITWISE_OR)
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 7)
                self.state = 490
                self.match(BosParser.BITWISE_XOR)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 8)
                self.state = 491
                self.match(BosParser.LOGICAL_AND)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 9)
                self.state = 492
                self.match(BosParser.LOGICAL_OR)
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 10)
                self.state = 493
                self.match(BosParser.LOGICAL_XOR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LINEAR_CONSTANT(self):
            return self.getToken(BosParser.LINEAR_CONSTANT, 0)

        def DEGREES_CONSTANT(self):
            return self.getToken(BosParser.DEGREES_CONSTANT, 0)

        def INT(self):
            return self.getToken(BosParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BosParser.FLOAT, 0)

        def getRuleIndex(self):
            return BosParser.RULE_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant" ):
                listener.enterConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant" ):
                listener.exitConstant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstant" ):
                return visitor.visitConstant(self)
            else:
                return visitor.visitChildren(self)




    def constant(self):

        localctx = BosParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 496
            _la = self._input.LA(1)
            if not(((((_la - 76)) & ~0x3f) == 0 and ((1 << (_la - 76)) & 15) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unknown_unit_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNKNOWN_UNIT_VALUE(self):
            return self.getToken(BosParser.UNKNOWN_UNIT_VALUE, 0)

        def L_PAREN(self):
            return self.getToken(BosParser.L_PAREN, 0)

        def INT(self):
            return self.getToken(BosParser.INT, 0)

        def R_PAREN(self):
            return self.getToken(BosParser.R_PAREN, 0)

        def getRuleIndex(self):
            return BosParser.RULE_unknown_unit_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnknown_unit_value" ):
                listener.enterUnknown_unit_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnknown_unit_value" ):
                listener.exitUnknown_unit_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnknown_unit_value" ):
                return visitor.visitUnknown_unit_value(self)
            else:
                return visitor.visitChildren(self)




    def unknown_unit_value(self):

        localctx = BosParser.Unknown_unit_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_unknown_unit_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498
            self.match(BosParser.UNKNOWN_UNIT_VALUE)
            self.state = 499
            self.match(BosParser.L_PAREN)
            self.state = 500
            self.match(BosParser.INT)
            self.state = 501
            self.match(BosParser.R_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(BosParser.STRING, 0)

        def getRuleIndex(self):
            return BosParser.RULE_stringConstant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringConstant" ):
                listener.enterStringConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringConstant" ):
                listener.exitStringConstant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringConstant" ):
                return visitor.visitStringConstant(self)
            else:
                return visitor.visitChildren(self)




    def stringConstant(self):

        localctx = BosParser.StringConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_stringConstant)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 503
            self.match(BosParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





