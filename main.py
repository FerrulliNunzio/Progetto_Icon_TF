import random as random
from pyswip import Prolog

def createKB():
    kb = Prolog()
    for i in range(3):
        kb.assertz("caserma(caserma_" + (i+1) + ")")

    kb.assertz("agenti(caserma_1, 7)")
    kb.assertz("agenti(caserma_2, 15)")
    kb.assertz("agenti(caserma_3, 22)")

    kb.assertz("veicoli(caserma_1, 2)")
    kb.assertz("veicoli(caserma_2, 5)")
    kb.assertz("veicoli(caserma_3, 8)")

    kb.assertz("veicoli_speciali(caserma_1, 0)")
    kb.assertz("veicoli_speciali(caserma_2, 3)")
    kb.assertz("veicoli_speciali(caserma_3, 5)")

    return kb

