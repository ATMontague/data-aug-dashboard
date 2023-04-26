import streamlit as st
import os


IMG_SIZE = (224, 224)
# IMG_OPTIONS = ('shark0', 'elephant')
# todo: rename these to: 'great white', tiger, hammer, ..., some turtle, tiny turtle...
# todo: make sure you used the ones that are 224x224
IMG_OPTIONS = ('shark0', 'shark1', 'shark2', 'shark3',
               'turtle0', 'turtle1', 'turtle2', 'turtle3')

AUG_OPTIONS = ('baseline',
               'drop',
               'emboss',
               'gray')

AUG_PATH = 'data/aug_ex'
VIZ_PATH = 'data/viz_ex'
DATA_PATH = 'data/SharksAndTurtles'


def main():
    st.set_page_config(layout='wide')

    ####################
    # SIDE BAR PORTION #
    ####################

    current_image = None

    input_image = st.sidebar.selectbox(label='Input Image', options=IMG_OPTIONS)

    # reading image based off of user selection
    img = os.path.join(DATA_PATH, 'input', '{}.JPEG'.format(input_image))
    st.sidebar.image(image=img, width=IMG_SIZE[0], caption='input image')

    # if input_image == 'shark0':
    #     current_image = 'shark0'
    #     img = 'data/imgs/shark0.jpg'
    #     st.sidebar.image(image=img, width=IMG_SIZE[0], caption='input image')
    # elif input_image == 'elephant':
    #     current_image = 'elephant'
    #     img = 'data/imgs/elephant.jpg'
    #     st.sidebar.image(image=img, width=IMG_SIZE[0], caption='input image')

    st.sidebar.button('add custom image (todo)')

    # adding option for selecting aug methods
    option = st.sidebar.selectbox(label='Augmentation to apply', options=AUG_OPTIONS)

    # todo: set up to use original input images so we can delete the extra baseline folder in \input_aug
    aug_image = os.path.join(DATA_PATH, 'input_aug', option, '{}.JPEG'.format(input_image))

    # aug_image = os.path.join(AUG_PATH, '{}_{}.png'.format(current_image, option))

    st.sidebar.image(image=aug_image, width=IMG_SIZE[0], caption='augmented image')

    ############################
    # END OF SIDE BAR PORTION  #
    ############################

    ######################
    # MAIN SECTION START #
    ######################
    st.title('Exploring Data Augmentation for Classification')
    # note, 'input_image' gives use 'shark0' and 'option' gives us the method

    sal_map_img = os.path.join(DATA_PATH, 'sm', option, 'sm_{}.png'.format(input_image))
    sal_map_overlay = os.path.join(DATA_PATH, 'sm', option, 'sm_img_{}.png'.format(input_image))

    gc_img = os.path.join(DATA_PATH, 'gc', option, 'gc_{}.png'.format(input_image))
    gc_img_overlay = os.path.join(DATA_PATH, 'gc', option, 'gc_img_{}.png'.format(input_image))

    lime_img = os.path.join(DATA_PATH, 'lime', option, 'lime_{}.png'.format(input_image))

    # sal_map_img = os.path.join(VIZ_PATH, '{}_saliency.png'.format(current_image))
    # sal_map_overlay = os.path.join(VIZ_PATH, '{}_saliency_overlay.png'.format(current_image))
    # gc_img = os.path.join(VIZ_PATH, '{}_gradcam.png'.format(current_image))
    # gc_img_overlay = os.path.join(VIZ_PATH, '{}_gradcam_overlay.png'.format(current_image))
    # lime_img = os.path.join(VIZ_PATH, '{}_lime.png'.format(current_image))


    # # stuff related to entire model/data trained on specific aug (not image dependent)
    # with st.container():
    #     st.write('container test')
    #     tsne = '/home/adam/repos/edtech/data-aug-dashboard/data/imgs/T-SNE_Embedding_of_MNIST.png'
    #     st.image(image=tsne, caption='tsne test ex')

    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image(sal_map_img, caption='Saliency Map')
            st.image(gc_img, caption='Grad-CAM')
            st.image(lime_img, caption='LIME')
            tsne = 'data/imgs/T-SNE_Embedding_of_MNIST.png'
            st.image(image=tsne, caption='tsne test ex')

        with col2:
            st.image(sal_map_overlay, caption='with overlay')
            # st.image(gc_img, caption='Grad-CAM')
            st.image(gc_img_overlay, caption='with overlay')
        # with col3:
        #     st.image(lime_img, caption='LIME')
        #     st.image(sal_map_img, caption='with overlay')
        # with col4:
        #     st.header('t-sne ex')
        #     st.image('data/imgs/T-SNE_Embedding_of_MNIST.png')

    with st.container():
        st.text_area(label='test', value='Model statistics / top predictions placeholder')



if __name__ == '__main__':
    main()