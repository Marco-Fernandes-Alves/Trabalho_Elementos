from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
import os

def unsupervised_analysis(df, output_dir):
    try:
        numeric_df = df.select_dtypes(include='number').drop(columns=['Ano'])
        
        # Verifica se há dados para análise
        if numeric_df.empty:
            print('Erro: Nenhuma coluna numérica para análise.')
            return None
            
        # elbow-method
        distortions = []
        K_range = range(2, 6)
        for k in K_range:
            kmeans = KMeans(n_clusters=k, random_state=42)
            kmeans.fit(numeric_df)
            distortions.append(kmeans.inertia_)
        
        plt.figure(figsize=(8, 4))
        plt.plot(K_range, distortions, 'bx-')
        plt.xlabel('Número de Clusters (k)')
        plt.ylabel('Inércia')
        plt.title('Método do Cotovelo')
        plt.savefig(os.path.join(output_dir, 'elbow_method.png'))
        plt.close()
        
        # Clusterização (K=3)
        kmeans = KMeans(n_clusters=3, random_state=42)
        df['Cluster'] = kmeans.fit_predict(numeric_df)
        
        # PCA
        pca = PCA(n_components=2)
        principal_components = pca.fit_transform(numeric_df)
        df['PCA1'] = principal_components[:, 0]
        df['PCA2'] = principal_components[:, 1]
        
        # Guardar CSVs com clusters
        df.to_csv(os.path.join(output_dir, 'clusters_pca.csv'), index=False)
        
        # Gráfico de Clusters
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=df, x='PCA1', y='PCA2', hue='Cluster', palette='viridis')
        plt.title('Agrupamento de Municípios')
        plt.savefig(os.path.join(output_dir, 'clustering_analysis.png'))
        plt.close()
        
        return df
    
    except Exception as e:
        print(f'Erro na análise: {str(e)}')
        return None
