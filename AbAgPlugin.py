#from data_prepare import extract_ppi_lists, download

import PyIO
import PyPluMA
import os

class AntibodyBLASTPlugin:
    def input(self, inputfile):
        self.parameters = PyIO.readParameters(inputfile)

    def run(self):
        pass

    def output(self, outputfile):
        #print("singularity "+self.parameters["container"]+" python 1_SAbDab.py --input_dir"+PyPluMA.prefix()+"/"+self.parameters["input_dir"]+" --output_dir"+outputfile)
        os.system("singularity exec "+PyPluMA.prefix()+"/"+self.parameters["container"]+" python plugins/AntibodyBLAST/run_AntibodyBLAST.py --input_dir "+PyPluMA.prefix()+"/"+self.parameters["input_dir"]+" --output_dir "+outputfile+" --db_pickle "+PyPluMA.prefix()+"/"+self.parameters["db_pickle"]+" --target_pickle "+PyPluMA.prefix()+"/"+self.parameters["target_pickle"])

        #ppi_list_db, ppi_list_target = extract_ppi_lists(, False)
        #updated_ppi_list_db = download(ppi_list_db, config, to_write=config['db_list'], min_seq_len=None)
        #updated_ppi_list_target = download(ppi_list_target, config, to_write=config['target_list'], min_seq_len=min_seq_len)
