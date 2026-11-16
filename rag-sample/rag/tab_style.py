import streamlit as st

# Apply custom styles to Streamlit tabs for a more polished and visually appealing dashboard.
# This module defines a function to apply custom CSS styles to Streamlit tabs.


# function to apply custom tab styles
def apply_tab_styles():
    # Inject custom CSS styles into the Streamlit app to enhance the appearance of tabs.
    """Apply custom CSS styles to Streamlit tabs."""
    # The styles include customizations for the tab navigation shell, tab buttons, active tab highlighting,
    # responsive adjustments for narrow screens, and adaptations for dark mode themes.
    return st.markdown(
        """
        <style>
        /* Tab navigation shell */
        .stTabs [data-baseweb="tab-list"] {
            display: flex;
            gap: 0.55rem;
            padding: 0.45rem;
            margin: 0.5rem 0 1.25rem;
            border: 1px solid rgba(100, 116, 139, 0.22);
            border-radius: 16px;
            background: linear-gradient(135deg, rgba(37, 99, 235, 0.10), rgba(6, 182, 212, 0.08));
            box-shadow: 0 8px 24px rgba(15, 23, 42, 0.08);
        }
        /* Tab buttons */
        .stTabs [data-baseweb="tab"] {
            flex: 1;
            justify-content: center;
            min-height: 3.15rem;
            padding: 0.45rem 1rem;
            border-radius: 11px;
            color: #64748b;
            font-size: 0.98rem;
            font-weight: 700;
            transition: all 180ms ease;
        }
        .stTabs [data-baseweb="tab"]:hover {
            color: #2563eb;
            background: rgba(255, 255, 255, 0.62);
            transform: translateY(-1px);
        }
        /* Active tab */
        .stTabs [aria-selected="true"] {
            color: #1d4ed8;
            background: rgba(255, 255, 255, 0.96);
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.18);
        }
        .stTabs [data-baseweb="tab-highlight"] {
            height: 3px;
            border-radius: 3px;
            background: linear-gradient(90deg, #2563eb, #06b6d4);
        }
        /* Keep the layout comfortable on narrow screens and dark themes. */
        @media (max-width: 640px) {
            .stTabs [data-baseweb="tab"] {
                min-height: 2.8rem;
                padding: 0.35rem 0.45rem;
                font-size: 0.78rem;
            }
        }
        @media (prefers-color-scheme: dark) {
            .stTabs [data-baseweb="tab-list"] {
                background: linear-gradient(135deg, rgba(37, 99, 235, 0.20), rgba(6, 182, 212, 0.14));
            }
            .stTabs [aria-selected="true"] {
                color: #93c5fd;
                background: rgba(30, 41, 59, 0.92);
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
