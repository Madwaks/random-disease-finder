import pandas as pd
import os
print(os.path)


class FindDisease():
    def __init__(self):
        self.dis_sympt = pd.read_csv("app/back/data/diseases_symptoms.csv", sep= ";")

        # transform data to set
        self.dis_sympt.loc[:, 'symptom_ids'] = self.dis_sympt.symptom_ids.map(lambda l: set(
                                                                            map(int, l.split(':'))
                                                                         )
                                                            )

        self.dis = pd.read_csv("app/back/data/diseases.csv", sep= ";")
        self.sympt = pd.read_csv("app/back/data/symptoms.csv", sep= ";")

        self.dis_dict = self.dis.to_dict(orient='records')

        self.sympt_dict = self.sympt.to_dict(orient='records')

    def compute_jaccard(self, list_symp):
        d_s = self.dis_sympt.copy()
        set_symp = set(self.list_symp)
        # Compute jaccard index
        d_s.loc[:, 'probability'] = d_s.symptom_ids.map(lambda s: len(set_symp.intersection(s)) / len(set_symp.union(s)))

        # Returns dataframe with jaccard index for every observation
        return d_s
    
    def get_ids_names(self, list_symp=[]):
        ids_df = self.compute_jaccard(list_symp)
        dis_df = self.dis.copy()
        symp_df = self.sympt.copy()

        names_df = ids_df[['probability']]
        names_df = names_df[names_df['probability'] > 0]
        names_df['disease_name'] = ids_df['disease_id'].map(lambda val: self.dis.loc[self.dis.id == val, 'name'].values[0])
        names_df['symptoms_names'] = ids_df['symptom_ids'].map(lambda s: [symp_df.loc[self.sympt.id == elem, 'name'].values[0] for elem in s])
        return names_df
    
    