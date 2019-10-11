import xml.etree.ElementTree as ET

class GetFiles:

    def ObtainXMLFile(self):
        with open("C:\\Apollo\\XML_Translation\\XML_In\\00-445511-PM.xml", encoding='UTF-8') as self.CFIN:
            self.tree = ET.parse(self.CFIN)
            self.assembly = self.tree.getroot()
            self.product = self.assembly.find("IDNUMBER").text
        return self.assembly, self.product

    def TestXMLFile(self):
        with open("C:\\Apollo\\XML_Translation\\XML_In\\00-445511-PM.xml", encoding='UTF-8') as self.CFIN:
            self.tree = ET.parse(self.CFIN)
            self.assembly = self.tree.getroot()
            self.product = self.assembly.find("IDNUMBER").text
        return self.assembly, self.product, self.tree




    def InitiateJsonFile(self):
        self.jsonoutput = open("C:\\Apollo\\XML_Translation\\XML_Processed\\logfile.json","a")
        return self.jsonoutput

    def CloseJsonFile(self):
        self.jsonoutput.close()
