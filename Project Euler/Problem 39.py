# -*- coding: utf-8 -*-
# Problem 39
# Integer right triangles

# If p is the perimeter of a right angle triangle with integral length sides,
# {a,b,c}, there are exactly three solutions for p = 120.

# {20,48,52}, {24,45,51}, {30,40,50}

# For which value of p ≤ 1000, is the number of solutions maximised?


def is_right_triangle(a, b, c):
    return a ** 2 + b ** 2 == c ** 2

from time import time

start_time = time()

p = 12      # starts with 3, 4, 5
d = {}
while p <= 1000:
    for a in range(3, p):
        for b in range(a + 1, p):
            c = p - a - b
            if c <= b:      # we have to have a < b < c
                break

            if is_right_triangle(a, b, c):
                if p in d:
                    d[p].append((a, b, c))
                else:
                    d[p] = [(a, b, c)]

    p += 1

summary = {k: len(d[k]) for k in d}

print len(d)
print d

l = []
m = max(summary.values())
for k in summary:
    if summary[k] == m:
        l.append(k)

print l

print "Total Time: ", time() - start_time

# Completed on Tue, 4 Mar 2014, 22:53
# Solve by: 35395
# ---------------
# 190
# {516: [(129, 172, 215)], 520: [(104, 195, 221), (120, 182, 218)], 12: [(3, 4, 5)], 528: [(44, 240, 244), (132, 176, 220), (144, 165, 219)], 532: [(140, 171, 221)], 24: [(6, 8, 10)], 540: [(54, 240, 246), (90, 216, 234), (135, 180, 225)], 30: [(5, 12, 13)], 544: [(32, 255, 257)], 546: [(39, 252, 255), (105, 208, 233)], 36: [(9, 12, 15)], 40: [(8, 15, 17)], 48: [(12, 16, 20)], 564: [(141, 188, 235)], 56: [(7, 24, 25)], 570: [(95, 228, 247), (120, 209, 241)], 60: [(10, 24, 26), (15, 20, 25)], 576: [(64, 252, 260), (144, 192, 240)], 608: [(96, 247, 265)], 70: [(20, 21, 29)], 72: [(18, 24, 30)], 588: [(84, 245, 259), (147, 196, 245)], 80: [(16, 30, 34)], 952: [(119, 408, 425), (168, 374, 410)], 594: [(108, 231, 255)], 84: [(12, 35, 37), (21, 28, 35)], 782: [(204, 253, 325)], 598: [(69, 260, 269)], 600: [(100, 240, 260), (120, 225, 255), (150, 200, 250)], 90: [(9, 40, 41), (15, 36, 39)], 96: [(24, 32, 40)], 612: [(34, 288, 290), (153, 204, 255)], 992: [(31, 480, 481)], 616: [(77, 264, 275), (132, 224, 260)], 108: [(27, 36, 45)], 112: [(14, 48, 50)], 630: [(63, 280, 287), (105, 252, 273), (140, 225, 265), (180, 189, 261)], 120: [(20, 48, 52), (24, 45, 51), (30, 40, 50)], 636: [(159, 212, 265)], 126: [(28, 45, 53)], 640: [(128, 240, 272)], 704: [(192, 220, 292)], 132: [(11, 60, 61), (33, 44, 55)], 646: [(68, 285, 293)], 648: [(162, 216, 270)], 876: [(219, 292, 365)], 650: [(25, 312, 313)], 140: [(40, 42, 58)], 144: [(16, 63, 65), (36, 48, 60)], 792: [(66, 360, 366), (144, 308, 340), (198, 264, 330)], 660: [(55, 300, 305), (60, 297, 303), (110, 264, 286), (165, 220, 275), (176, 210, 274)], 150: [(25, 60, 65)], 154: [(33, 56, 65)], 156: [(39, 52, 65)], 160: [(32, 60, 68)], 624: [(48, 286, 290), (117, 240, 267), (156, 208, 260)], 960: [(60, 448, 452), (160, 384, 416), (192, 360, 408), (240, 320, 400)], 168: [(21, 72, 75), (24, 70, 74), (42, 56, 70)], 684: [(36, 323, 325), (171, 228, 285)], 176: [(48, 55, 73)], 690: [(115, 276, 299), (161, 240, 289)], 180: [(18, 80, 82), (30, 72, 78), (45, 60, 75)], 798: [(76, 357, 365)], 182: [(13, 84, 85)], 696: [(174, 232, 290)], 884: [(208, 306, 370)], 700: [(75, 308, 317), (200, 210, 290)], 702: [(195, 216, 291)], 192: [(48, 64, 80)], 800: [(160, 300, 340), (175, 288, 337)], 708: [(177, 236, 295)], 198: [(36, 77, 85)], 200: [(40, 75, 85)], 714: [(136, 273, 305)], 204: [(51, 68, 85)], 208: [(39, 80, 89)], 210: [(35, 84, 91), (60, 63, 87)], 216: [(54, 72, 90)], 220: [(20, 99, 101)], 224: [(28, 96, 100)], 720: [(45, 336, 339), (72, 320, 328), (80, 315, 325), (120, 288, 312), (144, 270, 306), (180, 240, 300)], 928: [(87, 416, 425)], 228: [(57, 76, 95)], 744: [(186, 248, 310)], 234: [(65, 72, 97)], 748: [(170, 264, 314)], 750: [(125, 300, 325)], 240: [(15, 112, 113), (40, 96, 104), (48, 90, 102), (60, 80, 100)], 552: [(23, 264, 265), (138, 184, 230)], 756: [(27, 364, 365), (108, 315, 333), (168, 270, 318), (189, 252, 315)], 760: [(38, 360, 362), (152, 285, 323)], 980: [(280, 294, 406)], 252: [(36, 105, 111), (56, 90, 106), (63, 84, 105)], 768: [(192, 256, 320)], 896: [(112, 384, 400)], 770: [(165, 280, 325), (220, 231, 319)], 260: [(60, 91, 109)], 264: [(22, 120, 122), (66, 88, 110)], 912: [(190, 336, 386), (228, 304, 380)], 780: [(104, 330, 346), (130, 312, 338), (180, 273, 327), (195, 260, 325)], 270: [(27, 120, 123), (45, 108, 117)], 784: [(98, 336, 350)], 728: [(52, 336, 340), (91, 312, 325)], 276: [(69, 92, 115)], 280: [(35, 120, 125), (56, 105, 119), (80, 84, 116)], 644: [(115, 252, 277)], 286: [(44, 117, 125)], 288: [(32, 126, 130), (72, 96, 120)], 560: [(70, 240, 250), (112, 210, 238), (160, 168, 232)], 804: [(201, 268, 335)], 732: [(183, 244, 305)], 810: [(81, 360, 369), (135, 324, 351)], 300: [(50, 120, 130), (75, 100, 125)], 816: [(204, 272, 340), (238, 240, 338)], 306: [(17, 144, 145)], 308: [(66, 112, 130)], 312: [(24, 143, 145), (78, 104, 130)], 828: [(180, 299, 349), (207, 276, 345)], 320: [(64, 120, 136)], 736: [(207, 224, 305)], 324: [(81, 108, 135)], 840: [(40, 399, 401), (56, 390, 394), (105, 360, 375), (120, 350, 370), (140, 336, 364), (168, 315, 357), (210, 280, 350), (240, 252, 348)], 330: [(55, 132, 143), (88, 105, 137)], 336: [(42, 144, 150), (48, 140, 148), (84, 112, 140)], 850: [(225, 272, 353)], 340: [(51, 140, 149)], 858: [(132, 351, 375)], 348: [(87, 116, 145)], 350: [(100, 105, 145)], 352: [(96, 110, 146)], 864: [(96, 378, 390), (135, 352, 377), (216, 288, 360)], 870: [(29, 420, 421), (145, 348, 377)], 360: [(36, 160, 164), (60, 144, 156), (72, 135, 153), (90, 120, 150)], 572: [(88, 234, 250)], 874: [(152, 345, 377)], 364: [(26, 168, 170)], 880: [(80, 396, 404), (176, 330, 374), (240, 275, 365)], 882: [(196, 315, 371)], 372: [(93, 124, 155)], 374: [(85, 132, 157)], 888: [(222, 296, 370)], 378: [(84, 135, 159)], 380: [(19, 180, 181)], 384: [(96, 128, 160)], 832: [(156, 320, 356)], 900: [(90, 400, 410), (150, 360, 390), (225, 300, 375), (252, 275, 373)], 390: [(52, 165, 173), (65, 156, 169)], 392: [(49, 168, 175)], 396: [(33, 180, 183), (72, 154, 170), (99, 132, 165)], 910: [(65, 420, 425), (260, 273, 377)], 400: [(80, 150, 170)], 920: [(120, 391, 409), (184, 345, 391)], 918: [(51, 432, 435), (189, 340, 389)], 408: [(102, 136, 170), (119, 120, 169)], 836: [(114, 352, 370)], 924: [(42, 440, 442), (77, 420, 427), (132, 385, 407), (198, 336, 390), (231, 308, 385)], 988: [(266, 312, 410)], 416: [(78, 160, 178)], 418: [(57, 176, 185)], 420: [(28, 195, 197), (60, 175, 185), (70, 168, 182), (105, 140, 175), (120, 126, 174)], 936: [(72, 429, 435), (234, 312, 390), (260, 288, 388)], 432: [(48, 189, 195), (108, 144, 180)], 948: [(237, 316, 395)], 950: [(228, 325, 397)], 440: [(40, 198, 202), (88, 165, 187)], 442: [(104, 153, 185)], 444: [(111, 148, 185)], 448: [(56, 192, 200)], 672: [(84, 288, 300), (96, 280, 296), (160, 231, 281), (168, 224, 280)], 450: [(45, 200, 205), (75, 180, 195)], 966: [(84, 437, 445)], 456: [(95, 168, 193), (114, 152, 190)], 972: [(243, 324, 405)], 930: [(155, 372, 403)], 462: [(21, 220, 221), (99, 168, 195)], 468: [(117, 156, 195), (130, 144, 194)], 984: [(246, 328, 410)], 986: [(145, 408, 433)], 476: [(84, 187, 205)], 990: [(99, 440, 451), (165, 396, 429), (180, 385, 425), (264, 315, 411)], 480: [(30, 224, 226), (80, 192, 208), (96, 180, 204), (120, 160, 200)], 996: [(249, 332, 415)], 1000: [(200, 375, 425)], 490: [(140, 147, 203)], 492: [(123, 164, 205)], 494: [(133, 156, 205)], 680: [(102, 280, 298), (136, 255, 289)], 504: [(63, 216, 225), (72, 210, 222), (112, 180, 212), (126, 168, 210)], 852: [(213, 284, 355)], 510: [(60, 221, 229), (85, 204, 221)]}
# [840]
# Total Time:  16.8469998837
# [Finished in 17.1s]
