from . import data_loader
from sklearn.decomposition import PCA
import pandas as pd



from sklearn.externals import joblib
# Output a pickle file for the model
joblib.dump(clf, 'saved_model.pkl') 



n_components = 5


def pca_dim_reduction(m_df):
    m_df = data_loader.load_methylation_df()
    

    pca = PCA(n_components=n_components)
    pca.fit(m_df)

    #print(m_df.shape)
    print("explained variance ration",pca.explained_variance_ratio_)

    # pca_df = pd.DataFrame(data = pca.components_, index=['PC{}'.format(x) for x in range(1, n_components+1)], columns = m_df.columns)

    # pca_df.to_csv('../data/methylation_PCA.tsv')
    
    return pca