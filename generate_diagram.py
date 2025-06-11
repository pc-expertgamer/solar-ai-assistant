# generate_diagram.py

import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Removed unused imports (numpy, pandas) for cleaner code.

def create_architecture_diagram():
    """
    Generates and saves the system architecture diagram for the solar analysis project.
    """
    fig, ax = plt.subplots(figsize=(14, 10))

    # Define colors for consistency
    primary_color = '#1f77b4'    # Data Sources
    secondary_color = '#ff7f0e'  # AI Processing
    tertiary_color = '#2ca02c'   # Analysis Engine
    quaternary_color = '#d62728' # Output Layer

    # --- Draw Components ---
    # Data Sources Layer
    ax.add_patch(patches.Rectangle((0.5, 8), 2.5, 1.5, facecolor=primary_color, alpha=0.7, edgecolor='black'))
    ax.text(1.75, 8.75, 'Satellite Imagery\n(User Upload)', ha='center', va='center', fontsize=10, fontweight='bold', color='white')

    ax.add_patch(patches.Rectangle((3.5, 8), 2.5, 1.5, facecolor=primary_color, alpha=0.7, edgecolor='black'))
    ax.text(4.75, 8.75, 'User Context\n(Location, Cost)', ha='center', va='center', fontsize=10, fontweight='bold', color='white')

    # AI Processing Layer
    ax.add_patch(patches.Rectangle((2.5, 5.5), 4, 2, facecolor=secondary_color, alpha=0.7, edgecolor='black'))
    ax.text(4.5, 6.5, 'Vision AI Analysis\n(OpenRouter - Claude 3 Haiku)', ha='center', va='center', fontsize=12, fontweight='bold', color='white')

    # Application Layer
    ax.add_patch(patches.Rectangle((2.5, 3.5), 4, 1.5, facecolor=tertiary_color, alpha=0.7, edgecolor='black'))
    ax.text(4.5, 4.25, 'Backend & UI\n(Python & Streamlit)', ha='center', va='center', fontsize=11, fontweight='bold', color='white')

    # Output Layer
    ax.add_patch(patches.Rectangle((0.5, 1.5), 9, 1.5, facecolor=quaternary_color, alpha=0.7, edgecolor='black'))
    ax.text(5, 2.25, 'Solar Potential Report | ROI Analysis | Installation Recommendations', ha='center', va='center', fontsize=11, fontweight='bold', color='white')

    # --- Add Arrows for Data Flow ---
    arrow_props = dict(arrowstyle='->', lw=2.5, color='black')

    # From Data Sources to AI
    ax.annotate('', xy=(3.5, 7.5), xytext=(2.75, 8), arrowprops=arrow_props)
    ax.annotate('', xy=(5.5, 7.5), xytext=(5.25, 8), arrowprops=arrow_props)
    
    # From AI to Application
    ax.annotate('', xy=(4.5, 5.0), xytext=(4.5, 5.5), arrowprops=arrow_props)

    # From Application to Output
    ax.annotate('', xy=(5, 3.0), xytext=(4.5, 3.5), arrowprops=arrow_props)

    # --- Final Touches ---
    ax.set_title('Solar AI Assistant - System Architecture', fontsize=16, fontweight='bold', pad=20)

    # Set axis limits and remove axes for a clean look
    ax.set_xlim(0, 10)
    ax.set_ylim(1, 10.5)
    ax.set_aspect('equal', adjustable='box')
    ax.axis('off')

    plt.tight_layout()
    # Save the figure with a white background
    plt.savefig('solar_system_architecture.png', dpi=300, bbox_inches='tight', facecolor='white')
    print("Diagram 'solar_system_architecture.png' saved successfully.")
    plt.show()


# It's good practice to wrap script execution in a main guard.
if __name__ == "__main__":
    create_architecture_diagram()