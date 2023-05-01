import streamlit as st

st.title('Explainability Methods')

sm_url = 'https://arxiv.org/abs/1312.6034'
st.header('[Saliency Maps](%s)' % sm_url)
st.markdown(
    """
    Saliency maps are a visualization technique applied to CNNs to try to understand how the model is making predictions.
    A saliency map highlights the most important regions of an input image, to show what the model is focusing on when making a prediction.
    Saliency maps can be useful in understanding how a CNN works and in identifying potential areas for improvement or fine-tuning.
    """
)

gc_url = 'https://arxiv.org/abs/1610.02391'
st.header('[Grad-CAM](%s)' % gc_url)
st.markdown(
    """
Grad-CAM (Gradient-weighted Class Activation Mapping) is a visualization technique applied to CNNs to try to understand which parts of an input image
are most relevant to the model's prediction. It is an extension of the original CAM (Class Activation Mapping) method,
which was used to identify the most important regions of an image for a specific class.
Unlike a saliency map (which highlight individual pixels or regions of an image), Grad-CAM produces a heatmap that is aligned with the input image.

 """
)


lime_url = 'https://arxiv.org/abs/1602.04938'
st.header('[LIME](%s)' % lime_url)

# todo: mention difference between both limes as shown in dashboard
st.markdown(
    """
LIME (Local Interpretable Model-Agnostic Explanations) is a technique used to explain the prediction of a machine learning classifier on an image.
It works by generating a simplified model that approximates the behavior of the original classifier in a local region around the image.
    """
)


tsne_url = "https://en.wikipedia.org/wiki/T-distributed_stochastic_neighbor_embedding"
st.header('[t-distributed stochastic neighbor embedding (t-SNE)](%s)' % tsne_url)
st.markdown(
    """
t-SNE is a non-linear dimensionality reduction technique that can be used to visualize high-dimensional data.
It generates a probability distribution over the original data and then a second probability distribution is created
over points in a lower dimensional space and then measures the divergence between the two distributions. By minimizing
the divergence the end result is a set of points in 2d or 3d space that can then be visualized.
    """
)

pca_url = 'https://en.wikipedia.org/wiki/Dimensionality_reduction#Principal_component_analysis_(PCA)'
st.header('[Principal Component Analysis (PCA)](%s)' % pca_url)
st.markdown(
    """
PCA is a linear algebra technique that can be used for dimensionality reduction. By reducing the feature space from n dimensions
to 2 or 3 dimensions it is then possible to visualize these features by plotting them.

 """
)