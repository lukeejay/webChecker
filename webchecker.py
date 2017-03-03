import argparse
import urllib.request
import simpleaudio as sa



def main(url):
    wave_obj = sa.WaveObject.from_wave_file("cheer.wav")



    try:
        if (urllib.request.urlopen(url).getcode() == 200):
            play_obj = wave_obj.play()
            play_obj.wait_done()
    except IOError:
        print("NotFound")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'url', help='Url wanting to be checked')
    args = parser.parse_args()
    main(args.url)
