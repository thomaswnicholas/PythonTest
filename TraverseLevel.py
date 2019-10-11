from Node import Node
from ObtainElement import ObtainElement
from Optioning import Optioning
from GetFiles import GetFiles
import pandas as pd
from pandas import DataFrame as DF



class TraverseLevel:

        


    def Event(self):
        
        instructions = []
        twodvisuals = []
        metricnames = []
        metricdescriptions = []
        istables = []
        metrictypes = []
        mandatorys = []
        metrictargets = []
        rangefroms = []
        rangetos = []
        torques = []
        tolerances = []
        torquecommands = []
        angletargets = []
        angletolerances = []
        anglerangefroms = []
        anglerangetos = []
        anglevalidations = []
        angleuoms = []
        metricgates = []
        metricfilenames = []
        tablecolumncounts = []
        tablerowcounts = []
        ipns = []        
        ipndescriptions = []
        ipnlineitems = []
        iqtys = []
        ipnuoms = []
        imatgroups = []
        iparentpns = []
        ibomstructures = []
        isubassemblypns = []
        


        for self.event in self.operation.iter("EVENT"):                
            
            einstructions = ObtainElement.GetInstruction(self, self.event)
            instructions= instructions + einstructions
            einstructions.clear()

            etwodvisuals = ObtainElement.GetTwodvisual(self, self.event)
            twodvisuals = twodvisuals + etwodvisuals
            etwodvisuals.clear()


            (emetricnames,emetricdescriptions,eistables,emetrictypes,
                emandatorys,emetrictargets,erangefroms,erangetos,
                etorques,etolerances,etorquecommands,eangletargets,
                eangletolerances,eanglerangefroms,eanglerangetos,
                eanglevalidations,eangleuoms,emetricgates,emetricfilenames,
                etablecolumncounts,etablerowcounts
                ) = ObtainElement.GetMetric(self, self.event)
            
            metricnames = metricnames + emetricnames
            emetricnames.clear
            
            metricdescriptions = metricdescriptions + emetricdescriptions
            emetricdescriptions.clear

            istables = istables + eistables
            eistables.clear

            metrictypes = metrictypes + emetrictypes
            emetrictypes.clear

            mandatorys = mandatorys + emandatorys
            emandatorys.clear

            metrictargets = metrictargets + emetrictargets
            emetrictargets.clear

            rangefroms = rangefroms + erangefroms
            erangefroms.clear

            rangetos = rangetos + erangetos
            erangetos.clear

            torques = torques + etorques
            etorques.clear

            tolerances = tolerances + etolerances
            etolerances.clear

            torquecommands = torquecommands + etorquecommands
            etorquecommands.clear

            angletargets = angletargets + eangletargets
            eangletargets.clear

            angletolerances = angletolerances + eangletolerances
            eangletolerances.clear

            anglerangefroms = anglerangefroms + eanglerangefroms
            eanglerangefroms.clear

            anglerangetos = anglerangetos + eanglerangetos
            eanglerangetos.clear

            anglevalidations = anglevalidations + eanglevalidations
            eanglevalidations.clear

            angleuoms = angleuoms + eangleuoms
            eangleuoms.clear

            metricgates = metricgates + emetricgates
            emetricgates.clear

            metricfilenames = metricfilenames + emetricfilenames
            emetricfilenames.clear

            tablecolumncounts = tablecolumncounts + etablecolumncounts
            etablecolumncounts.clear

            tablerowcounts = tablerowcounts + etablerowcounts
            etablerowcounts.clear
 
            (eipns,eipndescriptions,eipnlineitems,eiqtys,eipnuoms,eimatgroups,
                eiparentpns,eibomstructures,eisubassemblypns
                ) = ObtainElement.GetMaterial(self, self.event)

            ipns = ipns + eipns
            eipns.clear

            ipndescriptions = ipndescriptions + eipndescriptions
            eipndescriptions.clear

            ipnlineitems = ipnlineitems + eipnlineitems
            eipnlineitems.clear

            iqtys = iqtys + eiqtys
            eiqtys.clear

            ipnuoms = ipnuoms + eipnuoms
            eipnuoms.clear

            imatgroups = imatgroups + eimatgroups
            eimatgroups.clear

            iparentpns = iparentpns + eiparentpns
            eiparentpns.clear

            ibomstructures = ibomstructures + eibomstructures
            eibomstructures.clear
            
            isubassemblypns = isubassemblypns + eisubassemblypns
            eisubassemblypns.clear

        return (instructions,twodvisuals,metricnames,metricdescriptions,istables,metrictypes,mandatorys,metrictargets,rangefroms,rangetos,
                    torques,tolerances,torquecommands,angletargets,angletolerances,anglerangefroms,anglerangetos,anglevalidations,angleuoms,
                    metricgates,metricfilenames,tablecolumncounts,tablerowcounts,ipns,ipndescriptions,ipnlineitems,iqtys,ipnuoms,imatgroups,
                    iparentpns,ibomstructures,isubassemblypns)

    def Operation(self, assembly, product):
        nextnodehash = 0
        

        for self.operation in assembly.iter("OPERATION"):        
            self.opnumber = self.operation.find("IDNUMBER").text
            self.opdescription = self.operation.find("DESCRIPTION").text


            (instructions,twodvisuals,metricnames,metricdescriptions,istables,metrictypes,mandatorys,metrictargets,rangefroms,rangetos,
                    torques,tolerances,torquecommands,angletargets,angletolerances,anglerangefroms,anglerangetos,anglevalidations,angleuoms,
                    metricgates,metricfilenames,tablecolumncounts,tablerowcounts,ipns,ipndescriptions,ipnlineitems,iqtys,ipnuoms,imatgroups,
                    iparentpns,ibomstructures,isubassemblypns) = TraverseLevel.Event(self)

            Node.CreateNode(self,product,self.opnumber,instructions,twodvisuals,metricnames,metricdescriptions,istables,metrictypes,mandatorys,metrictargets,rangefroms,rangetos,
                    torques,tolerances,torquecommands,angletargets,angletolerances,anglerangefroms,anglerangetos,anglevalidations,angleuoms,
                    metricgates,metricfilenames,tablecolumncounts,tablerowcounts,ipns,ipndescriptions,ipnlineitems,iqtys,ipnuoms,imatgroups,
                    iparentpns,ibomstructures,isubassemblypns,nextnodehash,self.opdescription)

            

            nextnodehash += 1            

