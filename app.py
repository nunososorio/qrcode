import streamlit as st
import qrcode
from PIL import Image
import io
url = st.text_input('Enter the URL', 'https://reduce.streamlit.app/')
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img_byte_arr = io.BytesIO()
img.save(img_byte_arr, format='PNG')
img_byte_arr = img_byte_arr.getvalue()
st.image(img_byte_arr, caption='QR Code', use_column_width=True)
