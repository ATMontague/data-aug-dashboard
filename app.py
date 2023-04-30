import streamlit as st
import os
from utils import load_model, get_prediction
import cv2
import random

from utils import IMG_OPTIONS, IMG_NAME_MAP, IMG_SIZE


# IMG_SIZE = (224, 224)


# todo: rename these to: 'great white', tiger, hammer, ..., some turtle, tiny turtle...
#
# IMG_OPTIONS = ('shark0', 'shark1', 'shark2', 'shark3',
#                'turtle0', 'turtle1', 'turtle2', 'turtle3')

# IMG_OPTIONS = ('Great White',
#                'Hammerhead',
#                'Tiger Shark',
#                'Loggerhead Turtle',
#                'Leatherback Turtle')
#
# # todo: add these to utils.py and import wherever necessary
# # note: this only works if we randomly select an image
# img_name_map = {
#     'Great White': ['shark0'],
#     'Hammerhead': ['shark1'],
#     'Tiger Shark': ['shark2', 'shark3'],
#     'Loggerhead Turtle': ['turtle0', 'turtle2'],
#     'Leatherback Turtle': ['turtle1', 'turtle3'],
# }

AUG_OPTIONS = ('baseline',
               'drop',
               'emboss',
               'gray')


DATA_PATH = 'data/SharksAndTurtles'


def main():
    st.set_page_config(layout='wide')

    ####################
    # SIDE BAR PORTION #
    ####################

    input_image = st.sidebar.selectbox(label='Input Image', options=IMG_OPTIONS)

    # when we have multiple images for same animal
    if input_image == 'Tiger Shark' or input_image == 'Loggerhead Turtle' or input_image == 'Leatherback Turtle':
        # note: only works if each have same number of options
        idx = random.randint(0, 1)
    else:
        idx = 0

    # note: this is where we convert from selected option to name of actual file
    img_name = IMG_NAME_MAP[input_image][idx]

    # reading image based off of user selection
    img = os.path.join(DATA_PATH, 'input_aug', 'baseline', '{}.JPEG'.format(img_name))
    st.sidebar.image(image=img, width=IMG_SIZE[0], caption='input image')

    # adding option for selecting aug methods
    option = st.sidebar.selectbox(label='Augmentation to apply', options=AUG_OPTIONS)

    aug_image = os.path.join(DATA_PATH, 'input_aug', option, '{}.JPEG'.format(img_name))

    # todo: set up to use original input images so we can delete the extra baseline folder in \input_aug
    # aug_image = os.path.join(DATA_PATH, 'input_aug', option, '{}.JPEG'.format(input_image))
    # aug_image = os.path.join(AUG_PATH, '{}_{}.png'.format(current_image, option))

    st.sidebar.image(image=aug_image, width=IMG_SIZE[0], caption='augmented image')

    ############################
    # END OF SIDE BAR PORTION  #
    ############################

    ######################
    # MAIN SECTION START #
    ######################
    st.title('AugUnderstander: Exploring Data Augmentation in Image Classification')
    # note, 'input_image' gives use 'shark0' and 'option' gives us the method

    sal_map_img = os.path.join(DATA_PATH, 'sm', option, 'sm_{}.png'.format(img_name))
    sal_map_overlay = os.path.join(DATA_PATH, 'sm', option, 'sm_img_{}.png'.format(img_name))

    gc_img = os.path.join(DATA_PATH, 'gc', option, 'gc_{}.png'.format(img_name))
    gc_img_overlay = os.path.join(DATA_PATH, 'gc', option, 'gc_img_{}.png'.format(img_name))

    lime_img = os.path.join(DATA_PATH, 'lime', option, 'lime_{}.png'.format(img_name))
    lime_img2 = os.path.join(DATA_PATH, 'lime2', option, 'lime2_{}.png'.format(img_name))

    tsne = os.path.join(DATA_PATH, 'tsne', 'tsne_{}.png'.format(option))
    pca = os.path.join(DATA_PATH, 'pca', 'pca_{}.png'.format(option))

    # # stuff related to entire model/data trained on specific aug (not image dependent)
    # with st.container():
    #     st.write('container test')
    #     tsne = '/home/adam/repos/edtech/data-aug-dashboard/data/imgs/T-SNE_Embedding_of_MNIST.png'
    #     st.image(image=tsne, caption='tsne test ex')

    img_res = 300
    with st.container():

        st.header('Image Level')
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image(sal_map_img, width=img_res, caption='Saliency Map')
            st.image(gc_img, width=img_res, caption='Grad-CAM')
            # st.image(lime_img, caption='LIME')
            # tsne = 'data/imgs/T-SNE_Embedding_of_MNIST.png'
            # st.image(image=tsne, caption='tsne test ex')

        with col2:
            st.image(sal_map_overlay, width=img_res, caption='with overlay')
            # st.image(gc_img, caption='Grad-CAM')
            st.image(gc_img_overlay, width=img_res, caption='with overlay')
        with col3:
            st.image(lime_img, width=img_res, caption='LIME')
            st.image(lime_img2, width=img_res, caption='LIME2')
        # with col4:
        #     st.header('t-sne ex')
        #     st.image('data/imgs/T-SNE_Embedding_of_MNIST.png')

    with st.container():
        larger_res = 500
        st.header('Dataset level')
        st.image(tsne, width=larger_res, caption='t-SNE')
        st.image(pca, width=larger_res, caption='PCA')
        # col1, col2 = st.columns(2)
        # with col1:
        #     st.image(tsne, width=larger_res)
        # with col2:
        #     st.image(pca, width=larger_res)

    # load model and get prediction
    # note: need to remove this since it seems to be broken
    model = load_model(which=option)
    image_to_use = cv2.imread(img)

    # note: wtf
    # question: why is it not predicting turtle
    # todo: make it predict turtle
    #   if it works then add part where they add their own image...
    #   separate page??

    st.header('Model Prediction')
    probs = get_prediction(model, image_to_use)
    format_out = probs[0]

    # note: hardcode accuracy results since models arent working
    #   but need actual results first...
    #   train on like 0.3, val on 0.15, then test the rest
    out_shark = 'Shark probability: {:.4f}'.format(format_out[0])
    out_turtle = 'Turtle probability: {:.4f}'.format(format_out[1])
    # st.text_area(label=out_text, value=out_text)
    st.subheader(body=out_shark)
    st.subheader(body=out_turtle)


if __name__ == '__main__':
    main()