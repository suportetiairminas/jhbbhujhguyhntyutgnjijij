import subprocess
import os

teste = subprocess.check_output('''powershell -Command "ipconfig /all"''',shell=True, encoding="CP1252", errors="replace")#ip
impre = subprocess.check_output('''powershell -Command "Get-Printer | Select-Object Name , DriverName , PortName"''',shell=True,  encoding="CP1252", errors="replace")#impressora

cmd = (
    'powershell -NoProfile -Command '
    '"$os=Get-CimInstance Win32_OperatingSystem; '
    '$cs=Get-CimInstance Win32_ComputerSystem; '
    '$cpu=Get-CimInstance Win32_Processor; '
    '$disk=Get-CimInstance Win32_LogicalDisk -Filter \\"DeviceID=\'C:\'\\"; '
    '[PSCustomObject]@{'
    '\'Versão do Windows\'=\\"$($os.Caption) $($os.Version)\\"; '
    '\'Memória RAM (GB)\'=[math]::Round($cs.TotalPhysicalMemory/1GB,2); '
    '\'Tipo de Sistema\'=$os.OSArchitecture; '
    '\'Modelo do PC\'=$cs.Model; '
    '\'Processador\'=$cpu.Name; '
    '\'Disco Total C: (GB)\'=[math]::Round($disk.Size/1GB,2); '
    '\'Disco Livre C: (GB)\'=[math]::Round($disk.FreeSpace/1GB,2)'
    '}"'
)#resto

telas = subprocess.check_output(cmd, shell=True, encoding="CP1252", errors="replace")#executa

pasta = os.path.expanduser("~/")+"Downloads"

arquivo = os.path.join(pasta, "informacao_para_nilson.txt")#cria o arquivo informacao_para_nilson.txt
# Abra o arquivo em modo de escrita e insira o texto
with open(arquivo, "w", encoding="CP1252") as f:#coloca o texo no arquivo
    f.write("infos gerais:")
    f.write(telas)
    f.write("confg ip:")
    f.write(teste)
    f.write("impressoras:")
    f.write(impre)

subprocess.run("desk.cpl",shell=True)#liga a coisa da tela