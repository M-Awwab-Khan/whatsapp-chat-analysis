from urlextract import URLExtract
from wordcloud import WordCloud
extractor = URLExtract()

def fetch_stats(selected_user, df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    num_messages = df.shape[0]
    num_words = 0
    num_media = df[df['message'] == '<Media omitted>\n'].shape[0]
    num_links = 0
    for msg in df['message']:
        num_links += len(extractor.find_urls(msg))
        num_words += len(msg.split())
    return num_messages, num_words, num_media, num_links

def most_active_users(df):
    active_users = df['user'].value_counts().head()
    proportion_active_users = round(df['user'].value_counts(normalize=True)*100, 2).reset_index().rename(columns={'index': 'name', 'user': 'percent'})
    return active_users, proportion_active_users

def create_wordcloud(selected_user, df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    wc = WordCloud(width=500,height=500,min_font_size=10,background_color='white')
    df_wc = wc.generate(df['message'].str.cat(sep=" "))
    return df_wc