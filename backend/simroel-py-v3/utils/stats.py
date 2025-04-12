
import pandas as pd
class Statistics(object):
    def __init__(self):
        self.n_handled = 0
        self.n_allocted = 0

        self.b_resource = 0
        self.b_osnr = 0
        self.b_crosstalk = 0
        self.b_nli = 0

    def allocated(self):
        self.n_allocted += 1

    def handled(self):
        self.n_handled += 1

    def resource(self):
        self.b_resource += 1

    def osnr(self):
        self.b_osnr += 1

    def crosstalk(self):
        self.b_crosstalk += 1
    def nli(self):
        self.b_nli +=1

    def block_control(self, alloc_status):
        if alloc_status == "resource":
            self.resource()
            return False
        elif alloc_status == "osnr":
            self.osnr()
            return False
        elif alloc_status == "crosstalk":
            self.crosstalk()
            return False
        elif alloc_status == "nli":
            self.nli()
            return False
        elif alloc_status == "allocated":
            self.allocated()
            return True
        else:
            raise ValueError("alloc_status must be 'resource', 'osnr', 'crosstalk' or 'allocated'")

    def summarize(self):
        text = f"""
        [*] Total connections handled: {self.n_handled}
        [*] Total connections allocated: {self.n_allocted} ({(self.n_allocted / self.n_handled) * 100:.2f}%)
        ********* BLOCKED (+) *********
        [-] Resource: {self.b_resource} ({(self.b_resource / self.n_handled) * 100:.4f}%)
        [-] OSNR: {self.b_osnr} ({(self.b_osnr / self.n_handled) * 100:.4f}%)
        [-] OSNR_NLI: {self.b_nli} ({(self.b_nli / self.n_handled) * 100:.4f}%)
        [-] XT: {self.b_crosstalk} ({(self.b_crosstalk / self.n_handled) * 100:.4f}%)
        ********** DEBUG (+) **********
        [+] Total: {self.b_resource + self.b_osnr + self.b_crosstalk + self.n_allocted}
        """
        print(text)
    def results(self):
        print(f' {[self.b_resource, self.b_osnr, self.b_crosstalk,self.b_nli,self.n_handled]}')
        output = pd.DataFrame([self.b_resource, self.b_osnr, self.b_crosstalk,self.b_nli,self.n_handled]).T
        output.columns = ['Resource', 'OSNR', 'Crosstalk', 'nli', 'Allocted']
        return output