
# dfs_optimizer.py — value calculator for DFS picks

def optimize_dfs(df, salary_dict):
    df = df.copy()
    df['salary'] = df['player'].map(salary_dict).fillna(4000)
    df['value_score'] = df['HR_probability'] / df['salary']
    df = df.sort_values(by='value_score', ascending=False)
    return df[['player', 'HR_probability', 'salary', 'value_score']]
