import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_link = 'https://drive.google.com/uc?id=1dKZxapT3xLzOTOpy1LCyqctL8YEvzp4Y'
df = pd.read_csv(data_link)

rating_text_col = 'Rating text'

positive_keywords = {'Excellent': 'excellent', 'Good': 'very good', 'Average': 'good'}
negative_keywords = {'Average': 'average', 'Not Rated': 'not rated', 'Poor': 'poor'}

df['Positive Keywords Count'] = 0
df['Negative Keywords Count'] = 0

for keyword, synonym in positive_keywords.items():
    df[keyword] = df[rating_text_col].astype(str).str.lower().str.count(synonym)
    df['Positive Keywords Count'] += df[keyword]

for keyword, synonym in negative_keywords.items():
    df[keyword] = df[rating_text_col].astype(str).str.lower().str.count(synonym)
    df['Negative Keywords Count'] += df[keyword]

print("\nPositive Keywords Count:")
print(df[['Excellent', 'Good', 'Average']].sum().to_string(header=False))
print("\nNegative Keywords Count:")
print(df[['Average', 'Not Rated', 'Poor']].sum().to_string(header=False))

df['Review Length'] = df[rating_text_col].apply(lambda rating_text: len(str(rating_text).split()))
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['Review Length'], y=df['Aggregate rating'], color='skyblue', alpha=0.6)

plt.title('Review Length vs. Rating')
plt.xlabel('Review Length (Number of Words)')
plt.ylabel('Average Rating')
plt.show()

print("\nAverage Review Length:", df['Review Length'].mean())
