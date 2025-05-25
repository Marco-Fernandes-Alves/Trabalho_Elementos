from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def unsupervised_analysis(df, output_dir):
    try:
        numeric_df = df.select_dtypes(include='number').drop(columns=['Ano'])
        
        # Método do Cotovelo
        distortions = []
        K_range = range(2, 6)
        for k in K_range:
            kmeans = KMeans(n_clusters=k, random_state=42)
            kmeans.fit(numeric_df)
            distortions.append(kmeans.inertia_)
        
        plt.figure(figsize=(10, 5))  # Aumentado para 10x5
        plt.plot(K_range, distortions, 'bx-')
        plt.xlabel('Número de Clusters (k)', fontsize=12)
        plt.ylabel('Inércia', fontsize=12)
        plt.title('Método do Cotovelo', fontsize=14)
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'elbow_method.png'))
        plt.close()
        
        # Clusterização
        kmeans = KMeans(n_clusters=3, random_state=42)
        df['Cluster'] = kmeans.fit_predict(numeric_df)
        
        # Silhouette Score
        silhouette_avg = silhouette_score(numeric_df, df['Cluster'])
        
        # PCA
        pca = PCA(n_components=2)
        principal_components = pca.fit_transform(numeric_df)
        df['PCA1'] = principal_components[:, 0]
        df['PCA2'] = principal_components[:, 1]
        
        # Visualização
        plt.figure(figsize=(12, 8))  # Aumentado para 12x8
        sns.scatterplot(data=df, x='PCA1', y='PCA2', hue='Cluster', palette='viridis', s=80)
        plt.title(f'Agrupamento de Municípios (Silhouette Score: {silhouette_avg:.2f})', fontsize=14)
        plt.xlabel('PCA1', fontsize=12)
        plt.ylabel('PCA2', fontsize=12)
        plt.legend(title='Cluster', fontsize=10)
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'clustering_analysis.png'))
        plt.close()
        
        # Salvar variância do PCA
        pca_df = pd.DataFrame({
            'Componente': ['PCA1', 'PCA2'],
            'Variância Explicada': pca.explained_variance_ratio_
        })
        pca_df.to_csv(os.path.join(output_dir, 'pca_variance.csv'), index=False)
        
        return df
    
    except Exception as e:
        print(f'Erro na análise: {str(e)}')
        return None
