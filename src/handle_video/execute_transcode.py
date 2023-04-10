import subprocess
import time
from functools import wraps

urls = ['https://10.0.62.21/source/Digital Production Studio 6/DPS Projects/Viral POV Series/POV Amir Go 2.mp4',
        'https://10.0.62.21/source/Digital Production Studio 6/DPS Projects/Viral POV Series/POV Billy Perry MTB in NYC.mp4',
        'https://10.0.62.21/source/Content Collection 5/ONEX2/Cycling Related/210901 [Cycling Related] ONE X2 Alex21081201/Safa on Las Flores for Insta360 YT.mp4c for Insta360 YT.mp4',
        'https://10.0.62.21/source/Digital Production Studio 6/DPS Projects/Viral POV Series/POV Breathtaking Cruising Through the Deadly North Wall.mp4',
        'https://10.0.62.21/source/Digital Production Studio 6/DPS Projects/X3 Footage/Andras/220814_AndrasRa_Paris_Insta360_X3_4K_Preview.mp4',
        'https://10.0.62.21/source/Digital Production Studio 6/DPS Projects/X3 Footage/ES-Dons Cliff Jumping/Es_dons x Insta360/Cliff Cruise Edit 16x9 v2_2.00x_3840x2160_amq-12.mp4',
        'https://10.0.62.21/source/Digital Production Studio 6/X3 Launch Assets/Showcases/Moto360/MOTO360 4K with en endcard.mp4',
        'https://10.0.62.21/source/Digital Production Studio 6/X3 Launch Assets/Showcases/Claire&Peter/Claire&Peter YT with EN subcard.mp4',
        'https://10.0.62.21/source/Digital Production Studio 6/DM Campaigns/RS 1-Inch 360/1-Inch 360 Showcases/Carchase/Exports/Car chase EN 16-9 end + Sub card_3.mp4',
        'https://10.0.62.21/source/Digital Production Studio 6/DM Campaigns/RS 1-Inch 360/1-Inch 360 Showcases/Outdoor Videography/Exports/Ourdoors_Colored_Master Youtube version.mp4',
        'https://10.0.62.21/source/Digital Production Studio 6/DM Campaigns/RS 1-Inch 360/1-Inch 360 Showcases/Virtual Tour/Exports/Virtual Tour EN 16-9 4k - 80.mp4',
        'https://10.0.62.21/source/Digital Production Studio 6/DM Campaigns/RS 1-Inch 360/1-Inch 360 Showcases/Aki From Japan/Exports/16*9/hyperlapse 1-inch YT Endcard + Subcard.mp4',
        'https://10.0.62.21/source/rsTemp/Sphere%20Showcase%20-%20Winga/Showcase%20%20-%20Original/Winga%20showcase%20EN%204k.mp4',
        'https://10.0.62.21/source/rsTemp/Sphere%20Cbenfey/1x%20Full%20YT%20Making%20of%20Video/All%204/All4_D2.1.mp4',
        'https://10.0.62.21/source/Digital%20Production%20Studio%206/DPS%20Projects/V%235229%20Gimbal%20Guru%20Bullet%20Time%20YT%20Post-Editing/V%235229%20Gimbal%20Guru%20Bullet%20Time.mp4',
        'https://10.0.62.21/source/Digital%20Production%20Studio%206/DPS%20Projects/V%235236%20Luke%20Edwin%20Freeze%20Frame%20tutorial/V%235236%20Luke%20Edwin%20Freeze%20Frame%20tutorial.mp4',
        'https://10.0.62.21/source/Digital%20Production%20Studio%206/DPS%20Projects/V%235193%20Jordi%207%20creative%20shots%20YT%20Post-Editing/Export/V%235193%20Jordi%207%20creative%20shots%20YT%20Post-Editing%2002%20%EF%BC%88subcard%20altered%29.mp4',
        'https://10.0.62.21/source/Digital%20Production%20Studio%206/DPS%20Projects/V%235188%20Gimbal%20Guru%209%20Tricks%20YT%20Post-editing/V%235188%20Gimbal%20Guru%209%20Tricks%20YT%20Post-editing.mp4']

command = "ffmpeg -y -i '%s' -vcodec libx264 -crf 26 -g 29.9 -maxrate 8M -bufsize 16M -pass 1 -acodec aac -f mp4 '%s'"


def find_nth_occurrence(s, char, n) -> int:
    i = -1
    for _ in range(n):
        i = s.find(char, i + 1)
        if i == -1:
            return -1
    return i


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f'Total elapsed time: {round(elapsed_time, 2)}s')
        return result

    return wrapper


@timer
def main():
    with open('result.txt', 'w') as f:
        for url in urls:
            file_path = url[find_nth_occurrence(url, '/', 3):]
            file_name = file_path[file_path.rfind('/') + 1:]
            status = subprocess.getstatusoutput(command % (url, file_name))
            if status[0] == 0:
                print('%s: DONE!' % file_name)
            else:
                print('%s: FAILED!' % file_name)
                f.write('[ERROR] file_path is %s' % file_path + '\n' + status[1] + '\n\n')
        print('======= WELL DONE ========')


main()
