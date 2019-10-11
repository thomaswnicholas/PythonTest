import pandas as pd
from pandas import DataFrame as DF


class Optioning:

    def Crawler(self, option, opnumber, opdescription):
        options = pd.DataFrame(columns=("Operation","Operation_Description","Option_1_type","Option_1","Option_2_type","Option_2"))
        loweroptions = pd.DataFrame(columns=("Option_type","Option"))
        numnextlevel = int            
        opt1 = option.find("IDNUMBER").text
        opttype1 = option.find("OPTIONTYPE").text
        
        numnextlevel = len(option.findall("OPTION"))

        if numnextlevel != 0:
            
            for option in option.findall("OPTION"):
                    
                    opttype2 = option.find("OPTIONTYPE").text
                    opt2 = option.find("IDNUMBER").text
                    
                    loweroptions = loweroptions.append({'Option_type': opttype1,'Option': str(opt1)}, ignore_index=True)
                    loweroptions = loweroptions.append({'Option_type': opttype2,'Option': str(opt2)}, ignore_index=True)
                    loweroptions.sort_values(by=['Option'])
                    
                    options = options.append({'Operation': opnumber,'Operation_Description': opdescription,
                        'Option_1_type':loweroptions.iloc[0]["Option_type"],
                        'Option_1':loweroptions.iloc[0]["Option"],
                        'Option_2_type':loweroptions.iloc[1]["Option_type"],
                        'Option_2':loweroptions.iloc[1]["Option"]},
                        ignore_index=True)

                    loweroptions.drop(loweroptions.index, inplace=True)
        else:

            options = options.append({'Operation': opnumber,'Operation_Description': opdescription,
                        'Option_1_type':opttype1,
                        'Option_1':opt1,
                        'Option_2_type':'NaN',
                        'Option_2':'NaN'}, ignore_index=True)
        
        return options
    
    def OperationOptionListBuilder(self, operation, opnumber, opdescription):
        options = pd.DataFrame(columns=("Operation","Operation_Description","Option_1_type","Option_1","Option_2_type","Option_2"))
        for option in operation.findall("OPTION"):
            options = Optioning.Crawler(self, option, opnumber, opdescription)

        return options

    def EventOptionListBuilder(self, event, opnumber, opdescription):
        options = pd.DataFrame(columns=("Operation","Operation_Description","Option_1_type","Option_1","Option_2_type","Option_2"))
        for option in event.findall("OPTION"):
            options = Optioning.Crawler(self, option, opnumber, opdescription)

        return options

    def OptionListBuilder(self,assembly):
        assemblyoptions = pd.DataFrame(columns=("Operation","Operation_Description","Option_1_type","Option_1","Option_2_type","Option_2"))
        operationoptions = pd.DataFrame(columns=("Operation","Operation_Description","Option_1_type","Option_1","Option_2_type","Option_2"))
        eventoptions = pd.DataFrame(columns=("Operation","Operation_Description","Option_1_type","Option_1","Option_2_type","Option_2"))

        for self.operation in assembly.iter("OPERATION"):        
            self.opnumber = self.operation.find("IDNUMBER").text
            self.opdescription = self.operation.find("DESCRIPTION").text

            operationoptions = Optioning.OperationOptionListBuilder(self, self.operation, self.opnumber, self.opdescription)

            for self.event in self.operation.iter("EVENT"):            
                eventoptions = Optioning.EventOptionListBuilder(self, self.operation, self.opnumber, self.opdescription)
                operationoptions = pd.concat([operationoptions,eventoptions])

            assemblyoptions = pd.concat([assemblyoptions,operationoptions])
            assemblyoptions = assemblyoptions.drop_duplicates()

        return assemblyoptions