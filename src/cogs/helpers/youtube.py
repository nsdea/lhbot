import os

from dotenv import load_dotenv
from pyyoutube import Api

load_dotenv()

api = Api(
    # client_id=os.getenv('YOUTUBE_ID'),
    api_key=os.getenv('YOUTUBE_KEY')
)

# API RATELIMIT NOTES
# 10.000 Quotas / day

def channel_data() -> dict:
    channel_by_id = api.get_channel_info(channel_id='UCe4PsvZK8Tdn1R3M-j-bqOQ')
    full_data = channel_by_id.items[0].to_dict()

    return_data = {
        'subs': full_data['statistics']['subscriberCount'],
        'views': full_data['statistics']['viewCount'],
        'videos': full_data['statistics']['videoCount'],
    }
    
    return return_data

if __name__ == '__main__':
    print(channel_data())