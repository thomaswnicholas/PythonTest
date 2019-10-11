import GetFiles
from GetFiles import GetFiles
import TraverseLevel
from TraverseLevel import TraverseLevel as TL
import Optioning
from Optioning import Optioning
import pandas as pd
from pandas import DataFrame as DF
import json



class Translator:


    def Main(self):        
        assembly, product = GetFiles.ObtainXMLFile(self)
        operationoptions = Optioning.OptionListBuilder(self, assembly)
        print(operationoptions)
        TL.Operation(self, assembly, product)
        GetFiles.CloseJsonFile(self)

    def Test(self):
        self.assembly, self.product, self.tree = GetFiles.TestXMLFile(self)
        #print(self.assembly.tag)
        for child in self.assembly:
            #print(child.tag, child.text)
            for element in child:
                print(element.tag, element.attrib, element.text)
                for somthing in element:
                    print(somthing.tag, somthing.attrib, somthing.text)

Translator().Main()

#Translator().Test()