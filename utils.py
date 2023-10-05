from bs4 import BeautifulSoup
from mastodon import Mastodon
from networkx import all_shortest_paths
def extract_mastodon(mastodon, topics : list): 
    # 定义要收集的话题
    Authors = []
    Contents = []
    Created_at = []
    # 收集每个话题的相关帖子
    for topic in topics:
        # 使用Mastodon API搜索相关帖子
        results = mastodon.timeline_hashtag(hashtag=topic, limit =100)  # 每个话题最多获取100条帖子

        # 处理搜索结果
        for status in results:
            # 可以在这里提取有关帖子的信息，如作者、内容、时间等
            author = status["account"]["username"]
            content = status["content"]
            created_at = status["created_at"]

            # 将信息存储到列表中

            Authors.append(author)
            Contents.append(content)
            Created_at.append(created_at)
            # 在这里进行数据存储或其他分析操作


    
    # 完成后的数据处理代码放在这里
    return Authors, Contents, Created_at
def treat_contents(Contents):
    all_text = []
    all_hashtags = []
    for lines in Contents:
        lines.replace('<p>', '')
    
    for html_string in  Contents:
        # Parse the HTML
        soup = BeautifulSoup(html_string, 'html.parser')

        # Extract the text content
        text_content = soup.get_text(strip=True, separator=' ')
        all_text.append(text_content)

        # Extract hashtags
        hashtags = [a.text for a in soup.find_all('a', class_='mention hashtag')]
        all_hashtags.append(hashtags)


    return all_text, all_hashtags



