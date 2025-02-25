# Generated from E:/bar_dev/antlr4_based_bos_parser/bos/BosParser.g4 by ANTLR 4.13.2
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
        4,1,88,521,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,58,1,0,
        5,0,120,8,0,10,0,12,0,123,9,0,1,1,1,1,1,1,3,1,128,8,1,1,2,1,2,1,
        2,1,2,5,2,134,8,2,10,2,12,2,137,9,2,1,2,1,2,1,3,1,3,1,4,1,4,1,4,
        1,4,5,4,147,8,4,10,4,12,4,150,9,4,1,4,1,4,1,5,1,5,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,5,6,163,8,6,10,6,12,6,166,9,6,1,6,1,6,3,6,170,8,6,
        1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,5,9,180,8,9,10,9,12,9,183,9,9,1,
        9,1,9,3,9,187,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,3,10,202,8,10,1,11,1,11,1,11,1,11,5,11,208,8,11,
        10,11,12,11,211,9,11,1,12,1,12,1,12,1,12,1,12,1,12,3,12,219,8,12,
        1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,3,15,238,8,15,1,15,1,15,1,15,1,16,1,16,1,16,
        1,16,1,16,1,16,3,16,249,8,16,1,17,1,17,1,17,1,18,1,18,1,18,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,3,19,282,
        8,19,1,20,1,20,1,20,3,20,287,8,20,1,21,1,21,1,21,1,22,1,22,1,22,
        1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,3,23,304,8,23,1,23,
        3,23,307,8,23,1,23,3,23,310,8,23,1,23,1,23,3,23,314,8,23,1,24,1,
        24,1,25,1,25,1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,
        26,1,26,1,27,1,27,1,27,3,27,335,8,27,1,28,1,28,1,28,1,28,1,28,1,
        28,1,28,3,28,344,8,28,1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,30,3,
        30,354,8,30,1,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,1,33,1,33,1,
        33,1,33,1,33,1,34,1,34,1,34,1,34,1,34,1,35,1,35,1,35,1,35,1,35,1,
        35,1,35,1,36,1,36,1,36,1,37,1,37,1,37,1,38,1,38,1,38,1,38,1,38,1,
        39,1,39,1,39,1,39,1,39,1,39,1,39,1,39,3,39,400,8,39,1,40,1,40,1,
        40,1,40,1,40,1,40,1,40,1,40,3,40,410,8,40,1,41,1,41,1,41,1,42,1,
        42,1,42,1,43,1,43,1,43,1,43,1,43,1,44,1,44,1,44,1,45,1,45,1,45,1,
        46,1,46,1,46,1,47,1,47,1,47,1,48,1,48,1,48,1,49,1,49,5,49,440,8,
        49,10,49,12,49,443,9,49,1,50,1,50,1,50,1,51,1,51,1,51,1,51,1,51,
        1,51,1,51,1,51,1,51,3,51,457,8,51,1,51,1,51,1,51,1,51,1,51,1,51,
        1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,51,
        1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,51,1,51,5,51,489,
        8,51,10,51,12,51,492,9,51,1,52,1,52,1,52,1,52,1,52,3,52,499,8,52,
        1,53,1,53,1,53,3,53,504,8,53,1,54,1,54,1,55,1,55,1,55,1,55,1,55,
        1,55,1,55,1,56,1,56,1,57,1,57,1,58,1,58,1,58,0,1,102,59,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,
        52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,
        96,98,100,102,104,106,108,110,112,114,116,0,7,1,0,71,73,2,0,11,11,
        28,28,1,0,12,14,1,0,10,11,1,0,22,25,1,0,20,21,1,0,75,77,532,0,121,
        1,0,0,0,2,127,1,0,0,0,4,129,1,0,0,0,6,140,1,0,0,0,8,142,1,0,0,0,
        10,153,1,0,0,0,12,155,1,0,0,0,14,173,1,0,0,0,16,175,1,0,0,0,18,186,
        1,0,0,0,20,201,1,0,0,0,22,203,1,0,0,0,24,212,1,0,0,0,26,220,1,0,
        0,0,28,223,1,0,0,0,30,229,1,0,0,0,32,248,1,0,0,0,34,250,1,0,0,0,
        36,253,1,0,0,0,38,281,1,0,0,0,40,286,1,0,0,0,42,288,1,0,0,0,44,291,
        1,0,0,0,46,313,1,0,0,0,48,315,1,0,0,0,50,317,1,0,0,0,52,324,1,0,
        0,0,54,334,1,0,0,0,56,336,1,0,0,0,58,345,1,0,0,0,60,348,1,0,0,0,
        62,355,1,0,0,0,64,358,1,0,0,0,66,363,1,0,0,0,68,368,1,0,0,0,70,373,
        1,0,0,0,72,380,1,0,0,0,74,383,1,0,0,0,76,386,1,0,0,0,78,391,1,0,
        0,0,80,401,1,0,0,0,82,411,1,0,0,0,84,414,1,0,0,0,86,417,1,0,0,0,
        88,422,1,0,0,0,90,425,1,0,0,0,92,428,1,0,0,0,94,431,1,0,0,0,96,434,
        1,0,0,0,98,437,1,0,0,0,100,444,1,0,0,0,102,456,1,0,0,0,104,498,1,
        0,0,0,106,503,1,0,0,0,108,505,1,0,0,0,110,507,1,0,0,0,112,514,1,
        0,0,0,114,516,1,0,0,0,116,518,1,0,0,0,118,120,3,2,1,0,119,118,1,
        0,0,0,120,123,1,0,0,0,121,119,1,0,0,0,121,122,1,0,0,0,122,1,1,0,
        0,0,123,121,1,0,0,0,124,128,3,4,2,0,125,128,3,8,4,0,126,128,3,12,
        6,0,127,124,1,0,0,0,127,125,1,0,0,0,127,126,1,0,0,0,128,3,1,0,0,
        0,129,130,5,36,0,0,130,135,3,6,3,0,131,132,5,1,0,0,132,134,3,6,3,
        0,133,131,1,0,0,0,134,137,1,0,0,0,135,133,1,0,0,0,135,136,1,0,0,
        0,136,138,1,0,0,0,137,135,1,0,0,0,138,139,5,8,0,0,139,5,1,0,0,0,
        140,141,5,87,0,0,141,7,1,0,0,0,142,143,5,34,0,0,143,148,3,10,5,0,
        144,145,5,1,0,0,145,147,3,10,5,0,146,144,1,0,0,0,147,150,1,0,0,0,
        148,146,1,0,0,0,148,149,1,0,0,0,149,151,1,0,0,0,150,148,1,0,0,0,
        151,152,5,8,0,0,152,9,1,0,0,0,153,154,5,87,0,0,154,11,1,0,0,0,155,
        169,3,14,7,0,156,157,5,2,0,0,157,170,5,3,0,0,158,159,5,2,0,0,159,
        164,3,16,8,0,160,161,5,1,0,0,161,163,3,16,8,0,162,160,1,0,0,0,163,
        166,1,0,0,0,164,162,1,0,0,0,164,165,1,0,0,0,165,167,1,0,0,0,166,
        164,1,0,0,0,167,168,5,3,0,0,168,170,1,0,0,0,169,156,1,0,0,0,169,
        158,1,0,0,0,170,171,1,0,0,0,171,172,3,18,9,0,172,13,1,0,0,0,173,
        174,5,87,0,0,174,15,1,0,0,0,175,176,5,87,0,0,176,17,1,0,0,0,177,
        181,5,4,0,0,178,180,3,20,10,0,179,178,1,0,0,0,180,183,1,0,0,0,181,
        179,1,0,0,0,181,182,1,0,0,0,182,184,1,0,0,0,183,181,1,0,0,0,184,
        187,5,5,0,0,185,187,3,20,10,0,186,177,1,0,0,0,186,185,1,0,0,0,187,
        19,1,0,0,0,188,189,3,38,19,0,189,190,5,8,0,0,190,202,1,0,0,0,191,
        192,3,22,11,0,192,193,5,8,0,0,193,202,1,0,0,0,194,202,3,24,12,0,
        195,202,3,28,14,0,196,202,3,30,15,0,197,198,3,32,16,0,198,199,5,
        8,0,0,199,202,1,0,0,0,200,202,5,8,0,0,201,188,1,0,0,0,201,191,1,
        0,0,0,201,194,1,0,0,0,201,195,1,0,0,0,201,196,1,0,0,0,201,197,1,
        0,0,0,201,200,1,0,0,0,202,21,1,0,0,0,203,204,5,35,0,0,204,209,3,
        10,5,0,205,206,5,1,0,0,206,208,3,10,5,0,207,205,1,0,0,0,208,211,
        1,0,0,0,209,207,1,0,0,0,209,210,1,0,0,0,210,23,1,0,0,0,211,209,1,
        0,0,0,212,213,5,30,0,0,213,214,5,2,0,0,214,215,3,102,51,0,215,216,
        5,3,0,0,216,218,3,18,9,0,217,219,3,26,13,0,218,217,1,0,0,0,218,219,
        1,0,0,0,219,25,1,0,0,0,220,221,5,31,0,0,221,222,3,18,9,0,222,27,
        1,0,0,0,223,224,5,32,0,0,224,225,5,2,0,0,225,226,3,102,51,0,226,
        227,5,3,0,0,227,228,3,18,9,0,228,29,1,0,0,0,229,230,5,33,0,0,230,
        231,5,2,0,0,231,232,3,102,51,0,232,233,5,8,0,0,233,234,3,102,51,
        0,234,235,5,8,0,0,235,237,3,102,51,0,236,238,5,8,0,0,237,236,1,0,
        0,0,237,238,1,0,0,0,238,239,1,0,0,0,239,240,5,3,0,0,240,241,3,18,
        9,0,241,31,1,0,0,0,242,243,3,10,5,0,243,244,5,9,0,0,244,245,3,102,
        51,0,245,249,1,0,0,0,246,249,3,34,17,0,247,249,3,36,18,0,248,242,
        1,0,0,0,248,246,1,0,0,0,248,247,1,0,0,0,249,33,1,0,0,0,250,251,5,
        15,0,0,251,252,3,10,5,0,252,35,1,0,0,0,253,254,5,16,0,0,254,255,
        3,10,5,0,255,37,1,0,0,0,256,282,3,78,39,0,257,282,3,80,40,0,258,
        282,3,56,28,0,259,282,3,60,30,0,260,282,3,50,25,0,261,282,3,52,26,
        0,262,282,3,64,32,0,263,282,3,66,33,0,264,282,3,68,34,0,265,282,
        3,42,21,0,266,282,3,72,36,0,267,282,3,74,37,0,268,282,3,76,38,0,
        269,282,3,82,41,0,270,282,3,84,42,0,271,282,3,44,22,0,272,282,3,
        46,23,0,273,282,3,86,43,0,274,282,3,88,44,0,275,282,3,40,20,0,276,
        282,3,70,35,0,277,282,3,90,45,0,278,282,3,92,46,0,279,282,3,94,47,
        0,280,282,3,96,48,0,281,256,1,0,0,0,281,257,1,0,0,0,281,258,1,0,
        0,0,281,259,1,0,0,0,281,260,1,0,0,0,281,261,1,0,0,0,281,262,1,0,
        0,0,281,263,1,0,0,0,281,264,1,0,0,0,281,265,1,0,0,0,281,266,1,0,
        0,0,281,267,1,0,0,0,281,268,1,0,0,0,281,269,1,0,0,0,281,270,1,0,
        0,0,281,271,1,0,0,0,281,272,1,0,0,0,281,273,1,0,0,0,281,274,1,0,
        0,0,281,275,1,0,0,0,281,276,1,0,0,0,281,277,1,0,0,0,281,278,1,0,
        0,0,281,279,1,0,0,0,281,280,1,0,0,0,282,39,1,0,0,0,283,287,5,65,
        0,0,284,285,5,65,0,0,285,287,3,102,51,0,286,283,1,0,0,0,286,284,
        1,0,0,0,287,41,1,0,0,0,288,289,5,56,0,0,289,290,3,102,51,0,290,43,
        1,0,0,0,291,292,5,51,0,0,292,293,3,104,52,0,293,294,5,41,0,0,294,
        295,3,102,51,0,295,45,1,0,0,0,296,297,5,52,0,0,297,314,3,104,52,
        0,298,299,5,52,0,0,299,300,3,104,52,0,300,301,5,2,0,0,301,303,3,
        102,51,0,302,304,3,100,50,0,303,302,1,0,0,0,303,304,1,0,0,0,304,
        306,1,0,0,0,305,307,3,100,50,0,306,305,1,0,0,0,306,307,1,0,0,0,307,
        309,1,0,0,0,308,310,3,100,50,0,309,308,1,0,0,0,309,310,1,0,0,0,310,
        311,1,0,0,0,311,312,5,3,0,0,312,314,1,0,0,0,313,296,1,0,0,0,313,
        298,1,0,0,0,314,47,1,0,0,0,315,316,7,0,0,0,316,49,1,0,0,0,317,318,
        5,37,0,0,318,319,3,6,3,0,319,320,5,41,0,0,320,321,3,48,24,0,321,
        322,3,102,51,0,322,323,3,54,27,0,323,51,1,0,0,0,324,325,5,39,0,0,
        325,326,3,6,3,0,326,327,5,41,0,0,327,328,3,48,24,0,328,329,3,102,
        51,0,329,330,3,54,27,0,330,53,1,0,0,0,331,335,5,43,0,0,332,333,5,
        44,0,0,333,335,3,102,51,0,334,331,1,0,0,0,334,332,1,0,0,0,335,55,
        1,0,0,0,336,337,5,45,0,0,337,338,3,6,3,0,338,339,5,38,0,0,339,340,
        3,48,24,0,340,341,5,44,0,0,341,343,3,102,51,0,342,344,3,58,29,0,
        343,342,1,0,0,0,343,344,1,0,0,0,344,57,1,0,0,0,345,346,5,46,0,0,
        346,347,3,102,51,0,347,59,1,0,0,0,348,349,5,47,0,0,349,350,3,6,3,
        0,350,351,5,38,0,0,351,353,3,48,24,0,352,354,3,62,31,0,353,352,1,
        0,0,0,353,354,1,0,0,0,354,61,1,0,0,0,355,356,5,48,0,0,356,357,3,
        102,51,0,357,63,1,0,0,0,358,359,5,49,0,0,359,360,3,6,3,0,360,361,
        5,38,0,0,361,362,3,48,24,0,362,65,1,0,0,0,363,364,5,50,0,0,364,365,
        3,6,3,0,365,366,5,40,0,0,366,367,3,48,24,0,367,67,1,0,0,0,368,369,
        5,55,0,0,369,370,3,102,51,0,370,371,5,42,0,0,371,372,3,6,3,0,372,
        69,1,0,0,0,373,374,5,70,0,0,374,375,5,2,0,0,375,376,3,116,58,0,376,
        377,5,1,0,0,377,378,3,102,51,0,378,379,5,3,0,0,379,71,1,0,0,0,380,
        381,5,57,0,0,381,382,3,6,3,0,382,73,1,0,0,0,383,384,5,58,0,0,384,
        385,3,6,3,0,385,75,1,0,0,0,386,387,5,59,0,0,387,388,3,6,3,0,388,
        389,5,60,0,0,389,390,3,102,51,0,390,77,1,0,0,0,391,392,5,53,0,0,
        392,399,3,14,7,0,393,394,5,2,0,0,394,400,5,3,0,0,395,396,5,2,0,0,
        396,397,3,98,49,0,397,398,5,3,0,0,398,400,1,0,0,0,399,393,1,0,0,
        0,399,395,1,0,0,0,400,79,1,0,0,0,401,402,5,54,0,0,402,409,3,14,7,
        0,403,404,5,2,0,0,404,410,5,3,0,0,405,406,5,2,0,0,406,407,3,98,49,
        0,407,408,5,3,0,0,408,410,1,0,0,0,409,403,1,0,0,0,409,405,1,0,0,
        0,410,81,1,0,0,0,411,412,5,61,0,0,412,413,3,102,51,0,413,83,1,0,
        0,0,414,415,5,62,0,0,415,416,3,102,51,0,416,85,1,0,0,0,417,418,5,
        63,0,0,418,419,3,102,51,0,419,420,5,41,0,0,420,421,3,102,51,0,421,
        87,1,0,0,0,422,423,5,64,0,0,423,424,3,102,51,0,424,89,1,0,0,0,425,
        426,5,66,0,0,426,427,3,6,3,0,427,91,1,0,0,0,428,429,5,67,0,0,429,
        430,3,6,3,0,430,93,1,0,0,0,431,432,5,68,0,0,432,433,3,6,3,0,433,
        95,1,0,0,0,434,435,5,69,0,0,435,436,3,6,3,0,436,97,1,0,0,0,437,441,
        3,102,51,0,438,440,3,100,50,0,439,438,1,0,0,0,440,443,1,0,0,0,441,
        439,1,0,0,0,441,442,1,0,0,0,442,99,1,0,0,0,443,441,1,0,0,0,444,445,
        5,1,0,0,445,446,3,102,51,0,446,101,1,0,0,0,447,448,6,51,-1,0,448,
        449,5,2,0,0,449,450,3,102,51,0,450,451,5,3,0,0,451,457,1,0,0,0,452,
        457,3,104,52,0,453,457,3,106,53,0,454,455,7,1,0,0,455,457,3,102,
        51,11,456,447,1,0,0,0,456,452,1,0,0,0,456,453,1,0,0,0,456,454,1,
        0,0,0,457,490,1,0,0,0,458,459,10,10,0,0,459,460,7,2,0,0,460,489,
        3,102,51,11,461,462,10,9,0,0,462,463,7,3,0,0,463,489,3,102,51,10,
        464,465,10,8,0,0,465,466,7,4,0,0,466,489,3,102,51,9,467,468,10,7,
        0,0,468,469,7,5,0,0,469,489,3,102,51,8,470,471,10,6,0,0,471,472,
        5,17,0,0,472,489,3,102,51,7,473,474,10,5,0,0,474,475,5,18,0,0,475,
        489,3,102,51,6,476,477,10,4,0,0,477,478,5,19,0,0,478,489,3,102,51,
        5,479,480,10,3,0,0,480,481,5,26,0,0,481,489,3,102,51,4,482,483,10,
        2,0,0,483,484,5,27,0,0,484,489,3,102,51,3,485,486,10,1,0,0,486,487,
        5,29,0,0,487,489,3,102,51,2,488,458,1,0,0,0,488,461,1,0,0,0,488,
        464,1,0,0,0,488,467,1,0,0,0,488,470,1,0,0,0,488,473,1,0,0,0,488,
        476,1,0,0,0,488,479,1,0,0,0,488,482,1,0,0,0,488,485,1,0,0,0,489,
        492,1,0,0,0,490,488,1,0,0,0,490,491,1,0,0,0,491,103,1,0,0,0,492,
        490,1,0,0,0,493,499,3,114,57,0,494,495,5,2,0,0,495,496,3,104,52,
        0,496,497,5,3,0,0,497,499,1,0,0,0,498,493,1,0,0,0,498,494,1,0,0,
        0,499,105,1,0,0,0,500,504,3,108,54,0,501,504,3,110,55,0,502,504,
        3,112,56,0,503,500,1,0,0,0,503,501,1,0,0,0,503,502,1,0,0,0,504,107,
        1,0,0,0,505,506,3,46,23,0,506,109,1,0,0,0,507,508,5,74,0,0,508,509,
        5,2,0,0,509,510,3,102,51,0,510,511,5,1,0,0,511,512,3,102,51,0,512,
        513,5,3,0,0,513,111,1,0,0,0,514,515,3,10,5,0,515,113,1,0,0,0,516,
        517,7,6,0,0,517,115,1,0,0,0,518,519,5,88,0,0,519,117,1,0,0,0,30,
        121,127,135,148,164,169,181,186,201,209,218,237,248,281,286,303,
        306,309,313,334,343,353,399,409,441,456,488,490,498,503
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
                     "'get'", "<INVALID>", "<INVALID>", "<INVALID>", "'sleep'", 
                     "'hide'", "'show'", "'explode'", "'type'", "'signal'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'return'", 
                     "'cache'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'rand'" ]

    symbolicNames = [ "<INVALID>", "COMMA", "L_PAREN", "R_PAREN", "L_BRACE", 
                      "R_BRACE", "L_SQUARE_BRACKET", "R_SQUARE_BRACKET", 
                      "SEMICOLON", "EQUAL_ASSIGN", "OP_ADD", "OP_MINUS", 
                      "OP_MULT", "OP_DIV", "OP_MOD", "OP_INCREMENT", "OP_DECREMENT", 
                      "BITWISE_AND", "BITWISE_OR", "BITWISE_XOR", "COMP_EQUAL", 
                      "COMP_NOT_EQUAL", "COMP_LESS", "COMP_LESS_EQUAL", 
                      "COMP_GREATER", "COMP_GREATER_EQUAL", "LOGICAL_AND", 
                      "LOGICAL_OR", "LOGICAL_NOT", "LOGICAL_XOR", "IF", 
                      "ELSE", "WHILE", "FOR", "STATIC_VAR", "VAR", "PIECE", 
                      "TURN", "AROUND", "MOVE", "ALONG", "TO", "FROM", "NOW", 
                      "SPEED", "SPIN", "ACCELERATE", "STOP_SPIN", "DECELERATE", 
                      "WAIT_FOR_TURN", "WAIT_FOR_MOVE", "SET", "GET", "CALL_SCRIPT", 
                      "START_SCRIPT", "EMIT_SFX", "SLEEP", "HIDE", "SHOW", 
                      "EXPLODE", "TYPE", "SIGNAL", "SET_SIGNAL_MASK", "ATTACH_UNIT", 
                      "DROP_UNIT", "RETURN", "CACHE", "DONT_CACHE", "DONT_SHADOW", 
                      "DONT_SHADE", "PLAY_SOUND", "X_AXIS", "Y_AXIS", "Z_AXIS", 
                      "RAND", "LINEAR_CONSTANT", "DEGREES_CONSTANT", "NUMBER", 
                      "FLOAT", "INT", "LINE_DIRECTIVE", "MULTI_LINE_MACRO", 
                      "DIRECTIVE", "LINE_COMMENT", "BLOCK_COMMENT", "WHITESPACE", 
                      "NEWLINE", "ID", "STRING" ]

    RULE_file = 0
    RULE_declaration = 1
    RULE_pieceDecl = 2
    RULE_pieceName = 3
    RULE_staticVarDecl = 4
    RULE_varName = 5
    RULE_funcDecl = 6
    RULE_funcName = 7
    RULE_argName = 8
    RULE_statementBlock = 9
    RULE_statement = 10
    RULE_varStatement = 11
    RULE_ifStatement = 12
    RULE_elseBlock = 13
    RULE_whileStatement = 14
    RULE_forStatement = 15
    RULE_assignStatement = 16
    RULE_incStatement = 17
    RULE_decStatement = 18
    RULE_keywordStatement = 19
    RULE_returnStatement = 20
    RULE_sleepStatement = 21
    RULE_setStatement = 22
    RULE_getStatement = 23
    RULE_axis = 24
    RULE_turnStatement = 25
    RULE_moveStatement = 26
    RULE_speedOrNow = 27
    RULE_spinStatement = 28
    RULE_acceleration = 29
    RULE_stopSpinStatement = 30
    RULE_deceleration = 31
    RULE_waitForTurnStatement = 32
    RULE_waitForMoveStatement = 33
    RULE_emitSfxStatement = 34
    RULE_playSoundStatement = 35
    RULE_hideStatement = 36
    RULE_showStatement = 37
    RULE_explodeStatement = 38
    RULE_callStatement = 39
    RULE_startStatement = 40
    RULE_signalStatement = 41
    RULE_setSignalMaskStatement = 42
    RULE_attachUnitStatement = 43
    RULE_dropUnitStatement = 44
    RULE_cacheStatement = 45
    RULE_dontCacheStatement = 46
    RULE_dontShadowStatement = 47
    RULE_dontShadeStatement = 48
    RULE_expressionList = 49
    RULE_commaExpression = 50
    RULE_expression = 51
    RULE_constTerm = 52
    RULE_varyingTerm = 53
    RULE_getTerm = 54
    RULE_randTerm = 55
    RULE_varNameTerm = 56
    RULE_constant = 57
    RULE_stringConstant = 58

    ruleNames =  [ "file", "declaration", "pieceDecl", "pieceName", "staticVarDecl", 
                   "varName", "funcDecl", "funcName", "argName", "statementBlock", 
                   "statement", "varStatement", "ifStatement", "elseBlock", 
                   "whileStatement", "forStatement", "assignStatement", 
                   "incStatement", "decStatement", "keywordStatement", "returnStatement", 
                   "sleepStatement", "setStatement", "getStatement", "axis", 
                   "turnStatement", "moveStatement", "speedOrNow", "spinStatement", 
                   "acceleration", "stopSpinStatement", "deceleration", 
                   "waitForTurnStatement", "waitForMoveStatement", "emitSfxStatement", 
                   "playSoundStatement", "hideStatement", "showStatement", 
                   "explodeStatement", "callStatement", "startStatement", 
                   "signalStatement", "setSignalMaskStatement", "attachUnitStatement", 
                   "dropUnitStatement", "cacheStatement", "dontCacheStatement", 
                   "dontShadowStatement", "dontShadeStatement", "expressionList", 
                   "commaExpression", "expression", "constTerm", "varyingTerm", 
                   "getTerm", "randTerm", "varNameTerm", "constant", "stringConstant" ]

    EOF = Token.EOF
    COMMA=1
    L_PAREN=2
    R_PAREN=3
    L_BRACE=4
    R_BRACE=5
    L_SQUARE_BRACKET=6
    R_SQUARE_BRACKET=7
    SEMICOLON=8
    EQUAL_ASSIGN=9
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
    CALL_SCRIPT=53
    START_SCRIPT=54
    EMIT_SFX=55
    SLEEP=56
    HIDE=57
    SHOW=58
    EXPLODE=59
    TYPE=60
    SIGNAL=61
    SET_SIGNAL_MASK=62
    ATTACH_UNIT=63
    DROP_UNIT=64
    RETURN=65
    CACHE=66
    DONT_CACHE=67
    DONT_SHADOW=68
    DONT_SHADE=69
    PLAY_SOUND=70
    X_AXIS=71
    Y_AXIS=72
    Z_AXIS=73
    RAND=74
    LINEAR_CONSTANT=75
    DEGREES_CONSTANT=76
    NUMBER=77
    FLOAT=78
    INT=79
    LINE_DIRECTIVE=80
    MULTI_LINE_MACRO=81
    DIRECTIVE=82
    LINE_COMMENT=83
    BLOCK_COMMENT=84
    WHITESPACE=85
    NEWLINE=86
    ID=87
    STRING=88

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
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 34)) & ~0x3f) == 0 and ((1 << (_la - 34)) & 9007199254740997) != 0):
                self.state = 118
                self.declaration()
                self.state = 123
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
            self.state = 127
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.pieceDecl()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.staticVarDecl()
                pass
            elif token in [87]:
                self.enterOuterAlt(localctx, 3)
                self.state = 126
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
            self.state = 129
            self.match(BosParser.PIECE)
            self.state = 130
            self.pieceName()
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 131
                self.match(BosParser.COMMA)
                self.state = 132
                self.pieceName()
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 138
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
            self.state = 140
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
            self.state = 142
            self.match(BosParser.STATIC_VAR)
            self.state = 143
            self.varName()
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 144
                self.match(BosParser.COMMA)
                self.state = 145
                self.varName()
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 151
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
            self.state = 153
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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.funcName()
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 156
                self.match(BosParser.L_PAREN)
                self.state = 157
                self.match(BosParser.R_PAREN)
                pass

            elif la_ == 2:
                self.state = 158
                self.match(BosParser.L_PAREN)
                self.state = 159
                self.argName()
                self.state = 164
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==1:
                    self.state = 160
                    self.match(BosParser.COMMA)
                    self.state = 161
                    self.argName()
                    self.state = 166
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 167
                self.match(BosParser.R_PAREN)
                pass


            self.state = 171
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
            self.state = 173
            self.match(BosParser.ID)
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
        self.enterRule(localctx, 16, self.RULE_argName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
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
        self.enterRule(localctx, 18, self.RULE_statementBlock)
        self._la = 0 # Token type
        try:
            self.state = 186
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.match(BosParser.L_BRACE)
                self.state = 181
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & -1153307797186576128) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 8388735) != 0):
                    self.state = 178
                    self.statement()
                    self.state = 183
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 184
                self.match(BosParser.R_BRACE)
                pass
            elif token in [8, 15, 16, 30, 32, 33, 35, 37, 39, 45, 47, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 87]:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
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
        self.enterRule(localctx, 20, self.RULE_statement)
        try:
            self.state = 201
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37, 39, 45, 47, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70]:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.keywordStatement()
                self.state = 189
                self.match(BosParser.SEMICOLON)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 2)
                self.state = 191
                self.varStatement()
                self.state = 192
                self.match(BosParser.SEMICOLON)
                pass
            elif token in [30]:
                self.enterOuterAlt(localctx, 3)
                self.state = 194
                self.ifStatement()
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 4)
                self.state = 195
                self.whileStatement()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 5)
                self.state = 196
                self.forStatement()
                pass
            elif token in [15, 16, 87]:
                self.enterOuterAlt(localctx, 6)
                self.state = 197
                self.assignStatement()
                self.state = 198
                self.match(BosParser.SEMICOLON)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 7)
                self.state = 200
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


    class VarStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BosParser.VAR, 0)

        def varName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BosParser.VarNameContext)
            else:
                return self.getTypedRuleContext(BosParser.VarNameContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BosParser.COMMA)
            else:
                return self.getToken(BosParser.COMMA, i)

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
        self.enterRule(localctx, 22, self.RULE_varStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(BosParser.VAR)
            self.state = 204
            self.varName()
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 205
                self.match(BosParser.COMMA)
                self.state = 206
                self.varName()
                self.state = 211
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 24, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self.match(BosParser.IF)
            self.state = 213
            self.match(BosParser.L_PAREN)
            self.state = 214
            self.expression(0)
            self.state = 215
            self.match(BosParser.R_PAREN)
            self.state = 216
            self.statementBlock()
            self.state = 218
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 217
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
        self.enterRule(localctx, 26, self.RULE_elseBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            self.match(BosParser.ELSE)
            self.state = 221
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
        self.enterRule(localctx, 28, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(BosParser.WHILE)
            self.state = 224
            self.match(BosParser.L_PAREN)
            self.state = 225
            self.expression(0)
            self.state = 226
            self.match(BosParser.R_PAREN)
            self.state = 227
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
        self.enterRule(localctx, 30, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(BosParser.FOR)
            self.state = 230
            self.match(BosParser.L_PAREN)
            self.state = 231
            self.expression(0)
            self.state = 232
            self.match(BosParser.SEMICOLON)
            self.state = 233
            self.expression(0)
            self.state = 234
            self.match(BosParser.SEMICOLON)
            self.state = 235
            self.expression(0)
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 236
                self.match(BosParser.SEMICOLON)


            self.state = 239
            self.match(BosParser.R_PAREN)
            self.state = 240
            self.statementBlock()
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


        def EQUAL_ASSIGN(self):
            return self.getToken(BosParser.EQUAL_ASSIGN, 0)

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
        self.enterRule(localctx, 32, self.RULE_assignStatement)
        try:
            self.state = 248
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [87]:
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                self.varName()
                self.state = 243
                self.match(BosParser.EQUAL_ASSIGN)
                self.state = 244
                self.expression(0)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 246
                self.incStatement()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 247
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
        self.enterRule(localctx, 34, self.RULE_incStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.match(BosParser.OP_INCREMENT)
            self.state = 251
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
        self.enterRule(localctx, 36, self.RULE_decStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(BosParser.OP_DECREMENT)
            self.state = 254
            self.varName()
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
        self.enterRule(localctx, 38, self.RULE_keywordStatement)
        try:
            self.state = 281
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [53]:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.callStatement()
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                self.startStatement()
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 3)
                self.state = 258
                self.spinStatement()
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 4)
                self.state = 259
                self.stopSpinStatement()
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 5)
                self.state = 260
                self.turnStatement()
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 6)
                self.state = 261
                self.moveStatement()
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 7)
                self.state = 262
                self.waitForTurnStatement()
                pass
            elif token in [50]:
                self.enterOuterAlt(localctx, 8)
                self.state = 263
                self.waitForMoveStatement()
                pass
            elif token in [55]:
                self.enterOuterAlt(localctx, 9)
                self.state = 264
                self.emitSfxStatement()
                pass
            elif token in [56]:
                self.enterOuterAlt(localctx, 10)
                self.state = 265
                self.sleepStatement()
                pass
            elif token in [57]:
                self.enterOuterAlt(localctx, 11)
                self.state = 266
                self.hideStatement()
                pass
            elif token in [58]:
                self.enterOuterAlt(localctx, 12)
                self.state = 267
                self.showStatement()
                pass
            elif token in [59]:
                self.enterOuterAlt(localctx, 13)
                self.state = 268
                self.explodeStatement()
                pass
            elif token in [61]:
                self.enterOuterAlt(localctx, 14)
                self.state = 269
                self.signalStatement()
                pass
            elif token in [62]:
                self.enterOuterAlt(localctx, 15)
                self.state = 270
                self.setSignalMaskStatement()
                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 16)
                self.state = 271
                self.setStatement()
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 17)
                self.state = 272
                self.getStatement()
                pass
            elif token in [63]:
                self.enterOuterAlt(localctx, 18)
                self.state = 273
                self.attachUnitStatement()
                pass
            elif token in [64]:
                self.enterOuterAlt(localctx, 19)
                self.state = 274
                self.dropUnitStatement()
                pass
            elif token in [65]:
                self.enterOuterAlt(localctx, 20)
                self.state = 275
                self.returnStatement()
                pass
            elif token in [70]:
                self.enterOuterAlt(localctx, 21)
                self.state = 276
                self.playSoundStatement()
                pass
            elif token in [66]:
                self.enterOuterAlt(localctx, 22)
                self.state = 277
                self.cacheStatement()
                pass
            elif token in [67]:
                self.enterOuterAlt(localctx, 23)
                self.state = 278
                self.dontCacheStatement()
                pass
            elif token in [68]:
                self.enterOuterAlt(localctx, 24)
                self.state = 279
                self.dontShadowStatement()
                pass
            elif token in [69]:
                self.enterOuterAlt(localctx, 25)
                self.state = 280
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
            self.kw = None # Token
            self.arg1 = None # ExpressionContext

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
        self.enterRule(localctx, 40, self.RULE_returnStatement)
        try:
            self.state = 286
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                localctx.kw = self.match(BosParser.RETURN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 284
                localctx.kw = self.match(BosParser.RETURN)
                self.state = 285
                localctx.arg1 = self.expression(0)
                pass


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
            self.kw = None # Token
            self.arg1 = None # ExpressionContext

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
        self.enterRule(localctx, 42, self.RULE_sleepStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            localctx.kw = self.match(BosParser.SLEEP)
            self.state = 289
            localctx.arg1 = self.expression(0)
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
            self.kw = None # Token
            self.arg1 = None # ConstTermContext
            self.arg2 = None # ExpressionContext

        def TO(self):
            return self.getToken(BosParser.TO, 0)

        def SET(self):
            return self.getToken(BosParser.SET, 0)

        def constTerm(self):
            return self.getTypedRuleContext(BosParser.ConstTermContext,0)


        def expression(self):
            return self.getTypedRuleContext(BosParser.ExpressionContext,0)


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
        self.enterRule(localctx, 44, self.RULE_setStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            localctx.kw = self.match(BosParser.SET)
            self.state = 292
            localctx.arg1 = self.constTerm()
            self.state = 293
            self.match(BosParser.TO)
            self.state = 294
            localctx.arg2 = self.expression(0)
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
            self.kw = None # Token
            self.arg1 = None # ConstTermContext
            self.arg2 = None # ExpressionContext
            self.arg3 = None # CommaExpressionContext
            self.arg4 = None # CommaExpressionContext

        def GET(self):
            return self.getToken(BosParser.GET, 0)

        def constTerm(self):
            return self.getTypedRuleContext(BosParser.ConstTermContext,0)


        def L_PAREN(self):
            return self.getToken(BosParser.L_PAREN, 0)

        def R_PAREN(self):
            return self.getToken(BosParser.R_PAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(BosParser.ExpressionContext,0)


        def commaExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BosParser.CommaExpressionContext)
            else:
                return self.getTypedRuleContext(BosParser.CommaExpressionContext,i)


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
        self.enterRule(localctx, 46, self.RULE_getStatement)
        self._la = 0 # Token type
        try:
            self.state = 313
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                localctx.kw = self.match(BosParser.GET)
                self.state = 297
                localctx.arg1 = self.constTerm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 298
                localctx.kw = self.match(BosParser.GET)
                self.state = 299
                localctx.arg1 = self.constTerm()
                self.state = 300
                self.match(BosParser.L_PAREN)
                self.state = 301
                localctx.arg2 = self.expression(0)
                self.state = 303
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                if la_ == 1:
                    self.state = 302
                    localctx.arg3 = self.commaExpression()


                self.state = 306
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                if la_ == 1:
                    self.state = 305
                    localctx.arg3 = self.commaExpression()


                self.state = 309
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 308
                    localctx.arg4 = self.commaExpression()


                self.state = 311
                self.match(BosParser.R_PAREN)
                pass


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
        self.enterRule(localctx, 48, self.RULE_axis)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            _la = self._input.LA(1)
            if not(((((_la - 71)) & ~0x3f) == 0 and ((1 << (_la - 71)) & 7) != 0)):
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
            self.kw = None # Token
            self.arg1 = None # PieceNameContext
            self.arg2 = None # AxisContext
            self.arg3 = None # ExpressionContext
            self.arg4 = None # SpeedOrNowContext

        def TO(self):
            return self.getToken(BosParser.TO, 0)

        def TURN(self):
            return self.getToken(BosParser.TURN, 0)

        def pieceName(self):
            return self.getTypedRuleContext(BosParser.PieceNameContext,0)


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
        self.enterRule(localctx, 50, self.RULE_turnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            localctx.kw = self.match(BosParser.TURN)
            self.state = 318
            localctx.arg1 = self.pieceName()
            self.state = 319
            self.match(BosParser.TO)
            self.state = 320
            localctx.arg2 = self.axis()
            self.state = 321
            localctx.arg3 = self.expression(0)
            self.state = 322
            localctx.arg4 = self.speedOrNow()
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
            self.kw = None # Token
            self.arg1 = None # PieceNameContext
            self.arg2 = None # AxisContext
            self.arg3 = None # ExpressionContext
            self.arg4 = None # SpeedOrNowContext

        def TO(self):
            return self.getToken(BosParser.TO, 0)

        def MOVE(self):
            return self.getToken(BosParser.MOVE, 0)

        def pieceName(self):
            return self.getTypedRuleContext(BosParser.PieceNameContext,0)


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
        self.enterRule(localctx, 52, self.RULE_moveStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            localctx.kw = self.match(BosParser.MOVE)
            self.state = 325
            localctx.arg1 = self.pieceName()
            self.state = 326
            self.match(BosParser.TO)
            self.state = 327
            localctx.arg2 = self.axis()
            self.state = 328
            localctx.arg3 = self.expression(0)
            self.state = 329
            localctx.arg4 = self.speedOrNow()
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
        self.enterRule(localctx, 54, self.RULE_speedOrNow)
        try:
            self.state = 334
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [43]:
                self.enterOuterAlt(localctx, 1)
                self.state = 331
                self.match(BosParser.NOW)
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 2)
                self.state = 332
                self.match(BosParser.SPEED)
                self.state = 333
                self.expression(0)
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
            self.kw = None # Token
            self.arg1 = None # PieceNameContext
            self.arg2 = None # AxisContext
            self.arg3 = None # ExpressionContext
            self.arg4 = None # AccelerationContext

        def AROUND(self):
            return self.getToken(BosParser.AROUND, 0)

        def SPEED(self):
            return self.getToken(BosParser.SPEED, 0)

        def SPIN(self):
            return self.getToken(BosParser.SPIN, 0)

        def pieceName(self):
            return self.getTypedRuleContext(BosParser.PieceNameContext,0)


        def axis(self):
            return self.getTypedRuleContext(BosParser.AxisContext,0)


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
        self.enterRule(localctx, 56, self.RULE_spinStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            localctx.kw = self.match(BosParser.SPIN)
            self.state = 337
            localctx.arg1 = self.pieceName()
            self.state = 338
            self.match(BosParser.AROUND)
            self.state = 339
            localctx.arg2 = self.axis()
            self.state = 340
            self.match(BosParser.SPEED)
            self.state = 341
            localctx.arg3 = self.expression(0)
            self.state = 343
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==46:
                self.state = 342
                localctx.arg4 = self.acceleration()


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
        self.enterRule(localctx, 58, self.RULE_acceleration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.match(BosParser.ACCELERATE)
            self.state = 346
            self.expression(0)
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
            self.kw = None # Token
            self.arg1 = None # PieceNameContext
            self.arg2 = None # AxisContext
            self.arg3 = None # DecelerationContext

        def AROUND(self):
            return self.getToken(BosParser.AROUND, 0)

        def STOP_SPIN(self):
            return self.getToken(BosParser.STOP_SPIN, 0)

        def pieceName(self):
            return self.getTypedRuleContext(BosParser.PieceNameContext,0)


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
        self.enterRule(localctx, 60, self.RULE_stopSpinStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            localctx.kw = self.match(BosParser.STOP_SPIN)
            self.state = 349
            localctx.arg1 = self.pieceName()
            self.state = 350
            self.match(BosParser.AROUND)
            self.state = 351
            localctx.arg2 = self.axis()
            self.state = 353
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==48:
                self.state = 352
                localctx.arg3 = self.deceleration()


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
        self.enterRule(localctx, 62, self.RULE_deceleration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.match(BosParser.DECELERATE)
            self.state = 356
            self.expression(0)
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
            self.kw = None # Token
            self.arg1 = None # PieceNameContext
            self.arg2 = None # AxisContext

        def AROUND(self):
            return self.getToken(BosParser.AROUND, 0)

        def WAIT_FOR_TURN(self):
            return self.getToken(BosParser.WAIT_FOR_TURN, 0)

        def pieceName(self):
            return self.getTypedRuleContext(BosParser.PieceNameContext,0)


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
        self.enterRule(localctx, 64, self.RULE_waitForTurnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            localctx.kw = self.match(BosParser.WAIT_FOR_TURN)
            self.state = 359
            localctx.arg1 = self.pieceName()
            self.state = 360
            self.match(BosParser.AROUND)
            self.state = 361
            localctx.arg2 = self.axis()
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
            self.kw = None # Token
            self.arg1 = None # PieceNameContext
            self.arg2 = None # AxisContext

        def ALONG(self):
            return self.getToken(BosParser.ALONG, 0)

        def WAIT_FOR_MOVE(self):
            return self.getToken(BosParser.WAIT_FOR_MOVE, 0)

        def pieceName(self):
            return self.getTypedRuleContext(BosParser.PieceNameContext,0)


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
        self.enterRule(localctx, 66, self.RULE_waitForMoveStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            localctx.kw = self.match(BosParser.WAIT_FOR_MOVE)
            self.state = 364
            localctx.arg1 = self.pieceName()
            self.state = 365
            self.match(BosParser.ALONG)
            self.state = 366
            localctx.arg2 = self.axis()
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
            self.kw = None # Token
            self.arg1 = None # ExpressionContext
            self.arg2 = None # PieceNameContext

        def FROM(self):
            return self.getToken(BosParser.FROM, 0)

        def EMIT_SFX(self):
            return self.getToken(BosParser.EMIT_SFX, 0)

        def expression(self):
            return self.getTypedRuleContext(BosParser.ExpressionContext,0)


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
        self.enterRule(localctx, 68, self.RULE_emitSfxStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            localctx.kw = self.match(BosParser.EMIT_SFX)
            self.state = 369
            localctx.arg1 = self.expression(0)
            self.state = 370
            self.match(BosParser.FROM)
            self.state = 371
            localctx.arg2 = self.pieceName()
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
            self.kw = None # Token
            self.arg1 = None # StringConstantContext
            self.arg2 = None # ExpressionContext

        def L_PAREN(self):
            return self.getToken(BosParser.L_PAREN, 0)

        def COMMA(self):
            return self.getToken(BosParser.COMMA, 0)

        def R_PAREN(self):
            return self.getToken(BosParser.R_PAREN, 0)

        def PLAY_SOUND(self):
            return self.getToken(BosParser.PLAY_SOUND, 0)

        def stringConstant(self):
            return self.getTypedRuleContext(BosParser.StringConstantContext,0)


        def expression(self):
            return self.getTypedRuleContext(BosParser.ExpressionContext,0)


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
        self.enterRule(localctx, 70, self.RULE_playSoundStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            localctx.kw = self.match(BosParser.PLAY_SOUND)
            self.state = 374
            self.match(BosParser.L_PAREN)
            self.state = 375
            localctx.arg1 = self.stringConstant()
            self.state = 376
            self.match(BosParser.COMMA)
            self.state = 377
            localctx.arg2 = self.expression(0)
            self.state = 378
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
            self.kw = None # Token
            self.arg1 = None # PieceNameContext

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
        self.enterRule(localctx, 72, self.RULE_hideStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            localctx.kw = self.match(BosParser.HIDE)
            self.state = 381
            localctx.arg1 = self.pieceName()
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
            self.kw = None # Token
            self.arg1 = None # PieceNameContext

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
        self.enterRule(localctx, 74, self.RULE_showStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            localctx.kw = self.match(BosParser.SHOW)
            self.state = 384
            localctx.arg1 = self.pieceName()
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
            self.kw = None # Token
            self.arg1 = None # PieceNameContext
            self.arg2 = None # ExpressionContext

        def TYPE(self):
            return self.getToken(BosParser.TYPE, 0)

        def EXPLODE(self):
            return self.getToken(BosParser.EXPLODE, 0)

        def pieceName(self):
            return self.getTypedRuleContext(BosParser.PieceNameContext,0)


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
        self.enterRule(localctx, 76, self.RULE_explodeStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            localctx.kw = self.match(BosParser.EXPLODE)
            self.state = 387
            localctx.arg1 = self.pieceName()
            self.state = 388
            self.match(BosParser.TYPE)
            self.state = 389
            localctx.arg2 = self.expression(0)
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
            self.kw = None # Token
            self.arg1 = None # FuncNameContext

        def CALL_SCRIPT(self):
            return self.getToken(BosParser.CALL_SCRIPT, 0)

        def funcName(self):
            return self.getTypedRuleContext(BosParser.FuncNameContext,0)


        def L_PAREN(self):
            return self.getToken(BosParser.L_PAREN, 0)

        def R_PAREN(self):
            return self.getToken(BosParser.R_PAREN, 0)

        def expressionList(self):
            return self.getTypedRuleContext(BosParser.ExpressionListContext,0)


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
        self.enterRule(localctx, 78, self.RULE_callStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            localctx.kw = self.match(BosParser.CALL_SCRIPT)
            self.state = 392
            localctx.arg1 = self.funcName()
            self.state = 399
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 393
                self.match(BosParser.L_PAREN)
                self.state = 394
                self.match(BosParser.R_PAREN)
                pass

            elif la_ == 2:
                self.state = 395
                self.match(BosParser.L_PAREN)
                self.state = 396
                self.expressionList()
                self.state = 397
                self.match(BosParser.R_PAREN)
                pass


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
            self.kw = None # Token
            self.arg1 = None # FuncNameContext

        def START_SCRIPT(self):
            return self.getToken(BosParser.START_SCRIPT, 0)

        def funcName(self):
            return self.getTypedRuleContext(BosParser.FuncNameContext,0)


        def L_PAREN(self):
            return self.getToken(BosParser.L_PAREN, 0)

        def R_PAREN(self):
            return self.getToken(BosParser.R_PAREN, 0)

        def expressionList(self):
            return self.getTypedRuleContext(BosParser.ExpressionListContext,0)


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
        self.enterRule(localctx, 80, self.RULE_startStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            localctx.kw = self.match(BosParser.START_SCRIPT)
            self.state = 402
            localctx.arg1 = self.funcName()
            self.state = 409
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 403
                self.match(BosParser.L_PAREN)
                self.state = 404
                self.match(BosParser.R_PAREN)
                pass

            elif la_ == 2:
                self.state = 405
                self.match(BosParser.L_PAREN)
                self.state = 406
                self.expressionList()
                self.state = 407
                self.match(BosParser.R_PAREN)
                pass


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
            self.kw = None # Token
            self.arg1 = None # ExpressionContext

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
        self.enterRule(localctx, 82, self.RULE_signalStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            localctx.kw = self.match(BosParser.SIGNAL)
            self.state = 412
            localctx.arg1 = self.expression(0)
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
            self.kw = None # Token
            self.arg1 = None # ExpressionContext

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
        self.enterRule(localctx, 84, self.RULE_setSignalMaskStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            localctx.kw = self.match(BosParser.SET_SIGNAL_MASK)
            self.state = 415
            localctx.arg1 = self.expression(0)
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
            self.kw = None # Token
            self.arg1 = None # ExpressionContext
            self.arg2 = None # ExpressionContext

        def TO(self):
            return self.getToken(BosParser.TO, 0)

        def ATTACH_UNIT(self):
            return self.getToken(BosParser.ATTACH_UNIT, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BosParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BosParser.ExpressionContext,i)


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
        self.enterRule(localctx, 86, self.RULE_attachUnitStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            localctx.kw = self.match(BosParser.ATTACH_UNIT)
            self.state = 418
            localctx.arg1 = self.expression(0)
            self.state = 419
            self.match(BosParser.TO)
            self.state = 420
            localctx.arg2 = self.expression(0)
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
            self.kw = None # Token
            self.arg1 = None # ExpressionContext

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
        self.enterRule(localctx, 88, self.RULE_dropUnitStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            localctx.kw = self.match(BosParser.DROP_UNIT)
            self.state = 423
            localctx.arg1 = self.expression(0)
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
            self.kw = None # Token
            self.arg1 = None # PieceNameContext

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
        self.enterRule(localctx, 90, self.RULE_cacheStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            localctx.kw = self.match(BosParser.CACHE)
            self.state = 426
            localctx.arg1 = self.pieceName()
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
            self.kw = None # Token
            self.arg1 = None # PieceNameContext

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
        self.enterRule(localctx, 92, self.RULE_dontCacheStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            localctx.kw = self.match(BosParser.DONT_CACHE)
            self.state = 429
            localctx.arg1 = self.pieceName()
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
            self.kw = None # Token
            self.arg1 = None # PieceNameContext

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
        self.enterRule(localctx, 94, self.RULE_dontShadowStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            localctx.kw = self.match(BosParser.DONT_SHADOW)
            self.state = 432
            localctx.arg1 = self.pieceName()
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
            self.kw = None # Token
            self.arg1 = None # PieceNameContext

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
        self.enterRule(localctx, 96, self.RULE_dontShadeStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            localctx.kw = self.match(BosParser.DONT_SHADE)
            self.state = 435
            localctx.arg1 = self.pieceName()
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

        def expression(self):
            return self.getTypedRuleContext(BosParser.ExpressionContext,0)


        def commaExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BosParser.CommaExpressionContext)
            else:
                return self.getTypedRuleContext(BosParser.CommaExpressionContext,i)


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
        self.enterRule(localctx, 98, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self.expression(0)
            self.state = 441
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 438
                self.commaExpression()
                self.state = 443
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 100, self.RULE_commaExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444
            self.match(BosParser.COMMA)
            self.state = 445
            self.expression(0)
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


        def getRuleIndex(self):
            return BosParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class VaryingTermExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BosParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def varyingTerm(self):
            return self.getTypedRuleContext(BosParser.VaryingTermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVaryingTermExpr" ):
                listener.enterVaryingTermExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVaryingTermExpr" ):
                listener.exitVaryingTermExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVaryingTermExpr" ):
                return visitor.visitVaryingTermExpr(self)
            else:
                return visitor.visitChildren(self)


    class UnaryExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BosParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.operand = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(BosParser.ExpressionContext,0)

        def OP_MINUS(self):
            return self.getToken(BosParser.OP_MINUS, 0)
        def LOGICAL_NOT(self):
            return self.getToken(BosParser.LOGICAL_NOT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpr" ):
                listener.enterUnaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpr" ):
                listener.exitUnaryExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpr" ):
                return visitor.visitUnaryExpr(self)
            else:
                return visitor.visitChildren(self)


    class BinaryExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BosParser.ExpressionContext
            super().__init__(parser)
            self.operand1 = None # ExpressionContext
            self.op = None # Token
            self.operand2 = None # ExpressionContext
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BosParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BosParser.ExpressionContext,i)

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryExpr" ):
                listener.enterBinaryExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryExpr" ):
                listener.exitBinaryExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryExpr" ):
                return visitor.visitBinaryExpr(self)
            else:
                return visitor.visitChildren(self)


    class ConstTermExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BosParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def constTerm(self):
            return self.getTypedRuleContext(BosParser.ConstTermContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstTermExpr" ):
                listener.enterConstTermExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstTermExpr" ):
                listener.exitConstTermExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstTermExpr" ):
                return visitor.visitConstTermExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a BosParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def L_PAREN(self):
            return self.getToken(BosParser.L_PAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(BosParser.ExpressionContext,0)

        def R_PAREN(self):
            return self.getToken(BosParser.R_PAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BosParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 102
        self.enterRecursionRule(localctx, 102, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 456
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                localctx = BosParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 448
                self.match(BosParser.L_PAREN)
                self.state = 449
                self.expression(0)
                self.state = 450
                self.match(BosParser.R_PAREN)
                pass

            elif la_ == 2:
                localctx = BosParser.ConstTermExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 452
                self.constTerm()
                pass

            elif la_ == 3:
                localctx = BosParser.VaryingTermExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 453
                self.varyingTerm()
                pass

            elif la_ == 4:
                localctx = BosParser.UnaryExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 454
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==11 or _la==28):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 455
                localctx.operand = self.expression(11)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 490
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 488
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                    if la_ == 1:
                        localctx = BosParser.BinaryExprContext(self, BosParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.operand1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 458
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 459
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 28672) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 460
                        localctx.operand2 = self.expression(11)
                        pass

                    elif la_ == 2:
                        localctx = BosParser.BinaryExprContext(self, BosParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.operand1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 461
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 462
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==10 or _la==11):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 463
                        localctx.operand2 = self.expression(10)
                        pass

                    elif la_ == 3:
                        localctx = BosParser.BinaryExprContext(self, BosParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.operand1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 464
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 465
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 62914560) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 466
                        localctx.operand2 = self.expression(9)
                        pass

                    elif la_ == 4:
                        localctx = BosParser.BinaryExprContext(self, BosParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.operand1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 467
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 468
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==20 or _la==21):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 469
                        localctx.operand2 = self.expression(8)
                        pass

                    elif la_ == 5:
                        localctx = BosParser.BinaryExprContext(self, BosParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.operand1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 470
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 471
                        localctx.op = self.match(BosParser.BITWISE_AND)
                        self.state = 472
                        localctx.operand2 = self.expression(7)
                        pass

                    elif la_ == 6:
                        localctx = BosParser.BinaryExprContext(self, BosParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.operand1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 473
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 474
                        localctx.op = self.match(BosParser.BITWISE_OR)
                        self.state = 475
                        localctx.operand2 = self.expression(6)
                        pass

                    elif la_ == 7:
                        localctx = BosParser.BinaryExprContext(self, BosParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.operand1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 476
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 477
                        localctx.op = self.match(BosParser.BITWISE_XOR)
                        self.state = 478
                        localctx.operand2 = self.expression(5)
                        pass

                    elif la_ == 8:
                        localctx = BosParser.BinaryExprContext(self, BosParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.operand1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 479
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 480
                        localctx.op = self.match(BosParser.LOGICAL_AND)
                        self.state = 481
                        localctx.operand2 = self.expression(4)
                        pass

                    elif la_ == 9:
                        localctx = BosParser.BinaryExprContext(self, BosParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.operand1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 482
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 483
                        localctx.op = self.match(BosParser.LOGICAL_OR)
                        self.state = 484
                        localctx.operand2 = self.expression(3)
                        pass

                    elif la_ == 10:
                        localctx = BosParser.BinaryExprContext(self, BosParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.operand1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 485
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 486
                        localctx.op = self.match(BosParser.LOGICAL_XOR)
                        self.state = 487
                        localctx.operand2 = self.expression(2)
                        pass

             
                self.state = 492
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ConstTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constant(self):
            return self.getTypedRuleContext(BosParser.ConstantContext,0)


        def L_PAREN(self):
            return self.getToken(BosParser.L_PAREN, 0)

        def constTerm(self):
            return self.getTypedRuleContext(BosParser.ConstTermContext,0)


        def R_PAREN(self):
            return self.getToken(BosParser.R_PAREN, 0)

        def getRuleIndex(self):
            return BosParser.RULE_constTerm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstTerm" ):
                listener.enterConstTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstTerm" ):
                listener.exitConstTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstTerm" ):
                return visitor.visitConstTerm(self)
            else:
                return visitor.visitChildren(self)




    def constTerm(self):

        localctx = BosParser.ConstTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_constTerm)
        try:
            self.state = 498
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [75, 76, 77]:
                self.enterOuterAlt(localctx, 1)
                self.state = 493
                self.constant()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 494
                self.match(BosParser.L_PAREN)
                self.state = 495
                self.constTerm()
                self.state = 496
                self.match(BosParser.R_PAREN)
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


    class VaryingTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getTerm(self):
            return self.getTypedRuleContext(BosParser.GetTermContext,0)


        def randTerm(self):
            return self.getTypedRuleContext(BosParser.RandTermContext,0)


        def varNameTerm(self):
            return self.getTypedRuleContext(BosParser.VarNameTermContext,0)


        def getRuleIndex(self):
            return BosParser.RULE_varyingTerm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVaryingTerm" ):
                listener.enterVaryingTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVaryingTerm" ):
                listener.exitVaryingTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVaryingTerm" ):
                return visitor.visitVaryingTerm(self)
            else:
                return visitor.visitChildren(self)




    def varyingTerm(self):

        localctx = BosParser.VaryingTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_varyingTerm)
        try:
            self.state = 503
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [52]:
                self.enterOuterAlt(localctx, 1)
                self.state = 500
                self.getTerm()
                pass
            elif token in [74]:
                self.enterOuterAlt(localctx, 2)
                self.state = 501
                self.randTerm()
                pass
            elif token in [87]:
                self.enterOuterAlt(localctx, 3)
                self.state = 502
                self.varNameTerm()
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


    class GetTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getStatement(self):
            return self.getTypedRuleContext(BosParser.GetStatementContext,0)


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
        self.enterRule(localctx, 108, self.RULE_getTerm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 505
            self.getStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RandTermContext(ParserRuleContext):
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
            return BosParser.RULE_randTerm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRandTerm" ):
                listener.enterRandTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRandTerm" ):
                listener.exitRandTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRandTerm" ):
                return visitor.visitRandTerm(self)
            else:
                return visitor.visitChildren(self)




    def randTerm(self):

        localctx = BosParser.RandTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_randTerm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 507
            self.match(BosParser.RAND)
            self.state = 508
            self.match(BosParser.L_PAREN)
            self.state = 509
            self.expression(0)
            self.state = 510
            self.match(BosParser.COMMA)
            self.state = 511
            self.expression(0)
            self.state = 512
            self.match(BosParser.R_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarNameTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varName(self):
            return self.getTypedRuleContext(BosParser.VarNameContext,0)


        def getRuleIndex(self):
            return BosParser.RULE_varNameTerm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarNameTerm" ):
                listener.enterVarNameTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarNameTerm" ):
                listener.exitVarNameTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarNameTerm" ):
                return visitor.visitVarNameTerm(self)
            else:
                return visitor.visitChildren(self)




    def varNameTerm(self):

        localctx = BosParser.VarNameTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_varNameTerm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 514
            self.varName()
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

        def NUMBER(self):
            return self.getToken(BosParser.NUMBER, 0)

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
        self.enterRule(localctx, 114, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 516
            _la = self._input.LA(1)
            if not(((((_la - 75)) & ~0x3f) == 0 and ((1 << (_la - 75)) & 7) != 0)):
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
        self.enterRule(localctx, 116, self.RULE_stringConstant)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 518
            self.match(BosParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[51] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 1)
         




