import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Create a random dataset
df = np.random.randn(30, 30)

# Customize the color palette in a diverging heatmap
fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(12, 3))
sns.heatmap(df, vmin=0, vmax=1, ax=axs[0])
axs[0].set_title('Default heatmap with range 0 to 1')
sns.heatmap(df, vmin=0.5, vmax=1, ax=axs[1])
axs[1].set_title('Dark heatmap with range 0.5 to 1')
sns.heatmap(df, vmin=0, vmax=0.5, ax=axs[2])
axs[2].set_title('Light heatmap with range 0 to 0.5')
plt.show()
