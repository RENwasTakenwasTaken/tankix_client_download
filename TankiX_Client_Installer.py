import patoolib, os, shutil

# define and declare the values of variables, which are required to do the installation tasks

updated_yml = "---\ninitUrl: http://main.txrevive.com/TXServer/StateServer/config/init.yml\nstateUrl: http://135.125.181.45/TXServer/StateServer/state/tankixprod_state.yml\ncurrentClientVersion: master-48606"
install_dir = os.environ['USERPROFILE'] + "\AppData\Local\TankiX"

# extraction process

print("Extracting Files... (Part 1 of 2)\nFiles are being extracted at:", install_dir)

patoolib.extract_archive('TankiXOld.rar', outdir=install_dir)

print("Extraction Process Done. (Part 1 of 2)")

# configuration process

print("Configuring Server Files... (Part 1 of 2)")

with open(install_dir + "/TankiX/tankix_Data/config/clientlocal/startup/public.yml", "w") as file1:
    file1.write(updated_yml)

print("Configuration Process Done. (Part 1 of 2).\nPlease create an account in this older version of client. When done, simply close the window.\nIf you are facing issues, feel free to join the our Discord Community https://discord.gg/54xQD4xKYP (if not joined already), and acknowledge the Admins about it.")
print("Running Older Client for account creation...")

# run the old client for account creation

os.system('"' + install_dir + "/TankiX/tankix.exe" + '"')

# residual file removal process

acc_created = print("NOTE: THIS WOULD REMOVE YOUR OLDER CLIENT. ONLY PROCEED WHEN ACCOUNT CREATION IS A SURE THING.\nAnswer (Y) when you have created your account.")

while 1:
    if acc_created == "Y":
        shutil.rmtree(install_dir + "/TankiX")
        break
    # keep on looping until the user inputs the right key
    else:
        acc_created = input("Please enter 'Y' when done:")
        pass

# extraction process - 2

print("Extracting Files... (Part 2 of 2)")

patoolib.extract_archive('Tanki X NEW.zip', outdir=install_dir)

print("Extraction Process Done. (Part 2 of 2)")

# configuration process - 2

print("Configuring Server Files... (Part 2 of 2)")

with open(install_dir + "/TankiX/tankix_Data/config/clientlocal/startup/public.yml", "w") as file1:
    file1.write(updated_yml)

print("Configuration Process Done... (Part 2 of 2)")

# yay-we-did-it! process. running of the new tanki x client and enjoying the OG game

print("Briliant! Everything is set up and ready to go!")
print("Tanki X client is installed at: " + install_dir + "\TankiX\\tankix.exe.\nYou can also 'tankix' in the search bar and run the Client.\nMeet you at the battlefield. Fire at will!")
run_tankix = input("Run Tanki X Client now? (Y/N)")

while 1:
    if run_tankix == "Y":
        os.system('"' + install_dir + '/TankiX/tankix.exe' + '"')
        break
    else:
        break
    
