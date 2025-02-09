from plot_charts import plot_and_save_charts
import matplotlib.pyplot as plt

def main():
    # Create a figure
    fig = plt.figure(figsize=(18, 6))

    # Set the title for the figure
    fig.suptitle('EmotionCat', fontsize=20, fontweight='bold')

    # Call the plotting function
    plot_and_save_charts(fig)

    # Show the plot
    plt.show()

if __name__ == "__main__":
    main()
