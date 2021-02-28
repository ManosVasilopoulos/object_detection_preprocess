import pymediainfo
from pprint import pprint

if __name__ == '__main__':
    file_path = 'C:\\Users\\emmanouil.vasilopoul\\Documents\\i-SENSE\\Effector\\Datasets\\Detection\\SEAGULL\\inputs\\videos\\Complete\\visible\\bigShipHighAlt_clip1.mp4'

    media_info = pymediainfo.MediaInfo.parse(file_path)

    for track in media_info.tracks:
        for key in track.__dict__.keys():
            try:
                if key == 'track_type':
                    print('\n-', key + ':', track.__dict__[key])
                else:
                    print(key + ':', track.__dict__[key])

            except:
                pass
