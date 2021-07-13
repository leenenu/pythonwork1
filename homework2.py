#!/usr/bin/env python
#coding:utf-8

import sys
from lxml import etree
from os import path
from optparse import OptionParser
def XMLDeal_warpper(func):

  def XMLDeal(fileName, elemTag, func4Element=None):

          count = 0
          es = ('end',)
          ns = func(fileName)
          ns = "{%s}"%ns

          context = etree.iterparse(fileName,events=es, tag=ns+elemTag)
          
          for event, elem in context:
              # Call the outside function to deal with the element here
              try:
                  func4Element(elem)            
              except Exception:
                  raise Exception("Something wrong in function parameter: func4Element")
              finally:
                  elem.clear()
                  count = count + 1
                  while elem.getprevious() is not None:
                      del elem.getparent()[0]
          del context         
          # Return how many elements had been parsed
          return count
  return XMLDeal
@XMLDeal_warpper
def DealwithXml(fileName):
        """"""
        if(not path.isfile(fileName) or not fileName.endswith("xml")):
            raise FileNotFoundError 
        result = ''
        es = ('start-ns',)
        context = etree.iterparse(fileName,events=es) 
        for event, elem in context:
            prefix, result = elem
            #print("%s, %d"%(elem, len(elem)))
            break
        del context
        return result



#----------------------------------------------------------------------
def dealwithElement(elem):
    """"""
    if isinstance(elem,object):
        print(elem.text)
        
if __name__ == "__main__":  
        fileName = "/content/P00734.xml"
        elemTag = "accession"
        count = DealwithXml(fileName, elemTag, dealwithElement)
        print("Already parsed %d XML elements."%count)
        
'''
CALL EXAMPLE 1:
COMMAND LINE:     python3 callDealer.py P00734.xml accession
OUTPUT:           
P00734
B2R7F7
B4E1A7
Q4QZ40
Q53H04
Q53H06
Q69EZ7
Q7Z7P3
Q9UCA1
Already parsed 9 XML elements.          


CALL EXAMPLE 2:
COMMAND LINE:     python3 callDealer.py P00734.xml sequence
OUTPUT:           
MAHVRGLQLPGCLALAALCSLVHSQHVFLAPQQARSLLQRVRRANTFLEEVRKGNLEREC
VEETCSYEEAFEALESSTATDVFWAKYTACETARTPRDKLAACLEGNCAEGLGTNYRGHV
NITRSGIECQLWRSRYPHKPEINSTTHPGADLQENFCRNPDSSTTGPWCYTTDPTVRRQE
CSIPVCGQDQVTVAMTPRSEGSSVNLSPPLEQCVPDRGQQYQGRLAVTTHGLPCLAWASA
QAKALSKHQDFNSAVQLVENFCRNPDGDEEGVWCYVAGKPGDFGYCDLNYCEEAVEEETG
DGLDEDSDRAIEGRTATSEYQTFFNPRTFGSGEADCGLRPLFEKKSLEDKTERELLESYI
DGRIVEGSDAEIGMSPWQVMLFRKSPQELLCGASLISDRWVLTAAHCLLYPPWDKNFTEN
DLLVRIGKHSRTRYERNIEKISMLEKIYIHPRYNWRENLDRDIALMKLKKPVAFSDYIHP
VCLPDRETAASLLQAGYKGRVTGWGNLKETWTANVGKGQPSVLQVVNLPIVERPVCKDST
RIRITDNMFCAGYKPDEGKRGDACEGDSGGPFVMKSPFNNRWYQMGIVSWGEGCDRDGKY
GFYTHVFRLKKWIQKVIDQFGE

Already parsed 1 XML elements.
'''
