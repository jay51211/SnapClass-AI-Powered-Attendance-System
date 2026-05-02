import streamlit as st


def subject_card(name, code, section, stats=None, footer_callback=None):

    stats_html = ""
    if stats:
        stats_html = "<div style='display:flex; gap:8px; flex-wrap:wrap; margin-top:14px;'>"
        for icon, label, value in stats:
            stats_html += f"""
                <div style='background:#00F0FF11; padding:6px 14px; border-radius:20px; font-size:0.85rem; color:#00F0FF; border: 1px solid #00F0FF33;'>
                    {icon} <b style='color:#FFFFFF;'>{value}</b> {label}
                </div>"""
        stats_html += "</div>"

    html = f"""
        <div style='
            background: #151522;
            border-left: 5px solid #00F0FF;
            padding: 20px 24px;
            border-radius: 16px;
            border: 1px solid #00F0FF44;
            box-shadow: 0px 0px 15px #00F0FF11;
            margin-bottom: 16px;
        '>
            <h3 style='margin:0 0 6px 0; color:#FFFFFF; font-size:1.3rem; font-family:Outfit, sans-serif; text-shadow: 0px 0px 5px #FFFFFF55;'>{name}</h3>
            <p style='color:#A0A0B0; margin:0; font-size:0.9rem; font-family:Outfit, sans-serif;'>
                Code: <span style='background:#FF005522; color:#FF0055; padding:2px 10px; border-radius:6px; font-weight:600; border: 1px solid #FF005555'>{code}</span>
                &nbsp;|&nbsp; Section: <span style='color:#E2E8F0;'>{section}</span>
            </p>
            {stats_html}
        </div>
    """

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()