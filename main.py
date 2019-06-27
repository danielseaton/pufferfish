import pufferfish as pu
from sklearn.decomposition import PCA
import joblib
import sklearn.ensemble
import sklearn.multioutput
import os
# def get_data_filepath(cluster_id):

#     filepath_dict = {'EBI': '/hps/nobackup2/research/stegle/users/CompetitionRetreat',
#                      'yoda': '/hps/nobackup/stegle/users/CompetitionRetreat',
#                      'DKFZ': '/icgc/dkfzlsdf/analysis/B260/projects/CompetitionRetreat'}

#     return filepath_dict[cluster_id]

working_dir = "/home/thorsten/Desktop/hackathon"

# load data
met = pu.load_methylation_df(working_dir=working_dir,nfiles=20,nrows=None)#, nrows=100, nfiles=20)
exp = pu.load_expression_data(working_dir=working_dir)



print(met.shape, exp.shape)


# pre processing
met = met.dropna()#.to_numpy()
exp = exp#.to_numpy()

pca_alg_file = 'dim_red_alg.pkl'
overwrite_pca = True
if (not os.path.exists(pca_alg_file)) or overwrite_pca:
    n_components = 5
    dim_red_alg = PCA(n_components=n_components) 
    met_red = dim_red_alg.fit(met)
    joblib.dump(dim_red_alg, pca_alg_file)
else:
    dim_red_alg = joblib.load(pca_alg_file) 

met_red = dim_red_alg.transform(met)


rf_reg = sklearn.ensemble.RandomForestRegressor(n_estimators=255)
mult_rf_reg = sklearn.multioutput.MultiOutputRegressor(estimator=rf_reg)

print(met_red.shape, exp.shape)
mult_rf_reg.fit(met_red, exp)