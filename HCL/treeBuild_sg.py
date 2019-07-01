# old file, stores first generation HCl from classical and quantum, and uses them
# to create ete3 PhyloTree objects, to find the edges in common via the
# Robinson Foulds metric. This metric has been incorporated into the main script

from ete3 import PhyloTree
import re


# top 44 genes of PC1 for lumAB
#classical44="(((((((((0,143),(53,217)),(93,153)),(154,232)),49),(19,117)),((((15,137),69),247),71)),((((((((1,(99,185)),(110,189)),(47,(94,112))),(((17,32),50),(84,(((103,234),114),(125,226))))),64),(((6,((80,147),167)),(45,206)),(((36,74),((115,244),225)),((62,(118,193)),((73,227),130))))),(((12,((20,61),136)),145),(24,(56,(215,(233,241)))))),(((8,160),(((25,163),((46,82),105)),180)),(((((18,(60,128)),(37,223)),146),((((23,55),109),230),221)),(((111,220),192),(121,(149,169))))))),(((((((2,10),(168,216)),((44,199),(57,229))),(((((29,31),235),(42,202)),(179,201)),(((78,106),90),(89,178)))),(((((11,35),214),((((14,124),231),171),((92,101),(141,245)))),((((26,184),100),97),(48,176))),(((27,127),((40,122),87)),(135,162)))),(((((((3,(70,159)),240),((((33,63),59),(172,173)),98)),(((13,34),(38,52)),((((28,(102,144)),(212,(222,239))),(158,188)),(248,249)))),(((67,85),165),95)),(((((7,68),120),(((58,197),75),(((140,210),155),205))),((131,(150,219)),224)),(((((54,191),132),(190,(228,242))),((79,83),(((129,204),166),243))),((126,174),(142,151))))),(((((5,198),66),200),((((16,(((116,177),207),213)),(138,152)),((21,208),(72,86))),(((65,77),(133,246)),(157,238)))),(((((((22,203),181),(81,107)),(148,194)),170),104),(((88,195),237),((183,187),211)))))),((((4,196),((((((9,139),161),(30,39)),(108,(134,156))),41),(((43,91),164),((((51,119),113),((76,209),175)),(182,218))))),((96,186),123)),236)));"
#quantum44="((((((((0,84),(53,217)),(((93,(143,153)),160),146)),(19,117)),((((15,137),69),(((17,50),32),(154,232))),(71,247))),(((8,(((25,46),163),180)),(((18,(60,128)),223),(37,105))),49)),(((((((((1,(99,185)),(118,193)),136),(110,189)),12),(20,61)),(((24,167),(56,(215,(233,241)))),145)),((((((23,55),109),((94,112),226)),(((103,234),114),125)),((62,130),(221,230))),64)),(((6,(45,206)),(((73,227),82),(80,147))),(((36,74),((115,244),225)),(121,(149,169)))))),((((((2,10),(168,216)),((((29,(31,235)),(42,202)),(179,201)),(((78,106),90),(89,178)))),(((((11,35),214),((((14,124),231),171),((92,101),(141,245)))),((((26,184),100),97),(48,(68,176)))),(((27,127),((40,122),87)),(135,162)))),((((((3,(70,(144,159))),240),((((33,63),59),(172,173)),98)),((((28,(222,239)),((34,212),(158,188))),((102,194),(248,249))),((38,52),65))),(((67,85),165),95)),((((((44,199),((57,229),(174,243))),((111,220),192)),((47,(((54,191),132),(190,(228,242)))),((79,83),(129,(166,204))))),(142,151)),(((((58,197),75),(((140,210),155),205)),120),((131,(150,219)),224))))),((((4,196),(((((((9,139),161),(30,39)),(134,156)),41),(((((43,76),209),164),(((51,119),(113,175)),108)),(91,(126,182)))),((96,186),123))),236),(((((5,198),66),200),(((((16,(86,218)),(133,246)),((21,208),72)),(138,152)),(77,(157,238)))),(((((7,104),(13,((22,181),(81,107)))),170),(((116,207),177),213)),((88,(((148,203),195),237)),((183,187),211)))))));"

