agentiInCaserma(cas1,1).
agentiInCaserma(cas1,2).
agentiInCaserma(cas1,3).
agentiInCaserma(cas1,4).
agentiInCaserma(cas1,5).
agentiInCaserma(cas2,1).
agentiInCaserma(cas2,2).
agentiInCaserma(cas2,3).
agentiInCaserma(cas2,4).
agentiInCaserma(cas2,5).
agentiInCaserma(cas2,6).
agentiInCaserma(cas2,7).
agentiInCaserma(cas2,8).
agentiInCaserma(cas2,9).
agentiInCaserma(cas2,10).
agentiInCaserma(cas3,1).
agentiInCaserma(cas3,2).
agentiInCaserma(cas3,3).
agentiInCaserma(cas3,4).
agentiInCaserma(cas3,5).
agentiInCaserma(cas3,6).
agentiInCaserma(cas3,7).
agentiInCaserma(cas3,8).
agentiInCaserma(cas3,9).
agentiInCaserma(cas3,10).
agentiInCaserma(cas3,11).
agentiInCaserma(cas3,12).
agentiInCaserma(cas3,13).
agentiInCaserma(cas3,14).
agentiInCaserma(cas3,15).
agentiInCaserma(cas3,16).
agentiInCaserma(cas3,17).
agentiInCaserma(cas3,18).
agentiInCaserma(cas3,19).
agentiInCaserma(cas3,20).


veicoliInCaserma(cas1,1).
veicoliInCaserma(cas1,2).
veicoliInCaserma(cas1,3).
veicoliInCaserma(cas2,1).
veicoliInCaserma(cas2,2).
veicoliInCaserma(cas2,3).
veicoliInCaserma(cas2,4).
veicoliInCaserma(cas2,5).
veicoliInCaserma(cas2,6).
veicoliInCaserma(cas2,7).
veicoliInCaserma(cas3,1).
veicoliInCaserma(cas3,2).
veicoliInCaserma(cas3,3).
veicoliInCaserma(cas3,4).
veicoliInCaserma(cas3,5).
veicoliInCaserma(cas3,6).
veicoliInCaserma(cas3,7).
veicoliInCaserma(cas3,8).
veicoliInCaserma(cas3,9).
veicoliInCaserma(cas3,10).


veicoliSPInCaserma(cas1,0).
veicoliSPInCaserma(cas2,0).
veicoliSPInCaserma(cas2,1).
veicoliSPInCaserma(cas2,2).
veicoliSPInCaserma(cas3,0).
veicoliSPInCaserma(cas3,1).
veicoliSPInCaserma(cas3,2).
veicoliSPInCaserma(cas3,3).
veicoliSPInCaserma(cas3,4).
veicoliSPInCaserma(cas3,5).



agentiNecessariCas1(X):-agentiInCaserma(cas1,X).
veicoliNecessariCas1(X):-veicoliInCaserma(cas1,X).
veicoliSPNecessariCas1(X):-veicoliSPInCaserma(cas1,X).

agentiNecessariCas2(X):-agentiInCaserma(cas2,X).
veicoliNecessariCas2(X):-veicoliInCaserma(cas2,X).
veicoliSPNecessariCas2(X):-veicoliSPInCaserma(cas2,X).

agentiNecessariCas3(X):-agentiInCaserma(cas3,X).
veicoliNecessariCas3(X):-veicoliInCaserma(cas3,X).
veicoliSPNecessariCas3(X):-veicoliSPInCaserma(cas3,X).

caserma1Giusta(X,Y,Z):-agentiNecessariCas1(X),veicoliNecessariCas1(Y),veicoliSPNecessariCas1(Z).
caserma2Giusta(X,Y,Z):-agentiNecessariCas2(X),veicoliNecessariCas2(Y),veicoliSPNecessariCas2(Z).
caserma3Giusta(X,Y,Z):-agentiNecessariCas3(X),veicoliNecessariCas3(Y),veicoliSPNecessariCas3(Z).
casermaGiusta(Cas,NumA,NumV,NumvSp):-agentiInCaserma(Cas,NumA),veicoliInCaserma(Cas,NumV),veicoliSPInCaserma(Cas,NumvSp).
