import pandas as pd
import glob
import os

def get_data_filepath(cluster_id):

    filepath_dict = {'EBI': '/hps/nobackup2/research/stegle/users/CompetitionRetreat',
                     'yoda': '/hps/nobackup/stegle/users/CompetitionRetreat',
                     'DKFZ': '/icgc/dkfzlsdf/analysis/B260/projects/CompetitionRetreat'}

    return filepath_dict[cluster_id]


def load_methylation_df(cluster_id='yoda', nrows=None, nfiles=None):
    # nrows, nfiles - set to smaller values for testing
    
    working_dir = get_data_filepath(cluster_id)
    methylation_files = glob.glob(os.path.join(working_dir, 'MethylationData/Imputed/*/*.bedGraph.gz'))

    if methylation_files is not None:
        methylation_files = methylation_files[:nfiles]

    list_of_dfs = []
    for filepath in methylation_files:
        sample_name = os.path.basename(filepath)
        df = pd.read_csv(filepath, sep='\t', nrows=nrows)
        df.columns = ['chr','start','end',sample_name]
        df = df.set_index('start')
        df = df[[sample_name]]
        list_of_dfs.append(df)

    meth_df = pd.concat(list_of_dfs, axis=1)

    return meth_df

#df = load_methylation_df(nrows=100, nfiles=20)
