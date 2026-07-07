"""
fetch_models.py
أداة سطر أوامر مساعدة لاختبار البحث على Sketchfab عبر sketchfab_helper.
"""

from sketchfab_helper import search_models
import os


def main():
    query = os.environ.get('SF_QUERY', 'ancient egypt')
    token = os.environ.get('SKETCHFAB_TOKEN')
    res = search_models(query, token=token, page=1)
    print('Results:')
    for item in res.get('results', []):
        print('-', item.get('name'), '|', item.get('uid') if 'uid' in item else item.get('id'))


if __name__ == '__main__':
    main()
