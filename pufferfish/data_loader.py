import pandas as pd
import glob
import os
from sklearn.decomposition import PCA
import re

def load_methylation_df(working_dir='/nfs/leia/research/stegle/dseaton/data/retreat_hackathon2019/CompetitionRetreat', nrows=None, nfiles=None):
    # nrows, nfiles - set to smaller values for testing

    methylation_files = glob.glob(os.path.join(working_dir, 'MethylationData/featurecompressed/*.gz'))

    if methylation_files is not None:
        methylation_files = methylation_files[:nfiles]

    list_of_dfs = []
    for filepath in methylation_files:
        sample_name = os.path.basename(filepath)
        df = pd.read_csv(filepath, sep='\t', nrows=nrows, na_values='.')
        df.columns = ['chr','start','end','feature_id',sample_name]
        df = df.drop_duplicates(subset='feature_id')
        df = df.set_index('feature_id')
        df = df[[sample_name]]
        list_of_dfs.append(df)

    meth_df = pd.concat(list_of_dfs, axis=1)

    return meth_df

def load_expression_data(working_dir='/nfs/leia/research/stegle/dseaton/data/retreat_hackathon2019/CompetitionRetreat'):
    
    expression_files = [os.path.join(working_dir, 'ExpressionMatrix', x) for x in ['exprs_UD.txt', 'exprs_D3_test.txt']]

    list_of_dfs = [pd.read_csv(x, sep='\t', index_col=0) for x in expression_files]
    exp_df = pd.concat(list_of_dfs, axis=1)

    return exp_df

def map_filename_to_sample_id(filename):
    sample_id = re.search('Joxm1\_([UD3]{2}\_+[A-Z][0-9]+)', filename).groups()[0]
    sample_id = sample_id.replace('__','_')
    return sample_id
