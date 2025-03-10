import streamlit as st

# Set up the page configuration
st.set_page_config(page_title="Well Shop", layout="wide")

# CSS for styling the page
st.markdown("""
    <style>
        html, body, [class*="st-emotion-cache"] {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(to right, #F5EFE6, #EAE7DC);
        }

        .title {
            font-size: 40px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 30px;
            color: #333;
        }

        .banner {
            width: 100%;
            height: 600px;
            background: linear-gradient(135deg, #6a11cb, #2575fc);
            border-radius: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 3px 5px 15px rgba(0, 0, 0, 0.2);
            overflow: hidden;
            position: relative;
            margin-bottom: 40px;
        }

        .banner img {
            width: 800px;
            height: 600px;
            object-fit: cover;
            border-radius: 20px;
            opacity: 0.85;
        }

        .banner-text {
            position: absolute;
            font-size: 32px;
            font-weight: bold;
            color: white;
            text-shadow: 2px 2px 10px rgba(0, 0, 0, 0.5);
        }

        .subtitle {
            font-size: 26px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 20px;
            color: #444;
        }

        .product-box {
            width: 100%;
            max-width: 500px;
            height: auto;
            border-radius: 15px;
            box-shadow: 2px 4px 8px rgba(0, 0, 0, 0.1);
            padding: 15px;
            text-align: center;
            background: white;
            transition: transform 0.2s, box-shadow 0.2s;
            margin-bottom: 20px;
        }

        .product-box img {
            width: 100%;
            height: auto;
            object-fit: cover;
            border-radius: 10px;
        }

        .product-box:hover {
            transform: scale(1.05);
            box-shadow: 4px 6px 12px rgba(0, 0, 0, 0.2);
        }

        .product-name {
            font-size: 16px;
            font-weight: bold;
            margin-top: 10px;
        }

        .product-price {
            font-size: 14px;
            color: #E44D26;
            font-weight: bold;
        }

        .product-quantity {
            font-size: 14px;
            color: #444;
            margin-top: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# Store name
st.markdown("<div class='title'>Well Shop</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Middle-aged and senior consumers with high spending power and frequent purchases</div>", unsafe_allow_html=True)

# Hot-Deal
st.markdown("<div class='subtitle'>❄️ Winter Hot Deal ❄️</div>", unsafe_allow_html=True)
st.image("https://i.imgur.com/y0JPr9L.png", use_container_width=True)

# Product categories and their respective images with titles, quantity and price range
categories = {
   "Accessories 💎": [
    {"url": "https://i.imgur.com/cTGUlUo.png", "title": "Jewelry", "quantity": 58, "price_range": "10 - 200"},
    {"url": "https://i.imgur.com/a8zy6bi.png", "title": "Gloves", "quantity": 45, "price_range": "20 - 150"},
    {"url": "https://i.imgur.com/9CTL0E3.png", "title": "Sunglasses", "quantity": 45, "price_range": "30 - 180"},
    {"url": "https://i.imgur.com/FGI4Qp0.png", "title": "Scarf", "quantity": 44, "price_range": "15 - 120"},
    {"url": "https://i.imgur.com/Icryt0V.png", "title": "Belt", "quantity": 40, "price_range": "20 - 100"},
    {"url": "https://i.imgur.com/KwqErQ3.png", "title": "Handbag", "quantity": 36, "price_range": "50 - 200"}
    ],
    "Clothings 👔": [
        {"url": "https://i.imgur.com/e5bDb7f.png", "title": "Sweater", "quantity": 54, "price_range": "100 - 180"},
        {"url": "https://i.imgur.com/SGCYXEY.png", "title": "Dress", "quantity": 50, "price_range": "80 - 200"},
        {"url": "https://i.imgur.com/aTeg6mo.png", "title": "Blouse", "quantity": 49, "price_range": "50 - 150"},
        {"url": "https://i.imgur.com/Xkv6BzX.png", "title": "Shorts", "quantity": 49, "price_range": "30 - 120"},
        {"url": "https://i.imgur.com/Vb8y1Zh.png", "title": "Pants", "quantity": 48, "price_range": "60 - 150"},
        {"url": "https://i.imgur.com/IttHh9c.png", "title": "Shirt", "quantity": 45, "price_range": "40 - 120"}
    ],
    "Footwear 👞": [
        {"url": "https://i.imgur.com/2apmT1k.png", "title": "Boots", "quantity": 48, "price_range": "120 - 200"},
        {"url": "https://i.imgur.com/SU3x3Sk.png", "title": "Shoes", "quantity": 43, "price_range": "70 - 180"},
        {"url": "https://i.imgur.com/zyaufwn.png", "title": "Sneakers", "quantity": 38, "price_range": "90 - 150"},
        {"url": "https://i.imgur.com/xbuOmUc.png", "title": "Sandals", "quantity": 35, "price_range": "30 - 100"}
    ],
    "Outerwear 🧥": [
        {"url": "https://i.imgur.com/7Nqp15f.png", "title": "Coat", "quantity": 50, "price_range": "150 - 200"},
        {"url": "https://i.imgur.com/EK1jESH.png", "title": "Jacket", "quantity": 35, "price_range": "100 - 180"},
    ]
}

cols_per_row = 4  # Define the number of columns per row

for category, products in categories.items():
    st.markdown(f"<div class='subtitle'>{category}</div>", unsafe_allow_html=True)
    total_products = len(products)
    index = 0
    
    # Calculate number of full rows and remainder products for the last row
    full_rows = total_products // cols_per_row
    remainder_products = total_products % cols_per_row

    # Display full rows
    for _ in range(full_rows):
        col_group = st.columns(cols_per_row)  # Create a full row of columns
        for col in col_group:
            product = products[index]
            with col:
                st.markdown(f"""
                    <div class='product-box'>
                        <img src='{product["url"]}' alt='{product["title"]}'>
                        <div class='product-name'>{product["title"]}</div>
                        <div class='product-quantity'>Quantity: {product["quantity"]}</div>
                        <div class='product-price'>Price: {product["price_range"]}</div>
                    </div>
                """, unsafe_allow_html=True)
            index += 1

    # Display remainder row with adjusted column widths if needed
    if remainder_products > 0:
        # Create adjusted column width ratios to fill the row
        col_widths = [1] * remainder_products  # This ensures each column takes up equal space
        col_group = st.columns(col_widths)
        
        for i in range(remainder_products):
            product = products[index]
            with col_group[i]:
                st.markdown(f"""
                    <div class='product-box'>
                        <img src='{product["url"]}' alt='{product["title"]}'>
                        <div class='product-name'>{product["title"]}</div>
                        <div class='product-quantity'>Quantity: {product["quantity"]}</div>
                        <div class='product-price'>Price: {product["price_range"]}</div>
                    </div>
                """, unsafe_allow_html=True)
            index += 1
