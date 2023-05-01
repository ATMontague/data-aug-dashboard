import streamlit as st
import os
import random

from utils import IMG_OPTIONS, IMG_NAME_MAP, IMG_SIZE

DATA_PATH = 'data/SharksAndTurtles'
VIZ_METHOD = ('Grad-CAM', 'Saliency Map', 'LIME (positive)', 'LIME (negative)')

VIZ_MAP = {
    'Grad-CAM': 'gc',
    'Saliency Map': 'sm',
    'LIME (positive)': 'lime',
    'LIME (negative)': 'lime2',
}


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

    # option = st.sidebar.selectbox(label='Augmentation to apply', options=VIZ_METHOD)
    opt = st.sidebar.selectbox(label='Visualization Method', options=VIZ_METHOD)

    option = VIZ_MAP[opt]


    ############################
    # END OF SIDE BAR PORTION  #
    ############################

    ######################
    # MAIN SECTION START #
    ######################
    st.title('Comparison Across Different Augmentation Methods')


    # todo: move this into other one and remove if/else statement
    if option == 'LIME (positive)' or option == 'LIME (negative)':
        base = os.path.join(DATA_PATH, option, 'baseline', '{}_{}.png'.format(option, img_name))
        blur = os.path.join(DATA_PATH, option, 'blur', '{}_{}.png'.format(option, img_name))
        drop = os.path.join(DATA_PATH, option, 'drop', '{}_{}.png'.format(option, img_name))
        emboss = os.path.join(DATA_PATH, option, 'emboss', '{}_{}.png'.format(option, img_name))
        gray = os.path.join(DATA_PATH, option, 'gray', '{}_{}.png'.format(option, img_name))
    else:

        # load image based on option: baseline, blur, drop, emboss, gray
        base = os.path.join(DATA_PATH, option, 'baseline', '{}_{}.png'.format(option, img_name))
        blur = os.path.join(DATA_PATH, option, 'blur', '{}_{}.png'.format(option, img_name))
        drop = os.path.join(DATA_PATH, option, 'drop', '{}_{}.png'.format(option, img_name))
        emboss = os.path.join(DATA_PATH, option, 'emboss', '{}_{}.png'.format(option, img_name))
        gray = os.path.join(DATA_PATH, option, 'gray', '{}_{}.png'.format(option, img_name))

        base_img = os.path.join(DATA_PATH, option, 'baseline', '{}_img_{}.png'.format(option, img_name))
        blur_img = os.path.join(DATA_PATH, option, 'blur', '{}_img_{}.png'.format(option, img_name))
        drop_img = os.path.join(DATA_PATH, option, 'drop', '{}_img_{}.png'.format(option, img_name))
        emboss_img = os.path.join(DATA_PATH, option, 'emboss', '{}_img_{}.png'.format(option, img_name))
        gray_img = os.path.join(DATA_PATH, option, 'gray', '{}_img_{}.png'.format(option, img_name))

    # todo: add other lime option
    with st.container():
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            if option == 'gc' or option == 'sm':
                st.image(base, caption='No Augmentation')
                st.image(base_img, caption='No Augmentation')
            else:
                st.image(base, caption='No Augmentation')
            # st.image(base, caption='base')
            # if option != 'lime':
            #     st.image(base_img, caption='No Augmentation')
        with col2:
            if option == 'gc' or option == 'sm':
                st.image(blur, caption='Blur')
                st.image(blur_img, caption='Blur')
            else:
                st.image(blur, caption='Blur')
            # if option != 'lime':
            #     st.image(blur_img, caption='Blur')
        with col3:
            if option == 'gc' or option == 'sm':
                st.image(drop, caption='Drop')
                st.image(drop_img, caption='Drop')
            else:
                st.image(drop, caption='Drop')
            # st.image(drop, caption='Drop')
            # if option != 'lime':
            #     st.image(drop_img, caption='Drop')
        with col4:
            if option == 'gc' or option == 'sm':
                st.image(emboss, caption='Emboss')
                st.image(emboss_img, caption='Emboss')
            else:
                st.image(emboss, caption='Emboss')
            # st.image(emboss, caption='Emboss')
            # if option != 'lime':
            #     st.image(emboss_img, caption='Emboss')
        with col5:
            if option == 'gc' or option == 'sm':
                st.image(gray, caption='Gray')
                st.image(gray_img, caption='Gray')
            else:
                st.image(gray, caption='Gray')
            # st.image(gray, caption='Gray')
            # if option != 'lime':
            #     st.image(gray_img, caption='Gray')


if __name__ == '__main__':
    main()
