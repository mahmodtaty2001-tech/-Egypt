# --- القاعة الأولى: تمثال رمسيس الثاني ---
with قاعات_المتحف[0]:
    st.markdown("<h2>🗿 تمثال الملك رمسيس الثاني الضخم</h2>")
    
    # الرابط الجديد المحدث لتمثال رمسيس الثاني لتفادي خطأ 404
    st.components.v1.html(
        """
        <iframe title="Ramesses II" frameborder="0" allowfullscreen mozallowfullscreen="true" webkitallowfullscreen="true" allow="autoplay; fullscreen; xr-spatial-tracking" xr-spatial-tracking execution-while-out-of-viewport execution-while-not-rendered web-share width="100%" height="450" src="https://sketchfab.com/models/19ebca33e8394e0996843477f72f2d90/embed?autostart=1&ui_controls=1&ui_infos=0&ui_watermark=0"></iframe>
        """,
        height=450
    )
