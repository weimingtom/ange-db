# -*- coding: utf-8 -*-
import os.path
import time
import requests
_CARD_URL = 'http://web.ange-app.com/ange/card/UserCardCollectionDetailPage?cid={0}'


def is_available(html_text):
    return len(html_text) > 20 * 1024


def do_crawl(start_id, end_id):
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_1 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Mobile/11D201',
        'F4S_CLIENT_VER': '1.0.3',
        'F4S_DL_VERSION': 21,
        'F4S_IOS_NOAHID': 0,
        'F4S_IOS_PLATFORM': 'iPhone6,1',
        'F4S_IOS_USER_ID': '9326413E-F153-42E5-BCDB-7524FF2E777F',
        'Referer': 'http://web.ange-app.com/ange/card/UserCardCollectionPage',
        'X-iOS-WebView-Response-Check': 1,
    }
    for card_id in range(start_id, end_id + 1):
        crawled_path = '../_crawled/{0}.html'.format(card_id)
        if os.path.exists(crawled_path):
            print('skipped: {0}'.format(card_id))
            continue

        res = requests.get(_CARD_URL.format(card_id), headers=headers, allow_redirects=False)
        if is_available(res.text):
            with open(crawled_path, 'w') as f:
                f.write(res.text)
                print('crawled: {0}'.format(card_id))

        time.sleep(1)


if __name__ == '__main__':
    do_crawl(1000, 1290)
