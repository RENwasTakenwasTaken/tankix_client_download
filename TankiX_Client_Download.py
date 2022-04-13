import requests, patoolib, os, shutil, time
from tqdm import tqdm       # retrieving a function which has the same name as the module

updated_yml = "---\ninitUrl: http://135.125.181.45/TXServer/StateServer/config/init.yml\nstateUrl: http://135.125.181.45/TXServer/StateServer/state/tankixprod_state.yml\ncurrentClientVersion: master-48606"
install_dir = os.environ['USERPROFILE'] + "/Documents"

print("Downloading TankiX Clients...\n(NOTE: Download speeds may be slow even after having a high-speed network, since it depends upon the Server Load and its transfer speed.)")

# original file link - https://www.mediafire.com/file/4b3bu83lds39y07/TankiXOld.rar/file
url = 'https://download1348.mediafire.com/ncnz8vo0sexg/4b3bu83lds39y07/TankiXOld.rar'
r = requests.get(url, allow_redirects=True, stream=True)

total_size_in_bytes= int(r.headers.get('content-length', 0))
block_size = 8192
progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)

with open(install_dir + '/TankiXOld.rar', 'wb') as file:
    for data in r.iter_content(block_size):
        progress_bar.update(len(data))
        file.write(data)

progress_bar.close()

# original file link - https://www.mediafire.com/file/khmz0243jla8wei/TankiX-20210425T231314Z-001.zip/file
url = 'https://download734.mediafire.com/6irfrb2xryqg/khmz0243jla8wei/Tanki+X+NEW.zip'

r = requests.get(url, allow_redirects=True, stream=True)

total_size_in_bytes= int(r.headers.get('content-length', 0))
block_size = 8192
progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)

with open(install_dir + '/TankiXNEW.zip', 'wb') as file:
    for data in r.iter_content(block_size):
        progress_bar.update(len(data))
        file.write(data)

progress_bar.close()

if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
    print("ERROR, something went wrong")
    time.sleep(10)
    exit()

print("New Client Downloaded. (Part 2 of 2)")
print("Extracting Old-Client Files...")

patoolib.extract_archive(install_dir + '/TankiXOld.rar', outdir=install_dir)

print("Extraction Process Part 1 Done.")
print("Configuring Server Files Part 1...")

with open(install_dir + "/TankiX/tankix_Data/config/clientlocal/startup/public.yml", "w") as file1:
    file1.write(updated_yml)

print("Tanki X Old Client configured. Running Client...")

os.system('"' + 'C:/Users/Aryan Aich/Documents/TankiX/tankix.exe' + '"')

print("Please create an account in this older version client.")

acc_created = print("NOTE: THIS WOULD REMOVE YOUR OLDER CLIENT. ONLY PROCEED WHEN ACCOUNT CREATION IS SURE SORTED.\nAnswer (Y) when you have created your account.")

while 1:
    if acc_created == "Y":
        os.remove(install_dir + "/TankiXOld.rar")
        shutil.rmtree(install_dir + "/TankiX")
        break
    else:
        acc_created = input("Please enter 'Y' when done:")
        pass

print("Extracting New-Client Files...")

patoolib.extract_archive(install_dir + '/TankiXNEW.zip', outdir=install_dir)
os.remove(install_dir + "/TankiXNEW.zip")

with open(install_dir + "/TankiX/tankix_Data/config/clientlocal/startup/public.yml", "w") as file1:
    file1.write(updated_yml)

print("Tanki X New Client Server Files Configured.")
print("Briliant! Everything is set up and ready to go!")
run_tankix = input("Run Tanki X Client now? (Y/N)")

while 1:
    if run_tankix == "Y":
        os.system('"' + install_dir + '/TankiX/tankix.exe' + '"')
        break
    else:
        break

print("Tanki X client is installed at: " + install_dir + "\TankiX\\tankix.exe.\nYou can also 'tankix' in the search bar and run the Client.\nMeet you at the battlefield. Fire at will!")