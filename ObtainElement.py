

class ObtainElement:

    def GetInstruction(self, event):
        instructions = []
        for instruction in event.iter("WORKINSTRUCTIONS"):
            instruction = str(event.find("WORKINSTRUCTIONS").text)
            instruction = instruction.replace("\n          "," ")
            instruction = instruction[:-10]
            instructions.append(instruction)
        return instructions

    def GetTwodvisual(self, event):
        twodvisuals = []
        for twodvisual in event.iter("SOURCEFILENAME"):
            twodvisual = event.find("SOURCEFILENAME").text
            twodvisuals.append(twodvisual)
        return twodvisuals

    def GetMetric(self, event):
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

        for metric in event.iter("METRIC"):
            
            metricname = metric.find("IDNUMBER").text
            metricnames.append(metricname)

            metricdescription = metric.find("DESCRIPTION").text
            metricdescriptions.append(metricdescription)

            istable = metric.find("ISTABLE").text
            istables.append(istable)

            metrictype = metric.find("METRICTYPE").text
            metrictypes.append(metrictype)

            mandatory = metric.find("MANDATORYMETRIC").text
            mandatorys.append(mandatory)

            metrictarget = metric.find("METRICTARGET").text
            metrictargets.append(metrictarget)

            rangefrom = metric.find("METRICRANGEFROM").text
            rangefroms.append(rangefrom)

            rangeto = metric.find("METRICRANGETO").text
            rangetos.append(rangeto)

            torque = metric.find("METRICTORQUE").text
            torques.append(torque)

            tolerance = metric.find("METRICTOLERANCE").text
            tolerances.append(tolerance)

            torquecommand = metric.find("TORQUECOMMAND").text
            torquecommands.append(torquecommand)

            angletarget = metric.find("METRICTORQUEANGLETARGET").text
            angletargets.append(angletarget)

            angletolerance = metric.find("METRICANGLETOLERANCE").text
            angletolerances.append(angletolerance)

            anglerangefrom = metric.find("METRICANGLERANGEFROM").text
            anglerangefroms.append(anglerangefrom)

            anglerangeto = metric.find("METRICANGLERANGETO").text
            anglerangetos.append(anglerangeto)

            anglevalidation = metric.find("METRICANGLEVALIDATIONREQUIRED").text
            anglevalidations.append(anglevalidation)

            angleuom = metric.find("METRICANGLEUOM").text
            angleuoms.append(angleuom)

            metricgate = metric.find("METRICBLOCKNAVIGATION").text
            metricgates.append(metricgate)

            metricfilename = metric.find("METRICFILENAME").text
            metricfilenames.append(metricfilename)

            tablecolumncount = metric.find("METRICTABLECOLUMNCOUNT").text
            tablecolumncounts.append(tablecolumncount)

            tablerowcount = metric.find("METRICTABLEROWCOUNT").text
            tablerowcounts.append(tablerowcount)
        
        return (metricnames,metricdescriptions,istables,metrictypes,
                mandatorys,metrictargets,rangefroms,rangetos,
                torques,tolerances,torquecommands,angletargets,
                angletolerances,anglerangefroms,anglerangetos,
                anglevalidations,angleuoms,metricgates,metricfilenames,
                tablecolumncounts,tablerowcounts
                )

    def GetMaterial(self, event):
        
        ipns = []        
        ipndescriptions = []
        ipnlineitems = []
        iqtys = []
        ipnuoms = []
        imatgroups = []
        iparentpns = []
        ibomstructures = []
        isubassemblypns = []

        for material in event.iter("COMPONENT"):
            
            ipn = material.find("IDNUMBER").text
            ipns.append(ipn)

            ipndescription = material.find("DESCRIPTION").text
            ipndescriptions.append(ipndescription)

            ipnlineitem = material.find("POSITION").text
            ipnlineitems.append(ipnlineitem)

            iqty = material.find("QTY").text
            iqtys.append(iqty)

            ipnuom = material.find("UOM").text
            ipnuoms.append(ipnuom)

            imatgroup = material.find("MATERIALGROUP").text
            imatgroups.append(imatgroup)

            iparentpn = material.find("BOM").text
            iparentpns.append(iparentpn)

            ibomstructure = material.find("BOMSTRUCTURE").text
            ibomstructures.append(ibomstructure)

            isubassemblypn = material.find("SUBASSEMBLY").text
            isubassemblypns.append(isubassemblypn)

        return (ipns, ipndescriptions, ipnlineitems, iqtys,
                ipnuoms,imatgroups, iparentpns, ibomstructures, isubassemblypns)