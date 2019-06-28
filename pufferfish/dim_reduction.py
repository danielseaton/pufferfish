from sklearn.decomposition import PCA
import data_loader
import pandas as pd



from sklearn.externals import joblib
# Output a pickle file for the model
#joblib.dump(clf, 'saved_model.pkl') 





def pca_dim_reduction(m_df, n_components=5):
#    m_df = data_loader.load_methylation_df()
    

    pca = PCA(n_components=n_components)
    pca.fit(m_df.values)

    #print(m_df.shape)
    print("explained variance ratios: ", pca.explained_variance_ratio_)

    # pca_df = pd.DataFrame(data = pca.components_, index=['PC{}'.format(x) for x in range(1, n_components+1)], columns = m_df.columns)

    return pca
