import data_loader
from sklearn.decomposition import PCA
import pandas as pd




n_components = 5

m_df = data_loader.load_methylation_df()

m_df = m_df.dropna()

pca = PCA(n_components=n_components)
pca.fit(m_df)

print(m_df.shape)
print(pca.explained_variance_ratio_)

pca_df = pd.DataFrame(data = pca.components_, index=['PC{}'.format(x) for x in range(1, n_components+1)], columns = m_df.columns)

pca_df.to_csv('../data/methylation_PCA.tsv')
