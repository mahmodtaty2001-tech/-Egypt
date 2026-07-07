"""
sketchfab_helper.py
مساعد بسيط للتعامل مع API الخاص بـ Sketchfab (بحث فقط)
يتطلب Sketchfab API token لاستخدام بعض النقاط النهائية إذا لزم.

ملاحظة: هذا السكربت لا يقوم بتنزيل نماذج محمية أو مخترقة الترخيص.
"""

import os
import requests

SKETCHFAB_SEARCH_URL = "https://api.sketchfab.com/v3/search"


def search_models(query, token=None, type_filter='models', license_filter=None, page=1, page_size=10):
    """
    البحث عن نماذج في Sketchfab.
    - query: نص البحث
    - token: (اختياري) توكن API لSketchfab. إن لم يُعطَ فسيتم محاولة طلب عام (قد يقيّد النتائج).
    - type_filter: عادة 'models'
    - license_filter: "cc0", "cc-by", "cc-by-sa", "all" إلخ.
    """
    params = {
        'type': type_filter,
        'q': query,
        'page': page,
        'downloadable': 'true',
        'staffpicked': 'false',
        'page_size': page_size,
    }
    if license_filter:
        params['license_type'] = license_filter

    headers = {}
    if token:
        headers['Authorization'] = f"Bearer {token}"

    resp = requests.get(SKETCHFAB_SEARCH_URL, params=params, headers=headers)
    resp.raise_for_status()
    return resp.json()


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Search Sketchfab for models (simple helper)')
    parser.add_argument('query', help='Search query, e.g., "ancient egypt"')
    parser.add_argument('--token', help='Sketchfab API token (optional)')
    parser.add_argument('--page', type=int, default=1)
    args = parser.parse_args()

    token = args.token or os.environ.get('SKETCHFAB_TOKEN')
    res = search_models(args.query, token=token, page=args.page)

    print(f"Found: {res.get('count', 'unknown')}")
    for i, item in enumerate(res.get('results', []), 1):
        uid = item.get('uid') or item.get('id')
        name = item.get('name')
        user = item.get('user', {}).get('displayName')
        downloadable = item.get('isDownloadable', False) or item.get('downloadable', False)
        license_name = item.get('license', {}).get('name') if item.get('license') else None
        print(f"{i}. {name} (id={uid}) by {user} | downloadable={downloadable} | license={license_name}")
