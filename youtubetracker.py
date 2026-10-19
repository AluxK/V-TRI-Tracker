from googleapiclient.discovery import build
import JSONUtil as JSON

# Instantiate connection to the Google API system
# FOR DEBUG ONLY, RECONFIGURE BEFORE RELEASE
api_key = ' '

youtube = build('youtube', 'v3', developerKey=api_key)
files = JSON.check_for_files()[1]


def prepare_data(response):
    data = []

    for x in response['items']:
        TEMP_data = {'pageToken': response['nextPageToken'], 'indexedStreamer': None}
        TEMP_indented_index = {'channelName': x['snippet']['channelTitle'], 'channelID': x['id']['channelId'],
                               'creationDate': x['snippet']['publishedAt'],
                               'thumbnailURL': x['snippet']['thumbnails']['high']['url']}
        TEMP_data['indexedStreamer'] = TEMP_indented_index
        print(TEMP_data)
        data.append(TEMP_data)
        print(data)
    return data

    # total_results = response['pageInfo']['totalResults']
    # print('Amount of Accounts which fits the search quarry: ' + str(total_results))
    # print('Next Page Token: ' + response['nextPageToken'])
    # print(response)
    # for x in response['items']:
    #    print('Account Name: ' + x['snippet']['channelTitle'])
    #    print('Channel ID: ' + x['id']['channelId'])
    #    print('Channel Published on: ' + x['snippet']['publishedAt'])
    #    print('Thumbnail: ' + x['snippet']['thumbnails']['high']['url'])
    #    print('Time of creation: ' + x['snippet']['publishedAt'])


def run_YT_Search():
    if not files:
        request = youtube.search().list(
            safeSearch='none',
            part='snippet',
            order='date',
            q='V-Tuber|VTuber|Virtual_YouTuber -archive|clip|VOD|playbacks|music|clips',
            type='channel',
            maxResults=50
        )
    else:
        newest_file = JSON.find_newest_datafile(files)
        page_token = newest_file[-1]['pageToken']
        print(page_token)
        latest_date = newest_file[-1]['indexedStreamer']['creationDate']
        print(latest_date)
        request = youtube.search().list(
            safeSearch='none',
            pageToken=page_token,
            part='snippet',
            order='date',
            q='V-Tuber|VTuber|Virtual YouTuber -archive|clip|VOD',
            type='channel',
            maxResults=50
        )
    response = request.execute()
    youtube.close()
    print(response)
    data = prepare_data(response)
    JSON.new_json_file(data, 'Youtube')

while True:
    run_YT_Search()
