import GetFiles
from GetFiles import GetFiles
import ObtainElement
from ObtainElement import ObtainElement
import json


class Node:

    def SetCordinate(self,product,opnumber):
        
        self.cordinate = {
                    'Product':product,
                    'Sector':[],
                    'Time':{
                        'Start':[],
                        'Duration':[],
                        'Sequence':opnumber
                        },
                    'Option':{
                        'Option_1_type': None,
                        'Option_1': None,
                        'Option_2_type': None,
                        'Option_2': None}
                        }
        return self.cordinate
    
    def SetMaterialIssuance(self,ipns,ipndescriptions,ipnlineitems,iqtys,ipnuoms,imatgroups,iparentpns,ibomstructures,isubassemblypns):
        self.materialissuance = {
                            'PN': ipns,
                            'PnDescription': ipndescriptions,
                            'LineItem': ipnlineitems,
                            'Qty': iqtys,
                            'UOM': ipnuoms,
                            'MaterialGroup': imatgroups,
                            'ParentPN': iparentpns,
                            'BomStructure': ibomstructures,
                            'SubAssembly': isubassemblypns
                            }
        return self.materialissuance
    
    def SetDataCollection(self,metricnames,metricdescriptions,istables,metrictypes,mandatorys,metrictargets,rangefroms,rangetos,
                    torques,tolerances,torquecommands,angletargets,angletolerances,anglerangefroms,anglerangetos,anglevalidations,angleuoms,
                    metricgates,metricfilenames,tablecolumncounts,tablerowcounts):

        self.datacollection = {
                        'Name': metricnames,
                        'Description': metricdescriptions,
                        'Table': istables,
                        'MetricType': metrictypes,
						'Mandatory': mandatorys,
						'MetricTarget': metrictargets,
                        'RangeFrom': rangefroms,
                        'RangeTo': rangetos,
                        'Torque': torques,
                        'Tolerance': tolerances,
						'TorqueCommand': torquecommands,
						'AngleTarget': angletargets,
						'AngleTolerance': angletolerances,
                        'AngleRangeFrom': anglerangefroms,
                        'AngleRangeTo': anglerangetos,
						'AngleValidation': anglevalidations,
                        'AngleUOM': angleuoms,
						'MetricGate': metricgates,
						'MetricFilename': metricfilenames,
                        'TableColumnCount': tablecolumncounts,
                        'TableRowCount': tablerowcounts
                        }
        return self.datacollection
    
    def SetMaterialPartialConsumption(self):
        self.materialpartialconsumption = {
                            'PN': [],
                            'PnDescription': [],
                            'LineItem': [],
                            'Qty': [],
                            'UOM': [],
                            'MaterialGroup': [],
                            'ParentPN': [],
                            'SubAssembly': []
                            }
        return self.materialpartialconsumption

    def SetMaterialFullConsumption(self):
        self.materialfullconsumption = {
                            'PN': [],
                            'PnDescription': [],
                            'LineItem': [],
                            'Qty': [],
                            'UOM': [],
                            'MaterialGroup': [],
                            'ParentPN': [],
                            'SubAssembly': []
                            }
        return self.materialfullconsumption
    
    def SetMaterialDependency(self):
        self.materialdependency = {
                            'PN': [],
                            'PnDescription': [],
                            'LineItem': [],
                            'Qty': [],
                            'UOM': [],
                            'MaterialGroup': [],
                            'ParentPN': [],
                            'SubAssembly': []
                            }
        return self.materialdependency

    def SetMaterial(self):
        self.material = {
                        'Issuance': self.materialissuance,
                        'PartialConsumption': self.materialpartialconsumption,
                        'FullConsumption': self.materialfullconsumption,
                        'Dependency':self.materialdependency
                        }
        return self.material

    def SetOrder(self):
        self.order = []
        return self.order

    def SetElements(self,instructions,twodvisuals):
        self.elements = {
                    'Instruction': instructions,
                    'TwoDVisual': twodvisuals,
                    'ThreeDVisual':[],
                    'DataCollection': self.datacollection,
                    'Material': self.material,
                    'Order': self.order
                    }
        return self.elements

    def SetNodeHeader(self,nextnodehash,opdescription):

        self.node = {
                'Hash':nextnodehash,
                'Name':opdescription,
                'NodeType':'Work',
                'Kit':'999-1337-999',
                'Coordinate': self.cordinate,
                'Elements': self.elements
                    }
        return self.node

    def CreateNode(self,product,opnumber,instructions,twodvisuals,metricnames,metricdescriptions,istables,metrictypes,mandatorys,metrictargets,rangefroms,rangetos,
                    torques,tolerances,torquecommands,angletargets,angletolerances,anglerangefroms,anglerangetos,anglevalidations,angleuoms,
                    metricgates,metricfilenames,tablecolumncounts,tablerowcounts,ipns,ipndescriptions,ipnlineitems,iqtys,ipnuoms,imatgroups,
                    iparentpns,ibomstructures,isubassemblypns,nextnodehash,opdescription):

        Node.SetCordinate(self,product,opnumber)        
        Node.SetDataCollection(self,metricnames,metricdescriptions,istables,metrictypes,mandatorys,metrictargets,rangefroms,rangetos,
                    torques,tolerances,torquecommands,angletargets,angletolerances,anglerangefroms,anglerangetos,anglevalidations,angleuoms,
                    metricgates,metricfilenames,tablecolumncounts,tablerowcounts)
        
        Node.SetMaterialDependency(self)
        Node.SetMaterialFullConsumption(self)
        Node.SetMaterialIssuance(self,ipns,ipndescriptions,ipnlineitems,iqtys,ipnuoms,imatgroups,iparentpns,ibomstructures,isubassemblypns)
        Node.SetMaterialPartialConsumption(self)
        Node.SetMaterial(self)
        Node.SetOrder(self)
        Node.SetElements(self,instructions,twodvisuals)
        Node.SetNodeHeader(self,nextnodehash,opdescription)
        Node.NodeOutput(self)

    def NodeOutput(self):
        jsonoutput = GetFiles.InitiateJsonFile(self)
        json.dump(self.node, jsonoutput, indent=True)
