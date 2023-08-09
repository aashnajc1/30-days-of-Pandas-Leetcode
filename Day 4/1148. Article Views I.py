import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
  authors = views[views['author_id'] == views['viewer_id']]
  unique_authors = authors['author_id'].unique()
  unique_authors = sorted(unique_authors)
  result = pd.DataFrame({'id' : unique_authors})
  return result
