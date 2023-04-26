import streamlit as st
import os


IMG_SIZE = (224, 224)
# IMG_OPTIONS = ('shark0', 'elephant')
# todo: rename these to: 'great white', tiger, hammer, ..., some turtle, tiny turtle...
# todo: make sure you used the ones that are 224x224
IMG_OPTIONS = ('shark0', 'shark1', 'shark2', 'shark3',
               'turtle0', 'turtle1', 'turtle2', 'turtle3')

VIZ_METHOD = ('gc', 'sm', 'lime')

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

    option = st.sidebar.selectbox(label='Augmentation to apply', options=VIZ_METHOD)

    ############################
    # END OF SIDE BAR PORTION  #
    ############################

    ######################
    # MAIN SECTION START #
    ######################
    st.title('Comparison Across Different Augmentation Methods')

    # todo: map VIZ_METHOD to gc, sn, lime (in box show Grad-CAM, ...)

    if option == 'lime':
        base = os.path.join(DATA_PATH, option, 'baseline', '{}_{}.png'.format(option, input_image))
        blur = os.path.join(DATA_PATH, option, 'blur', '{}_{}.png'.format(option, input_image))
        drop = os.path.join(DATA_PATH, option, 'drop', '{}_{}.png'.format(option, input_image))
        emboss = os.path.join(DATA_PATH, option, 'emboss', '{}_{}.png'.format(option, input_image))
        gray = os.path.join(DATA_PATH, option, 'gray', '{}_{}.png'.format(option, input_image))
    else:

        # load image based on option: baseline, blur, drop, emboss, gray
        base = os.path.join(DATA_PATH, option, 'baseline', '{}_{}.png'.format(option, input_image))
        blur = os.path.join(DATA_PATH, option, 'blur', '{}_{}.png'.format(option, input_image))
        drop = os.path.join(DATA_PATH, option, 'drop', '{}_{}.png'.format(option, input_image))
        emboss = os.path.join(DATA_PATH, option, 'emboss', '{}_{}.png'.format(option, input_image))
        gray = os.path.join(DATA_PATH, option, 'gray', '{}_{}.png'.format(option, input_image))

        base_img = os.path.join(DATA_PATH, option, 'baseline', '{}_img_{}.png'.format(option, input_image))
        blur_img = os.path.join(DATA_PATH, option, 'blur', '{}_img_{}.png'.format(option, input_image))
        drop_img = os.path.join(DATA_PATH, option, 'drop', '{}_img_{}.png'.format(option, input_image))
        emboss_img = os.path.join(DATA_PATH, option, 'emboss', '{}_img_{}.png'.format(option, input_image))
        gray_img = os.path.join(DATA_PATH, option, 'gray', '{}_img_{}.png'.format(option, input_image))

    with st.container():
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.image(base, caption='base')
            if option != 'lime':
                st.image(base_img, caption='base')
        with col2:
            st.image(blur, caption='blur')
            if option != 'lime':
                st.image(blur_img, caption='blur')
        with col3:
            st.image(drop, caption='drop')
            if option != 'lime':
                st.image(drop_img, caption='drop')
        with col4:
            st.image(emboss, caption='emboss')
            if option != 'lime':
                st.image(emboss_img, caption='emboss')
        with col5:
            st.image(gray, caption='Gray')
            if option != 'lime':
                st.image(gray_img, caption='Gray')


if __name__ == '__main__':
    main()
