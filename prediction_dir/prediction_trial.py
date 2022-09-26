import streamlit as st
from PIL import Image
import numpy as np

# import tensorflow as tf for predicting with model #! no model as it's not trainable on local machine atm

"""
# Markdown will be rendered if provided between `triple quotes`  
```py
import numpy as np
arr=np.random.randint(5)
print(arr)
```

To run application as streamlit
```py
streamlit run ./file/path.py
```
"""
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:

    image = Image.open(uploaded_file)
    img = image.resize((224, 224))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)  # [batch_size, row, col, channel]
    # result = model.predict(img_array) # [[0.99, 0.01], [0.99, 0.01]]

    # argmax_index = np.argmax(result, axis=1) # [0, 0]
    # if argmax_index[0] == 0:
    # st.image(image, caption="predicted: cat")
    # else:
    # st.image(image, caption='predicted: dog')
    st.image(image, caption="predicted: dog")

# uploaded_file = st.file_uploader("Choose Image", accept_multiple_files=True)
# uploaded_file_list = []
# if uploaded_file:
#     st.button("Bleh")
#     for file_path in uploaded_file:
#         uploaded_file_list.append(Image.open(file_path))
#     st.image(uploaded_file_list)