classical44="(((((((((0,143),(32,84)),(53,217)),(93,153)),(154,232)),(19,117)),(((((15,137),69),49),247),71)),((((((1,118),(189,193)),((215,233),241)),((24,((99,185),114)),((80,147),167))),(((12,110),((20,61),136)),(56,145))),(((8,160),(((25,163),((46,82),105)),180)),(((((17,(50,125)),(((23,55),(94,112)),((103,234),226))),64),((((18,128),(60,109)),(37,223)),(((62,230),221),(((73,227),130),146)))),(((36,74),((115,244),225)),(((111,220),192),(121,(149,169)))))))),(((((((((2,248),((33,63),59)),((3,(70,159)),240)),((((28,(212,(222,239))),(102,144)),(158,188)),(98,(172,173)))),(((67,85),165),((75,141),(92,101)))),((((((26,184),100),245),97),(48,176)),(((27,127),((40,122),87)),(135,162)))),(((((7,68),120),((((21,208),72),205),(((58,197),238),((140,210),155)))),(((10,(150,219)),131),224)),(((47,(((54,191),132),(190,(228,242)))),((79,83),(((129,204),166),243))),((126,174),(142,151))))),(((6,(45,206)),(((11,35),((14,124),231)),(171,214))),(((((29,235),31),(42,202)),(179,201)),(((44,199),(57,229)),(((78,106),90),((89,178),(168,216))))))),(((((4,196),157),((((((9,139),161),((30,39),164)),41),(108,(134,156))),((96,186),123))),236),((((((5,198),66),200),(((65,77),(133,246)),95)),(((((13,(81,107)),((86,(148,194)),170)),((22,203),104)),(34,(38,52))),(((((116,177),207),213),138),(152,(181,249))))),(((16,(43,91)),((((51,119),113),((76,209),175)),(182,218))),(((88,195),237),((183,187),211)))))));"
quantum44="(((((((0,143),(53,217)),((93,153),160)),(19,117)),((((8,((17,32),24)),(154,232)),((15,137),69)),(71,247))),(((((((1,(50,125)),((99,114),185)),(((47,(94,112)),110),(84,((103,234),226)))),64),(6,((80,147),167))),((((36,206),(118,193)),((215,233),241)),((62,((73,227),130)),221))),(((12,((20,61),136)),(56,145)),(((((18,128),223),146),((((55,169),60),109),(121,149))),(((((25,46),163),(37,(74,(82,105)))),180),49))))),((((((((2,10),(168,216)),((44,199),(57,229))),(((27,127),((40,122),87)),(135,162))),((((((26,184),(100,204)),(48,176)),(141,245)),((111,(192,220)),((115,244),225))),(((((54,191),132),(190,((228,248),242))),(150,224)),(((79,129),166),243)))),((((((3,(70,159)),(97,240)),(((33,63),59),(98,(172,173)))),((((((28,222),(212,239)),158),(65,((102,144),249))),(34,(38,52))),((83,238),((126,188),174)))),((142,151),157)),((((7,68),120),((((21,208),72),((58,(197,219)),75)),(131,(((140,210),155),205)))),(((67,85),165),95)))),(((((11,35),((14,124),231)),45),(((23,(92,101)),(214,230)),(171,189))),(((((29,235),31),(42,202)),(179,201)),(((78,106),90),(89,178))))),((((4,196),((((((9,139),30),(39,164)),((43,91),(((51,119),((76,209),175)),108))),(41,((134,161),156))),(96,(123,186)))),236),((((((5,198),66),200),((88,195),237)),((((16,(86,113)),(182,218)),(138,152)),(77,(133,246)))),(((((13,((81,194),107)),(((22,181),(148,203)),170)),104),(((116,207),177),213)),((183,187),211))))));"
ct44=PhyloTree(classical44)
qt44=PhyloTree(quantum44)

diff_44=qt44.compare(ct44)['source_edges_in_ref']

print("classical vs quantum HCl tree similarity on lumAB training set for top n pc1 genes:\n n=44: {:.4f}".format(diff_44))