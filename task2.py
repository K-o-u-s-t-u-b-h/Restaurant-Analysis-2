import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_link = 'https://drive.google.com/uc?id=1dKZxapT3xLzOTOpy1LCyqctL8YEvzp4Y'
df = pd.read_csv(data_link)

votes_col = 'Votes'
rating_col = 'Aggregate rating'
restaurant_name_col = 'Restaurant Name'

highest_votes_restaurant = df.loc[df[votes_col].idxmax(), restaurant_name_col]
lowest_votes_restaurant = df.loc[df[votes_col].idxmin(), restaurant_name_col]
print(f"Restaurant with the Highest Number of Votes: {highest_votes_restaurant} ({df[votes_col].max()} votes)")
print(f"Restaurant with the Lowest Number of Votes: {lowest_votes_restaurant} ({df[votes_col].min()} votes)")

print("The correlation between the number of votes and the rating of a restaurant can be displayed by plotting a scatter graph of Number of Votes against Average Rating.")

plt.figure(figsize=(10, 6))
sns.scatterplot(x=df[votes_col], y=df[rating_col], color='coral', alpha=0.6)
plt.title('Number of Votes vs. Average Rating')
plt.xlabel('Number of Votes')
plt.ylabel('Average Rating')
plt.show()
