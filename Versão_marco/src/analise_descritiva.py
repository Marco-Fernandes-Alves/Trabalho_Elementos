from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import os

def unsupervised_analysis(df, output_dir):
    try:
        # Clusterização (K-means)
        numeric_df = df.select_dtypes(include='number').drop(columns=['Ano'])
        kmeans = KMeans(n_clusters=3, random_state=42)
        df['Cluster'] = kmeans.fit_predict(numeric_df)

        # Redução de dimensionalidade (PCA)
        pca = PCA(n_components=2)
        principal_components = pca.fit_transform(numeric_df)
        df['PCA1'] = principal_components[:, 0]
        df['PCA2'] = principal_components[:, 1]

        # Visualização
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=df, x='PCA1', y='PCA2', hue='Cluster', palette='viridis')
        plt.title('Agrupamento de Municípios (PCA + K-means)')
        plt.savefig(os.path.join(output_dir, 'clustering_analysis.png'))
        plt.close()

        return df
    
    except Exception as e:
        print(f"Erro na análise: {str(e)}")
        return None