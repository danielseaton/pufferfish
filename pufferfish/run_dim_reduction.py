from dim_reduction import pca_dim_reduction
from data_loader import load_methylation_df, map_filename_to_sample_id
import pandas as pd

# m_df = load_methylation_df()
# m_df = m_df.dropna()
# m_df.columns = [map_filename_to_sample_id(x) for x in m_df.columns]
# m_df.to_csv('../data/merged_methylation_data.tsv', sep='\t')

m_df = pd.read_csv('../data/merged_methylation_data.tsv', sep='\t', index_col=0)

m_df = m_df[m_df.var(axis=1)>0.05]

n_components = 5
pca = pca_dim_reduction(m_df, n_components=n_components)

pca_df = pd.DataFrame(data = pca.components_, index=['PC{}'.format(x) for x in range(1, n_components+1)], columns = m_df.columns)

pca_df.to_csv('../data/methylation_PCA.tsv', sep='\t')
