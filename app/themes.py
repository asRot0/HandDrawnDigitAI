# Define themes as a dictionary
themes = {
    "pink_black": {
        "text_colors": ['#FF007F', '#000000'],
        "bg_colors": ['#FFC0CB', '#F5F5F5'],
        "hover_colors": ['#FF66B2', '#E6E6E6']  # Light pink hover
    },
    "black_pink": {
        "text_colors": ['#000000', '#F5F5F5'],
        "bg_colors": ['#FFC0CB', '#000000'],
        "hover_colors": ['#FFB6C1', '#333333']  # Subtle dark hover effect
    },
    "dark_mode": {
        "text_colors": ['#00FF00', '#FFD700'],
        "bg_colors": ['#333333', '#444444'],
        # Adding low light hover effects: darker background for hover
        "hover_colors": ['#222222', '#555555']  # Darker shades of background for hover
    },
    "oceanic": {
        "text_colors": ['#1E90FF', '#00CED1'],
        "bg_colors": ['#E0FFFF', '#B0E0E6'],
        # Slightly darker hover shades for better visual contrast
        "hover_colors": ['#B0E0E6', '#A9D0D3']  # Lighter blue hover effect
    },
    "corporate": {
        "text_colors": ['#2C3E50', '#E74C3C'],  # Professional blue and red
        "bg_colors": ['#D9E2E8', '#BDC3C7'],  # Subtle light gray-blue for better contrast
        "hover_colors": ['#C5D1D8', '#A5B3B9']  # Slightly darker shades for hover
    },
    "vibrant": {
        "text_colors": ['#FF4500', '#32CD32'],
        "bg_colors": ['#FFFFE0', '#FFDAB9'],
        # Light shade hover effects
        "hover_colors": ['#FFD700', '#FF8C00']  # Slightly deeper shades for hover
    },
    # New themes
    "neon": {
        "text_colors": ['#39FF14', '#F5A623'],
        "bg_colors": ['#222222', '#333333'],
        # Neon glow hover effect with a darker background
        "hover_colors": ['#1A1A1A', '#2A2A2A']  # Darker backgrounds on hover for neon effect
    },
    "pastel_sunset": {
        "text_colors": ['#F4A300', '#FF58A3'],
        "bg_colors": ['#F3D5B5', '#FFD1E1'],
        # Pastel colors with hover effects that darken the background
        "hover_colors": ['#F6C51F', '#FF6FA1']  # Darker pastel hover
    },
    "retro": {
        "text_colors": ['#FF6347', '#FFD700'],
        "bg_colors": ['#FFFACD', '#FAF0E6'],
        # Retro theme hover effect for subtle interaction
        "hover_colors": ['#FF7F50', '#FFB6C1']  # A warm hover effect
    },
    "cyberpunk": {
        "text_colors": ['#8A2BE2', '#00FFFF'],
        "bg_colors": ['#282828', '#404040'],
        # Dark hover effect to fit cyberpunk aesthetics
        "hover_colors": ['#1A1A1A', '#333333']  # Deep dark hover for a cyberpunk feel
    },
    "forest": {
        "text_colors": ['#228B22', '#32CD32'],
        "bg_colors": ['#98FB98', '#8FBC8F'],
        # Earthy hover effect to reflect the forest theme
        "hover_colors": ['#006400', '#3CB371']  # Darker green hover effect
    },
    "galaxy": {
        "text_colors": ['#B0E0E6', '#8A2BE2'],
        "bg_colors": ['#1E1E2F', '#4B0082'],
        # Lighter shade of dark background for the galaxy hover
        "hover_colors": ['#2E2E3E', '#5A4D8E']  # Darker, space-themed hover effect
    }
}
